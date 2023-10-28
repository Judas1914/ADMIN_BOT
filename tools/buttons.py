from aiogram.types import InlineKeyboardButton
from aiogram import Bot, Dispatcher, types
from settings import *


keyboard1 = types.InlineKeyboardMarkup()
start_button = types.InlineKeyboardButton(text="Начать/Start", callback_data="st.start")
keyboard1.add(start_button)

sell = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton(text="Plati.Market", callback_data="mr.PM")
button2 = types.InlineKeyboardButton(text="GGSel.net", callback_data="mr.GGS")
button3 = types.InlineKeyboardButton(text="WMCentre.net", callback_data="mr.WMC")
button4 = types.InlineKeyboardButton(text="Другое/Another", callback_data="mr.GGS")
sell.add(button1, button2, button3, button4)

lang = types.InlineKeyboardMarkup()
ru = types.InlineKeyboardButton(text="РУССКИЙ🇷🇺️", callback_data="l.ru")
en = types.InlineKeyboardButton(text="ENGLISH🇬🇧️", callback_data="l.en")
lang.add(ru, en)

ok = types.InlineKeyboardMarkup()
ok_bt = types.InlineKeyboardButton(text="Согласен/Agree", callback_data="k.ok")
ok.add(ok_bt)

ok1 = types.InlineKeyboardMarkup()
ok_bt1 = types.InlineKeyboardButton(text="Согласен/Agree", callback_data="k.ok1")
ok1.add(ok_bt1)

okk2 = types.InlineKeyboardMarkup()
okk_bt2 = types.InlineKeyboardButton(text="Согласен/Agree", callback_data="ko.ok2")
okk2.add(okk_bt2)

okk3 = types.InlineKeyboardMarkup()
okk_bt3 = types.InlineKeyboardButton(text="Согласен/Agree", callback_data="ko.ok3")
okk3.add(okk_bt3)

go = types.InlineKeyboardMarkup()
go_bt = types.InlineKeyboardButton(text="Перейти/Start", url=config['url']['StGw'])
go.add(go_bt)

###################################################################

Help = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton(text="1️⃣Не приходит Steam Guard", callback_data="H.1")
button2 = types.InlineKeyboardButton(text="2️⃣ОШИБКА", callback_data="H.2")
button3 = types.InlineKeyboardButton(text="3️⃣Я купил два и более аккаунтов", callback_data="H.3")
button4 = types.InlineKeyboardButton(text="4️⃣Окно о сбросе пароля", callback_data="H.4")
button5 = types.InlineKeyboardButton(text="5️⃣Нет игры на Аккаунте", callback_data="H.5")
button6 = types.InlineKeyboardButton(text="6️⃣Кто-то еще заходит в мой аккаунт", callback_data="H.6")
button7 = types.InlineKeyboardButton(text="7️⃣Family Library Sharing", callback_data="H.7")
button8 = types.InlineKeyboardButton(text="8️⃣Не нашли нужного", callback_data="H.8")
button9 = types.InlineKeyboardButton(text='❗️Вернуться в "Steam Guard"❗️' , url=config['url']['StGw'])
Help.add(button1)
Help.add(button2)
Help.add(button3)
Help.add(button4)
Help.add(button5)
Help.add(button6)
Help.add(button7)
Help.add(button8)
Help.add(button9)

Suport = types.InlineKeyboardMarkup()
Sup = types.InlineKeyboardButton(text="🤙ПОДДЕРЖКА", url=config['url']['Supp'])
Back = types.InlineKeyboardButton(text="↩️НАЗАД В МЕНЮ", callback_data="SUP.hi")
Suport.add(Sup)
Suport.add(Back)

Sup_inf = types.InlineKeyboardMarkup()
Support = types.InlineKeyboardButton(text="🤙ПОДДЕРЖКА", callback_data="Sup.all")
Sup_inf.add(Support)
Sup_inf.add(Back)

not_all = types.InlineKeyboardMarkup()
Supp = types.InlineKeyboardButton(text="Не мой случай", callback_data="Not.all")
not_all.add(Supp)
not_all.add(Back)

back_SG = types.InlineKeyboardMarkup()
back_SG.add(button9)
back_SG.add(Back)

Backk = types.InlineKeyboardMarkup()
Backk.add(Back)

Suport_back = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton(text="Не приходит Steam Guard", callback_data="F.1")
button2 = types.InlineKeyboardButton(text="Слишком много попыток", callback_data="F.2")
button3 = types.InlineKeyboardButton(text="Ошибка", callback_data="F.3")
button4 = types.InlineKeyboardButton(text="Помощь", url=config['url']['ADmB'])
Suport_back.add(button1)
Suport_back.add(button2)
Suport_back.add(button3, button4)

###########################################################################
# Помошь в Help_Steam_Guard

Help_Steam_Guard = types.ReplyKeyboardMarkup(resize_keyboard=True)
prob = types.KeyboardButton("меню")
Help_Steam_Guard.add(prob)


