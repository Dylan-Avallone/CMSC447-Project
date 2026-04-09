CREATE VIEW LibraryTraffic AS
SELECT 
    FROM_UNIXTIME(FLOOR(UNIX_TIMESTAMP(eventTime) / 300) * 300) AS timeBucket,
    SUM(CASE 
        WHEN eventType = 'ENTER' THEN 1
        WHEN eventType = 'EXIT' THEN -1
    END) AS netChange
FROM GateEvents
GROUP BY timeBucket;
