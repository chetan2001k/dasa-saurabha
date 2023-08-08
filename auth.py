from flask import Blueprint,render_template

auth=Blueprint('auth',__name__)

@auth.route('/signup')
def signup():
    return 'this will be sign up page'

@auth.route('/login')
def login():
    return 'this will be login page'

@auth.route('/logout')
def logout():
    return 'this will be logout page'