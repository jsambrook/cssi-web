import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set the style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")

# Extract data from the research
categories = [
    'Development Time Reduction',
    'Faster Time-to-Market',
    'Maintenance Cost Reduction',
    'Error Reduction'
]

# Midpoint values from the ranges mentioned in the research
values = [80, 40, 25, 67.5]  # Using midpoints of ranges (80%, 30-50%, 20-30%, 60-75%)

# Create a DataFrame
df = pd.DataFrame({
    'Benefit Category': categories,
    'Percentage Improvement': values
})

# Create the visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Create horizontal bar chart
bars = sns.barplot(x='Percentage Improvement', y='Benefit Category', data=df, ax=ax)

# Add value labels to the bars
for i, v in enumerate(values):
    ax.text(v + 1, i, f"{v}%", va='center')

# Customize the plot
ax.set_title('Key Value Propositions of Middleware SDKs', fontsize=16, fontweight='bold')
ax.set_xlabel('Percentage Improvement (%)', fontsize=12)
ax.set_ylabel('')
ax.set_xlim(0, 100)

# Add a note about the data source
plt.figtext(0.5, 0.01, 
            'Source: Research data on middleware SDK benefits', 
            ha='center', fontsize=9, style='italic')

# Add annotations explaining the context
plt.figtext(0.5, 0.95, 
            'Shifting Focus from Cost to Value: Quantifiable Benefits of Middleware SDKs', 
            ha='center', fontsize=11, fontweight='bold')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the figure
plt.savefig('output.png', dpi=300, bbox_inches='tight')