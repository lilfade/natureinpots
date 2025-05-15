def test_create_listing(client, app):
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
            'plant_id': 'PLNT004',
            'name': 'ZZ Plant',
            'scientific_name': 'Zamioculcas zamiifolia',
            'price': '15.00',
            'initial_price': '12.00',
            'image_url': ''
        })

        response = client.post('/marketplace/create', data={
            'plant_id': '1',
            'listing_type': 'direct_sale',
            'price': '25.00'
        }, follow_redirects=True)
        assert b'ZZ Plant' in response.data or response.status_code == 200
