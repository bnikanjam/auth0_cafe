"""Build Auth0 Login URL
"""

import webbrowser
from os import environ as env

AUTH0_DOMAIN = env.get('AUTH0_DOMAIN')
AUTH0_CLIENT_ID = env.get('AUTH0_CLIENT_ID')
API_AUDIENCE = env.get('API_IDENTIFIER')
AUTH0_CALLBACK_URL = env.get('AUTH0_CALLBACK_URL')
RESPONSE_TYPE = "token"


def build_login_url():
    login_url = "https://{}/authorize?audience={}&response_type={}&client_id={}&redirect_uri={}" \
        .format(
            AUTH0_DOMAIN,
            API_AUDIENCE,
            RESPONSE_TYPE,
            AUTH0_CLIENT_ID,
            AUTH0_CALLBACK_URL
        )
    return login_url


if __name__ == "__main__":
    auth0_login_url = build_login_url()
    webbrowser.open(auth0_login_url)
