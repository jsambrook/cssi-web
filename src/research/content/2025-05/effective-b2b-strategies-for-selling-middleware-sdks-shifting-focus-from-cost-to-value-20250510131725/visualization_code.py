import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set the style for the visualization
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Blues_r")

# Extract data from the research
categories = ['Development Time Reduction', 'Faster Time-to-Market', 
              'Maintenance Cost Reduction', 'Error Reduction']

values = [80, 40, 25, 67.5]  # Using midpoints of ranges: 80%, 30-50%, 20-30%, 60-75%

# Create a DataFrame for easier plotting
df = pd.DataFrame({'Category': categories, 'Percentage': values})

# Create the visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Plot horizontal bars
bars = sns.barplot(x='Percentage', y='Category', data=df, ax=ax)

# Add value labels to the end of each bar
for i, v in enumerate(values):
    ax.text(v + 1, i, f"{v}%", va='center')

# Customize the plot
ax.set_title('Key Value Propositions of Middleware SDKs', fontsize=16, fontweight='bold')
ax.set_xlabel('Percentage Improvement (%)', fontsize=12)
ax.set_ylabel('')
ax.set_xlim(0, 100)

# Add a note about the data source
plt.figtext(0.5, 0.01, 
            'Source: Research data on middleware SDK benefits across industries', 
            ha='center', fontsize=9, style='italic')

# Add annotations to explain the context
plt.figtext(0.5, 0.95, 
            'Shifting Focus from Cost to Value: Quantifiable Benefits of Middleware SDKs', 
            ha='center', fontsize=12, fontweight='bold')

# Adjust layout and save
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('output.png', dpi=300, bbox_inches='tight')