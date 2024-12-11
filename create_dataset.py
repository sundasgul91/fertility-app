import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Create sample data
num_samples = 100  # Number of records

# Features
ages = np.random.randint(18, 45, num_samples)  # Random ages between 18 and 45
bmi = np.random.uniform(15, 40, num_samples)  # Random BMI values between 15 and 40
children = np.random.randint(0, 4, num_samples)  # Random number of children between 0 and 3
smoking = np.random.randint(0, 2, num_samples)  # 0 = No, 1 = Yes
exercise = np.random.randint(0, 2, num_samples)  # 0 = No, 1 = Yes

# Target variable (fertility status)
fertility_status = []
for i in range(num_samples):
    # Fertility criteria based on age, BMI, smoking, and exercise
    if ages[i] > 30 or bmi[i] < 18 or bmi[i] > 30 or smoking[i] == 1 or exercise[i] == 0:
        fertility_status.append(0)  # Not fertile
    else:
        fertility_status.append(1)  # Fertile

# Create DataFrame
data = pd.DataFrame({
    'Age': ages,
    'BMI': bmi,
    'Children': children,
    'Smoking': smoking,
    'Exercise': exercise,
    'Fertility_Status': fertility_status
})

# Save to CSV
data.to_csv('fertility_data_with_target.csv', index=False)

print("Dataset created and saved as 'fertility_data_with_target.csv'.")

