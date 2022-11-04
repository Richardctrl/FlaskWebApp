from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'richard961'

    #importing blueprints
    from .views import views
    from .auth import auth

    #registering blueprints
    #url prefix means the prefix in url: adding to slash would mean another route in url (/auth/route)
    #route is the route in auth (in views it is simply route('/') meaining only a slash)
    #extra prefix would be added ahead of route, currently simply accessing with / (no prefix)
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
