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

# Values extracted from the research
values = [80, 40, 25, 67.5]  # Using midpoints of ranges where applicable (30-50% → 40%, 20-30% → 25%, 60-75% → 67.5%)

# Create a DataFrame for easier plotting
df = pd.DataFrame({'Category': categories, 'Percentage': values})

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create the horizontal bar chart
bars = sns.barplot(x='Percentage', y='Category', data=df, ax=ax)

# Add value labels to the bars
for i, v in enumerate(values):
    ax.text(v + 1, i, f"{v}%", va='center', fontweight='bold')

# Customize the plot
ax.set_title('Key Value Propositions of Middleware SDKs', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Percentage Improvement (%)', fontsize=14, labelpad=10)
ax.set_ylabel('Value Category', fontsize=14, labelpad=10)
ax.set_xlim(0, 100)  # Set x-axis limit to 0-100%

# Add a subtitle explaining the chart
plt.figtext(0.5, 0.01, 
            'Source: Analysis of middleware SDK benefits based on industry research data', 
            ha='center', fontsize=10, style='italic')

# Add annotations to provide context
ax.annotate('Middleware SDKs can reduce development\neffort by up to 80% compared to\nbuilding custom integrations', 
            xy=(80, 0), xytext=(60, 0.3), 
            arrowprops=dict(arrowstyle='->'), fontsize=9)

ax.annotate('Companies using integration middleware\nreport 30-50% faster feature deployment', 
            xy=(40, 1), xytext=(20, 1.3), 
            arrowprops=dict(arrowstyle='->'), fontsize=9)

# Adjust layout and save the figure
plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.savefig('output.png', dpi=300, bbox_inches='tight')