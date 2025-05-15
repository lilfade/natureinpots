from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app import db
from app.models.marketplace import MarketplaceListing, ListingType
from app.models.plant import Plant

bp = Blueprint('marketplace', __name__, url_prefix='/marketplace')

@bp.route('/')
@login_required
def index():
    listings = MarketplaceListing.query.all()
    return render_template('marketplace/index.html', listings=listings)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        listing = MarketplaceListing(
            plant_id=request.form['plant_id'],
            listing_type=request.form['listing_type'],
            price=request.form['price'],
            status='active'
        )
        db.session.add(listing)
        db.session.commit()
        return redirect(url_for('marketplace.index'))
    plants = Plant.query.all()
    return render_template('marketplace/create.html', plants=plants)
