-- ==========================================
-- AL-AHRUF AL-MUQATHTHAAH ANALYSIS
-- Exploratory Data Analysis (EDA)
-- Author : Arnawan Dwi Nugraha
-- ==========================================

USE al_ahruf_analysis;

-- ==========================================
-- SECTION 1
-- Dataset Overview
-- ==========================================

-- Total Number of Surahs

-- Distribution by Revelation Period

-- Distribution of Muqaththaah Patterns

SELECT COUNT(*) AS Total_Surahs
FROM muqaththaah;

SELECT
    Revelation_Period,
    COUNT(*) AS Total
FROM muqaththaah    
GROUP BY Revelation_Period;

SELECT
    Pattern,
    COUNT(*) AS Total
FROM muqaththaah
GROUP BY Pattern
ORDER BY Total DESC;

-- ==========================================
-- SECTION 2
-- Statistical Summary
-- ==========================================

-- Average Number of Muqaththaah Letters

SELECT
    AVG(Letter_Count) AS Average_Letters
FROM muqaththaah;

-- ==========================================
-- SECTION 3
-- Category Analysis
-- ==========================================

-- Distribution of Interpretation Categories

SELECT
    Interpretation_Category,
    COUNT(*) AS Total
FROM muqaththaah
GROUP BY Interpretation_Category
ORDER BY Total DESC;

-- ==========================================
-- SECTION 4
-- Filtering Queries
-- ==========================================

-- Surahs with Five-Letter Muqaththaah

-- Madinan Surahs with Muqaththaah

-- Meccan Surahs with Two-Letter Muqaththaah

SELECT
    Surah_Name,
    Muqaththaah
FROM muqaththaah
WHERE Letter_Count = 5;

SELECT
    Surah_Name,
    Muqaththaah
FROM muqaththaah
WHERE Revelation_Period = 'Madinan';

SELECT
    Surah_Name,
    Muqaththaah
FROM muqaththaah
WHERE Revelation_Period = 'Meccan'
AND Letter_Count = 2;

-- ==========================================
-- FINAL REPORT
-- Comprehensive Muqaththaah Report
-- ==========================================

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