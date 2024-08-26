from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY')

class DevConfig(Config):
    DEBUG=True

config = {
    'development': DevConfig
}
