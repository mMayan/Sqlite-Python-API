from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import dbb.crud_db as crud_db
import users_related.users as users

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta' 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)
jwt = JWTManager(app)


# ----------- users management ----------- #

@app.route('/register', methods=['POST'])
def register_user():
    details = request.get_json()
    username = details['username']
    password = details['password']
    final_user = users.register_user(username, password)
    return jsonify(final_user)

# Rota para login e geração do token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    if username and password not in users.get_one_user(username, password):
        return jsonify({"msg": "Usuário ou senha incorretos"}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/login/<id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    final = users.delete_user(id)
    return jsonify(final)


# ----------- CRUD database ----------- #

@app.route('/produtos', methods=['GET'])
@jwt_required()
def get_products(): 
    products = crud_db.get_product()
    return jsonify(products)


@app.route('/produto', methods=['POST'])
@jwt_required()
def insert_products():
    details = request.get_json()
    produto = details['produto'] 
    valor = details['valor']
    estoque = details['estoque']
    final = crud_db.insert_product(produto, valor, estoque)
    return jsonify(final)


@app.route('/produto', methods=['PUT'])
@jwt_required()
def update_products():
    details = request.get_json()
    produto = details['produto']
    valor = details['valor']
    estoque = details['estoque']
    final = crud_db.update_product(produto, valor, estoque)
    return jsonify(final)


@app.route('/produto/<id>', methods=['DELETE'])
@jwt_required()
def delete_products(id):
    final = crud_db.delete_product(id)
    return jsonify(final)


if __name__ == "__main__":
    crud_db.create_table()
    users.create_user_table()

    app.run(host='0.0.0.0', port=8000, debug=True)



# worth reading:
# https://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html <- post de um BR
# https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3 <- tutorial gringo
# https://www.sqlite.org/lang.html <- a própria documentação do sqlite3
# https://docs.python.org/3/library/sqlite3.html <- a documentação do módulo do sqlite3 no python

# https://medium.com/@hedgarbezerra35/api-rest-com-flask-autenticacao-25d99b8679b6 <- link q tem a ver

# https://docs.github.com/pt/enterprise-server@3.10/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-json-web-token-jwt-for-a-github-app
# acima como gerar um token jwt
