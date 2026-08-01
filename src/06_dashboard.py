# ==========================================
# AL-AHRUF AL-MUQATHTHAAH ANALYSIS
# Visualization
# ==========================================

import matplotlib.pyplot as plt
import os
import seaborn as sns

from database import load_data

df = load_data()

pattern_counts = df['Pattern'].value_counts()
revelation = df['Revelation_Period'].value_counts()
category = df['Interpretation_Category'].value_counts()
letter_counts = df['Letter_Count'].value_counts().sort_index()

fig, axes = plt.subplots(2,2,figsize=(14,14))

sns.set_theme(
    style='whitegrid',
    palette='Set2',
    font_scale=1.1
)

# ==========================================
# SECTION 1
# Pattern Distribution
# ==========================================

ax_pattern = pattern_counts.plot(
    kind='bar',
    ax=axes[0,0],
    color=[
        "#E74C3C",
        "#F39C12",
        "#2ECC71",
        "#3498DB",
        "#9B59B6"
    ]
)

ax_pattern.set_title(
    "Distribution of Muqaththaah Patterns",
    fontsize=11,
    fontweight='bold'
)

ax_pattern.set_xlabel('')

for bar in ax_pattern.patches:

    ax_pattern.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height()+0.05,
        int(bar.get_height()),
        ha='center',
        fontsize=9
    )
ax_pattern.spines['top'].set_visible(False)
ax_pattern.spines['right'].set_visible(False)
ax_pattern.tick_params(axis='x', rotation=15)
ax_pattern.grid(
    axis='y',
    linestyle='--',
    linewidth=0.6, 
    alpha=0.35
)
ax_pattern.xaxis.grid(False)

# ==========================================
# SECTION 2
# Revelation Period
# ==========================================

ax_revelation = revelation.plot(
    kind='bar',
    ax=axes[0,1],
    color=["#3498DB","#2ECC71"]
)

ax_revelation.set_title(
    'Revelation Period',
    fontsize=11,
    fontweight='bold'
)

ax_revelation.set_xlabel('')

for bar in ax_revelation.patches:

    ax_revelation.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height()+0.05,
        int(bar.get_height()),
        ha="center"
    )
ax_revelation.spines['top'].set_visible(False)
ax_revelation.spines['right'].set_visible(False)
ax_revelation.tick_params(axis='x', rotation=0)
ax_revelation.grid(
    axis='y',
    linestyle='--',
    linewidth=0.6, 
    alpha=0.35
)
ax_revelation.xaxis.grid(False)

# ==========================================
# SECTION 3
# Interpretation Category
# ==========================================

ax_category = category.plot(
    kind='bar',
    ax=axes[1,0],
    color=[ 
        "#2ECC71",
        "#F39C12",
        "#9B59B6"
    ] 
)

ax_category.set_title(
    'Interpretation Categories',
    fontsize=11,
    fontweight='bold'
)

ax_category.set_xlabel('')

for bar in ax_category.patches:

    ax_category.text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+0.05,
        int(bar.get_height()),
        ha='center'
    )
ax_category.spines['top'].set_visible(False)
ax_category.spines['right'].set_visible(False)
ax_category.tick_params(axis='x', rotation=0)
ax_category.grid(
    axis='y',
    linestyle='--',
    linewidth=0.6, 
    alpha=0.35
)
ax_category.xaxis.grid(False)

# ==========================================
# SECTION 4
# Letter Count
# ==========================================

ax_letter_counts = letter_counts.plot(
    kind='bar',
    ax=axes[1,1],
    color=[
        "#E74C3C",
        "#F39C12",
        "#2ECC71",
        "#3498DB",
        "#9B59B6"
    ]
)

ax_letter_counts.set_title(
    "Letter Count Distribution",
    fontsize=11,
    fontweight='bold'
)

ax_letter_counts.set_xlabel('')

for bar in ax_letter_counts.patches:

    ax_letter_counts.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.05,
        int(bar.get_height()),
        ha="center",
        fontsize=9
    )

ax_letter_counts.spines["top"].set_visible(False)
ax_letter_counts.spines["right"].set_visible(False)
ax_letter_counts.tick_params(axis='x', rotation=0)
ax_letter_counts.grid(
    axis='y',
    linestyle='--',
    linewidth=0.6, 
    alpha=0.35
)
ax_letter_counts.xaxis.grid(False)

axes[1,1].set_xlabel('')

total_surahs = df['Surah_Number'].nunique()

unique_patterns = df['Muqaththaah'].nunique()

fig.suptitle(
    "Al-Ahruf Al-Muqaththaah Dataset Dashboard",
    fontsize=20,
    fontweight='bold',
    y=0.95
)

fig.text(
    0.5,
    0.89,
    f"{total_surahs} Surahs | {unique_patterns} Unique Muqaththaah Patterns",
    ha="center",
    fontsize=11,
    color="dimgray"
)

plt.tight_layout(
    rect=[0.03,0.08,0.97,0.93],
    pad=2
)

plt.subplots_adjust(
    hspace=0.45,
    wspace=0.25
)

fig.text(
    0.5,
    0.060,
    "Source:", 
    ha='center', 
    fontsize=10,
    fontweight="bold",
    color="dimgray"
)

fig.text(
    0.5,
    0.012,
    "AD Nugraha (2024), Tafsir and Local Interpretation Analysis:\nStudy of Muqaththaah Letters in Tafsir Al-Ibriz", 
    ha='center', 
    fontsize=9,
    fontstyle="italic",
    color="dimgray"
)

plt.savefig('visualization/summary_dashboard.png', dpi=300, bbox_inches="tight")

plt.show()