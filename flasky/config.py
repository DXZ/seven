import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = "2321899383@qq.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[SEVEN]'
    FLASKY_SENDER = 'ADMIN SEVEN <2321899383@qq.com>'
    FLASKY_ADMIN = os.environ.get('FLASK_ADMIN')
    FLASKY_POSTS_PRE_PAGE = 20
    FLASKY_FOLLOWERS_PRE_PAGE = 50
    FLASKY_COMMENT_PRE_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME = 0.5

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'mysql://root:1234507@localhost:3306/flasky'

config = {
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}


      
