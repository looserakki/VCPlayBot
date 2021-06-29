# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAOSxIXTcYySfkWKac5GH6vOtTyUbYd2M76QHmeP0W5HzBLIMkPI8tv4bvmBChxE1cKSm3UsBmOxDXGPE0ia0gW0KTYuiWCzWXffYD2F0Jsb8SHShUGvKx81wwBWpifo086IunLkVFb0SgjU5NTPQ7_h6w2NsZxfxTIUo6YgaaZz46rda_FQj6xb_xzV8nU7MH7aryl1m6ZhlRUVd9HirsYG7PJ8-RAyCf-s6UEt3s1YVMMCYtC54gm3_qTiF3ivT7K0f4JbuiRkilveiPninfU9WLA_oAO3nLyqgXu8wQ4nTm3DvcTSZzg-1tMpBnMLy4g6-kn1BXIUleYL6FLn7vrb6crEAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1728730929:AAGdj_UpflyimraBPr-MRHi8PtVMwKZMWr4")
BOT_NAME = getenv("BOT_NAME", "PATRICIA")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Patricia_updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/1cdf49c8a44fab5bce0ad.png")
admins = {}
API_ID = int(getenv("API_ID", "5786603"))
API_HASH = getenv("API_HASH", "a1354f206a4a05109d0fc916c0f150d0")
BOT_USERNAME = getenv("BOT_USERNAME", "PATRICIA_ROBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "PatriciaXmusic")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Patricia_robot")
PROJECT_NAME = getenv("PROJECT_NAME", "Patricia")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamOfDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "QNCTYU-IKMXKR-XZRFBF-CZQOCG-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "-1001435961283")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1832447570").split()))
