from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    load_dotenv()
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "devkey")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///local.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Import models and register user loader AFTER extensions are initialized
    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import other models just to register with SQLAlchemy
    from app.models import user, plant  # Extend as needed

    # Register Blueprints
    from app.modules.auth import bp as auth_bp
    from app.modules.plants import bp as plants_bp
    from app.modules.dashboard import bp as dash_bp
    from app.modules.home import bp as home_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(plants_bp)
    app.register_blueprint(dash_bp)
    app.register_blueprint(home_bp)

    return app
