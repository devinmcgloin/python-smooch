import logging
from .endpoint import ask
from .exceptions import InvalidWebhookTrigger

possible_triggers = ["message", "message:appUser", "message:appMaker", "postback"]


def valid_triggers(triggers):
    return all([trig in possible_triggers for trig in triggers])


def list_webhooks():
    return ask('webhooks', {}, 'get')


def get_webhook(webhook_id):
    logging.debug("Get webhook: {}".format(webhook_id))
    return ask('webhooks/{}'.format(webhook_id), {}, "get")


def create_webhook(target, triggers=None):
    logging.debug("Creating webhook: {}".format(target))
    if triggers:
        if not valid_triggers(triggers):
            raise InvalidWebhookTrigger(triggers)
        return ask('webhooks', {"target": target, "triggers": triggers}, 'post')
    else:
        return ask('webhooks', {"target": target}, 'post')


def update_webhook(webhook_id, target, triggers=None):
    logging.debug("Updating webhook: {0} at {1}".format(webhook_id, target))
    if triggers:
        if not valid_triggers(triggers):
            raise InvalidWebhookTrigger(triggers)
        return ask('webhooks/{0}'.format(webhook_id), {"target": target, "triggers": triggers}, 'put')
    else:
        return ask('webhooks/{0}'.format(webhook_id), {"target": target}, 'put')


def delete_webhook(webhook_id):
    logging.debug("Deleting webhook: {}".format(webhook_id))
    return ask('webhooks/{0}'.format(webhook_id), {}, 'delete')


def delete_all_webhooks():
    webhooks_response = list_webhooks()
    webhooks = webhooks_response.json()['webhooks']

    responses = []
    for webhook in webhooks:
        dr = delete_webhook(webhook['_id'])
        responses.append(dr)

    return responses


def ensure_webhook_exist(trigger, webhook_url):
    logging.debug("Ensuring that webhook exist: %s; %s", trigger, webhook_url)
    r = list_webhooks()
    data = r.json()

    message_webhook_id = False
    message_webhook_needs_updating = False
    webhook_secret = None

    for value in data["webhooks"]:
        if trigger in value["triggers"]:
            message_webhook_id = value["_id"]
            webhook_secret = value["secret"]
            if value["target"] != webhook_url:
                message_webhook_needs_updating = True
            break

    logging.debug("message_webhook_id: %s", message_webhook_id)
    logging.debug("message_webhook_needs_updating: %s", message_webhook_needs_updating)
    if not message_webhook_id:
        logging.debug("Creating webhook")
        r = create_webhook(webhook_url, [trigger])
        data = r.json()
        message_webhook_id = data["webhook"]["_id"]
        webhook_secret = data["webhook"]["secret"]

    if message_webhook_needs_updating:
        logging.debug("Updating webhook")
        update_webhook(message_webhook_id, webhook_url, [trigger])

    return message_webhook_id, webhook_secret
