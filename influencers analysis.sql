SELECT *, 
       (Avg_Likes + Avg_Comments) / Followers AS Engagement_Ratio 
FROM influencers;

SELECT *
FROM influencers
WHERE Location IN ('California', 'Oregon', 'Washington', 'Nevada')
AND Followers BETWEEN 10000 AND 100000
ORDER BY Engagement_Rate DESC;

SELECT *, 
       (Avg_Likes + Avg_Comments) / Followers AS Engagement_Ratio
FROM influencers
WHERE Location IN ('California', 'Oregon', 'Washington', 'Nevada')
AND Followers BETWEEN 10000 AND 100000
ORDER BY Engagement_Ratio DESC;