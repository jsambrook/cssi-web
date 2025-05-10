import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set the style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")

# Extract data from the research
categories = [
    'Development time reduction',
    'Faster time-to-market',
    'Maintenance cost reduction',
    'Error reduction'
]

percentages = [
    80,  # "middleware SDKs can reduce development effort by up to 80%"
    40,  # "30-50% faster feature deployment cycles" (using midpoint)
    25,  # "reduce long-term maintenance costs by 20-30%" (using midpoint)
    67.5  # "decrease production incidents by 60-75%" (using midpoint)
]

# Create a DataFrame
df = pd.DataFrame({
    'Benefit Category': categories,
    'Percentage Improvement': percentages
})

# Create the visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bar chart
bars = sns.barplot(
    x='Percentage Improvement',
    y='Benefit Category',
    data=df,
    orient='h',
    ax=ax
)

# Add value labels to the bars
for i, v in enumerate(percentages):
    ax.text(v + 1, i, f"{v}%", va='center', fontweight='bold')

# Add a vertical line at 0
ax.axvline(x=0, color='gray', linestyle='-', alpha=0.3)

# Customize the chart
ax.set_title('Key Value Propositions of Middleware SDKs', fontsize=18, pad=20)
ax.set_xlabel('Percentage Improvement (%)', fontsize=14, labelpad=10)
ax.set_ylabel('Benefit Category', fontsize=14, labelpad=10)
ax.tick_params(axis='both', labelsize=12)

# Set x-axis limits
ax.set_xlim(0, max(percentages) + 10)

# Add annotations
plt.figtext(0.5, 0.01, 
            "Source: Analysis of middleware SDK benefits from research data", 
            ha="center", fontsize=10, style='italic')

# Add explanatory text at the top
plt.figtext(0.5, 0.95, 
            "Shifting Focus from Cost to Value: Quantifiable Benefits of Middleware SDKs", 
            ha="center", fontsize=14, fontweight='bold')

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(top=0.9, bottom=0.1)

# Save the figure
plt.savefig('output.png', dpi=300, bbox_inches='tight')