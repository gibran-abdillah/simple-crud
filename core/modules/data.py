from flask_sqlalchemy import SQLAlchemy
from core import app


db = SQLAlchemy(app)


class data_siswa(db.Model):

    __tablename__ = 'datasiswa'

    id = db.Column(db.Integer,primary_key=True,nullable=False)
    nama = db.Column(db.String(64),index=True)
    kelas = db.Column(db.String(10))

    def __repr__(self):
        return '<nama:{}'.format(self.nama)