from fastapi.testclient import TestClient
from square_commons import get_api_output_in_standard_format


def test_read_main(set_env):
    from square_administration.configuration import config_str_module_name
    from square_administration.main import (
        app,
    )

    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == get_api_output_in_standard_format(
        log=config_str_module_name
    )
