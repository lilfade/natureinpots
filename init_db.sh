#!/bin/bash

echo "⏳ Waiting for MySQL to be ready..."
until nc -z db 3306; do
  sleep 1
done
echo "✅ MySQL is ready!"

echo "🔄 Running DB migrations..."

# Activate virtual environment if needed, otherwise skip
# source venv/bin/activate  # Uncomment if you're using a venv

# Ensure Flask app context is set
export FLASK_APP=run.py

# Check if migrations folder exists
if [ ! -d "migrations" ]; then
  echo "📁 Migrations folder not found. Initializing..."
  flask db init
fi

# Run migrations
flask db migrate -m "Auto migration"
flask db upgrade

echo "👤 Checking for default admin user..."
python3 <<EOF
from app import create_app, db
from app.models.user import User
app = create_app()
with app.app_context():
    if not User.query.filter_by(email='admin@example.com').first():
        user = User(username='admin', email='admin@example.com')
        user.set_password('admin123')
        db.session.add(user)
        db.session.commit()
        print("✅ Default admin user created.")
    else:
        print("ℹ️ Admin user already exists.")
EOF

echo "🚀 DB init complete. Starting Flask..."
