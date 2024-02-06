-- Some changes where made, regarding attributes for particular relations, from the original ER-Model after a more detailed analysis.

DROP TABLE IF EXISTS AnimeInfo;
DROP TABLE IF EXISTS ShowDescription;
DROP TABLE IF EXISTS AnimeRatings;
DROP TABLE IF EXISTS BroadcastInfo;
DROP TABLE IF EXISTS Production;
DROP TABLE IF EXISTS Music;
DROP TABLE IF EXISTS UserInfo;
DROP TABLE IF EXISTS UserStats;
DROP TABLE IF EXISTS UserActivity;
DROP TABLE IF EXISTS OnlineHistory;
DROP TABLE IF EXISTS ShowsWatched;
DROP TABLE IF EXISTS UserRatings;

-- rank is a reserved word, so we enclose it by ``.
CREATE TABLE AnimeInfo (
    animeID INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    titleEnglish VARCHAR(200),
    source VARCHAR(15) NOT NULL,
    episodes INT NOT NULL,
    status VARCHAR(30),
    airing TINYINT(1), -- MySQL does not support booleans.
    rating VARCHAR(30),
    score DECIMAL(4,2),
    `rank` INT, 
    durationPerEpisode VARCHAR(50)
);

-- Make sure that rank is a positive value:
ALTER TABLE AnimeInfo
ADD CONSTRAINT positive_rank CHECK (`rank` >= 0);

CREATE INDEX idx_title ON AnimeInfo (title);

-- Load Data to our table:
LOAD DATA INFILE '/var/lib/mysql-files/AnimeInfo.csv'
    INTO TABLE AnimeInfo
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;


