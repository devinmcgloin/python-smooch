from .endpoint import ask
import logging

def request_payment(user_id, message, short_text, amount):
    """Note that amount is a integer which specifies the amount of cents in the transaction"""
    logging.debug("Requesting payment: user_id={0} message={1} short_text={2} amount={3}"
                  .format(user_id, message, short_text, amount))
    role = "appMaker"

    data = {"text": message,
            "role": role,
            "actions": [{
                "type": "buy",
                "text": short_text,
                "amount": amount
            }]}
    return ask('appusers/{0}/conversation/messages'.format(user_id),
                        data,
                        'post')
