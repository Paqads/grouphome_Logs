from app import db, create_app
from app.models import LogEntry

app = create_app()

with app.app_context():
    db.create_all()
    print("Database schema updated.")