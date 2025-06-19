from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("24219127"))
API_HASH = getenv("4ede46a38016f3574a35ab60055ce51a")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/c34fc9d62d93032868f02-ffd4f1f6e48434a23a.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/c34fc9d62d93032868f02-ffd4f1f6e48434a23a.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5463728082").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
