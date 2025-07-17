import requests

def test_create_and_fetch_user():
    url = 'http://localhost:5000/users'
    payload = {'name': 'John Doe', 'email': 'john@example.com'}

    r = requests.post(url, json=payload)
    assert r.status_code == 200

    r2 = requests.get(url)
    data = r2.json()
    assert any(u['name'] == 'John Doe' for u in data)
