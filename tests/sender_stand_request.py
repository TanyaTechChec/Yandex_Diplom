# Астахова Татьяна, 19-я когорта — Финальный проект. Инженер по тестированию плюс


import psycopg2
import requests
import configuration

def create_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDERS,
        json=body
    )

def get_order(track_number):
    return requests.get(
        configuration.URL_SERVICE + configuration.TRACK_ORDERS + track_number
    )

def get_couriers_in_delivery():
    try:
        conn = psycopg2.connect(
            dbname="scooter_rent",
            user="morty",
            password="smith",
            host="serverhub.praktikum-services.ru",
            port="4554",
            sslmode='disable'
        )
        cur = conn.cursor()
        query = """
        SELECT "CourierLogin", COUNT(*) as order_count
        FROM "Orders"
        WHERE "inDelivery" = true
        GROUP BY "CourierLogin";
        """
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(f"Courier Login: {row[0]}, Order Count: {row[1]}")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

def get_order_statuses():
    try:
        conn = psycopg2.connect(
            dbname="scooter_rent",
            user="morty",
            password="smith",
            host="serverhub.praktikum-services.ru",
            port="4554",
            sslmode='disable'
        )
        cur = conn.cursor()
        query = """
        SELECT "TrackNumber", 
               CASE 
                   WHEN "finished" = true THEN 2
                   WHEN "cancelled" = true THEN -1
                   WHEN "inDelivery" = true THEN 1
                   ELSE 0
               END as status
        FROM "Orders";
        """
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(f"Track Number: {row[0]}, Status: {row[1]}")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
