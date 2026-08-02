from database import load_data

df = load_data()

df.to_csv(
    "dataset/muqaththaah_dataset.csv",
    index=False,
)

print("CSV exported successfully.")