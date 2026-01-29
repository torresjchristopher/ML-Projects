def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict_success(client):
    headers = {"Authorization": "Bearer super-secret"}
    sample = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=sample, headers=headers)
    assert response.status_code == 200
    assert "predicted_class" in response.json()

def test_predict_unauthorized(client):
    sample = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=sample)  # No token
    assert response.status_code == 401
