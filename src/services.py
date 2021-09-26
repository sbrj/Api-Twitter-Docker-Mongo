from typing import Any, Literal
import tweepy

from src.secrets import apikey, apisecret, access, secret

def get_trends(woe_id: int) -> list[dict[Literal: Any]]:

    auth = tweepy.OAuthHandler(consumer_key=apikey, consumer_secret=apisecret)
    auth.set_access_token(access, secret)

    api = tweepy.API(auth)

    trends = api.trends_place(woe_id)

    return trends[0]['trends']
