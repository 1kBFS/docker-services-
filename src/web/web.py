import sys
import json
import os
from flask import Flask, request, make_response

sys.path.append("..")
from src.DBManager import DBManager

app = Flask(__name__)


@app.route('/')
def all_data():
    if request.method == "GET":
        conn = DBManager(password=os.environ['MARIADB_ROOT_PASSWORD'])
        response = None
        try:
            result_db_contents = dict(conn.select_all())
            response = make_response(json.dumps(result_db_contents), 200)
        except Exception as ex:
            response = make_response(json.dumps({"status": "Internal Server Error"}), 500)
        finally:
            conn.close()
        return response
    else:
        return make_response("404 Not Found", 404)


@app.route('/health')
def health_status():
    if request.method == "GET":
        return json.dumps({"status": "OK"}), 200
    else:
        return make_response("404 Not Found", 404)


if __name__ == '__main__':
    app.run(host="web", port=8000)
