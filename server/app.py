from flask import Flask
from flask_migrate import Migrate
from .models import db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza
from .config import Config
from .controllers.restaurant_controller import restaurant_bp



from .controllers.pizza_controller import pizza_bp
from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app

# For Flask CLI to recognize the app
app = create_app()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
