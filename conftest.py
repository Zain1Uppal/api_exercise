import pytest
import server

@pytest.fixture
def api(monkeypatch):
    test_game = 'farcry 6'
    monkeypatch.setattr(server, "Games", test_game)
    api = server.app.test_client()
    return api