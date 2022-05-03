import requests
from aiogram import executor
from handlers import dp
import config
from items import item
async def on(dp):
    await item.set(dp)
    requests.post(f"https://api.telegram.org/bot{config.token}/sendMessage?chat_id={config.ip}&text=Online")
executor.start_polling(dp,on_startup=on)
