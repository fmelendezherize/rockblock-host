from .rockblock_host import app
from flask import request

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if request.form['imei']:
            imei = request.form['imei']
            print "post imei %s" % imei

        return '', 200
    else:
        return 'Index Page'

