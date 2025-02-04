# Influencer Marketing Campaign for Toy Subscription Box

## Overview

As a marketing analyst at a toy box subscription company, you are starting an influencer marketing campaign, and your team wants to know which influencers you are potentially working with will have the most chance to get the highest return on investment. 

## Step 1: Collecting Influencer Data

First, collect the data from **FeedSpot**, which is a paid service provider that provides statistics for influencers across platforms in a CSV file.

### Scraping Instagram Influencers with Python

We can build a Python script to scrape Instagram influencers.

```python
import instaloader
import pandas as pd

# Initialize Instaloader
L = instaloader.Instaloader()

# Define hashtags related to maternity and baby products
hashtags = ["momlife", "babyproducts", "maternityfashion"]

influencers_data = []

for tag in hashtags:
    posts = instaloader.Hashtag.from_name(L.context, tag).get_posts()
    
    for post in posts:
        username = post.owner_username
        followers = post.owner_profile.followers
        engagement = post.likes / followers if followers > 0 else 0

        if 10000 <= followers <= 100000:  # Micro-influencers range
            influencers_data.append([username, followers, engagement])

        if len(influencers_data) >= 100:  # Limit results
            break

# Save to CSV
df = pd.DataFrame(influencers_data, columns=["Username", "Followers", "Engagement"])
df.to_csv("micro_influencers.csv", index=False)

print("CSV file saved successfully!")
```

## Step 2: Analyzing the Data

The dataset includes key details such as:

- **Influencer Name**
- **Username**
- **Location**
- **Followers**
- **Engagement Rate**
- **Niche**
- **Average Likes**
- **Average Comments**

### Engagement Rate Calculation

The Engagement Rate (ER) is a key metric used in influencer marketing to measure how actively an audience interacts with an influencer’s content.

#### Formula for Engagement Rate:

\[
\text{Engagement Rate (\%)} = \left(\frac{\text{Total Engagements}}{\text{Total Followers}}\right) \times 100
\]

Where:

- **Total Engagements** = Likes + Comments  
- **Total Followers** = Number of followers the influencer has

---

## Step 3: Filtering Influencers Using SQL

Considering the market and the product, we use SQL to perform the following:

1. **Filter influencers based on West Coast states**
2. **Filter for micro-influencers (10K - 100K followers)**
3. **Rank by Engagement Rate to prioritize highly engaged influencers**

```sql
SELECT *
FROM influencers
WHERE Location IN ('California', 'Oregon', 'Washington', 'Nevada')
  AND Followers BETWEEN 10000 AND 100000
ORDER BY Engagement_Rate DESC;
```

# Step 4: Engagement-to-Follower Ratio (Authenticity Check)

Instead of just using the engagement rate, we calculate the **Engagement-to-Follower Ratio** to identify influencers with a truly engaged audience.

#### Formula:
\[
\text{Engagement Ratio} = \frac{\text{Avg Likes} + \text{Avg Comments}}{\text{Followers}}
\]

```sql
SELECT *, 
       (Avg_Likes + Avg_Comments) / Followers AS Engagement_Ratio
FROM influencers
WHERE Location IN ('California', 'Oregon', 'Washington', 'Nevada')
  AND Followers BETWEEN 10000 AND 100000
ORDER BY Engagement_Ratio DESC;
```

# Step 5: Cost-Effectiveness Analysis (CPM & CPE)

If pricing data is available, we calculate the following metrics:

### Cost per Thousand Impressions (CPM):
\[
\text{CPM} = \left(\frac{\text{Cost}}{\text{Followers}}\right) \times 1000
\]

### Cost per Engagement (CPE):
\[
\text{CPE} = \frac{\text{Cost}}{\text{Avg Likes} + \text{Avg Comments}}
\]

```sql
SELECT *, 
       (Cost / Followers) * 1000 AS CPM, 
       (Cost / (Avg_Likes + Avg_Comments)) AS CPE
FROM influencers
WHERE Location IN ('California', 'Oregon', 'Washington', 'Nevada')
  AND Followers BETWEEN 10000 AND 100000
ORDER BY CPE ASC;
```
# Step 6: Comparing Influencer Performance

After generating two tables—one sorted by Engagement-to-Follower Ratio and the other by Engagement Rate—we perform key comparisons:

- **Overlapping Influencers:**  
  Identify influencers appearing in both lists. These influencers are highly engaged and authentic, making them top choices.

- **Followers vs. Engagement Rate:**  
  - Some influencers may have a high engagement rate but a low engagement-to-follower ratio, indicating a large following with a relatively passive audience.
  - Others may have a high engagement-to-follower ratio but a lower engagement rate, meaning they have a smaller yet more dedicated audience.

- **Content Authenticity vs. Viral Potential:**  
  - A high engagement-to-follower ratio suggests a more authentic audience.
  - A high engagement rate indicates a greater chance of virality, even if the engagement-to-follower ratio is lower.

