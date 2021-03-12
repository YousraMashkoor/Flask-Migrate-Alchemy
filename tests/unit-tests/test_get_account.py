import json

def test_get_account(client, database):
    response = client.get(
        '/accounts'
    )

    data = json.loads(response.data)

    assert response.status_code == 200