# Install Tidyverse and Dummies Package
# install.packages("tidyverse")
# install.packages("dummies", repos = NULL, type="source")

#Load Tidyverse and Dummies
library(tidyverse)
library(dummies)
library(scales)

# Set Working Directory to Lab04
setwd("C:/Users/ual-laptop/Desktop/MIS545/Lab04")
getwd()

# Read TireTread.csv into a tibble
tireTread1 <- read_csv(file = "TireTread.csv",
                       col_types = "cfnni",
                       col_names = TRUE)

# Display tireTread1 tibble in the console
print(tireTread1)

# Display the structure of tireTread1 in the console
str(tireTread1)

# Display the summary of tireTread1 in the console
summary(tireTread1)

# Impute missing data with mean
tireTread2 <- tireTread1 %>%
  mutate(UsageMonths = ifelse(
    is.na(UsageMonths),
    mean(UsageMonths, na.rm = TRUE),UsageMonths))

# Display summary of tireTread2 to check if missing values are imputed
summary(tireTread2)

# Determine outlierMin in TreadDepth feature
outlierMin <- quantile(tireTread2$TreadDepth, .25) - 
  (IQR(tireTread2$TreadDepth)*1.5)

# Determine outlierMax in TreadDepth feature
outlierMax <- quantile(tireTread2$TreadDepth, .75) - 
  (IQR(tireTread2$TreadDepth)*1.5)

# Add the outliers to their own tibble called treadDepthOutliers
treadDepthOutliers <- tireTread2 %>%
  filter(TreadDepth < outlierMin | TreadDepth > outlierMax)

# Normalize the UsageMonths
tireTread3 <- tireTread2 %>%
  mutate(LogUsageMonths = log(UsageMonths))

# Discretize TreadDepth into NeedsReplacing i.e
# tires with tread depth of less than or equal to 1.6mm need replacing
tireTread4 <- tireTread3 %>%
  mutate(NeedsReplacing = TreadDepth <= 1.6)

# Add a comment here
tireTread4dataframe <- data.frame(tireTread4)
tireTread5 <- as_tibble(dummy.data.frame(data = tireTread4dataframe,
                                         names = "Position"))

# ScatterPlot of Miles with TreadDepth
scatterPlotMilesTreadDepth <- ggplot(data = tireTread5,
                                     aes(x = Miles,
                                         y = TreadDepth))+
    labs(title = "Tire Miles and Tread Depth Scatter Plot")

# Add Geometry Layer
scatterPlotMilesTreadDepth + geom_point(color = "dark gray") + 
  geom_smooth(method = lm,
              level = 0,
              color = "red")
