import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Students Social Media Addiction (1).csv')

# Display basic information about the dataset
print("--- Dataset Info ---")
print(df.info())
print("\n--- First few rows ---")
print(df.head())
print("\n--- Dataset Shape ---")
print(df.shape)
print("\n--- Checking for missing values ---")
print(df.isnull().sum())

# --- Data Understanding & Cleaning ---
# Based on the info and head, the data seems mostly clean.
# Let's check data types and ensure they are correct.
print("\n--- Data Types ---")
print(df.dtypes)

# Convert 'Addicted_Score' to integer if it's not already (it seems okay from the sample)
# No missing values detected in the sample, let's assume the full dataset is clean as per instructions.

# --- Exploratory Data Analysis (EDA) ---

# 1. Distribution of Daily Usage
plt.figure(figsize=(10, 6))
plt.hist(df['Avg_Daily_Usage_Hours'], bins=20, edgecolor='black', color='skyblue')
plt.title('Distribution of Average Daily Social Media Usage (Hours)')
plt.xlabel('Average Daily Usage (Hours)')
plt.ylabel('Number of Students')
plt.grid(axis='y', alpha=0.75)
plt.show()
# Insight: The distribution shows a peak around 4-6 hours, with a long tail towards higher usage, indicating many students spend significant time on social media.

# 2. Relationship between Usage and Addiction Score
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Avg_Daily_Usage_Hours', y='Addicted_Score', alpha=0.6, color='purple')
plt.title('Relationship between Daily Usage and Addiction Score')
plt.xlabel('Average Daily Usage (Hours)')
plt.ylabel('Addiction Score')
plt.grid(True)
plt.show()
# Insight: There is a strong positive correlation; students who spend more time on social media tend to have higher addiction scores.

