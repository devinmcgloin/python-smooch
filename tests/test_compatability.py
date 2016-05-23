from smooch import list_webhooks
import pytest
import smooch.exceptions


def test_compatability():
    with pytest.raises(smooch.exceptions.UnauthorizedRequestError):
        list_webhooks()
