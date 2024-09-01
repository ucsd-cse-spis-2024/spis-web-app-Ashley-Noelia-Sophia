from flask import Flask

def create_app(): #Classes
    app = Flask(__name__)
    #Controls session data
    app.config['SECRET_KEY'] = 'jfjejfejfafi jefejsifjs' #Secret Key

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app 

