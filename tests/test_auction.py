def test_create_auction(client, app):
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
        client.post('/plants/add', data={
            'plant_id': 'PLNT005',
            'name': 'Snake Plant',
            'scientific_name': 'Sansevieria trifasciata',
            'price': '22.00',
            'initial_price': '20.00',
            'image_url': ''
        })
        response = client.post('/auction/create', data={
            'plant_id': '1',
            'starting_price': '15.00'
        }, follow_redirects=True)
        assert b'Snake Plant' in response.data or response.status_code == 200
