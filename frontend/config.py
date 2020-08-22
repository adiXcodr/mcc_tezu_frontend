import os
class Config:
    RECAPTCHA_PUBLIC_KEY='6Le5H8IZAAAAAGXorLGje5uPPzgyxG87UifV9k8N'
    RECAPTCHA_PRIVATE_KEY='6Le5H8IZAAAAAOwFH0av-IeIlKBuuGfQhcFjJAOk'
class Development(Config):
    SECRET_KEY='damnSimplESecrEtKEy'
    RECAPTCHA_PUBLIC_KEY='6LeLZPEUAAAAADqu8vW2IEam3ZjgsLot11Uhe9EP'
    RECAPTCHA_PRIVATE_KEY='6LeLZPEUAAAAAHjeIVUeVOqcrVXLsSMOOPjT7_Fy'
    DEBUG=True
class Production(Config):
    SECRET_KEY=os.environ.get('SECRET_KEY') 
    DEBUG=False