CREATE TABLE ShowDescription (
    title VARCHAR(100) PRIMARY KEY,
    animeID INT NOT NULL,
    titleSynonyms VARCHAR(300),
    type VARCHAR(20),
    aired VARCHAR(50),
    airedFrom DATE,
    airedTo DATE,
    FOREIGN KEY (animeID) REFERENCES AnimeInfo(animeID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Load Data to our table:
LOAD DATA INFILE '/var/lib/mysql-files/ShowDescription.csv'
    INTO TABLE ShowDescription
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (title, animeID, titleSynonyms, type, aired, @airedFrom, @airedTo)
    SET airedFrom = STR_TO_DATE(@airedFrom, '%m/%d/%Y'),
        airedTo = STR_TO_DATE(@airedTo, '%m/%d/%Y');

CREATE TABLE AnimeRatings (
    scoredBy INT NOT NULL,
    animeID INT,
    duration VARCHAR(50),
    popularity INT,
    members INT,
    favorites INT,
    PRIMARY KEY (scoredBy, animeID),
    FOREIGN KEY (animeID) REFERENCES AnimeInfo(animeID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Make sure that specific attributes is a positive value:
ALTER TABLE AnimeRatings
ADD CONSTRAINT positive_members CHECK (members >= 0);
ALTER TABLE AnimeRatings
ADD CONSTRAINT favorites_members CHECK (favorites >= 0);

-- Load Data to our table:
LOAD DATA INFILE '/var/lib/mysql-files/AnimeRatings.csv'
    INTO TABLE AnimeRatings
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;

CREATE TABLE BroadcastInfo (
    title VARCHAR(100),
    aired VARCHAR(100),
    background VARCHAR(1500),
    premiered VARCHAR(30),
    broadcasted VARCHAR(50),
    PRIMARY KEY (title, aired),
    FOREIGN KEY (title) REFERENCES ShowDescription(title) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Load Data to our table:
LOAD DATA INFILE '/var/lib/mysql-files/BroadcastInfo.csv'
    INTO TABLE BroadcastInfo
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;

CREATE TABLE Production (
    studio VARCHAR(200),
    title VARCHAR(100),
    producer VARCHAR(500) NOT NULL,
    licensor VARCHAR(100) NOT NULL,
    genre VARCHAR(200) NOT NULL,
    PRIMARY KEY (studio, title)
    -- There seems to be some data incosistency in field title, so we skip a foreign key here.
    -- We can still "suboptimally" perform join operations on this attribute with other relations.
);

-- Make sure that genre doesn't contain numeric characters:
ALTER TABLE Production
ADD CONSTRAINT check_genre CHECK (genre REGEXP '^[^0-9]*$');

-- Load Data to our table:
LOAD DATA INFILE '/var/lib/mysql-files/Production.csv'
    INTO TABLE Production
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;

CREATE TABLE Music (
    openingTheme VARCHAR(700) PRIMARY KEY,
    title VARCHAR(100),
    premiered VARCHAR(30),
    studio VARCHAR(200),
    endingTheme VARCHAR(800) NOT NULL
);

-- Load Data to our table:
LOAD DATA INFILE '/var/lib/mysql-files/Music.csv'
    INTO TABLE Music
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;

CREATE TABLE UserInfo (
    userID INT NOT NULL,
    username VARCHAR(30),
    gender ENUM('Male', 'Female', 'Non-Binary'),
    location VARCHAR(100),
    birthDate DATE,
    PRIMARY KEY (userID, username)
);

CREATE INDEX idx_username ON UserInfo (username);

-- Load Data to our table:
LOAD DATA INFILE '/var/lib/mysql-files/UserInfo.csv'
    INTO TABLE UserInfo
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (userID, username, gender, location, @birthDate)
    SET birthDate = STR_TO_DATE(@birthDate, '%m/%d/%Y');

CREATE TABLE UserStats ( 
    userID INT,
    meanScore DECIMAL(4,2),
    statsRewatched INT,
    statsEpisode INT,
    PRIMARY KEY (userID, meanScore)
);

-- Load Data to our table:
LOAD DATA INFILE '/var/lib/mysql-files/UserStats.csv'
    INTO TABLE UserStats
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;


CREATE TABLE UserActivity (
    userID INT PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    userWatching INT,
    userCompleted INT,
    userOnHold INT,
    userDropped INT,
    userPlanToWatch INT,
    FOREIGN KEY (username) REFERENCES UserInfo(username) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Load Data to our table:
LOAD DATA INFILE '/var/lib/mysql-files/UserActivity.csv'
    INTO TABLE UserActivity
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;

CREATE TABLE OnlineHistory (
    userID INT,
    username VARCHAR(30),
    daysWatched DECIMAL(12,9),
    joinDate DATE NOT NULL,
    lastOnline DATE NOT NULL,
    PRIMARY KEY (userID, username),
    FOREIGN KEY (userID) REFERENCES UserInfo(userID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- We have to make sure that lastOnline does not precede joinDate:
ALTER TABLE OnlineHistory
ADD CONSTRAINT check_dates CHECK (STR_TO_DATE(lastOnline, '%Y-%m-%d') >= STR_TO_DATE(joinDate, '%Y-%m-%d'));

-- Load Data to our table:
LOAD DATA INFILE '/var/lib/mysql-files/OnlineHistory.csv'
    INTO TABLE OnlineHistory
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (userID, username, daysWatched, @joinDate, @lastOnline)
    SET joinDate = STR_TO_DATE(@joinDate, '%m/%d/%Y'),
        lastOnline = STR_TO_DATE(@lastOnline, '%m/%d/%Y');

CREATE TABLE ShowsWatched (
    animeID INT,
    username VARCHAR(30),
    PRIMARY KEY (animeID, username)
);

-- Load Data to our table:
LOAD DATA INFILE '/var/lib/mysql-files/ShowsWatched.csv'
    INTO TABLE ShowsWatched
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;

-- An user can only see his/her own ratings:
CREATE TABLE UserRatings(
    userID INT,
    animeID INT,
    personalScore DECIMAL(4,2),
    liked TINYINT(1),
    PRIMARY KEY (userID, animeID)
);

-- An user will only be able to like his top 10 favorite animes (for testing purposes of this prototype).
-- So, we need a trigger to check this:

DELIMITER //  
CREATE TRIGGER ratingsLimit
BEFORE INSERT ON UserRatings
FOR EACH ROW
BEGIN
    DECLARE numberOfLikes INT;
    SELECT COUNT(*) INTO numberOfLikes FROM UserRatings
    WHERE userID = NEW.userID AND liked = 1;
    IF numberOfLikes > 9 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'You can only like your top 10 anime shows.';
    END IF;
END//
