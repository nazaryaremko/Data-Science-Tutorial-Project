data <- read.csv(file = '/Users/nazaryaremko/Desktop/archive (2)/life_expectancy.csv')
head(data)

install.packages("leaps")
library(leaps)
regsubsets.out <-
  regsubsets(Life.expectancy ~ Adult.Mortality + infant.deaths + Alcohol + percentage.expenditure + Hepatitis.B + 
               Measles + BMI + under.five.deaths + Polio + Total.expenditure + Diphtheria + HIV.AIDS + GDP + Population +
               thinness..1.19.years + thinness.5.9.years + Income.composition.of.resources + Schooling,
             data = data,
             nbest = 1,       # 1 best model for each number of predictors
             nvmax = NULL,    # NULL for no limit on number of variables
             force.in = NULL, force.out = NULL,
             method = "exhaustive")


plot(regsubsets.out, scale = "adjr2", main = "Adjusted R^2")

