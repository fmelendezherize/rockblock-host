from app import app, models, db
from flask import request, render_template
import struct

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/sat', methods=['GET','POST'])
def sat_api():
    if request.method == 'POST':
        sat_message = models.Satellite_Message()
        if 'imei' in request.form:
            imei = request.form['imei']
            sat_message.imei = imei
            print "post imei %s" % imei
        if 'momsn' in request.form:
            momsn = request.form['momsn']
            sat_message.momsn = momsn
            print "post momsn %s" % momsn
        if 'transmit_time' in request.form:
            transmit_time = request.form['transmit_time']
            sat_message.transmit_time = transmit_time
            print "post transmit_time %s" % transmit_time
        if 'iridium_latitude' in request.form:
            iridium_latitude = request.form['iridium_latitude']
            sat_message.iridium_latitude = iridium_latitude
            print "post iridium_latitude %s" % iridium_latitude
        if 'iridium_longitude' in request.form:
            iridium_longitude = request.form['iridium_longitude']
            sat_message.iridium_longitude = iridium_longitude
            print "post iridium_longitude %s" % iridium_longitude
        if 'iridium_cep' in request.form:
            iridium_cep = request.form['iridium_cep']
            sat_message.iridium_cep = iridium_cep
            print "post iridium_cep %s" % iridium_cep
        if 'data' in request.form:
            data = request.form['data'].decode("hex")
            decoded_data = struct.unpack('< B B B B B', data)
            sat_message.data = str(decoded_data)
            print type(decoded_data)
            print str(decoded_data)
            print list(decoded_data)

        db.session.add(sat_message)
        db.session.commit()
        return '', 200
    else:
        return '', 405

@app.route('/sat-panel')
def sat_panel():
    sat_messages = models.Satellite_Message.query.order_by(models.Satellite_Message.id.desc()).all()
    return render_template("sat_panel.html",
                           sat_messages = sat_messages)

