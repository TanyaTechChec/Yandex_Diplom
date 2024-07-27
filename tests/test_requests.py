import sender_stand_request
import data

def test_order_creation_and_retrieval():
    response = sender_stand_request.create_order(data.order_body)
    assert response.status_code == 201
    order_track = response.json()["track"]
    response = sender_stand_request.get_order(str(order_track))
    assert response.status_code == 200

def test_get_couriers_in_delivery():
    sender_stand_request.get_couriers_in_delivery()

def test_get_order_statuses():
    sender_stand_request.get_order_statuses()
