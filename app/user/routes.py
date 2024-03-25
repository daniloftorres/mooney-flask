from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ..extensions import db
from .models import User
from .blueprint import user_bp


@user_bp.route('/teste', methods=['GET'])
def teste():
    return jsonify({'mensagem': 'Tudo funcionando perfeitamente!'}), 200


@user_bp.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify({"mensagem": "Username e password são necessários!"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"mensagem": "Username já existe!"}), 409

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201


@user_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"mensagem": "Credenciais inválidas!"}), 401


@user_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
