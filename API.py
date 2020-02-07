import tweepy
import json

# 4 cadenas para la autenticacion
consumer_key = "c1puDQIMq1MpDr88O20Mikuov"
consumer_secret = "9geqMXSPspTe0MQryxFIOZmOYAMMvtXGTJgo5auPLYOCTVIEQH"

access_token = "733698865-K7vUXj8FwCknXeFRec2tIUDHhOeiqDbryQDonhBV"
access_token_secret= "hooloYnM31HZnHqbTw0NY5e1lY9bgjXAKgpqwpXqNp0Mk"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# con este objeto realizaremos todas las llamadas al API
api = tweepy.API(auth,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

#Obtener informacion de un usario
data = api.me()
print (data)

#Obtener informacion de otros usarios
data = api.get_user("elruinaversal")
print (data)

#Obtener followers
data = api.followers(screen_name="elruinaversal")

for user in data:
    print (data)
 # Explicar cursor
for user in tweepy.Cursor(api.followers, screen_name="elruinaversal").items():
   print (data)

#Obtener followees
for user in tweepy.Cursor(api.friends, screen_name="elruinaversal").items(2):
    print (data)

#Obtener un timeline
for tweet in tweepy.Cursor(api.user_timeline, screen_name="elruinaversal", tweet_mode="extended").items(10):
   print (data)

#Buscar Tweets
for tweet in tweepy.Cursor(api.search, q="Politica", tweet_mode="extended").items(5):
   print (data)
