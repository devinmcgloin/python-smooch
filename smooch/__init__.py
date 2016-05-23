"""
smooch_python

__init__ is going to export all the code written in this module.
Makes it super easy for people to import smooch and call whatever they need.
"""
import os

if os.getenv("SMOOCH_KEY_ID") is None or os.getenv("SMOOCH_SECRET") is None:
    print("Smooch must have access to the SMOOCH_KEY_ID and SMOOCH_SECRET to operate."
          "\nSpecify environment variables in order to proceed."
          "\n'export SMOOCH_SECRET=\"your_smooch_secret\"'")
    exit(1)

from .conversations import (
    send_message, get_conversation
)

from .payments import request_payment

from .webhooks import (
    get_webhook, delete_all_webhooks, create_webhook,
    list_webhooks, ensure_webhook_exist, delete_webhook, update_webhook
)

from .app_users import (
    pre_create_user, get_user, update_user, init_user
)
