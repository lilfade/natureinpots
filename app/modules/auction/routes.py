from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from datetime import datetime, timedelta
from app import db
from app.models.auction import Auction
from app.models.plant import Plant

bp = Blueprint('auction', __name__, url_prefix='/auction')

@bp.route('/')
@login_required
def index():
    auctions = Auction.query.all()
    return render_template('auction/index.html', auctions=auctions)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        auction = Auction(
            plant_id=request.form['plant_id'],
            starting_price=request.form['starting_price'],
            end_date=datetime.utcnow() + timedelta(days=7)
        )
        db.session.add(auction)
        db.session.commit()
        return redirect(url_for('auction.index'))
    plants = Plant.query.all()
    return render_template('auction/create.html', plants=plants)
