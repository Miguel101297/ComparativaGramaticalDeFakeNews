import tweepy
import json

# 4 cadenas para la autenticacion
consumer_key = "c1puDQIMq1MpDr88O20Mikuov"
consumer_secret = "9geqMXSPspTe0MQryxFIOZmOYAMMvtXGTJgo5auPLYOCTVIEQH"
access_token = "733698865-YkoekRV1T9rPbnAv929eWJKkzBqpx8JgBeUItPUw"
access_token_secret = "7FhXKuqw9ZWU9dWazcX0ujBRjtubZ4x7xaxsyWs8NU5VB"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# con este objeto realizaremos todas las llamadas al API
api = tweepy.API(auth,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
#Obtener informacion de otros usarios
data = api.get_user("elruinaversal")
print json.dumps(data._json, indent=4)
