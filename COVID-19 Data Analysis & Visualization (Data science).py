# COVID-19 Data Analysis & Visualization (Data science).py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# STEP 1: Load Data
data = {
    "USMER": [2,2,2,2,2,2,2,2,2,2,2,2,2],
    "MEDICAL_UNIT": [1]*13,
    "SEX": [1,2,2,1,2,1,1,1,1,1,1,2,2],
    "PATIENT_TYPE": [1,1,2,1,1,2,1,1,1,1,1,2,2],
    "DATE_DIED": ["03/05/2020","03/06/2020","09/06/2020","12/06/2020","21/06/2020","9999-99-99",
                  "9999-99-99","9999-99-99","9999-99-99","9999-99-99","9999-99-99","9999-99-99","9999-99-99"],
    "INTUBED": [97,97,1,97,97,2,97,97,2,2,97,2,2],
    "PNEUMONIA": [1,1,2,2,2,1,2,1,2,2,2,2,2],
    "AGE": [65,72,55,53,68,40,64,64,37,25,38,24,30],
    "PREGNANT": [2,97,97,2,97,2,2,2,2,2,2,97,97],
    "DIABETES": [2,2,1,2,1,2,2,1,1,2,2,2,2],
    "COPD": [2]*13,
    "ASTHMA": [2]*13,
    "INMSUPR": [2]*13,
    "HIPERTENSION": [1,1,2,2,1,2,2,1,2,2,2,2,2],
    "OTHER_DISEASE": [2]*13,
    "CARDIOVASCULAR": [2,2,2,2,2,2,2,2,1,2,2,2,2],
    "OBESITY": [2,1,2,2,2,2,2,2,2,2,2,2,2],
    "RENAL_CHRONIC": [2,1,2,2,2,2,2,1,2,2,2,2,2],
    "TOBACCO": [2]*13,
    "CLASIFFICATION_FINAL": [3,5,3,7,3,3,3,3,3,3,3,3,3],
    "ICU": [97,97,2,97,97,2,97,97,2,2,97,2,2]
}

df = pd.DataFrame(data)

# Replace unknowns (97 and 9999-99-99) with NaN
df.replace({97: pd.NA, "9999-99-99": pd.NA}, inplace=True)

# -------------------------------
# STEP 2: Create 'died' column
df["died"] = df["DATE_DIED"].notna()

# -------------------------------
# STEP 3: Death Count Pie Chart
death_counts = df["died"].value_counts()

plt.figure(figsize=(5,5))
plt.pie(
    death_counts, 
    labels=["Survived", "Died"], 
    autopct='%1.1f%%', 
    colors=['green', 'red'],
    startangle=90
)
plt.title("Patient Death Rate")
plt.axis('equal')
plt.show()

# -------------------------------
# STEP 4: Comorbidity vs Death
comorbidities = ["DIABETES", "OBESITY", "COPD", "ASTHMA", "HIPERTENSION", "CARDIOVASCULAR"]

for condition in comorbidities:
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x=condition, hue="died", palette='Set1')
    plt.title(f"{condition} vs Death")
    plt.xlabel(condition)
    plt.ylabel("Number of Patients")
    plt.legend(["Survived", "Died"])
    plt.tight_layout()
    plt.show()

# -------------------------------
# STEP 5: Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["AGE"], bins=8, kde=True, color='purple')
plt.title("Patient Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -------------------------------
# STEP 6: ICU Admission vs Death
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="ICU", hue="died", palette="Set2")
plt.title("ICU Admission vs Death")
plt.xlabel("ICU Status")
plt.ylabel("Patients")
plt.legend(["Survived", "Died"])
plt.tight_layout()
plt.show()

# -------------------------------
# STEP 7: Patient Type vs Death
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="PATIENT_TYPE", hue="died", palette="Set3")
plt.title("Patient Type vs Death")
plt.xlabel("Outpatient (2) or Inpatient (1)")
plt.ylabel("Number of Patients")
plt.legend(["Survived", "Died"])
plt.tight_layout()
plt.show()
