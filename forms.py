#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms import Form, SelectField, StringField, PasswordField, validators

class CommentForm(Form):
	username= StringField('Usuario:', [validators.Required('Ingrese un Usuario')])
	password= PasswordField('Password:', [validators.Required('Es necesario ingresar el Password')])


class Registro_Form(Form):
	username= StringField('Usuario:', [validators.Required('Ingrese un Usuario')])
	password= PasswordField('Password:', [validators.Required('Es necesario ingresar el Password')])
	apellido= StringField('Apellido:', [validators.Required('Ingrese apellido')])
	genero= SelectField('Sexo:', choices=[('', 'Seleccione:'), ('F', 'Femenino'), ('M', 'Masculino')])
