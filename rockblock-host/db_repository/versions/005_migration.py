from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
satellite__message = Table('satellite__message', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('imei', String(length=240)),
    Column('momsn', String(length=240)),
    Column('transmit_time', String(length=240)),
    Column('iridium_latitude', String(length=240)),
    Column('iridium_longitude', String(length=240)),
    Column('iridium_cep', String(length=240)),
    Column('data', String(length=240)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['satellite__message'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['satellite__message'].drop()
