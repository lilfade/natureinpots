def test_register_and_login(client, app):
    with app.app_context():
        response = client.post('/auth/register', data={
            'username': 'tester',
            'email': 'test@example.com',
            'password': 'testpass'
        }, follow_redirects=True)
        assert b'Please log in' in response.data

        response = client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'testpass'
        }, follow_redirects=True)
        assert b'Logout' in response.data
