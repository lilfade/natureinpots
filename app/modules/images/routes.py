from flask import Blueprint, request, redirect, url_for, render_template, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
from app import db
from app.models.image import PlantImage

bp = Blueprint('images', __name__, url_prefix='/images')

@bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files.get('image')
        plant_id = request.form.get('plant_id')
        if file and plant_id:
            filename = secure_filename(file.filename)
            upload_path = os.path.join('uploads', filename)
            file.save(upload_path)
            image = PlantImage(plant_id=plant_id, image_url=upload_path)
            db.session.add(image)
            db.session.commit()
            return redirect(url_for('plants.index'))
    return render_template('images/upload.html')
