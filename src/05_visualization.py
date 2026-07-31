# ==========================================
# AL-AHRUF AL-MUQATHTHAAH ANALYSIS
# Visualization
# ==========================================

import matplotlib.pyplot as plt
import os

from database import load_data

df = load_data()

# ==========================================
# DISTRIBUTION OF MUQATHTHAAH PATTERNS
# ==========================================

# ==========================================
# SECTION 1
# Pattern Distribution
# ==========================================

pattern_counts = df['Pattern'].value_counts()

plt.figure(figsize=(8,5))

pattern_counts.plot(kind="bar")

plt.title("Distribution of Muqaththaah Patterns")

plt.xlabel("Pattern")

plt.ylabel('Frequency')

plt.tight_layout()

plt.savefig("visualization/pattern_distribution.png")

plt.show()


# ==========================================
# SECTION 2
# Revelation Period
# ==========================================

revelation = df["Revelation_Period"].value_counts()

plt.figure(figsize=(6,5))

revelation.plot(kind='bar')

plt.title('Revelation Period')

plt.xlabel('Period')

plt.ylabel('Number of Surahs')

plt.tight_layout()

plt.savefig('visualization/revelation_period.png')

plt.show()

# ==========================================
# SECTION 3
# Interpretation Category
# ==========================================

category = df['Interpretation_Category'].value_counts()

plt.figure(figsize=(8,5))

category.plot(kind='bar')

plt.title('Interpretation Categories')

plt.xlabel('Category')

plt.ylabel('Frequency')

plt.tight_layout()

plt.savefig('visualization/interpretation_category.png')

plt.show()

# ==========================================
# SECTION 4
# Letter Count Distribution
# ==========================================

plt.figure(figsize=(7,5))

plt.hist(df["Letter_Count"], bins=5)

plt.title('Distribution of Letter Count')

plt.xlabel('Letter Count')

plt.ylabel('Frequency')

plt.tight_layout()

plt.savefig('visualization/letter_count_distribution.png')

plt.close()