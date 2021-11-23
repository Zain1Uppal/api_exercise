import json

def test_api_get_games(api):
    res = api.get('/Games')
    assert res.json == {'Game':'farcry 6'}

def test_api_not_found(api):
    res = api.get('/sleep')
    assert res.status == '404 NOT FOUND'
    assert 'Error' in res.json['message']