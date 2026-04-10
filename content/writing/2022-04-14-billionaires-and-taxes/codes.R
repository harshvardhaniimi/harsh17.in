library(tidyverse)
library(tidylog)
library(stringr)
library(scales)

data = read_csv("/Users/harshvardhan/Desktop/Dump/income_taxes.csv")
data
data_modified = na.omit(data)
data_modified

# function to convert currency in dollars to values
currency = function(x)
{
   for (i in seq_along(x))
   {
   if(str_sub(x[i], start = -1) == "B")
   {
      x[i] = as.numeric(str_sub(x[i], 2, -2)) * 10^9
   }
   
   if(str_sub(x[i], start = -1) == "M")
      x[i] = as.numeric(str_sub(x[i], 2, -2)) * 10^6
   }
   return(x)
}

percentage = function(x)
{
   x = as.numeric(str_sub(x, 1, -2))
   return(x)
}

data_modified$Income = as.numeric(currency(data_modified$Income))
data_modified$Fed_Tax = percentage(data_modified$`Federal Tax Rate`)
data_modified$Inc_Low_Tax = percentage(data_modified$`%income in lower tax rate`)
data_modified$Tax_Deduc_Inc = percentage(data_modified$`% of income deducted`)

View(data_modified)


data = data_modified %>% 
   select(-`Federal Tax Rate`, -`%income in lower tax rate`, -`% of income deducted`)
data

p = data %>% 
   #filter(Income > 10^9) %>% 
   ggplot(aes(x = Income, y = Fed_Tax, colour = Sector, text = Name)) +
   geom_point() +
   guides(x = guide_axis(angle = 90)) +
   scale_x_continuous(trans = "log10", labels = label_dollar()) +
   theme_minimal()

p = p + geom_hline(yintercept = 22.4)

p = p + annotate("text", x = 2e9, y = 25, label = "Average US Tax Rate")


plotly::ggplotly(p)

p = p + geom_hline(yintercept = 22.4)

p + xlab("Log Average Income (2013 - 18)") + 
   ylab("Effective Federal Tax Rate") +
   labs(title = "Rich People and Taxes",
        caption = "There's high variance in high income earners. The general trend hints at lower income tax rates as the income increases.")

data %>% 
   #filter(Income > 10^9) %>% 
   ggplot(aes(x = Income, y = Fed_Tax, colour = Sector, text = Name)) +
   geom_point() +
   guides(x = guide_axis(angle = 90)) +
   scale_x_continuous(trans = "log10", labels = label_dollar()) +
   xlab("Log Average Income (2013 - 18)") + 
   ylab("Effective Federal Tax Rate") +
   labs(title = "Rich People and Taxes",
        caption = "There's high variance in high income earners. The general trend hints at lower income tax rates as the income increases.") +
   theme_linedraw()


p = data %>% 
   ggplot(aes(x = Income, y = Fed_Tax, colour = Sector, text = Name)) +
   geom_point() +
   geom_smooth() +
   scale_x_continuous(trans = "log10", labels = label_dollar()) +
   guides(x = guide_axis(angle = 90)) +
   ylim(c(0, 60)) +
   facet_wrap(. ~ Sector) +
   xlab("Log Average Income (2013 - 18)") + 
   ylab("Effective Federal Tax Rate") +
   labs(title = "Rich People and Taxes",
        caption = "There is greater consistency between the sectors") +
   theme_linedraw()

plotly::ggplotly(p)

