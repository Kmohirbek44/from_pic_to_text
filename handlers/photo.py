from loader import dp
from handlers.from_pic_get_text import main
from handlers.translation import translation
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
import pyttsx3
from aiogram.types.base import InputFile
from gtts import gTTS
from loader import dp,bot
from time import sleep

# @dp.message_handler(Command('start'))
# async def audio(message:Message):

# await message.answer('textni kiriting')

@dp.message_handler(Command("start"))
async def start(message:Message):
    await message.reply("rasm yuboring")

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):

    await message.photo[-1].download('pictranslate/test.jpg')

    a=main()
    t=translation(a[1:-1])
    await message.reply(t)

    engine = pyttsx3.init()

    print(type(t))
    print(t)
    engine.say(t)
    print(t)
    tts = gTTS(text=t, lang='ru')
    tts.save('file.mp3')
    await bot.send_audio(message.from_user.id, open('file.mp3', 'rb'))