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

### v3.4.0

- authentication
    - add update_password_v0.

### v3.3.1

- authentication
    - move refresh token to cookie in register_login_google_v0, reset_password_and_login_using_backup_code_v0 and
      reset_password_and_login_using_reset_email_code_v0.

### v3.3.0

- authentication
    - add new endpoint -> register_login_google_v0.
    - add new endpoint -> reset_password_and_login_using_backup_code_v0.
    - add new endpoint -> reset_password_and_login_using_reset_email_code_v0.

### v3.2.2

- remove config.ini and config.testing.ini from version control.

### v3.2.1

- testing
    - update get_patched_configuration and create_client_and_cleanup to be session scoped.
- env
    - add ALLOW_ORIGINS

### v3.2.0

- move global_int_app_id getting logic from configuration.py to utils->common
- env
    - add DB_IP, DB_PORT, DB_USERNAME, DB_PASSWORD
    - add config.testing.ini
    - file path reading through os.path.join method.
- testing
    - add conftest file to create and cleanup test database, also to patch config file.
    - update existing tests to use the new fixtures.

### v3.1.1

- bump square_logger to 2.0.0

### v3.1.0

- add pytest as dependency.
- add dummy test case.

### v3.0.2

- update logic to get usernames for non-anonymous greetings in get_all_greetings_v0.

### v3.0.1

- add logging decorator to all functions.

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