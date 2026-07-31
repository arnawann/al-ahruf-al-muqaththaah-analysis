# ==========================================
# AL-AHRUF AL-MUQATHTHAAH ANALYSIS
# Visualization
# ==========================================

import matplotlib.pyplot as plt
import os

from database import load_data

df = load_data()

pattern_counts = df['Pattern'].value_counts()
revelation = df['Revelation_Period'].value_counts()
category = df['Interpretation_Category'].value_counts()

fig, axes = plt.subplots(2,2,figsize=(14,10))

pattern_counts.plot(kind='bar',ax=axes[0,0])
axes[0,0].set_title('Pattern Distribution')

revelation.plot(kind='bar',ax=axes[0,1])
axes[0,1].set_title('Revelation Period')

category.plot(kind='bar',ax=axes[1,0])
axes[1,0].set_title('Interpretation Category')

axes[1,1].hist(df['Letter_Count'],bins=5)
axes[1,1].set_title('Letter Count')

plt.tight_layout()

plt.savefig('visualization/summary_dashboard.png', dpi=300, bbox_inches="tight")

plt.show()