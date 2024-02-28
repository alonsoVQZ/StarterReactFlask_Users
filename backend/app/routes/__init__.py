from flask import Blueprint
from .user_routes import user_blueprint

api = Blueprint('api', __name__)

api.register_blueprint(user_blueprint, url_prefix='/user')