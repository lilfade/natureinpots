def test_health_scan(client, app):
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
        # Add plant
        client.post('/plants/add', data={
            'plant_id': 'PLNT002',
            'name': 'Ficus',
            'scientific_name': 'Ficus elastica',
            'price': '20.00',
            'initial_price': '18.00',
            'image_url': ''
        })
        # Simulate scan call (image ID manually assumed as 1)
        response = client.get('/health/scan/1', follow_redirects=True)
        assert response.status_code == 200
