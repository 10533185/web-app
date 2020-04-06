import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    application = app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite')
    )

    # Registering views

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)

    from . import Cart
    app.register_blueprint(Cart.bp)

    from . import products
    app.register_blueprint(products.bp)
    app.add_url_rule('/', endpoint='index')

    return app
