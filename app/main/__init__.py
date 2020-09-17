from flask import Blueprint

# main Blueprint object
main = Blueprint('main', __name__)

# importing views and errors
from . import views, errors