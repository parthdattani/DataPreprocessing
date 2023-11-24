# Tire Tread Analysis

## Requirements

Before running the code, ensure that you have the following R packages installed:

- `tidyverse`
- `dummies`
- `scales`

You can install these packages using the following R commands:

```R
install.packages("tidyverse")
install.packages("dummies", repos = NULL, type="source")
```

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/varunkapuria96/data-preprocessing-with-r.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd data-preprocessing-with-r.R
   ```

3. Run the R script `DataPreprcessing.R` in your R environment or RStudio.

## Description

The code performs the following tasks:

1. Loads the required libraries, including `tidyverse`, `dummies`, and `scales`.

2. Reads the dataset, "TireTread.csv," into a tibble named `tireTread1`.

3. Cleans and imputes missing data by replacing missing `UsageMonths` values with the mean.

4. Detects outliers in the `TreadDepth` feature and creates a separate tibble for outliers.

5. Normalizes the `UsageMonths` feature by taking its natural logarithm.

6. Discretizes the `TreadDepth` feature into a binary variable `NeedsReplacing` indicating whether tires need replacement.

7. Converts the data frame to a tibble and creates dummy variables for the `Position` feature.

8. Generates a scatter plot to visualize the relationship between `Miles` and `TreadDepth`.

## Dataset

The dataset, "TireTread.csv," contains information about tire tread measurements, usage months, miles driven, and position.

Please ensure you have this dataset in the same directory as the R script or update the file path accordingly.
