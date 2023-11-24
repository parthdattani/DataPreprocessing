# Install required packages
# !pip install pandas seaborn numpy

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Set Working Directory to Lab04
# Replace the path with your actual path
working_directory = "C:/Users/ual-laptop/Desktop/MIS545/Lab04"
tireTread_path = "TireTread.csv"
tireTread_full_path = f"{working_directory}/{tireTread_path}"

# Read TireTread.csv into a pandas DataFrame
tireTread1 = pd.read_csv(tireTread_full_path)

# Display tireTread1 DataFrame in the console
print(tireTread1)

# Display the structure of tireTread1 in the console
print(tireTread1.info())

# Display the summary of tireTread1 in the console
print(tireTread1.describe())

# Impute missing data with mean
tireTread2 = tireTread1.copy()
tireTread2['UsageMonths'] = tireTread2['UsageMonths'].fillna(tireTread2['UsageMonths'].mean())

# Display summary of tireTread2 to check if missing values are imputed
print(tireTread2.describe())

# Determine outlierMin in TreadDepth feature
outlierMin = np.percentile(tireTread2['TreadDepth'], 25) - (1.5 * np.subtract(*np.percentile(tireTread2['TreadDepth'], [75, 25])))

# Determine outlierMax in TreadDepth feature
outlierMax = np.percentile(tireTread2['TreadDepth'], 75) + (1.5 * np.subtract(*np.percentile(tireTread2['TreadDepth'], [75, 25])))

# Add the outliers to their own DataFrame called treadDepthOutliers
treadDepthOutliers = tireTread2[(tireTread2['TreadDepth'] < outlierMin) | (tireTread2['TreadDepth'] > outlierMax)]

# Normalize the UsageMonths
tireTread3 = tireTread2.copy()
tireTread3['LogUsageMonths'] = np.log(tireTread3['UsageMonths'])

# Discretize TreadDepth into NeedsReplacing i.e tires with tread depth of less than or equal to 1.6mm need replacing
tireTread4 = tireTread3.copy()
tireTread4['NeedsReplacing'] = tireTread4['TreadDepth'] <= 1.6

# ScatterPlot of Miles with TreadDepth
scatterPlotMilesTreadDepth = sns.lmplot(data=tireTread4, x='Miles', y='TreadDepth', fit_reg=False, height=6, aspect=1.5)
scatterPlotMilesTreadDepth.fig.suptitle("Tire Miles and Tread Depth Scatter Plot", y=1.02)

# Add Regression Line
sns.regplot(data=tireTread4, x='Miles', y='TreadDepth', scatter=False, ax=scatterPlotMilesTreadDepth.ax)

plt.show()
