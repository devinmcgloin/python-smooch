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

