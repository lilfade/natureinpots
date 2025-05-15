from flask import Blueprint, redirect, url_for
from flask_login import login_required
from app import db
from app.models.backup import Backup

bp = Blueprint('backup', __name__, url_prefix='/backup')

@bp.route('/log')
@login_required
def log_backup():
    # Stub backup path — in production, this would be actual export logic
    backup = Backup(path='/backups/backup_latest.json')
    db.session.add(backup)
    db.session.commit()
    return redirect(url_for('dashboard.index'))
