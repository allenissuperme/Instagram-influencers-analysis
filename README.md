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
