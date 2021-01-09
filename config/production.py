from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'_\x85\xfe{,\x7fQa\xf3\xc1\x91\x8a*\xe7\xae\xa9'
