from flask import Blueprint, jsonify, request
from models.UserModel import UserModel
from models.entities.User import User
import uuid

main=Blueprint('user_blueprint',__name__)

@main.route('/')
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_user(id):
    try:
        user = UserModel.get_user(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_user():
    try:
        ########### AGREGAR VALIDACIONES
        name = request.json['name']
        surname = request.json['surname']
        email = request.json['email']
        password = request.json['password']
        id = uuid.uuid4()
        user = User(str(id), name, surname, email, password)

        affected_rows = UserModel.add_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({"message":"Error al insertar"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        
        user = User(id)

        affected_rows = UserModel.delete_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({"message":"Error al eliminar"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/update/<id>', methods=['PUT'])
def update_user(id):
    try:
        ########### AGREGAR VALIDACIONES
        name = request.json['name']
        surname = request.json['surname']
        email = request.json['email']
        password = request.json['password']

        user = User(id, name, surname, email, password)

        affected_rows = UserModel.update_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({"message":"Error al actualizar"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500