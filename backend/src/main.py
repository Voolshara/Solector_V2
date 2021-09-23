from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # настройка CORS POLICY

@app.route('/marketplace', methods=['POST'])  # роут сборки шаблонов
def parser():
    parser_out = Parser.parser_shell(parser_data.parse_obj(request.get_json()))