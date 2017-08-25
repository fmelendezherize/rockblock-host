from app import db

class SatelliteMessage(db.Model):
    __tablename__ = "SatelliteMessage"
    id = db.Column(db.Integer, primary_key=True)
    imei = db.Column(db.String(240), nullable=True)
    momsn = db.Column(db.String(240), nullable=True)
    transmit_time = db.Column(db.String(240), nullable=True)
    iridium_latitude = db.Column(db.String(240), nullable=True)
    iridium_longitude = db.Column(db.String(240), nullable=True)
    iridium_cep = db.Column(db.String(240), nullable=True)
    data = db.Column(db.String(240), nullable=True)

    def __str__(self):
        return "%s %s" % (self.id, self.imei)