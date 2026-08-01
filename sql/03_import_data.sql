-- ==========================================
-- AL-AHRUF AL-MUQATHTHAAH ANALYSIS
-- Import Data
-- ==========================================

USE al_ahruf_analysis;

INSERT INTO muqaththaah
(
    Surah_Name,
    Surah_Number,
    Verse_Number,
    Muqaththaah,
    Pattern,
    Letter_Count,
    Revelation_Period,
    Interpretation_Category
)
VALUES
('Al-Baqarah',2,1,'الم','Three Letters',3,'Madinan','Multiple Interpretations'),
('Ali ''Imran',3,1,'الم','Three Letters',3,'Madinan','Multiple Interpretations'),
('Al-A''raf',7,1,'المص','Four Letters',4,'Meccan','Only Allah Knows'),
('Yunus',10,1,'الر','Three Letters',3,'Meccan','Only Allah Knows'),
('Hud',11,1,'الر','Three Letters',3,'Meccan','Only Allah Knows'),
('Yusuf',12,1,'الر','Three Letters',3,'Meccan','Only Allah Knows'),
('Ar-Ra''d',13,1,'المر','Four Letters',4,'Madinan','Only Allah Knows'),
('Ibrahim',14,1,'الر','Three Letters',3,'Meccan','Only Allah Knows'),
('Al-Hijr',15,1,'الر','Three Letters',3,'Meccan','Only Allah Knows'),
('Maryam',19,1,'كهيعص','Five Letters',5,'Meccan','Only Allah Knows'),
('Ta-Ha',20,1,'طه','Two Letters',2,'Meccan','Prophet''s Name'),
('Ash-Shu''ara''',26,1,'طسم','Three Letters',3,'Meccan','Only Allah Knows'),
('An-Naml',27,1,'طس','Two Letters',2,'Meccan','Only Allah Knows'),
('Al-Qasas',28,1,'طسم','Three Letters',3,'Meccan','Only Allah Knows'),
('Al-''Ankabut',29,1,'الم','Three Letters',3,'Meccan','Only Allah Knows'),
('Ar-Rum',30,1,'الم','Three Letters',3,'Meccan','Only Allah Knows'),
('Luqman',31,1,'الم','Three Letters',3,'Meccan','Only Allah Knows'),
('As-Sajdah',32,1,'الم','Three Letters',3,'Meccan','Only Allah Knows'),
('Ya-Sin',36,1,'يس','Two Letters',2,'Meccan','Prophet''s Name'),
('Sad',38,1,'ص','One Letter',1,'Meccan','Only Allah Knows'),
('Ghafir',40,1,'حم','Two Letters',2,'Meccan','Only Allah Knows'),
('Fussilat',41,1,'حم','Two Letters',2,'Meccan','Only Allah Knows'),
('Ash-Shura',42,1,'حم','Two Letters',2,'Meccan','Only Allah Knows'),
('Ash-Shura',42,2,'عسق','Three Letters',3,'Meccan','Only Allah Knows'),
('Az-Zukhruf',43,1,'حم','Two Letters',2,'Meccan','Only Allah Knows'),
('Ad-Dukhan',44,1,'حم','Two Letters',2,'Meccan','Only Allah Knows'),
('Al-Jathiyah',45,1,'حم','Two Letters',2,'Meccan','Only Allah Knows'),
('Al-Ahqaf',46,1,'حم','Two Letters',2,'Meccan','Only Allah Knows'),
('Qaf',50,1,'ق','One Letter',1,'Meccan','Only Allah Knows'),
('Al-Qalam',68,1,'ن','One Letter',1,'Meccan','Only Allah Knows');