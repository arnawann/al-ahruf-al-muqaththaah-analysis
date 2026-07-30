CREATE TABLE muqaththaah (
    Record_ID INT AUTO_INCREMENT PRIMARY KEY,
    Surah_Number INT,
    Surah_Name VARCHAR,
    Verse_Number INT,
    Muqaththaah VARCHAR(20),
    Pattern VARCHAR(20),
    Letter_Count INT,
    Revelation_Period VARCHAR(10),
    Interpretation_Category VARCHAR(50)
);