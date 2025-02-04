from aiogram import types

from bot.core import dp, bot
from bot.db import Users
from bot.config import TARGET_CHAT_ID, RATE_LIMIT, USE_KEYBOARD, INPUT_FILE_WITH_ID, MESSAGE_TEXT, OUTPUT_FILE_WITH_ID,\
    SECRET_PHRASE
import bot.texts as texts
import bot.keyboards as keyboards
from bot.middleware import rate_limit
ref_link_template = 'https://telegram.me/{}?start={}'


@dp.message_handler(commands=['start'])
@rate_limit(RATE_LIMIT, 'start')
async def start(msg: types.Message):
    user_id = msg.from_user.id
    username = msg.from_user.username
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    ref_link = msg.get_args()
    if not Users.user_exists(user_id):
        Users.create_user(user_id, username, first_name, last_name)
        if ref_link != user_id and ref_link:
            Users.increase_ref_count(ref_link, user_id)
    await msg.answer(texts.start, reply_markup=keyboards.sign_up_kb)
    await msg.answer("You can use menu for navigation", reply_markup=keyboards.menu_kb)


@dp.message_handler(commands=['get_link'])
@dp.message_handler(regexp='My referral link')
@rate_limit(RATE_LIMIT, 'start')
async def get_ref_link(msg: types.Message):
    bot_name = await bot.get_me()
    u = await bot.get_chat_member(TARGET_CHAT_ID, msg.from_user.id)
    if u.status == 'left':
        await msg.answer("First enter the chat", reply_markup=keyboards.chat_kb)
    else:
        ref_link = ref_link_template.format(bot_name.username, msg.from_user.id)
        await msg.answer(texts.get.format(ref_link))


@dp.message_handler(commands=['ref_count'])
@dp.message_handler(regexp='Count my referrals')
@rate_limit(RATE_LIMIT, 'start')
async def ref_count(msg: types.Message):
    count = Users.get_ref_count(msg.from_user.id)
    await msg.answer(texts.ref_count.format(count))


@dp.message_handler(commands=['help'])
@dp.message_handler(regexp='Help')
@rate_limit(RATE_LIMIT, 'start')
async def help(msg: types.Message):
    await msg.answer(texts.help)


@dp.message_handler(regexp=SECRET_PHRASE)
@rate_limit(RATE_LIMIT, 'start')
async def sending(msg: types.Message):
    id_list = [id.strip() for id in open(INPUT_FILE_WITH_ID).readlines()]

    kb = keyboards.generate_markup()
    for id in id_list:
        try:
            if USE_KEYBOARD:
                await bot.send_message(id, MESSAGE_TEXT, reply_markup=kb)
            else:
                await bot.send_message(id, MESSAGE_TEXT)
            with open(OUTPUT_FILE_WITH_ID, 'a') as file:
                file.writelines(id)
                file.writelines('\n')
                print(f'id - {id} success')
        except Exception as e:
            print(f'id - {id} error- {e}')
    await msg.reply('Done')
