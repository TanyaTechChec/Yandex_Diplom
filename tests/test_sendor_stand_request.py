# Астахова Татьяна, 19-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data

def create_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREAT_ORDERS,  # исправлено на CREAT_ORDERS
        json=body
    )

def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response

def test_order_creation_and_retrieval():
    response = create_order(data.order_body)
    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)

    order_response = get_order(track_number)
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:", order_data)