from flask import Blueprint, redirect, url_for, send_file
from flask_login import login_required
from app import db
from app.models.qrlink import QRLink
from app.models.plant import Plant
import qrcode
import os

bp = Blueprint('qrcodegen', __name__, url_prefix='/qr')

@bp.route('/generate/<int:plant_id>')
@login_required
def generate_qr(plant_id):
    qr_path = f'uploads/qr_plant_{plant_id}.png'
    qr_data = f'https://natureinpots.com/plants/{plant_id}'
    qr = qrcode.make(qr_data)
    qr.save(qr_path)

    qr_record = QRLink(plant_id=plant_id, qr_code=qr_path)
    db.session.add(qr_record)
    db.session.commit()
    return redirect(url_for('plants.index'))

@bp.route('/view/<int:plant_id>')
@login_required
def view_qr(plant_id):
    qr_record = QRLink.query.filter_by(plant_id=plant_id).first()
    if qr_record:
        return send_file(qr_record.qr_code, mimetype='image/png')
    return "QR code not found", 404
