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
