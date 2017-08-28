import unittest
import os
from app import app, db
from app.models import SatelliteMessage
from config import basedir
from coverage import coverage
cov = coverage(branch=True, omit=['flask/*', 'tests.py',])
cov.start()

class Test_tests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_insert_sat_message(self):
        sat_message_test = SatelliteMessage()
        sat_message_test.data = 1
        sat_message_test.imei = 2
        sat_message_test.iridium_cep = 3
        sat_message_test.iridium_latitude = 4
        sat_message_test.iridium_longitude = 5
        sat_message_test.momsn = 6
        sat_message_test.transmit_time = 7
        db.session.add(sat_message_test)
        db.session.commit()
        assert SatelliteMessage.query.count() == 1

    def test_sat_page(self):
        with app.test_client() as c:
            response = c.get('/sat-panel')
            self.assertEquals(response.status_code, 200)

    def test_index_page(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertEquals(response.status_code, 200)

    def test_sat_message_post(self):
        with app.test_client() as c:
            response = c.post('/api/sat', data=dict(
                imei="123",
                momsn="123",
                transmit_time="456",
                iridium_latitude="456"))
            self.assertEquals(response.status_code, 200)
            assert SatelliteMessage.query.count() == 1

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
    cov.stop()
    cov.save()
    print("\n\nCoverage Report:\n")
    cov.report()
    print("HTML version: " + os.path.join(basedir, "tmp/coverage/index.html"))
    cov.html_report(directory='tmp/coverage')
    cov.erase()