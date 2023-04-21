"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13np33cv203bulhrt0-a ",
        database="todo_ry44 ",
        user="chandra",
        password="noAW0PcIQGCzhErZJ6TWRGeTkVMAEfo8")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
