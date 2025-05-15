from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app import db
from app.models.presale import Presale
from app.models.plant import Plant

bp = Blueprint('presale', __name__, url_prefix='/presale')

@bp.route('/')
@login_required
def index():
    presales = Presale.query.all()
    return render_template('presale/index.html', presales=presales)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        presale = Presale(
            plant_id=request.form['plant_id'],
            user_email=request.form['user_email'],
            status=request.form['status']
        )
        db.session.add(presale)
        db.session.commit()
        return redirect(url_for('presale.index'))
    plants = Plant.query.all()
    return render_template('presale/create.html', plants=plants)
