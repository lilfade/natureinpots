def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code in (302, 401)
