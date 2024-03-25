from flask import Blueprint

classification_bp = Blueprint('classification', __name__, url_prefix='/classification')

from . import routes