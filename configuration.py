class Config(object):
    'Configuracion basica'
    SECRET_KEY='Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@localhost:3306/pyalmacen'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
class ProduccionConfig(Config):
    'Configurtacion produccion'
    DEBUG=True
class DevelopmentConfig(Config):
    'Configuracion de desarrollo'
    DEBUG = True
    TESTING = True
    SECREY_KEY='desarrollo key' 
