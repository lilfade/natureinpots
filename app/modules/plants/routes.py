from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app import db
from app.models.plant import Plant

bp = Blueprint('plants', __name__, url_prefix='/plants')

@bp.route('/')
@login_required
def index():
    plants = Plant.query.all()
    return render_template('plants/index.html', plants=plants)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        plant = Plant(
            plant_id=request.form['plant_id'],
            name=request.form['name'],
            scientific_name=request.form.get('scientific_name'),
            description=request.form.get('description'),
            price=request.form.get('price'),
            initial_price=request.form.get('initial_price'),
            image_url=request.form.get('image_url')
        )
        db.session.add(plant)
        db.session.commit()
        return redirect(url_for('plants.index'))
    return render_template('plants/add.html')
