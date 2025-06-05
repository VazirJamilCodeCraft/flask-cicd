def test_status_response():
    from app import app
    client = app.test_client()
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json['status'] == 'App is running'
