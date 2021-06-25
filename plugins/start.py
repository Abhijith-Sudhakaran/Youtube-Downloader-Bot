from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Lasiya = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("Youtube App ❤", url="https://www.youtube.com")],
        [InlineKeyboardButton(
            "Report Bugs 📋", url="https://t.me/Cat_Telegram_Project_Club")],
        [InlineKeyboardButton(
            "Bot Updates ⚙",url="https://t.me/Cat_Telegram_Projects")]
    ])
    thumbnail_url = "https://telegra.ph/file/a488092b0f602ae43bbf0.jpg"
    await message.reply_photo(thumbnail_url, caption=f"Hellow<b>{message.from_user.first_name}</b>\n\n<b>Instructions for use..</b>\n• Type /help to get instructins.\n• ───── ❝ **Lets Play** ❞ ─────\n ", reply_markup=Lasiya)
    raise StopPropagation
