import os

import jwt


def jwt_token():
    return jwt.encode({'scope': 'app'},
                      SECRET,
                      algorithm='HS256',
                      headers={"kid": KEY_ID, "alg": "HS256"}).decode("utf-8")


def jwt_for_user(user_id):
    return jwt.encode({'scope': 'appUser', 'userId': user_id},
                      SECRET,
                      algorithm='HS256',
                      headers={"kid": KEY_ID,
                               "alg": "HS256"}).decode("utf-8")


KEY_ID = os.getenv("SMOOCH_KEY_ID")
SECRET = os.getenv("SMOOCH_SECRET")

JWT_TOKEN = jwt_token()
