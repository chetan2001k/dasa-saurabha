from flask import Flask

def create_app():
    app=Flask(__name__,template_folder='Template')

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    if __name__ == '__main__':
        app.run(debug=True)

create_app()