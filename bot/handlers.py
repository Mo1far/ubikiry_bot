from aiogram import types

from bot.core import dp, bot
from bot.db import Users
from bot.config import TARGET_CHAT_ID
import bot.texts as texts
import bot.keyboards as keyboards
from bot.middleware import rate_limit
ref_link_template = 'https://telegram.me/MyFirstFackingBot?start=x3v5{}'


@dp.message_handler(commands=['start'])
@rate_limit(5, 'start')
async def start(msg: types.Message):
    user_id = msg.from_user.id
    username = msg.from_user.username
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    ref_link = msg.get_args()
    if not Users.user_exists(user_id):
        Users.create_user(user_id, username, first_name, last_name)
        if ref_link != user_id:
            Users.increase_ref_count(ref_link, user_id)
    await msg.answer(texts.start, reply_markup=keyboards.sign_up_kb)


@dp.message_handler(commands=['my_link'])
async def get_ref_link(msg: types.Message):
    u = await bot.get_chat_member(TARGET_CHAT_ID, msg.from_user.id)
    if u.status == 'left':
        await msg.answer("First enter the chat", reply_markup=keyboards.chat_kb)
    else:
        ref_link = ref_link_template.format(msg.from_user.id)
        await msg.answer(texts.get.format(ref_link))


@dp.message_handler(commands=['count'])
async def ref_count(msg: types.Message):
    count = Users.get_ref_count(msg.from_user.id)
    await msg.answer(texts.ref_count.format(count))


@dp.message_handler(commands=['g'])
async def h(msg: types.Message):
    chat_id = msg.chat.id
    user_id = msg.from_user.id
    await msg.answer(f"Chat id - {chat_id} user_id-{user_id}")
