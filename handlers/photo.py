
from handlers.from_pic_get_text import main
from handlers.translation import translation
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
import pyttsx3

from gtts import gTTS
from loader import dp,bot





from keybord.default import button
@dp.message_handler(Command("start"))
async def start(message:Message):
    await message.reply("Kategoriyani tanlang",reply_markup=button)
@dp.message_handler(text="Rasmdagi matnni o'zbek tiliga tarjima qilish")
async def start(message:Message):
    await message.reply("Rasm tashlang")
    @dp.message_handler(content_types=['photo'])
    async def handle_docs_photo(message):

        await message.photo[-1].download('pictranslate/test.jpg')

        a=main()
        t=translation(a[1:-1])
        await message.reply(t)


@dp.message_handler(text="Texni o'zbek tiliga tarjima qilish")
async def start(message:Message):
    await message.reply("Textni tashlang")


    @dp.message_handler()
    async def translate(message:Message):
        text = message.text

        t = translation(text)
        await message.reply(t)

@dp.message_handler(text="Texni auidoga ogirish")
async def audio_start(message:Message):
    await message.reply("Textni tashlang")


    @dp.message_handler(content_types='text')
    async def auido(message:Message):
        text=message.text
        engine = pyttsx3.init()


        engine.say(text)
        print(text)
        tts = gTTS(text=text, lang='ru')
        tts.save('file.mp3')
        await bot.send_audio(message.from_user.id, open('file.mp3', 'rb'))
