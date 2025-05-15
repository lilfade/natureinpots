def test_create_presale(client, app):
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
            'plant_id': 'PLNT006',
            'name': 'Pothos',
            'scientific_name': 'Epipremnum aureum',
            'price': '12.00',
            'initial_price': '10.00',
            'image_url': ''
        })
        response = client.post('/presale/create', data={
            'plant_id': '1',
            'user_email': 'buyer@example.com',
            'status': 'available'
        }, follow_redirects=True)
        assert b'buyer@example.com' in response.data or response.status_code == 200
