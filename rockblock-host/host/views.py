from .rockblock_host import app
from flask import request
import struct

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'imei' in request.form:
            imei = request.form['imei']
            print "post imei %s" % imei
        if 'momsn' in request.form:
            momsn = request.form['momsn']
            print "post momsn %s" % momsn
        if 'transmit_time' in request.form:
            transmit_time = request.form['transmit_time']
            print "post transmit_time %s" % transmit_time
        if 'iridium_latitude' in request.form:
            iridium_latitude = request.form['iridium_latitude']
            print "post iridium_latitude %s" % iridium_latitude
        if 'iridium_longitude' in request.form:
            iridium_longitude = request.form['iridium_longitude']
            print "post iridium_longitude %s" % iridium_longitude
        if 'iridium_cep' in request.form:
            iridium_cep = request.form['iridium_cep']
            print "post iridium_cep %s" % iridium_cep
        if 'data' in request.form:
            data = request.form['data'].decode("hex")
            decoded_data = struct.unpack('< B B B B B', data)
            print type(decoded_data)
            print decoded_data
            print list(decoded_data)

        return '', 200
    else:
        return 'Index Page'

