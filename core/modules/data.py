from flask_sqlalchemy import SQLAlchemy
from core import *


db = SQLAlchemy(app)


class data_siswa(db.Model):
    __tablename__ = 'siswa'

    id = db.Column(db.Integer,primary_key=True,nullable=False)
    nama = db.Column(db.String(64),index=True)
    kelas = db.Column(db.String(5))