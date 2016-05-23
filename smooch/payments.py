from .endpoint import ask


def request_payment(user_id, message, short_text, amount):
    """Note that amount is a integer which specifies the amount of cents in the transaction"""
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
