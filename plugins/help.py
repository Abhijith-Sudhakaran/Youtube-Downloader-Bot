from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url...Join @Cat_Telegram_Project_Club to Support😊."
    await message.reply_text(helptxt)
