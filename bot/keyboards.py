from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

chat_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Join chat', 'https://t.me/cryptotribunal'))

sign_up_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Join chat', 'https://t.me/cryptotribunal'))
sign_up_kb.add(InlineKeyboardButton('Sign up', 'https://ubikiri.com/auth/login-registration?returnUrl=%2F'))

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)

link_btn = KeyboardButton("My referral link")
count_btn = KeyboardButton("Count my referrals")
help_btn = KeyboardButton("Help")

menu_kb.row(link_btn, count_btn, help_btn)