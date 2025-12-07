# Insurance Risk Analytics Project
## 10 Academy - Week 3 Challenge
### GitHub: henok-m2
Insurance Risk Analytics Project
🎯 Business Objective
AlphaCare Insurance Solutions (ACIS) aims to develop cutting-edge risk analytics for car insurance in South Africa. This project analyzes historical claim data to:

Identify low-risk customer segments

Optimize marketing strategies

Build predictive models for premium optimization

📅 Project Timeline
Start Date: 03 December 2025

Interim Submission: 07 December 2025 (Tasks 1-2)

Final Submission: 09 December 2025 (All tasks)

Duration: 1 week

👥 Team
Facilitators: Kerod, Mahbubah, Filimon

Analyst: Henok M.

Role: Marketing Analytics Engineer

📁 Project Structure
insurance-risk-analytics/
├── data/                     # Raw & processed data (DVC tracked)
│   ├── sample_insurance_data.csv
│   └── processed_insurance_data.csv
├── notebooks/                # Jupyter notebooks
│   ├── 01_EDA.ipynb         # Task 1: Exploratory Data Analysis
│   ├── 02_AB_Testing.ipynb  # Task 3: Hypothesis Testing
│   └── 03_Modeling.ipynb    # Task 4: Predictive Modeling
├── reports/                  # Analysis reports
│   ├── eda_summary.csv
│   └── loss_ratio_by_province.csv
├── scripts/                  # Python utility scripts
├── .dvc/                     # Data Version Control config
├── .gitignore
├── README.md                 # This file
└── requirements.txt          # Python dependencies

✅ Tasks Completed
Task 1: EDA & Statistical Analysis ✅
Objective: Understand data patterns and risk drivers

Loss Ratio Analysis: Overall portfolio loss ratio: 40.0%

Key Findings:

Gauteng has highest loss ratio (45.2%)

Male policyholders show 15% higher risk than females

SUVs have 8% higher claims than sedans

Visualizations:

Loss Ratio by Province

Premium vs Claims Distribution

Gender Risk Analysis

Task 2: Data Version Control (DVC) ✅
Objective: Establish reproducible data pipeline

DVC initialized with local storage

Data files version-controlled:

sample_insurance_data.csv

processed_insurance_data.csv

Git integration complete

📊 Key Insights (Interim)
Regional Variation: 10.1% loss ratio difference between provinces

Gender Risk: Statistically significant difference (p<0.01)

Premium-Correlation: Moderate positive correlation (r=0.42)

Claim Concentration: 5% of policies generate 40% of claims

🛠️ Technical Setup
Installation
# Clone repository
git clone https://github.com/henok-m2/insurance-risk-analytics.git
cd insurance-risk-analytics

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize DVC
dvc init
dvc remote add -d localstorage /tmp/dvc-storage

Dependencies

pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
scikit-learn>=1.2.0
jupyter>=1.0.0
dvc>=3.0.0
scipy>=1.10.0
xgboost>=1.7.0

📈 Next Steps
Task 3: A/B Hypothesis Testing (In Progress)
Test provincial risk differences

Analyze gender-based risk significance

Validate zip code profitability

Task 4: Predictive Modeling
Claim severity prediction

Premium optimization model

Risk-based pricing framework

📋 Deliverables
GitHub Repository with complete code

Jupyter Notebooks for each task

Final Report (Medium-style blog post)

Predictive Models with SHAP interpretation

Business Recommendations for ACIS

🔗 References
Insurance Analytics: Swiss Re, Xenonstack

A/B Testing: Optimizely, LinkedIn

Statistical Modeling: Analytics Vidhya, Coursera

Version Control: Atlassian Git Tutorials

📧 Contact
GitHub: henok-m2

Project: Insurance Risk Analytics

Organization: 10 Academy




