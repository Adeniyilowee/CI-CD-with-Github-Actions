import pytest
import sys

@pytest.fixture
def capture_stdout(monkeypatch):    # here fixture capture_stdout is also dependent on another in built fixture, called monkeypatch
    buffer = {"stdout": "", "write_calls": 0}    # Monkeypatch is crazy, see documentaries or watch video sgain Lol

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer


@pytest.fixture(scope="session")   # the session makes it possible to run this once and make all the output available to the function(s) that needs them
def db_conn():
    db = ...
    url = ...
    #with db.connect(url) as conn:  # connection will be torn down after all tests finish
    #    yield conn                 # used when we need some kind of connection, thus can be used for all functions that requires it
