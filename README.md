# python-smooch
Python wrapper for the [Smooch API](http://docs.smooch.io/rest).


## Installation
This will be on PyPI shortly. Currently you have to download the source and link it.
```
$ pip install smooch
```

## Usage

## API
| Module        | Method              | Endpoint                                                                                  |
|---------------|---------------------|-------------------------------------------------------------------------------------------|
| appUsers      | init_user           | [POST `/v1/init`](http://docs.smooch.io/rest/#init-beta)                                  |
|               | get_user            | [GET `/v1/appusers/:id`](http://docs.smooch.io/rest/#get-app-user)                        |
|               | update_user         | [PUT `/v1/appusers/:id`](http://docs.smooch.io/rest/#update-app-user)                     |
|               | track_event         | [POST `/v1/appusers/:id/events`](http://docs.smooch.io/rest/#track-event)                 |
|               | pre_create_user     | [POST `/v1/appusers`](http://docs.smooch.io/rest/#pre-create-app-user)                    |
| conversations | get_conversation    | [GET `/v1/appusers/:id/conversation`](http://docs.smooch.io/rest/#get-conversation)       |
|               | send_message        | [POST `/v1/appusers/:id/conversation/messages`](http://docs.smooch.io/rest/#post-message) |
| webhooks      | list_webhooks       | [GET `/v1/webhooks`](http://docs.smooch.io/rest/#list-webhook)                            |
|               | create_webhook      | [POST `/v1/webhooks`](http://docs.smooch.io/rest/#create-webhook)                         |
|               | get_webhook         | [GET `/v1/webhooks/:id`](http://docs.smooch.io/rest/#get-webhook)                         |
|               | update_webhook      | [PUT `/v1/webhooks/:id`](http://docs.smooch.io/rest/#update-webhook)                      |
|               | delete_webhook      | [DELETE `/v1/webhooks/:id`](http://docs.smooch.io/rest/#delete-webhook)                   |
|               | delete_all_webhooks | [DELETE `/v1/webhooks/:id`](http://docs.smooch.io/rest/#delete-webhook)                   |
| payments      | request_payment     |                                                                                           |