from typing import Any, List

import tweepy

from src.secrets import apikey, apisecret, access, secret

def get_trends(woe_id: int) -> List[dict[str: Any]]:

    """Pega os principais tópicos do twitter

    Args:
        woe_id (int): identificador de localidade


    Returns:
        [type]: [description]
    """

    auth = tweepy.OAuthHandler(consumer_key=apikey, consumer_secret=apisecret)
    auth.set_access_token(access, secret)

    api = tweepy.API(auth)

    trends = api.trends_place(woe_id)

    return trends[0]["trends"]
