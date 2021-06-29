import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", ")
BOT_TOKEN = getenv("BOT_TOKEN", "1728730929:AAGdj_UpflyimraBPr-MRHi8PtVMwKZMWr4")
BOT_NAME = getenv("BOT_NAME", "Patricia")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "patricia_updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/936443dca3f8230e90918.jpg")
admins = {}
API_ID = int(getenv("API_ID", "5786603"))
API_HASH = getenv("API_HASH", "a1354f206a4a05109d0fc916c0f150d0")
BOT_USERNAME = getenv("BOT_USERNAME", "PATRICIA_ROBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "patriciaXmusic")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "patricia_support")
PROJECT_NAME = getenv("PROJECT_NAME", "patricia v4")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/teamdaisyx/daisyxmusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "KYSKHT-YCCWMO-PBHTGX-HQCUKQ-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1832447570").split()))
