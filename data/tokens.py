"""tokens.py

The module provides the data to the program.

"""


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
API_KEY = "AIzaSyAgddL1nFKDhUNuiEAPFNUD-kNktOratbU"


def auth():
    """The function asks data to access twitter API

    () -> (dict)

    """
    consumer_key = input("consumer key: ")
    consumer_secret = input("consumer secret: ")
    token_key = input("token key: ")
    token_secret = input("token secret: ")

    return {
        "consumer_key": consumer_key,
        "consumer_secret": consumer_secret,
        "token_key": token_key,
        "token_secret": token_secret
    }
