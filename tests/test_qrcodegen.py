def test_qr_generation(client, app):
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
            'plant_id': 'PLNT003',
            'name': 'Aloe',
            'scientific_name': 'Aloe vera',
            'price': '10.00',
            'initial_price': '8.00',
            'image_url': ''
        })
        response = client.get('/qr/generate/1', follow_redirects=True)
        assert response.status_code == 200
