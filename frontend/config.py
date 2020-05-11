import os
class Config:
    RECAPTCHA_PUBLIC_KEY=os.environ.get('PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY=os.environ.get('PRIVATE_KEY')
