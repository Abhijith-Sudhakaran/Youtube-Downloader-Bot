from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/Cat_Telegram_Projects")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Cat_Telegram_Project_Club")]
    ]
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n I am the bot which allow to download videos & Audios from Youtube😜 with High Quality.use /help for More info.Send me your Youtube link First😊. Select Your Quality Of Video or Audio😊. **Note - If You Select High Quality File.Its normally Take some more Time to Upload😊** .Thank You For using Our service💟... Type /help To Get Some Informations About me..."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
