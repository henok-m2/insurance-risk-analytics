import pandas as pd
import numpy as np
import os

np.random.seed(42)

# Create directories
os.makedirs('data', exist_ok=True)
os.makedirs('reports', exist_ok=True)

# Create 1000 sample policies
n_samples = 1000
data = {
    'PolicyID': np.arange(1000, 1000 + n_samples),
    'Gender': np.random.choice(['Male', 'Female'], n_samples, p=[0.55, 0.45]),
    'Province': np.random.choice(['Gauteng', 'Western Cape', 'KZN', 'EC'], n_samples),
    'TotalPremium': np.random.exponential(5000, n_samples) + 1000,
    'TotalClaims': np.random.exponential(2000, n_samples),
}

df = pd.DataFrame(data)
df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']

# Save files
df.to_csv('data/sample_insurance_data.csv', index=False)
df.to_csv('data/processed_insurance_data.csv', index=False)

print(f"✅ Created {len(df)} sample policies")
print(f"📁 Files saved to data/")
print(f"   - sample_insurance_data.csv")
print(f"   - processed_insurance_data.csv")
