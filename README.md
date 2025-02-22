# square_administration

## about

administration business layer for my personal server.

## Installation

```shell
pip install square_administration
```

## env

- python>=3.12.0

## changelog

### v3.0.0

- add new parameter -> password in authentication -> remove_app_for_self_v0.

### v2.4.0

- auto docker image build github action.

### v2.3.0

- env
    - add new variable COOKIE_DOMAIN.
- util
    - add is_https.
- authentication
    - add domain, exp_time, secure and http_only flags for cookies generated in login_username_v0, register_username_v0.

### v2.2.1

- authentication
    - add validation for refresh token app id in logout_v0, generate_access_token_v0.

### v2.2.0

- authentication
    - logout_v0, generate_access_token_v0 remove refresh token from request header and accept in cookie.

### v2.1.0

- add authentication -> logout_v0, generate_access_token_v0.

### v2.0.0

- remove refresh token from response body and send in cookies.

### v1.2.1

- fix bug in core -> get_all_greetings_v0, now sending full response instead of only main.

### v1.2.0

- set allow_credentials=True.

### v1.1.0

- add core -> get_all_greetings_v0.

### v1.0.0

- initial implementation.

## Feedback is appreciated. Thank you!