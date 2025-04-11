import pytest


@pytest.fixture
def set_env(monkeypatch):
    monkeypatch.setenv("SQUARE_DATABASE_PROTOCOL", "http")
    monkeypatch.setenv("SQUARE_DATABASE_IP", "raspi.thepmsquare.com")
    monkeypatch.setenv("SQUARE_DATABASE_PORT", "20010")
    monkeypatch.setenv("SQUARE_AUTHENTICATION_PROTOCOL", "http")
    monkeypatch.setenv("SQUARE_AUTHENTICATION_IP", "raspi.thepmsquare.com")
    monkeypatch.setenv("SQUARE_AUTHENTICATION_PORT", "20011")
