import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('Students Social Media Addiction (1).csv')

# Create a line plot showing the relationship between the three indicators
plt.figure(figsize=(10, 6))

# Group by Academic_Level and Affects_Academic_Performance to show average Addicted_Score
grouped_data = df.groupby(['Academic_Level', 'Affects_Academic_Performance'])['Addicted_Score'].mean().reset_index()

# Create separate lines for Yes and No responses
for impact in grouped_data['Affects_Academic_Performance'].unique():
    subset = grouped_data[grouped_data['Affects_Academic_Performance'] == impact]
    plt.plot(subset['Academic_Level'], subset['Addicted_Score'], 
             marker='o', linewidth=2, markersize=8, label=f'Affects Academic Performance: {impact}')

# Customize the plot
plt.xlabel('Academic Level')
plt.ylabel('Average Addicted Score')
plt.title('Average Addicted Score by Academic Level and Academic Impact')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()