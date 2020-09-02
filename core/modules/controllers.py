from core import *
from core.modules.data import *

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/add-siswa',methods=["POST","GET"])

def add_data():
    if request.method == 'POST':
        nama = request.form['nama']
        kelas = request.form['kelas']
        anjg = data_siswa(nama=nama,kelas=kelas)
        db.session.add(anjg)
        db.session.commit()
        return 'Sukses'