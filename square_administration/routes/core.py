from fastapi import APIRouter
from square_database_helper.main import SquareDatabaseHelper

from square_administration.configuration import (
    config_str_square_database_ip,
    config_int_square_database_port,
    config_str_square_database_protocol,
)

router = APIRouter(
    tags=["core"],
)

global_object_square_database_helper = SquareDatabaseHelper(
    param_str_square_database_ip=config_str_square_database_ip,
    param_int_square_database_port=config_int_square_database_port,
    param_str_square_database_protocol=config_str_square_database_protocol,
)
