def get_user_id(conversation):
    """returns the _id used to send smooch requests"""
    return conversation["appUser"]["_id"]


def most_recent_msg(conversation, msg_from="appUser"):
    """returns most recent message from a given user type"""
    messages = [x for x in conversation["messages"] if x["role"] == msg_from]
    return messages[0]["text"]
