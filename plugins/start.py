from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/Cat_Telegram_Projects")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Cat_Telegram_Project_Club")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n https://telegra.ph/About-Yourtube-Bot-06-24"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
