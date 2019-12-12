import json
from jose import jwt
from urllib.request import urlopen
from os import environ as env

AUTH0_DOMAIN = env.get('AUTH0_DOMAIN')
AUTH0_CLIENT_ID = env.get('AUTH0_CLIENT_ID')
API_AUDIENCE = env.get('API_IDENTIFIER')
AUTH0_CALLBACK_URL = env.get('AUTH0_CALLBACK_URL')
RESPONSE_TYPE = "token"
ALGORITHMS = ['RS256']

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik9VTXpPVE00TURFNFJUQkVNalkyUXpKRk1USTFRVUkzUTBGR05VSTNORFk0TjBJME9FSXdRdyJ9.eyJpc3MiOiJodHRwczovL2ZsYXNrYXBpLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTUzNDM3MzA3ODI3MDI3NTgyNiIsImF1ZCI6WyJBdXRoQ2FmZUFQSS1JZGVudGlmaWVyIiwiaHR0cHM6Ly9mbGFza2FwaS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc2MDQ3OTk0LCJleHAiOjE1NzYwNTUxOTQsImF6cCI6Ik16cG1OVDBIbTdaaXJkSFlaNldtNjVvWHBiN1c2bGNxIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbXX0.GaN01lFJmtI6W6RD4EetxgpMk8R45tmMsEVXZzNE4fW4tEWdQrNt9x1pLsuOp-ponxc_o8GyGoayVGrSyBoEuhAV6gzTSkd7yzI5ZNwd6m0FYz6_1rSrEDAEAVyurukd_WwPOiLH1HXJKvCinkV-Z9ZQ7GZmPL4Q4knQy4XaeUnQ5SdXvFfnmhKnctO8DE1xqBjh8HnuHsIbfG0fRII-MDlFuZxgXGq9JUgzm8WF3n93vVrJpR5sAB3k_YBu5NB8HuA8u6BuwMFZFfRiKRXM9f-CLuaKbMO3O1NN1Mz3UKDyqYJJxvlEYwBBcp3P68feb1di9H6L2x2pUQ5UxjF7GA&scope=openid%20profile%20email&expires_in=7200&token_type=Bearer&state=g6Fo2SBRcHNRNEszZ1VURU9NTUs2Ti1jTnNTei13Um0zZE9DcKN0aWTZIHBGSDFJbmwzeUU2aURmcW9abkJpWks4Z29QOEhrVzJao2NpZNkgTXpwbU5UMEhtN1ppcmRIWVo2V202NW9YcGI3VzZsY3E"


class AuthError(Exception):
    """ AuthError Exception: A standardized way to communicate auth failure modes
    """

    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Auth Header
def verify_decode_jwt(token):
    # GET THE PUBLIC KEY FROM AUTH0
    json_url = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(json_url.read())

    # GET THE DATA IN THE HEADER
    unverified_header = jwt.get_unverified_header(token)

    # CHOOSE OUR KEY
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            # USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
        'description': 'Unable to find the appropriate key.'
    }, 400)


if __name__ == '__main__':
    verify_decode_jwt(token)
