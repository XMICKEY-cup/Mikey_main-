from pyrogram import Client, filters
from pyrogram.types import Message
from Alya import app

@app.on_message(filters.command("groupinfo", prefixes="/"))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("Please provide a group username. Example: `/groupinfo YourGroupUsername`")
        return
    
    group_username = message.command[1]
    
    try:
        group = await app.get_chat(group_username)
    except Exception as e:
        await message.reply(f"Error: {e}")
        return
    
    total_members = await app.get_chat_members_count(group.id)
    group_description = group.description or 'N/A'
    premium_acc = banned = deleted_acc = bot = 0  

    response_text = (
        f"▰▰▰▰▰▰▰▰▰\n"
        f"➲ GROUP NAME : {group.title} ✅\n"
        f"➲ GROUP ID : `{group.id}`\n"
        f"➲ TOTAL MEMBERS : {total_members}\n"
        f"➲ DESCRIPTION : `{group_description}`\n"
        f"➲ USERNAME : @{group_username}\n"
        f"▰▰▰▰▰▰▰▰▰"
    )
    
    await message.reply(response_text)


@app.on_message(filters.command("status") & filters.group)
def group_status(client, message):
    chat = message.chat
    status_text = (
        f"Group ID: {chat.id}\n"
        f"Title: {chat.title}\n"
        f"Type: {chat.type}\n"
    )
                  
    if chat.username:
        status_text += f"Username: @{chat.username}"
    else:
        status_text += "Username: None"

    message.reply_text(status_text)
