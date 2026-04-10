x <- c(5,17,31,9,17,10,30,28,16,29,14,34)
y <- c(1,2,3,4,5,6,7,8,9,10,11,12)
day <- c(1,2,3,4,5,6,7,8,9,10,11,12)
df1 <- data.frame(x,y,day)
df1

df2 <- reshape::melt(df1, id = c("day"))
df2


phds %>% 
  filter(major_field)

phds_top_engineering = phds %>% 
  filter(broad_field == "Engineering") %>% 
  group_by(field) %>% 
  summarise(n_phds = sum(n_phds)) %>% 
  filter(n_phds > 100) %>% 
  slice_max(order_by = n_phds, n = 6)

phds_top_engineering
  

phds_top_engineering %>%
ggplot(aes(x = year, y = n_phds, fill = field)) + 
  geom_bar(stat = "identity") + 
  facet_wrap( ~ field) + 
  scale_x_continuous(breaks = seq(1, 12, 2))


phds %>% 
  filter(field %in% phds_top_engineering$field) %>% 
ggplot(aes(x = year, y = n_phds, fill = field)) +
  geom_bar(stat = "identity") + 
  scale_x_continuous(labels = scales::label_number(accuracy = 1)) +
  scale_fill_manual(values = MetBrewer::met.brewer("Hokusai1", 6)) +
  facet_wrap( ~ field) +
  labs(x = "Year", y = "Number of PhDs", fill = "Field")
