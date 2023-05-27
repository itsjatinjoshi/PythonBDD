
import tweepy

api_key = "S0cpL8dp0BjM4YSEzESKpYmO0"
api_secrets = "rCzqYxxFuW6IcpXCTZHUR9w7QpupfdGaRfeJQSsN2HMbu6D42y"
access_token = "286092861-axs5Vc6y7ZVwSJYRzpwgowfzODssEwzIEnz298UZ"
access_secret = "Sng6RyGh6XCbL6HlgmREfjKiJDYMFsUFvi3qlUNqfAI9W"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')