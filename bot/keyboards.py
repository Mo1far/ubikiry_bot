from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

chat_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Join chat', 'https://t.me/cryptotribunal'))

sign_up_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Join chat', 'https://t.me/cryptotribunal'))
sign_up_kb.add(InlineKeyboardButton('Sign up', 'http://ubikiri.com/auth/telegram-login?returnUrl=%2F'))

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)

link_btn = KeyboardButton("My refferal link")
count_btn = KeyboardButton("Count of my refferals")
help_btn = KeyboardButton("Help")

menu_kb.row(link_btn, count_btn, help_btn)