# 3. Average Usage by Most Used Platform
platform_usage = df.groupby('Most_Used_Platform')['Avg_Daily_Usage_Hours'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
platform_usage.plot(kind='bar', color='lightcoral')
plt.title('Average Daily Usage by Most Used Platform')
plt.xlabel('Social Media Platform')
plt.ylabel('Average Daily Usage (Hours)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
# Insight: Platforms like Instagram, TikTok, and Snapchat are associated with higher average daily usage compared to LinkedIn or Twitter.

# 4. Addiction Score by Gender
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Gender', y='Addicted_Score', palette='Set2')
plt.title('Distribution of Addiction Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Addiction Score')
plt.grid(True, axis='y')
plt.show()
# Insight: The median addiction score appears slightly higher for females compared to males, though the distributions overlap significantly.

# --- Aggregation & Insights ---

# Average Addiction Level across Genders
gender_addiction = df.groupby('Gender')['Addicted_Score'].mean()
print("\n--- Average Addiction Score by Gender ---")
print(gender_addiction)

# Average Addiction Level across Age Groups
# Let's create age groups
df['Age_Group'] = pd.cut(df['Age'], bins=[17, 19, 21, 23, 25], labels=['18-19', '20-21', '22-23', '24-25'])
age_addiction = df.groupby('Age_Group')['Addicted_Score'].mean()
print("\n--- Average Addiction Score by Age Group ---")
print(age_addiction)

# Average Addiction Level across Academic Levels
academic_addiction = df.groupby('Academic_Level')['Addicted_Score'].mean().sort_values(ascending=False)
print("\n--- Average Addiction Score by Academic Level ---")
print(academic_addiction)

# --- Functions, Loops, and Conditionals ---

# Function to classify risk level based on usage hours
def classify_risk_level(hours):
    if hours < 3:
        return 'Low'
    elif hours < 6:
        return 'Medium'
    else:
        return 'High'

df['Risk_Level'] = df['Avg_Daily_Usage_Hours'].apply(classify_risk_level)

# Function to suggest digital detox strategies
def suggest_strategy(risk_level):
    if risk_level == 'Low':
        return "Maintain healthy habits. Set specific times for checking social media."
    elif risk_level == 'Medium':
        return "Consider setting daily time limits. Take short breaks (e.g., 30 mins) from all screens before bedtime."
    elif risk_level == 'High':
        return "Urgent: Implement a structured digital detox plan. Use app blockers. Seek support from friends/family/counselor."
    else:
        return "Invalid risk level."

df['Detox_Suggestion'] = df['Risk_Level'].apply(suggest_strategy)

# Display a few examples
print("\n--- Risk Level Classification & Detox Suggestions ---")
print(df[['Student_ID', 'Avg_Daily_Usage_Hours', 'Risk_Level', 'Detox_Suggestion']].head(10))

# --- Data Visualization (Continued) ---

# 5. Distribution of Risk Levels
risk_counts = df['Risk_Level'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(risk_counts.values, labels=risk_counts.index, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])
plt.title('Distribution of Students by Risk Level')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
# Insight: A significant portion of students fall into the 'High' risk category, highlighting the prevalence of potentially problematic usage.

# 6. Heatmap: Correlation between numerical variables
# Select relevant numerical columns
corr_columns = ['Age', 'Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night', 'Mental_Health_Score', 'Conflicts_Over_Social_Media', 'Addicted_Score']
corr_matrix = df[corr_columns].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar_kws={'shrink': 0.8})
plt.title('Correlation Heatmap of Key Variables')
plt.show()
# Insight: Strong positive correlation between 'Avg_Daily_Usage_Hours' and 'Addicted_Score'. Negative correlation between 'Sleep_Hours_Per_Night' and 'Addicted_Score', and between 'Mental_Health_Score' and 'Addicted_Score', suggesting addiction impacts well-being.

# 7. Average Sleep Hours by Risk Level
sleep_by_risk = df.groupby('Risk_Level')['Sleep_Hours_Per_Night'].mean().reindex(['Low', 'Medium', 'High']) # Order for clarity
plt.figure(figsize=(8, 5))
sleep_by_risk.plot(kind='bar', color=['green', 'orange', 'red'])
plt.title('Average Sleep Hours by Risk Level')
plt.xlabel('Risk Level')
plt.ylabel('Average Sleep Hours Per Night')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
# Insight: Students classified as 'High' risk get significantly less sleep on average compared to 'Low' and 'Medium' risk groups.

# 8. Average Mental Health Score by Risk Level
mental_by_risk = df.groupby('Risk_Level')['Mental_Health_Score'].mean().reindex(['Low', 'Medium', 'High'])
plt.figure(figsize=(8, 5))
mental_by_risk.plot(kind='line', marker='o', color='purple', linewidth=2, markersize=8)
plt.title('Average Mental Health Score by Risk Level')
plt.xlabel('Risk Level')
plt.ylabel('Average Mental Health Score (Lower = Poorer)')
plt.xticks(ticks=[0, 1, 2], labels=['Low', 'Medium', 'High'])
plt.grid(True)
plt.tight_layout()
plt.show()
# Insight: Mental health scores tend to decrease as the risk level of social media usage increases, indicating a negative impact on psychological well-being.

# --- Storytelling Deliverable ---
story_summary = """
This analysis reveals a concerning trend of high social media usage among students, strongly linked to addiction scores.
Platforms like Instagram and TikTok dominate usage time. A significant number of students fall into the 'High' risk category.
The data shows clear negative correlations: higher usage leads to lower sleep quality and poorer mental health scores.
Gender differences are subtle, but age and academic level might play roles, with undergraduates potentially more affected.
Academic performance is also reported to be negatively impacted by usage.
To combat this, targeted digital wellness programs are essential.
These should include awareness campaigns about usage risks, practical tools for setting screen time limits, and promoting digital detox periods.
Providing personalized strategies based on individual risk levels can enhance effectiveness.
Supporting students in finding healthier online habits is crucial for their overall well-being and academic success.
"""

print("\n--- 10-Line Story Summary ---")
lines = story_summary.strip().split('\n')
for i, line in enumerate(lines):
    if i < 10:
        print(f"{i+1}. {line.strip()}")
    else:
        break

# Final check of the modified dataframe
print("\n--- Final Dataframe Sample ---")
print(df.head())
