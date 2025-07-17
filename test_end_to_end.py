import requests
# Minor change to trigger Jenkins build


def test_create_and_fetch_user():
    base_url = 'http://localhost:5000/users'

    # Step 1: Create a user
    payload = {
        'name': 'Test User',
        'email': 'testuser@example.com'
    }
    response = requests.post(base_url, json=payload)
    assert response.status_code == 200
    print("✅ POST /users successful")

    # Step 2: Fetch all users
    response = requests.get(base_url)
    assert response.status_code == 200
    users = response.json()

    # Step 3: Check that Test User is in the list
    found = any(u['name'] == 'Test User' and u['email'] == 'testuser@example.com' for u in users)
    assert found, "Test User not found in user list"
    print("✅ GET /users returned the expected user")
