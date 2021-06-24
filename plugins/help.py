from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Hey.I am Currently Support Single Youtube Links.(Playlist Added Soon)</b>\n I Am Currently Running in Pyrogram.Sometime speed become slowed down due to heavy Traffic.</b>\n **My Master is** @Cat_of_TelegramX .</b>\n If You Have Any Doubts Contact in @Cat_Telegram_Project_Club 🤗.</b>\n Thank You For Using Our Services💟."
    await message.reply_text(helptxt)
