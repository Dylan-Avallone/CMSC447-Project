-- Query data / Output randomized student counter 
SELECT 
    t1.timeBucket,
    (
        SELECT SUM(t2.netChange)
        FROM LibraryTraffic t2
        WHERE t2.timeBucket <= t1.timeBucket
    ) AS currentCount
FROM LibraryTraffic t1
ORDER BY t1.timeBucket;
