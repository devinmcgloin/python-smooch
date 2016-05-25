# python-smooch
Python wrapper for the [Smooch API](http://docs.smooch.io/rest).


## Installation

```
$ pip install python-smooch
```

## Usage
Before using python-smooch you have to export your `SMOOCH_KEY_ID` and `SMOOCH_SECRET`
to your local environment.

```
export SMOOCH_KEY_ID="your_key_id"
export SMOOCH_SECRET="your_secret"
```

## API

This is a listing of the methods provided by python-smooch and the arguments they take.
I've only gone into detail in places where I made representational choices. So you don't have to go
through the code. The definitive API Docs are from [Smooch](http://docs.smooch.io/rest).

### Messages

* send_message
    * user_id
    * plain_text
    * sent_by_maker is assumed to be true. Optionally false.
* get_conversation
    * user_id

For all the following methods options is a python dictionary in which the keys are the short discription.
* send_links
    * user_id
    * message_text
    * options is a python dict, values are uris
* send_postbacks
    * user_id
    * message_text
    * options is a python dict, values the postback payload. You need to set up a webhook to listen for the postback.
* request_payment
    * user_id
    * message_text
    * options is a python dict, values are the amount of the transaction. Amounts are specified in cents in the default currency. Need Stripe for this to work.

* send_buttons
    * user_id
    * message_text
    * options is an array of tuples. with (message_text, kind, result). This allows you to mix buttons.

### Users

* pre_create_user
    * user_id
* get_user
    * user_id
* update_user
    * user_id
    * data
* init_user
    * device
    * user_id (optional)

### Webhooks

* get_webhook
    * webhook_id
* create_webhook
    * target
    * triggets
* list_webhooks
* ensure_webhook_exist
    * target
    * trigger
* delete_webhook
    * webhook_id
* delete_all_webhooks
* update_webhook

## License

[MIT License](https://opensource.org/licenses/MIT)