import os
import sys
import ssl

import aiohttp

# Bot
SKIP_UPDATES = True
BOT_TOKEN = '635489344:AAH7s0PY_qOqnNepnxFA5sLzfCF6LdnKGXs' # 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
LOGFILE = ''  # logs/bot.log
OWNER_ID = 0  # your id for access to admin panel
RATE_LIMIT = 0.5  # You can use  command every N seconds

# Proxy
PROXY_URL = '' # http or socks5://user:pass@host:port
PROXY_LOGIN = ''
PROXY_PASS = ''

# Webhook
APP_HOST = 'localhost' # 192.168.1.1XX, or localhost if use nginx
APP_PORT = 3001
USE_WEBHOOK = True
WEBHOOK_HOST = '' # example.com or ip
WEBHOOK_PATH = '' # /webhook
WEBHOOK_PORT = 443
SSL_CERT = '' # path to ssl certificate
SSL_KEY = '' # path to ssl private key, hide if use nginx proxy_pass

# Database
DB_URL = "sqlite:///db.sqlite3" # db.sqlite3

# Redis
REDIS_SETTINGS = {}


ROOT_DIR = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))

# Webhook init
WEBHOOK_URL = f'https://{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}'
WEBHOOK_SERVER = {
    'host': APP_HOST,
    'port': APP_PORT,
    'webhook_path': WEBHOOK_PATH,
}

# ssl context
if SSL_CERT and SSL_KEY:
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(SSL_CERT, SSL_KEY)
    WEBHOOK_SERVER['ssl_context'] = context

# i18n
I18N_DOMAIN = 'bot'
LOCALES_DIR = os.path.join(ROOT_DIR, 'locales')

# proxy_auth
PROXY_AUTH = aiohttp.BasicAuth(login=PROXY_LOGIN, password=PROXY_PASS)


TARGET_CHAT_ID = '-320534198'


# message sending block
INPUT_FILE_WITH_ID = 'input_id.txt'  # path to input file
OUTPUT_FILE_WITH_ID = 'result_id.txt'  # path to output file
MESSAGE_TEXT = 'Привет это тестовая рассылка 123'
USE_KEYBOARD = True  # use True or False
BTN_LIST = [{'text': '1 кнопка', 'link': 'https://t.me/durov_russia'},
            {'text': '2 кнопка', 'link': 'https://t.me/durov'},
            {'text': '2 кнопка', 'link': 'https://ubikiri.com/'}
            ]

BTN_1_TEXT = '1 кнопка'
BTN_1_URL = 'https://t.me/durov_russia'
BTN_2_TEXT = '1 кнопка'
BTN_2_URL = 'https://t.me/durov'
BTN_3_TEXT = '1 кнопка'
BTN_3_URL = 'https://ubikiri.com/'
SECRET_PHRASE = 'sendf'
