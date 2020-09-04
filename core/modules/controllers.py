from core import *
from core.modules.data import *

@app.route('/')
def index_page():
    return render_template('index.html',data=enumerate(data_siswa.query.all(),1))

# add data ..
@app.route('/add-siswa',methods=["POST","GET"])

def add_data():
    if request.method == 'POST':
        try:
            nama = request.form['nama']
            kelas = request.form['kelas']
            data_student = data_siswa(nama=nama,kelas=kelas)
            db.session.add(data_student) # add session 
            db.session.commit()
        except Exception as e:
            return e # show an error 

        return redirect(url_for('index_page'))
    else:return render_template('index.html',data=enumerate(data_siswa.query.all(),1))

# delete data 
@app.route('/delete/<int:id>')
def delete_data(id):
    datasis = data_siswa.query.filter_by(id=id).first() # filter by id 
    db.session.delete(datasis)
    db.session.commit()
    return redirect(url_for('index_page'))

# edit data
@app.route('/edit/<int:id>',methods=["GET","POST"])

def edit_page(id):
    if request.method == 'POST':
        datasis = data_siswa.query.filter_by(id=id).first()
        datasis.nama = request.form['nama']
        datasis.kelas = request.form['kelas']
        db.session.commit()
        return redirect(url_for('index_page'))
    get_data = data_siswa.query.filter_by(id=id).first()
    return render_template('edit_page.html',nama=get_data.nama,kelas=get_data.kelas)