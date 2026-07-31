# ==========================================
# AL-AHRUF AL-MUQATHTHAAH ANALYSIS
# Exploratory Data Analysis (EDA)
# ==========================================

from database import load_data

df = load_data()

# ==========================================
# SECTION 1
# TOTAL SURAHS
# ==========================================

print("===== TOTAL SURAHS =====")
print(len(df))

# ==========================================
# SECTION 2
# REVELATION PERIOD
# ==========================================

print("\n===== REVELATION PERIOD =====")

print(df["Revelation_Period"].value_counts())

# ==========================================
# SECTION 3
# MUQATHTHAAH PATTERN
# ==========================================

print("\n===== MUQATHTHAAH PATTERN =====")

print(df["Pattern"].value_counts())

# ==========================================
# SECTION 4
# AVERAGE LETTER COUNT
# ==========================================

print("\n===== AVERAGE LETTER COUNT =====")

print(df["Letter_Count"].mean())

# ==========================================
# SECTION 5
# INTERPRETATION CATEGORY
# ==========================================

print("\n===== INTERPRETATION CATEGORY =====")

print(df["Interpretation_Category"].value_counts())

# ==========================================
# SECTION 6
# LONGEST MUQATHTHAAH
# ==========================================

print("\n===== LONGEST MUQATHTHAAH =====")

print(
    df[df["Letter_Count"] == df["Letter_Count"].max()]
)

# ==========================================
# SECTION 7
# MADINAN SURAHS
# ==========================================

print("\n===== MADINAN SURAHS =====")

print(
    df[df["Revelation_Period"] == "Madinan"]
)

# ==========================================
# SECTION 8
# MECCAN - TWO LETTERS
# ==========================================

print("\n===== MECCAN - TWO LETTERS =====")

meccan_two_letters = df[
    (df["Revelation_Period"] == "Meccan") &
    (df["Letter_Count"] == 2)
]

print(meccan_two_letters)

print("\nTotal:")

print(len(meccan_two_letters))