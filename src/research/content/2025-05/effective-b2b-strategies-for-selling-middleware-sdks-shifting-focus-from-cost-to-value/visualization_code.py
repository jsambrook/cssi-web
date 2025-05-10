import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set the style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")

# Data extracted from the research
categories = [
    'Development Time Reduction',
    'Faster Time-to-Market',
    'Maintenance Cost Reduction',
    'Error Reduction'
]

# Extract the midpoint of the percentage ranges mentioned in the research
values = [80, 40, 25, 67.5]  # 80%, 30-50% (avg 40%), 20-30% (avg 25%), 60-75% (avg 67.5%)

# Create a DataFrame
df = pd.DataFrame({
    'Benefit Category': categories,
    'Percentage Improvement': values
})

# Sort by impact
df = df.sort_values('Percentage Improvement', ascending=False)

# Create the visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bar chart
bars = sns.barplot(
    x='Percentage Improvement',
    y='Benefit Category',
    data=df,
    ax=ax,
    palette='viridis'
)

# Add value labels to the bars
for i, v in enumerate(df['Percentage Improvement']):
    ax.text(v + 1, i, f"{v}%", va='center', fontweight='bold')

# Add a vertical line at 0
ax.axvline(x=0, color='black', linestyle='-', alpha=0.3)

# Customize the chart
ax.set_title('Key Value Propositions of Middleware SDKs', fontsize=18, pad=20)
ax.set_xlabel('Percentage Improvement (%)', fontsize=14, labelpad=10)
ax.set_ylabel('Benefit Category', fontsize=14, labelpad=10)
ax.tick_params(axis='both', which='major', labelsize=12)

# Set x-axis limits
ax.set_xlim(0, 100)

# Add annotations
plt.figtext(0.5, 0.01, 
            "Source: Research data on middleware SDK benefits and ROI metrics", 
            ha="center", fontsize=10, style='italic')

# Add a subtle grid on the x-axis only
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Remove top and right spines
sns.despine()

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig('output.png', dpi=300, bbox_inches='tight')