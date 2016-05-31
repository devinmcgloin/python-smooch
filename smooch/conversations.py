from .endpoint import ask
import logging


def send_message(user_id, message, sent_by_maker=True):
    logging.debug("Sending message: user_id={0} message={1} sent_by_make={2}".format(user_id, message, sent_by_maker))
    role = "appMaker"
    if not sent_by_maker:
        role = "appUser"

    data = {"text": message, "role": role}
    return ask('appusers/{0}/conversation/messages'.format(user_id),
               data,
               'post')


def get_conversation(user_id):
    logging.debug("Get conversation: user_id={}".format(user_id))
    return ask('appusers/{0}/conversation'.format(user_id), {}, 'get')


def request_payment(user_id, message,  options):
    """Note that amount is a integer which specifies the amount of cents in the transaction
    Smooch will default to the currency specified in your account settings."""
    role = "appMaker"

    buttons = []

    for short_text, result in options:
        buttons.append({
            "type": "buy",
            "text": short_text,
            "amount": result})

    data = {"text": message,
            "role": role,
            "actions": buttons}
    return ask('appusers/{0}/conversation/messages'.format(user_id),
               data,
               'post')

def send_links(user_id, message, options):
    """Sends a series of links. The options field is a dictionary in which the keys are
    descriptions and values uris"""
    role = "appMaker"

    buttons = []

    for short_text, result in options:
        buttons.append({
            "type": "link",
            "text": short_text,
            "uri": result})

    data = {"text": message,
            "role": role,
            "actions": buttons}
    return ask('appusers/{0}/conversation/messages'.format(user_id),
               data,
               'post')

def send_postbacks(user_id, message, options):
    """Sends a series of options that you can listen for on your webhook. The options field is a dictionary in which the keys are
    descriptions and values the postback payload. You need to set up a webhook to listen for the postback."""
    role = "appMaker"

    buttons = []

    for short_text, result in options:
        buttons.append({
            "type": "postback",
            "text": short_text,
            "payload": result
        })

    data = {"text": message,
            "role": role,
            "actions": buttons}
    return ask('appusers/{0}/conversation/messages'.format(user_id),
               data,
               'post')

def send_buttons(user_id, message, options):
    """Options is a list of tuples in which the first element is the type of the button,
    second the short text, and third the result for the specified type."""

    role = "appMaker"

    buttons = []

    for text, kind, result in options:
        buttons.append({
            "type": kind,
            "text": text,
            "payload": result
        })

    data = {"text": message,
            "role": role,
            "actions": buttons}

    return ask('appusers/{0}/conversation/messages'.format(user_id),
               data,
               'post')