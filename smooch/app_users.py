"""

"""

import logging
from .endpoint import ask


def get_user(user_id):
    logging.debug("Get user: {}".format(user_id))
    return ask('appusers/{0}'.format(user_id), {}, 'get')


def update_user(user_id, data):
    """It's left to the user to build the payload themselves.
    Look at http://docs.smooch.io/rest/#update for documentation"""
    logging.debug("Uptating user: user_id={}".format(user_id))
    return ask('appusers/{0}'.format(user_id), data, 'put')


def init_user(device, user_id=None):
    """ If you're specifying a userId then in order to keep conversations private
    we strongly suggest authenticating your users. If a userId is used without a
    JWT credential, then anyone who can discover a user's userId could potentially
    eavesdrop on the conversation."""
    logging.debug("Initializing user: device={0} user_id={1}".format(device, user_id))
    if user_id:
        data = {
            "device": {
                "id": device,
                "platform": "other"
            },
            "userId": user_id
        }
    else:
        data = {
            "device": {
                "id": device,
                "platform": "other"
            }
        }
    return ask('init', data, 'post')


def pre_create_user(user_id):
    logging.debug("pre_create_user: {}".format(user_id))
    data = {
        "userId": user_id
    }
    return ask('appusers', data, 'post')

