// Embeds a search query for the semantic tier of /search/.
// Provider must match the one used to build static/embeddings.json
// (generate-embeddings.py). Keys come from Netlify env vars:
//   gemini -> GEMINI_API_KEY (or GOOGLE_API_KEY)   [default]
//   openai -> OPENAI_API_KEY  (set EMBED_PROVIDER=openai)

const DIMS = 768;

async function embedGemini(q, key) {
  const model = "gemini-embedding-001";
  const res = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/${model}:embedContent`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json", "x-goog-api-key": key },
      body: JSON.stringify({
        content: { parts: [{ text: q }] },
        taskType: "RETRIEVAL_QUERY",
        outputDimensionality: DIMS,
      }),
    }
  );
  if (!res.ok) throw new Error(`gemini ${res.status}`);
  const data = await res.json();
  return { model, vec: data.embedding.values };
}

async function embedOpenAI(q, key) {
  const model = "text-embedding-3-small";
  const res = await fetch("https://api.openai.com/v1/embeddings", {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${key}` },
    body: JSON.stringify({ model, input: q, dimensions: DIMS }),
  });
  if (!res.ok) throw new Error(`openai ${res.status}`);
  const data = await res.json();
  return { model, vec: data.data[0].embedding };
}

export default async (req) => {
  if (req.method !== "POST")
    return new Response("Method Not Allowed", { status: 405 });

  let q;
  try {
    ({ q } = await req.json());
  } catch {
    return Response.json({ error: "bad body" }, { status: 400 });
  }
  if (typeof q !== "string" || q.trim().length < 2 || q.length > 300)
    return Response.json({ error: "bad query" }, { status: 400 });

  const provider = (process.env.EMBED_PROVIDER || "gemini").toLowerCase();
  const key =
    provider === "gemini"
      ? process.env.GEMINI_API_KEY || process.env.GOOGLE_API_KEY
      : process.env.OPENAI_API_KEY;
  if (!key) return Response.json({ error: "no api key configured" }, { status: 500 });

  try {
    const { model, vec } =
      provider === "gemini"
        ? await embedGemini(q.trim(), key)
        : await embedOpenAI(q.trim(), key);
    const norm = Math.sqrt(vec.reduce((a, v) => a + v * v, 0)) || 1;
    const out = vec.map((v) => Math.round((v / norm) * 1e5) / 1e5);
    return Response.json(
      { provider, model, dims: out.length, vec: out },
      { headers: { "Cache-Control": "no-store" } }
    );
  } catch (e) {
    return Response.json({ error: "embed failed" }, { status: 502 });
  }
};

export const config = { path: "/api/embed-query" };
