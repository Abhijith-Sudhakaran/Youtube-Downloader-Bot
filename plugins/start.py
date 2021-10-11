from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Lasiya = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("Owner 🌻", url="https://t.me/Telecat_X")],
        [InlineKeyboardButton(
            "Complaint & Suggestions📋", url="https://t.me/CatX_botz_chat")],
        [InlineKeyboardButton(
            "Updates ⚙",url="https://t.me/CatX_botz")]
    ])
    thumbnail_url = "https://telegra.ph/file/a488092b0f602ae43bbf0.jpg"
    await message.reply_photo(thumbnail_url, caption=f"Hellow<b>{message.from_user.first_name}</b>\n\n **• I am a Simple Youtube Downloader Bot. I can Download your Youtube Videos as Fast as I can.**\n\n ! - Sometime Downloading Became slowed down due to Heavy traffic in Server.\n•Join Update Channel Must for New features!.\n\n **Powered by** @CatX_botz 💚", reply_markup=Lasiya)
    raise StopPropagation
