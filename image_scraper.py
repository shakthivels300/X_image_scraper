
# Replace with your actual Bearer Token from Twitter Developer Portal
BEARER_TOKEN = "bearertokenadfdsasdf44"
USERNAME = "iYogiBabu"

# Authenticate using OAuth 2.0
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Get user ID from username
user = client.get_user(username=USERNAME)
user_id = user.data.id

# Fetch recent tweets (including media attachments)
tweets = client.get_users_tweets(
    id=user_id,
    max_results=50,  # Adjust the number of tweets to check
    tweet_fields=["attachments"],
    expansions=["attachments.media_keys"],
    media_fields=["url"]
)

# Create folder to save images
os.makedirs("images", exist_ok=True)

# Extract images
if tweets.includes and "media" in tweets.includes:
    for media in tweets.includes["media"]:
        if media["type"] == "photo":
            img_url = media["url"]
            img_name = os.path.join("images", img_url.split("/")[-1])

            # Download image
            img_data = requests.get("https://pbs.twimg.com/media/GieR-xGbYAAVxyY?format=jpg&name=900x900").content
            with open(img_name, "wb") as file:
                file.write(img_data)
            print(f"Downloaded: {img_name}")

print("Download complete!")