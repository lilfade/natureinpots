from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.plant import Plant
from app.models.user import User

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
@login_required
def index():
    plant_count = Plant.query.count()
    user_count = User.query.count()
    return render_template('dashboard/index.html', plant_count=plant_count, user_count=user_count)
