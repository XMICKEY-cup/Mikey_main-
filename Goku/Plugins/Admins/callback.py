import asyncio
import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from Alya import YouTube, app
from Alya.core.call import alya
from Alya.misc import SUDOERS, db
from Alya.utils.database import (
    get_active_chats,
    get_assistant,
    get_lang,
    get_upvote_count,
    is_active_chat,
    is_music_playing,
    is_nonadmin_chat,
    music_off,
    music_on,
    mute_off,
    mute_on,
    is_muted,
    set_loop,
)
from Alya.utils.decorators.language import languageCB
from Alya.utils.formatters import seconds_to_min
from Alya.utils.inline import close_markup, stream_markup, stream_markup_timer
from Alya.utils.inline.play import panel_markup_1
from Alya.utils.stream.autoclear import auto_clean
from Alya.utils.thumbnails import get_thumb
from config import BANNED_USERS, SOUNCLOUD_IMG_URL, STREAM_IMG_URL, TELEGRAM_AUDIO_URL, TELEGRAM_VIDEO_URL, adminlist, confirmer, votemode
from strings import get_string
import config

wrong = {}


@app.on_callback_query(filters.regex("PanelMarkup") & ~BANNED_USERS)
@languageCB
async def markup_panel(client, CallbackQuery: CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, chat_id = callback_request.split("|")
    buttons = panel_markup_1(_, videoid, chat_id)
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as e:
        print(f"Error in markup_panel: {e}")
        return

@app.on_callback_query(filters.regex("MainMarkup") & ~BANNED_USERS)
@languageCB
async def main_markup_handler(client, CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, chat_id = callback_request.split("|")
    buttons = stream_markup(_, chat_id)
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as e:
        print(f"Error in main_markup_handler: {e}")
        return

@app.on_callback_query(filters.regex("Pages") & ~BANNED_USERS)
@languageCB
async def pages_handler(client, CallbackQuery, _):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    state, pages, videoid, chat = callback_request.split("|")
    chat_id = int(chat)
    pages = int(pages)
    if state == "Forw":
        buttons = panel_markup_1(_, videoid, chat_id)
    else:
        buttons = stream_markup(_, chat_id)
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as e:
        print(f"Error in pages_handler: {e}")
        return


@app.on_callback_query(filters.regex("unban_assistant"))
async def unban_assistant(_, callback: CallbackQuery):
    chat_id = callback.message.chat.id
    userbot = await get_assistant(chat_id)
    
    try:
        await app.unban_chat_member(chat_id, userbot.id)
        await callback.answer("ᴍʏ ᴀssɪsᴛᴀɴᴛ ɪᴅ ᴜɴʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🥰🥳\n\n➻ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ sᴏɴɢs🫠🔉\n\nTʜᴀɴᴋ ʏᴏᴜ💗", show_alert=True)
    except Exception as e:
        await callback.answer(f"Fᴀɪʟʟᴇᴅ ᴛᴏ ᴜɴʙᴀɴ ᴍʏ ᴀssɪssᴛᴀɴᴛ ʙᴇᴄᴀᴜsᴇ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʙᴀɴ ᴘᴏᴡᴇʀ\n\n➻ Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴍᴇ ʙᴀɴ ᴘᴏᴡᴇʀ sᴏ ᴛʜᴀᴛ ɪ ᴄᴀɴ ᴜɴʙᴀɴ ᴍʏ ᴀssɪssᴛᴀɴᴛ ɪᴅ", show_alert=True)


checker = {}
upvoters = {}


@app.on_callback_query(filters.regex("ADMIN") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    command, chat = callback_request.split("|")
    if "_" in str(chat):
        bet = chat.split("_")
        chat = bet[0]
        counter = bet[1]
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_5"], show_alert=True)
    mention = CallbackQuery.from_user.mention
    if command == "UpVote":
        if chat_id not in votemode:
            votemode[chat_id] = {}
        if chat_id not in upvoters:
            upvoters[chat_id] = {}

        voters = (upvoters[chat_id]).get(CallbackQuery.message.id)
        if not voters:
            upvoters[chat_id][CallbackQuery.message.id] = []

        vote = (votemode[chat_id]).get(CallbackQuery.message.id)
        if not vote:
            votemode[chat_id][CallbackQuery.message.id] = 0

        if CallbackQuery.from_user.id in upvoters[chat_id][CallbackQuery.message.id]:
            (upvoters[chat_id][CallbackQuery.message.id]).remove(
                CallbackQuery.from_user.id
            )
            votemode[chat_id][CallbackQuery.message.id] -= 1
        else:
            (upvoters[chat_id][CallbackQuery.message.id]).append(
                CallbackQuery.from_user.id
            )
            votemode[chat_id][CallbackQuery.message.id] += 1
        upvote = await get_upvote_count(chat_id)
        get_upvotes = int(votemode[chat_id][CallbackQuery.message.id])
        if get_upvotes >= upvote:
            votemode[chat_id][CallbackQuery.message.id] = upvote
            try:
                exists = confirmer[chat_id][CallbackQuery.message.id]
                current = db[chat_id][0]
            except:
                return await CallbackQuery.edit_message_text(f"ғᴀɪʟᴇᴅ.")
            try:
                if current["vidid"] != exists["vidid"]:
                    return await CallbackQuery.edit_message.text(_["admin_35"])
                if current["file"] != exists["file"]:
                    return await CallbackQuery.edit_message.text(_["admin_35"])
            except:
                return await CallbackQuery.edit_message_text(_["admin_36"])
            try:
                await CallbackQuery.edit_message_text(_["admin_37"].format(upvote))
            except:
                pass
            command = counter
            mention = "ᴜᴘᴠᴏᴛᴇs"
        else:
            if (
                CallbackQuery.from_user.id
                in upvoters[chat_id][CallbackQuery.message.id]
            ):
                await CallbackQuery.answer(_["admin_38"], show_alert=True)
            else:
                await CallbackQuery.answer(_["admin_39"], show_alert=True)
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=f"👍 {get_upvotes}",
                            callback_data=f"ADMIN  UpVote|{chat_id}_{counter}",
                        )
                    ]
                ]
            )
            await CallbackQuery.answer(_["admin_40"], show_alert=True)
            return await CallbackQuery.edit_message_reply_markup(reply_markup=upl)
    else:
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            if CallbackQuery.from_user.id not in SUDOERS:
                admins = adminlist.get(CallbackQuery.message.chat.id)
                if not admins:
                    return await CallbackQuery.answer(_["admin_13"], show_alert=True)
                else:
                    if CallbackQuery.from_user.id not in admins:
                        return await CallbackQuery.answer(
                            _["admin_14"], show_alert=True
                        )
    if command == "Pause":
        if not await is_music_playing(chat_id):
            return await CallbackQuery.answer(_["admin_1"], show_alert=True)
        await CallbackQuery.answer()
        await music_off(chat_id)
        await alya.pause_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_2"].format(mention)
        )
    elif command == "Resume":
        if await is_music_playing(chat_id):
            return await CallbackQuery.answer(_["admin_3"], show_alert=True)
        await CallbackQuery.answer()
        await music_on(chat_id)
        await alya.resume_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_4"].format(mention)
        )
    elif command == "Stop" or command == "End":
        await CallbackQuery.answer()
        await alya.stop_stream(chat_id)
        await set_loop(chat_id, 0)
        await CallbackQuery.message.reply_text(
            _["admin_5"].format(mention), reply_markup=close_markup(_)
        )
        await CallbackQuery.message.delete()
    elif command == "Mute":
        if await is_muted(chat_id):
            return await CallbackQuery.answer(
                _["admin_45"], show_alert=True
            )
        await CallbackQuery.answer()
        await mute_on(chat_id)
        await alya.mute_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_46"].format(mention)
        )
    elif command == "Unmute":
        if not await is_muted(chat_id):
            return await CallbackQuery.answer(
                _["admin_47"], show_alert=True
            )
        await CallbackQuery.answer()
        await mute_off(chat_id)
        await alya.unmute_stream(chat_id)
        await CallbackQuery.message.reply_text(
            _["admin_48"].format(mention)
        )
    elif command == "Loop":
        await CallbackQuery.answer()
        await set_loop(chat_id, 3)
        await CallbackQuery.message.reply_text(
            _["admin_41"].format(mention, 3)
        )
    elif command == "Shuffle":
        check = db.get(chat_id)
        if not check:
            return await CallbackQuery.answer(
                _["admin_42"], show_alert=True
            )
        try:
            popped = check.pop(0)
        except:
            return await CallbackQuery.answer(
                _["admin_43"], show_alert=True
            )
        check = db.get(chat_id)
        if not check:
            check.insert(0, popped)
            return await CallbackQuery.answer(
                _["admin_43"], show_alert=True
            )
        await CallbackQuery.answer()
        random.shuffle(check)
        check.insert(0, popped)
        await CallbackQuery.message.reply_text(
            _["admin_44"].format(mention)
        )
    elif command == "Skip" or command == "Replay":
        check = db.get(chat_id)
        if command == "Skip":
            txt = f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"
            popped = None
            try:
                popped = check.pop(0)
                if popped:
                    await auto_clean(popped)
                if not check:
                    await CallbackQuery.edit_message_text(
                        f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"
                    )
                    await CallbackQuery.message.reply_text(
                        text=_["admin_6"].format(
                            mention, CallbackQuery.message.chat.title
                        ),
                        reply_markup=close_markup(_),
                    )
                    try:
                        return await alya.stop_stream(chat_id)
                    except:
                        return
            except:
                try:
                    await CallbackQuery.edit_message_text(
                        f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"
                    )
                    await CallbackQuery.message.reply_text(
                        text=_["admin_6"].format(
                            mention, CallbackQuery.message.chat.title
                        ),
                        reply_markup=close_markup(_),
                    )
                    return await alya.stop_stream(chat_id)
                except:
                    return
        else:
            txt = f"➻ sᴛʀᴇᴀᴍ ʀᴇ-ᴘʟᴀʏᴇᴅ 🎄\n│ \n└ʙʏ : {mention} 🥀"
        await CallbackQuery.answer()
        queued = check[0]["file"]
        title = (check[0]["title"]).title()
        user = check[0]["by"]
        duration = check[0]["dur"]
        streamtype = check[0]["streamtype"]
        videoid = check[0]["vidid"]
        status = True if str(streamtype) == "video" else None
        db[chat_id][0]["played"] = 0
        exis = (check[0]).get("old_dur")
        if exis:
            db[chat_id][0]["dur"] = exis
            db[chat_id][0]["seconds"] = check[0]["old_second"]
            db[chat_id][0]["speed_path"] = None
            db[chat_id][0]["speed"] = 1.0
        if "live_" in queued:
            n, link = await YouTube.video(videoid, True)
            if n == 0:
                return await CallbackQuery.message.reply_text(
                    text=_["admin_7"].format(title),
                    reply_markup=close_markup(_),
                )
            try:
                image = await YouTube.thumbnail(videoid, True)
            except:
                image = None
            try:
                await alya.skip_stream(chat_id, link, video=status, image=image)
            except:
                return await CallbackQuery.message.reply_text(_["call_6"])
            button = stream_markup(_, chat_id)
            img = await get_thumb(videoid)
            run = await CallbackQuery.message.reply_photo(
                photo=img,
                caption=_["stream_1"].format(
                    f"https://t.me/{app.username}?start=info_{videoid}",
                    title[:23],
                    duration,
                    user,
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
            await CallbackQuery.edit_message_text(txt, reply_markup=close_markup(_))
        elif "vid_" in queued:
            mystic = await CallbackQuery.message.reply_text(
                _["call_7"], disable_web_page_preview=True
            )
            try:
                file_path, direct = await YouTube.download(
                    videoid,
                    mystic,
                    videoid=True,
                    video=status,
                )
            except:
                return await mystic.edit_text(_["call_6"])
            try:
                image = await YouTube.thumbnail(videoid, True)
            except:
                image = None
            try:
                await alya.skip_stream(chat_id, file_path, video=status, image=image)
            except:
                return await mystic.edit_text(_["call_6"])
            button = stream_markup(_, chat_id)
            img = await get_thumb(videoid)
            run = await CallbackQuery.message.reply_photo(
                photo=img,
                caption=_["stream_1"].format(
                    f"https://t.me/{app.username}?start=info_{videoid}",
                    title[:23],
                    duration,
                    user,
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"
            await CallbackQuery.edit_message_text(txt, reply_markup=close_markup(_))
            await mystic.delete()
        elif "index_" in queued:
            try:
                await alya.skip_stream(chat_id, videoid, video=status)
            except:
                return await CallbackQuery.message.reply_text(_["call_6"])
            button = stream_markup(_, chat_id)
            run = await CallbackQuery.message.reply_photo(
                photo=STREAM_IMG_URL,
                caption=_["stream_2"].format(user),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
            await CallbackQuery.edit_message_text(txt, reply_markup=close_markup(_))
        else:
            if videoid == "telegram":
                image = None
            elif videoid == "soundcloud":
                image = None
            else:
                try:
                    image = await YouTube.thumbnail(videoid, True)
                except:
                    image = None
            try:
                await alya.skip_stream(chat_id, queued, video=status, image=image)
            except:
                return await CallbackQuery.message.reply_text(_["call_6"])
            if videoid == "telegram":
                button = stream_markup(_, chat_id)
                run = await CallbackQuery.message.reply_photo(
                    photo=TELEGRAM_AUDIO_URL
                    if str(streamtype) == "audio"
                    else TELEGRAM_VIDEO_URL,
                    caption=_["stream_1"].format(
                        config.SUPPORT_CHAT, title[:23], duration, user
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            elif videoid == "soundcloud":
                button = stream_markup(_, chat_id)
                run = await CallbackQuery.message.reply_photo(
                    photo=SOUNCLOUD_IMG_URL
                    if str(streamtype) == "audio"
                    else TELEGRAM_VIDEO_URL,
                    caption=_["stream_1"].format(
                        config.SUPPORT_CHAT, title[:23], duration, user
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            else:
                button = stream_markup(_, chat_id)
                img = await get_thumb(videoid)
                run = await CallbackQuery.message.reply_photo(
                    photo=img,
                    caption=_["stream_1"].format(
                        f"https://t.me/{app.username}?start=info_{videoid}",
                        title[:23],
                        duration,
                        user,
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "stream"
            await CallbackQuery.edit_message_text(txt, reply_markup=close_markup(_))

    else:
        playing = db.get(chat_id)
        if not playing:
            return await CallbackQuery.answer(
                _["queue_2"], show_alert=True
            )
        duration_seconds = int(playing[0]["seconds"])
        if duration_seconds == 0:
            return await CallbackQuery.answer(
                _["admin_22"], show_alert=True
            )
        file_path = playing[0]["file"]
        if "index_" in file_path or "live_" in file_path:
            return await CallbackQuery.answer(
                _["admin_22"], show_alert=True
            )
        duration_played = int(playing[0]["played"])
        if int(command) in [1, 2]:
            duration_to_skip = 10
        else:
            duration_to_skip = 30
        duration = playing[0]["dur"]
        if int(command) in [1, 3]:
            if (duration_played - duration_to_skip) <= 10:
                bet = seconds_to_min(duration_played)
                return await CallbackQuery.answer(
                    f"» ʙᴏᴛ ɪs ᴜɴᴀʙʟᴇ ᴛᴏ sᴇᴇᴋ ʙᴇᴄᴀᴜsᴇ ᴛʜᴇ ᴅᴜʀᴀᴛɪᴏɴ ᴇxᴄᴇᴇᴅs.\n\nᴄᴜʀʀᴇɴᴛʟʏ ᴩʟᴀʏᴇᴅ :** {bet}** ᴍɪɴᴜᴛᴇs ᴏᴜᴛ ᴏғ **{duration}** ᴍɪɴᴜᴛᴇs.",
                    show_alert=True,
                )
            to_seek = duration_played - duration_to_skip + 1
        else:
            if (
                duration_seconds
                - (duration_played + duration_to_skip)
            ) <= 10:
                bet = seconds_to_min(duration_played)
                return await CallbackQuery.answer(
                    f"» ʙᴏᴛ ɪs ᴜɴᴀʙʟᴇ ᴛᴏ sᴇᴇᴋ ʙᴇᴄᴀᴜsᴇ ᴛʜᴇ ᴅᴜʀᴀᴛɪᴏɴ ᴇxᴄᴇᴇᴅs.\n\nᴄᴜʀʀᴇɴᴛʟʏ ᴩʟᴀʏᴇᴅ :** {bet}** ᴍɪɴᴜᴛᴇs ᴏᴜᴛ ᴏғ **{duration}** ᴍɪɴᴜᴛᴇs.",
                    show_alert=True,
                )
            to_seek = duration_played + duration_to_skip + 1
        await CallbackQuery.answer()
        mystic = await CallbackQuery.message.reply_text(_["admin_24"])
        if "vid_" in file_path:
            n, file_path = await YouTube.video(
                playing[0]["vidid"], True
            )
            if n == 0:
                return await mystic.edit_text(_["admin_22"])
        try:
            await alya.seek_stream(
                chat_id,
                file_path,
                seconds_to_min(to_seek),
                duration,
                playing[0]["streamtype"],
            )
        except:
            return await mystic.edit_text(_["admin_26"])
        if int(command) in [1, 3]:
            db[chat_id][0]["played"] -= duration_to_skip
        else:
            db[chat_id][0]["played"] += duration_to_skip
        string = _["admin_25"].format(seconds_to_min(to_seek))
        await mystic.edit_text(
            f"{string}\n\nᴄʜᴀɴɢᴇs ᴅᴏɴᴇ ʙʏ : {mention} !"
        )

async def markup_timer():
    while not await asyncio.sleep(5):
        active_chats = await get_active_chats()
        for chat_id in active_chats:
            try:
                if not await is_music_playing(chat_id):
                    continue
                playing = db.get(chat_id)
                if not playing:
                    continue
                duration_seconds = int(playing[0]["seconds"])
                if duration_seconds == 0:
                    continue
                try:
                    mystic = playing[0]["mystic"]
                except:
                    continue
                try:
                    check = checker[chat_id][mystic.id]
                    if check is False:
                        continue
                except:
                    pass
                try:
                    language = await get_lang(chat_id)
                    _ = get_string(language)
                except:
                    _ = get_string("en")
                try:
                    buttons = stream_markup_timer(
                        _,
                        chat_id,
                        seconds_to_min(playing[0]["played"]),
                        playing[0]["dur"],
                    )
                    await mystic.edit_reply_markup(
                        reply_markup=InlineKeyboardMarkup(buttons)
                    )
                except:
                    continue
            except:
                continue


asyncio.create_task(markup_timer())