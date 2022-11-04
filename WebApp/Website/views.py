#storing main views/url endpoints for functioning frontend aspects of website
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"
