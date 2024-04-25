from flask import Blueprint, request, jsonify
from model.contact import Contact
from utils.db import db

#Creación de una instancia Blueprint, para cuando exista
#más de una carpeta models?
contacts = Blueprint('contacts', __name__)

###METODOS GET (CRUD = READ)

@contacts.route('/contactos/v1', methods = ['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-backend'
    return jsonify(result)

@contacts.route('/contactos/v1/listar', methods = ['GET'])
def getContactos():
    result = {}
    contactos = Contact.query.all() #"Select from Contact"
    result["data"] = contactos
    result["status_cod"] = 200 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Contacts were recovery succesfully..."
    return jsonify(result), 200

@contacts.route('/contactos/<int:id>', methods = ['GET'])
def getContacto(id):
    result = {}
    contactos = Contact.query.get(id) #"Select from Contact"
    result["data"] = contactos
    result["status_cod"] = 200 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Contacts were recovery succesfully..."
    return jsonify(result), 200

###METODOS INSERTAR  POST  (CRUD = CREATE)

@contacts.route('/contactos/v1/insert', methods = ['POST'])
def insert():
    result = {}
    body = request.get_json()
    fullname = body.get('fullname')
    email = body.get('email')
    phone = body.get('phone')
    
    if not fullname or not email or not phone:
        result["status_cod"] = 400 #Status_code se envia como resultado del query para FrontEnd
        result["status_msg"] = "Data is missing"
        return jsonify(result), 400
    
    contacto = Contact(fullname, email, phone)
    db.session.add(contacto) #"INSERT into ..."
    db.session.commit()
    result["data"] = contacto
    result["status_cod"] = 201 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Data was created"
    return jsonify(result), 201

###METODOS UPDATE  POST  (CRUD = UPDATE)

@contacts.route('/contactos/v1/update', methods = ['POST'])
def update():
    result = {}
    body = request.get_json()
    id = body.get('id')
    fullname = body.get('fullname')
    email = body.get('email')
    phone = body.get('phone')
    
    #if data is missing
    if not id or not fullname or not email or not phone:
        result["status_cod"] = 400 #Status_code se envia como resultado del query para FrontEnd
        result["status_msg"] = "Data is missing"
        return jsonify(result), 400
    
    contacto = Contact.query.get(id) #"Selecto from contacto where id = ..."
    
    #if id is not found
    if not contacto:
        result["status_cod"] = 400 #Status_code se envia como resultado del query para FrontEnd
        result["status_msg"] = "ID does not exist"
        return jsonify(result), 400
    
    #modifies
    contacto.fullname = fullname
    contacto.email = email
    contacto.phone = phone
    db.session.commit()
    
    #sends result
    result["data"] = contacto
    result["status_cod"] = 202 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Data was modified"
    return jsonify(result), 202

###METODOS UPDATE  POST  (CRUD = delete)
@contacts.route('/contactos/v1/delete', methods = ['DELETE'])
def delete():
    result = {}
    body = request.get_json()
    id = body.get('id')    

#if id is missing
    if not id:
        result["status_cod"] = 400 #Status_code se envia como resultado del query para FrontEnd
        result["status_msg"] = "ID must be provided"
        return jsonify(result), 400
    
    contacto = Contact.query.get(id) #"Selecto from contacto where id = ..."
    
    #if id is not found
    if not contacto:
        result["status_cod"] = 400 #Status_code se envia como resultado del query para FrontEnd
        result["status_msg"] = "ID does not exist"
        return jsonify(result), 400
    
    db.session.delete(contacto) #deletes contacto
    db.session.commit() #confirm changes
    
    #sends result
    result["data"] = contacto
    result["status_cod"] = 200 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Data was deleted"
    return jsonify(result), 200