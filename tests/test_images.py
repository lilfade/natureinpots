import io

def test_image_upload(client, app):
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

        # Create plant for reference
        client.post('/plants/add', data={
            'plant_id': 'PLNT001',
            'name': 'Monstera',
            'scientific_name': 'Monstera deliciosa',
            'price': '30.00',
            'initial_price': '25.00',
            'image_url': ''
        })

        data = {
            'plant_id': '1',
            'image': (io.BytesIO(b"test image content"), 'test.jpg')
        }
        response = client.post('/images/upload', data=data, content_type='multipart/form-data', follow_redirects=True)
        assert b'Monstera' in response.data
