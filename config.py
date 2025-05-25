import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 23169258
API_HASH = "aecf7c2d85b6aaa0e567b1fe03852441"
BOT_TOKEN = "7995633056:AAGHDbEo1Hohn2OkevXo2uEToHgL1AU_QW0"
OWNER_USERNAME = "Eren_Aethonix"
BOT_USERNAME = "juily_music_bot"
BOT_NAME = "˹𝖩ᴜɪʟʏ ꭙ 𝖬ᴜ𝗌ɪᴄ˼"
ASSUSERNAME = "juily_assistant"
EVALOP = list(map(int, getenv("EVALOP", "6305653111").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Alisha:Alisha123@cluster0.yqcpftw.mongodb.net/?retryWrites=true&w=majority")
LOGGER_ID = -1002116643591
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

GPT_API = getenv("GPT_API", None)
DEEP_API = getenv("DEEP_API", None)
OWNER_ID = 7267729758

HEROKU_APP_NAME = None
HEROKU_API_KEY = None
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/paradox-zenu/juily.git")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/hxh_network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/zenitsu_bot_support")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

STRING1 = getenv("STRING_SESSION", "BQGeps4ABoISXDJuVvQM-QTZXpKTxbM-mOsSgv7I2-8gLj4znpSS-rKqgQAQFS0BP9heyw4Ihlp7W9a2LEPfT4PUPGeDBA8BfF2fDk2qw3IAwV2-j8kMclxlKIoCv30Wk5ovaXCvD8mqnKcNO-bpg6FS31E0YjfaG1eZXBAOdKVetp60tG61QMnMpihq2bOaFnoU-hsapudYBXn8ArGImw9rdco-jucvGR-DWqME393QsIwccPULO00g_ynXkzxLxG7QCWARwQBeJCSN0y1etJwXfHcEBjrNCnJHQhXbN_CQWZ9ocjaPzv5v_6Xyt9TL_n5omDdjUGdrh8nr1LWMNG6SUmgjEwAAAAHjksDXAA") 
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


AYU = [
    "💞", "🦋", "🔍", "🧪", "🦋", "⚡️", "🔥", "🦋", "🎩", "🌈", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦋", "🦋", "🕊️", "🦋", "🕊️", "🦋", "🦋", "🦋", "🪄", "💌", "🦋", "🦋", "🧨"
]

AYUV = [ "<b>нєу</b> {0}, 💗\n\n๏ ᴛʜɪs ɪs {1} !\n\n➻ {1} ɪs ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ᴍᴜsɪᴄ ᴄᴏᴍᴘᴀɴɪᴏɴ, ʜᴇʀᴇ ᴛᴏ ʙʀɪɴɢ ʜᴀʀᴍᴏɴʏ ᴛᴏ ʏᴏᴜʀ ᴅᴀʏ. EɴJᴏʏ sᴇᴀᴍʟᴇss ᴍᴜsɪᴄ ᴘʟᴀʏʙᴀᴄᴋ, ᴄᴜʀᴀᴛᴇᴅ ᴘʟᴀʏʟɪsᴛs, ᴀɴᴅ ᴇғғᴏʀᴛʟᴇss ᴄᴏɴᴛʀᴏʟ, ᴀʟʟ ᴀᴛ ʏᴏᴜʀ ғɪɴɢᴇʀᴛɪᴘs. Lᴇᴛ {1} ᴇʟᴇᴠᴀᴛᴇ ʏᴏᴜʀ ʟɪsᴛᴇɴɪɴɢ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴡɪᴛʜ ᴇᴀsᴇ ᴀɴᴅ sᴛʏʟᴇ.\n\n<b><u>Sᴜᴘᴘᴏʀᴛᴇᴅ Pʟᴀᴛғᴏʀᴍs :</b></u> ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.\n──────────────────\n<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs🦋.</b> "  ,
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/y3yui4.jpg"
)
PING_VID_URL = getenv(
    "PING_VID_URL", "https://files.catbox.moe/lwpisw.mp4"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/ffb9qm.jpg"
STATS_VID_URL = "https://files.catbox.moe/8epb5p.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/9ot3k5.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/ffb9qm.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/y3yui4.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/9ot3k5.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/y3yui4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/9ot3k5.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/y3yui4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/ffb9qm.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
