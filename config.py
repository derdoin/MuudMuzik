from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
THUMB_IMG = getenv("THUMB_IMG", "https://graph.org/file/adc43233e02aa20cdc6fc.jpg")
START_IMAGE = getenv("START_IMAGE", "https://graph.org/file/fa5ccd7123f36f9e12592.jpg")
BOT_NAME = getenv("BOT_NAME", "🎧 Muud Müzik")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME") 
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "PlutoFederation")
PLAYLIST_NAME = getenv("PLAYLIST_NAME", "PlutoFm") 
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
PLAYLIST_ID = int(getenv("PLAYLIST_ID"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
