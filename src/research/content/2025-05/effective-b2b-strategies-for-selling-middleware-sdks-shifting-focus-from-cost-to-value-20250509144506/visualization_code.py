import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set the style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("deep")

# Extract data from the research
categories = [
    'Development Time Reduction',
    'Faster Time-to-Market',
    'Maintenance Cost Reduction',
    'Error Reduction'
]

# Midpoint values from the ranges mentioned in the research
values = [80, 40, 25, 67.5]  # Using midpoints of ranges: 80%, 30-50%, 20-30%, 60-75%

# Create a DataFrame
df = pd.DataFrame({
    'Benefit Category': categories,
    'Percentage Improvement': values
})

# Create the visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bar chart
bars = sns.barplot(x='Percentage Improvement', y='Benefit Category', data=df, 
                  palette='viridis', orient='h', ax=ax)

# Add value labels to the bars
for i, v in enumerate(values):
    ax.text(v + 1, i, f"{v}%", va='center', fontweight='bold')

# Customize the plot
ax.set_title('Key Value Propositions of Middleware SDKs', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Percentage Improvement (%)', fontsize=14, labelpad=10)
ax.set_ylabel('Benefit Category', fontsize=14, labelpad=10)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.set_xlim(0, 100)  # Set x-axis limit to 100%

# Add a note about the source
plt.figtext(0.1, 0.01, 'Source: Based on middleware SDK research data', fontsize=10, style='italic')

# Add a subtitle explaining the chart
plt.figtext(0.1, 0.95, 'Shifting focus from cost to value: Quantifiable benefits of middleware SDKs', 
           fontsize=12, style='italic')

# Adjust layout and save
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('output.png', dpi=300, bbox_inches='tight')