import json

def test_api_get_games(api):
    res = api.get('/Games')
    assert res.json == {'Game': {'name':'farcry 6'}}

def test_api_post_games(api):
    mock_data = json.dumps({"name":"game1"})
    mock_headers = {'Content-Type': 'application/json'}
    res = api.post('/Games', data=mock_data, headers=mock_headers)
    assert res.json['Games']['name'] == "game1"

def test_api_not_found(api):
    res = api.get('/sleep')
    assert res.status == '404 NOT FOUND'
    assert 'Error' in res.json['message']