import app

def test_index_route():
    app.app.testing = True
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Book an Appointment' in response.data
