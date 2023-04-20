#jaundice_prediction_model.py

import pandas as pd
import statsmodels.api as sm

# Load data
data = pd.read_csv("jaundice_data.csv")

# Define variables
X = data["Bilirubin"]
y = data["Jaundice"]

# Fit logistic regression model
X = sm.add_constant(X) # Add intercept term
model = sm.Logit(y, X)
result = model.fit()

# Print results
print(result.summary())
