from core import *
from .data import *

@app.route('/')
def index_page():
    return render_template('index.html')