from flask import Blueprint

# Initialize the blueprint
routes_bp = Blueprint('routes', __name__)

# Import routes
from . import some_route   # Update with actual route files as necessary
