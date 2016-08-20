# python-smooch
Python wrapper for the [Smooch API](http://docs.smooch.io/rest).


## Installation

```
$ pip install python-smooch
```

## Usage

Before using python-smooch you have to export your `SMOOCH_KEY_ID` and
`SMOOCH_SECRET` to your local environment.

```bash
export SMOOCH_KEY_ID="your_key_id"
export SMOOCH_SECRET="your_secret"
```

You can then import python-smooch with the following:

```python
import smooch
```

## API

This is a listing of the methods provided by python-smooch and the arguments
they take. I've only gone into detail in places where I made representational
choices. So you don't have to go through the code. The definitive API Docs are
from [Smooch](http://docs.smooch.io/rest).

### Messages
| Function         | Arguments                                                                   | Notes                                                    |
|:-----------------|:----------------------------------------------------------------------------|:---------------------------------------------------------|
| send_message     | user_id:string, plain_text:string, sent_by_maker=true                       |                                                          |
| get_conversation | user_id:string                                                              |                                                          |
| send_links       | user_id:string, message_text:string, options:[(tag, uri)]                   |                                                          |
| send_postbacks   | user_id:string, message_text:string, options:[(tag, postback payload)]      |                                                          |
| request_payment  | user_id:string, message_text:string, options:[(tag, price in cents)]        | Note [stripe](https://stripe.com) must be enabled.       |
| send_buttons     | user_id:string, message_text:string, options:[(message_text, kind, result)] | This allows you to mix button types in the same message. |

### Users
| Function        | Arguments                          | Notes |
|:----------------|:-----------------------------------|:------|
| pre_create_user | user_id:string                     |       |
| get_user        | user_id:string                     |       |
| update_user     | user_id:string, data:map           |       |
| init_user       | device:string, user_id:string=None |       |

### Webhooks
| Function             | Arguments                                        | Notes                                |
|:---------------------|:-------------------------------------------------|:-------------------------------------|
| get_webhook          | webhook_id:string                                |                                      |
| create_webhook       | target:uri, triggers:[string]                    | trigger types are defined by smooch. |
| list_webhooks        |                                                  |                                      |
| ensure_webhook_exist | target:uri, triggers:[string]                    | trigger types are defined by smooch. |
| delete_webhook       | webhook_id:string                                |                                      |
| delete_all_webhooks  |                                                  |                                      |
| update_webhook       | webhook_id:string, target:uri, triggers:[string] |                                      |

## License

[MIT License](https://opensource.org/licenses/MIT)
