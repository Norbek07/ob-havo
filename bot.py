import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.types import Message,CallbackQuery
from weather import inline_menu
import requests
from bs4 import BeautifulSoup as BS

TOKEN = "7083075969:AAGXj8oUQ_PVxwONVZ47chbiA4xlg-bYtgE" #Token kiriting
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Assalomu alaykum, botimizdan foydlanish uchun shaxar nomini bosing!", reply_markup=inline_menu)

city = {"Navoiy":"погода-навои","Fargona":"погода-фергана","Vobkent":"погода-баткен","Andijon":"погода-андижан","Jizzax":"погода-джизак","Qarshi":"погода-карши"}
# boshqa viloyatlarni xam qo'shish kerak. Aiogram botga ulash kerak 


@dp.callback_query(F.data=="navoiy")
async def navoiy_harorat(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    navoiy = ob_havo(city=city.get("Navoiy"))
    await callback.message.edit_text(text=f"Navoiy: {navoiy}")    

@dp.callback_query(F.data=="fargona")
async def fargona_xarorat(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    fargona = ob_havo(city=city.get("Fargona"))
    await callback.message.edit_text(text=f"Fargona: {fargona}")    

@dp.callback_query(F.data=="vobkent")
async def vobkent_harorat(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    vobkent = ob_havo(city=city.get("Vobkent"))
    await callback.message.edit_text(text=f"Vobkent: {vobkent}")   

@dp.callback_query(F.data=="andijon")
async def andijon_harorati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    andijon = ob_havo(city=city.get("Andijon"))
    await callback.message.edit_text(text=f"Andijon: {andijon}")

@dp.callback_query(F.data=="jizzax")
async def jizzax_haroati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    jizzax = ob_havo(city=city.get("Jizzax"))
    await callback.message.edit_text(text=f"Jizzax: {jizzax}")  

@dp.callback_query(F.data=="qarshi")
async def qarshi_harorati(callback:CallbackQuery):

    def ob_havo(city):
        t = requests.get(f"https://sinoptik.ua/{city}")
        html_t = BS(t.content,"html.parser")
        for el in html_t.select('#content'):
            min = el.select('.temperature .min') [0].text
            max = el.select('.temperature .max') [0].text
            return min,max

    qarshi = ob_havo(city=city.get("Qarshi"))
    await callback.message.edit_text(text=f"Qarshi: {qarshi}")           

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

