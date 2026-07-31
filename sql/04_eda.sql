USE al_ahruf_analysis;

#How many surahs are there?
SELECT COUNT(*) AS Total_Surahs
FROM muqaththaah;

#How many Meccan and Madinan surahs are there?
SELECT
    Revelation_Period,
    COUNT(*) AS Total
FROM muqaththaah    
GROUP BY Revelation_Period;

#The most common Muqaththaah pattern
SELECT
    Pattern,
    COUNT(*) AS Total
FROM muqaththaah
GROUP BY Pattern
ORDER BY Total DESC;

#Average number of letters
SELECT
    AVG(Letter_Count) AS Average_Letters
FROM muqaththaah;

#The number of entries in each category of exegesis
SELECT
    Interpretation_Category,
    COUNT(*) AS Total
FROM muqaththaah
GROUP BY Interpretation_Category
ORDER BY Total DESC;

#A Surah that has five letters
SELECT
    Surah_Name,
    Muqaththaah
FROM muqaththaah
WHERE Letter_Count = 5;

#Just the Madani Surah
SELECT
    Surah_Name,
    Muqaththaah
FROM muqaththaah
WHERE Revelation_Period = 'Madinan';

#A Meccan surah that uses two letters
SELECT
    Surah_Name,
    Muqaththaah
FROM muqaththaah
WHERE Revelation_Period = 'Meccan'
AND Letter_Count = 2;

#Mini Project - Muqaththaah Report
SELECT
    Surah_Name,
    Surah_Number,
    Verse_Number,
    Muqaththaah,
    Pattern,
    Letter_Count,
    Revelation_Period,
    Interpretation_Category
FROM muqaththaah
ORDER BY 
    Letter_Count DESC,
    Surah_Name ASC;