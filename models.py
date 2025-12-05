from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Lab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    location = db.Column(db.String, nullable=True)
    audits = db.relationship('Audit', backref='lab', lazy=True)

class Audit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lab_id = db.Column(db.Integer, db.ForeignKey('lab.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text, nullable=True)
    items = db.relationship('Item', backref='audit', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    audit_id = db.Column(db.Integer, db.ForeignKey('audit.id'), nullable=False)
    code = db.Column(db.String, nullable=False, index=True)
    name = db.Column(db.String, nullable=True, index=True)
    system_qty = db.Column(db.Integer, nullable=True)
    physical_qty = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String, nullable=True, index=True)
