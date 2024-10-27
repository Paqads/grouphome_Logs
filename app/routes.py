from flask import render_template, flash, redirect, url_for
from app import db
from app.models import LogEntry
from app.forms import LogEntryForm
from datetime import datetime

def init_routes(app):
    @app.route('/')
    @app.route('/index')
    def index():
        logs = LogEntry.query.order_by(LogEntry.timestamp.desc()).all()
        return render_template('index.html', title='Home', logs=logs)

    @app.route('/log', methods=['GET', 'POST'])
    def log_entry():
        form = LogEntryForm()
        if form.validate_on_submit():
            log = LogEntry(
                child_name=form.child_name.data,
                category=form.category.data,
                timestamp=form.timestamp.data,
                content=form.content.data
            )
            db.session.add(log)
            db.session.commit()
            flash('Log entry added successfully')
            return redirect(url_for('index'))
        return render_template('log_entry.html', title='New Log Entry', form=form)