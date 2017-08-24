import time
import tweepy
from local_settings import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Get user name and followers count
user = api.get_user('twitter')
print(user.screen_name, user.followers_count)

# Push new your Twitter status
# api.update_status('Просто так твит ни о чём!')

# Publish three new tweets
image_path = '/tmp/'

tweets = [
    ['elephant.jpg', 'Белый слон рождается только в джунглях'],
    ['shark.jpg', 'Акула будет рада, если весь мир окажется под водой'],
    ['nature.jpg', 'Законы джунглей давно уже шагнули в города.']
]

for tweet in tweets:
    status = api.update_with_media(image_path + tweet[0], tweet[1])
    frm = 'Create new tweet: media_path - {0}, media_name - {1}, tweet_text {2}'
    print(frm.format(image_path, tweet[0], tweet[1]))
    time.sleep(60)
