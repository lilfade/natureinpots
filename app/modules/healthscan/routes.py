from flask import Blueprint, redirect, url_for
from flask_login import login_required
from app import db
from app.models.healthscan import HealthScan

bp = Blueprint('healthscan', __name__, url_prefix='/health')

@bp.route('/scan/<int:image_id>')
@login_required
def scan(image_id):
    # Dummy health scan logic
    score = 87
    result = "Plant appears healthy."
    scan = HealthScan(image_id=image_id, score=score, result=result)
    db.session.add(scan)
    db.session.commit()
    return redirect(url_for('plants.index'))
