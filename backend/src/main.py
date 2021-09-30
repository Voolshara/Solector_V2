from flask import Flask, request
from typer import Typer 
from flask_cors import CORS
from src.db import DB_get


app = Flask(__name__)
CORS(app, resources={
    r"/marketplace/*": {"origins": "*"},
    r"/product/*": {"origins": "*"}
    }) # настройка CORS POLICY
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'

DBG = DB_get()
runner = Typer()

@app.route('/marketplace/get_filters', methods=['POST'])  # роут сборки шаблонов
def filters():
    return DBG.get_marketplace_data()

@app.route('/marketplace/data', methods=['POST'])  # роут сборки шаблонов
def marketplace():
    return {'data' : DBG.get_panels(request.json)}

@app.route('/product', methods=['POST'])  # роут сборки шаблонов
def product():
    return {'data' : DBG.get_product(request.json['product'])}


@runner.command()
def runner():
    app.run(host="192.168.1.82", port="4900") # запуск сервера
