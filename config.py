import os
# import sys
# import json

# CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")


# if not os.path.exists(CONFIG_PATH):
#     print(f'{CONFIG_PATH} not found')
#     sys.exit(1)


# configdata = json.load(open(CONFIG_PATH, 'r'))
# {
#     "ALLOWED_USER_NAMES": ["some_username"],
#     "OPENAI_API_KEY": "****",
#     "TELEGRAM_TOKEN": "****",
#     "ANTHROPIC_API_KEY": "****",
#     "REPLICATE_API_KEY": "",
#     "YT_DL_DIR": "/var/data/uploads",
#     "YT_DL_URL": "https://somehost.com/uploads",
#     "SCHEDULES": 1
# }


ALLOWED_USER_NAMES = os.environ.get['ALLOWED_USER_NAMES']

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
TELEGRAM_TOKEN = os.environ.get['TELEGRAM_TOKEN']
REPLICATE_API_KEY = os.environ.get('REPLICATE_API_KEY')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')

YT_DL_DIR = "/var/data/uploads"
YT_DL_URL = "https://somehost.com/uploads"
SCHEDULES = 1