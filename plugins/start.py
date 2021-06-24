from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/Cat_Telegram_Projects")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Cat_Telegram_Project_Club")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n I am the bot which allow to download videos from Youtube😜.use /help for More info and Usage.__Created by [CAT](https://t.me/Cat_of_telegramx)"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
