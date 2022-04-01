import pytest

@pytest.fixture(scope="session")
def get_token():
    token = "fcfcfedef925f9b5207127d64afad8e765cff8fddeae1ade14095165f89bd963"
    return token

