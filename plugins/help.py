from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Hey <b>{message.from_user.first_name}</b>\n I am Currently Support Single Youtube Links.(Playlist Added Soon)</b>\n I Am Currently Running in Pyrogram.Sometime speed become slowed down due to heavy Traffic.</b>\n **My Master is** @Telecat_X .</b>\n Join our Update's Channel now! @CatX_botx.</b>\n Thank You For Using Our Services 💟."
    await message.reply_text(helptxt)
