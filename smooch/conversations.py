from .endpoint import ask


def send_message(user_id, message, sent_by_maker=True):
    role = "appMaker"
    if not sent_by_maker:
        role = "appUser"

    data = {"text": message, "role": role}
    return ask('appusers/{0}/conversation/messages'.format(user_id),
               data,
               'post')


def get_conversation(user_id):
    return ask('appusers/{0}/conversation'.format(user_id), {}, 'get')

