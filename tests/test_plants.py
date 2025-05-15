def test_plant_creation(client, app):
    with app.app_context():
        client.post('/auth/register', data={
            'username': 'tester',
            'email': 'test@example.com',
            'password': 'testpass'
        })
        client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'testpass'
        })
        response = client.post('/plants/add', data={
            'plant_id': 'PLNT001',
            'name': 'Monstera',
            'scientific_name': 'Monstera deliciosa',
            'price': '30.00',
            'initial_price': '25.00',
            'image_url': 'http://example.com/image.png'
        }, follow_redirects=True)
        assert b'Monstera' in response.data
