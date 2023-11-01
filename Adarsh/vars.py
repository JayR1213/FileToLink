# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '29627910'))
    API_HASH = str(getenv('API_HASH', 'ef526b2a546ee6795514226f853d7ff0'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', "6538590558:AAFlH0hnNbidkac4zQvg-PK_kXb9HPd2pRo"))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001938404490'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5804202410").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = str(getenv('APP_NAME'))
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', "TechnoJay_bot"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://jayeshdb:bQmBrMvsaOSGb5dZ@cluster0.moiu8ck.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', '-1001913143847')
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", '-1001362659779')).split())) 

    STREAM_URL = (environ.get('STREAM_URL', "True") == "True")
    STREAM_API = environ.get("STREAM_API", "8e30cbc70ca83e674f9ce4e8a21d084f855d616c") 
    STREAM_SITE = environ.get("STREAM_SITE", "paisakamalo.in") 
    STREAM_LONG = environ.get("STREAM_LONG", False)
