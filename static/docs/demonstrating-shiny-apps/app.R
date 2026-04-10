library(shiny)
library(shinythemes)

ui = fluidPage(
    titlePanel("Central Limit Theorem"),
    theme = shinytheme("readable"),
    sidebarLayout(
        sidebarPanel(
            sliderInput(inputId = "num", "Sample size", min = 1, max = 100, value = 10),
            sliderInput(inputId = "num2", "Number of samples", min = 10, max = 1000, value = 100),
            radioButtons(inputId = "dist", label = "Distribution", choices = list("Normal" = 1, "Uniform" = 2, "Exponential" = 3, "Poisson" = 4), inline = T)
        ),
        mainPanel(
            plotOutput(outputId = "pl")
        )
    )
)

server = function(input, output) {
    output$pl = renderPlot({
        n = input$num
        num2 = input$num2
        xbar = numeric(num2)
        for(i in 1:num2)
        {
            if (input$dist == 1) xbar[i] = mean(rnorm(n))
            if (input$dist == 2) xbar[i] = mean(runif(n))
            if (input$dist == 3) xbar[i] = mean(rexp(n))
            if (input$dist == 4) xbar[i] = mean(rpois(n,1.5))
        }
        hist(xbar)
    })
}

shinyApp(ui = ui, server = server)