from settings import *
from .buttons import *
from .correct_mail import *
from .States import *
from models.users import User

# Jpg
file_list1 = ['data/1.jpg', 'data/2.jpg', 'data/3.jpg',
              'data/4.jpg', 'data/5.jpg', 'data/6.jpg',
              'data/7.jpg', 'data/8.jpg', 'data/9.jpg']

res_data1 = []
for file in file_list1:
    with open(file, 'rb') as fl:
        res_data1.append(fl.read())

file_list2 = ['data/10.jpg', 'data/11.jpg', 'data/12.jpg',
              'data/13.jpg', 'data/14.jpg', 'data/15.mp4',
              'data/16.jpg', 'data/17.jpg', 'data/18.jpg',
              'data/19.jpg', 'data/20.jpg', 'data/21.jpg',
              'data/22.jpg', 'data/23.jpg', 'data/24.jpg']

res_data2 = []
for file in file_list2:
    with open(file, 'rb') as fl:
        res_data2.append(fl.read())


@dp.message_handler(commands='start')
async def start(message: types.Message):
    if str(message.chat.id) != config['Chat']['chat_id']:
        id = str(message.chat.id)
        message.bot.user_data[id] = User(id, message.chat.username, message.chat.first_name) # Создание модели пользователя и

        await bot.send_photo(
            message.chat.id, res_data1[0],
            "🇷🇺️ Уважаемый {0.first_name} ❗\n"
            "Внимательно читайте и делайте что вам пишут, и проблем не будет.\n"
            "Нажми НАЧАТЬ  на кнопке снизу👇️и мы начнем\n"
            "--------------------------------------\n"
            "🇬🇧️ Dear {0.first_name} ❗\n"
            "Read carefully and do what they write to you, and there will be no "
            "problems.\n"
            "Click the START button on the bottom 👇️ and we will begin\n"
            .format(message.from_user), reply_markup=keyboard1)

    elif str(message.chat.id) == config['Chat']['chat_id']:
        chat_id = config['Chat']['chat_id']
        await bot.send_photo(
            chat_id, res_data2[9],
            "{0.first_name},не нужно здесь писать, здесь всё уже продумали за вас.\n\n"
            "Достаточно читать и делать как написано❗️"
            "-----------------------------------------------------------\n"
            "{0.first_name}, no need to write here, everything has already been thought out for you.\n\n"
            "It is enough to read and do as it is written❗️".format(message.from_user))

        await bot.delete_message(chat_id, message.message_id)
        await asyncio.sleep(5)
        await bot.delete_message(chat_id, message.message_id + 1)


@dp.callback_query_handler(lambda call: call.data == 'st.start')
async def mail_entry(call: types.CallbackQuery):

    await call.message.answer_photo(
        res_data1[1],
        "🇷🇺️ Напишите ПОЧТУ с которой вы покупали\n"
        "(которую вы вводили при покупке)👇️\n"
        "-----------------------------\n"
        "🇬🇧️ Write the MAIL with which you bought\n"
        "(which you entered when purchasing)👇️")

    await Form.mail.set()

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.message_handler(state=Form.mail)
async def mail_handler(message: types.Message, state: FSMContext):
    email = message.text

    if is_valid_email(email):
        id = str(message.chat.id)
        message.bot.user_data[id].mail = email

        async with state.proxy() as data:
            data['mail'] = message.text

        await bot.send_photo(
            message.chat.id, res_data1[2],
            "🇷🇺️Напишите название ИГРЫ которую приобрели👇\n"
            "️---------------------------------\n"
            "🇬🇧️Write the name of the GAME you purchased👇️")
        await Form.next()
    else:
        await bot.send_message(message.chat.id,
                         "Вас разве это попросили сделать⁉️")

        await bot.delete_message(message.chat.id, message.message_id)
        await asyncio.sleep(5)
        await bot.delete_message(message.chat.id, message.message_id + 1)


@dp.message_handler(state=Form.game)
async def game_handler(message: types.Message, state: FSMContext):
    game = message.text

    id = str(message.chat.id)
    message.bot.user_data[id].game_name = game

    await bot.send_photo(message.chat.id, res_data1[3],
                    "🇷🇺️Выберите площадку на которой приобретали ИГРУ👇️\n"
                    "---------------------------------\n"
                    "🇬🇧️Select the site where you purchased the GAME👇️\n", reply_markup=sell)
    await state.finish()


@dp.callback_query_handler(text_contains='mr.')
async def Shops(call: types.CallbackQuery):

    id = str(call.message.chat.id)
    call.bot.user_data[id].market_name = str(call.data) # user market

    json_data = check_n_load_json(BASE_JSON_FILEPATH)

    # Cохранение в JSON
    with open(BASE_JSON_FILEPATH, "w", encoding='utf-8') as file:
        # Добавление пользователя в БД
        json_data.update(call.bot.user_data[id].to_dict())
        # Запись в файд
        json.dump(json_data, file, indent=4, ensure_ascii=False)

        await bot.send_message(config['meid']['id'], call.bot.user_data[id].to_str())


    await bot.send_photo(call.message.chat.id, res_data1[4],
                   "🇷🇺️ Передача аккаунта третьим лицам строго ЗАПРЕЩЕНА, \n"
                   "влечет за собой ограничение на дальнейшие покупки и доступ в аккаунт\n"
                   "-------------------------------------------------------------\n"
                   "🇬🇧️ Transferring an account to third parties is strictly FORBIDDEN, "
                   "entails a restriction on further purchases and access to the account"
                   .format(call.message.from_user), reply_markup=ok)

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.callback_query_handler(text_contains='k.')
async def okey(call):
    username = call.message.chat.first_name
    if call.data == "k.ok":
        await bot.send_photo(call.message.chat.id, res_data1[5],
                       "🇷🇺Если вы купили с другом и вам попался одинаковый, не \n"
                       "паникуйте, напишете АДМИНУ и вам дадут другой аккаунт 👭️\n"
                       "------------------------------------------------\n"
                       "🇬🇧️If you bought with a friend and you got the same one, don't \n"
                       "panic, write to ADMIN and you will be given another account 👭️"
                       .format(call.message.from_user), reply_markup=ok1)


    elif call.data == "k.ok1":
        await bot.send_photo(call.message.chat.id, res_data1[6],
                       username + " На каком языке продолжить⁉️\n\n"
                        + username + " In which language to continue⁉️"
                       .format(call.message.from_user), reply_markup=lang)

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.callback_query_handler(text_contains='l.')
async def okey(call):
    if call.data == "l.ru":
        await bot.send_photo(call.message.chat.id, res_data1[7],
                       "Если у вас возникнет проблема или появится вопрос, то не"
                       "нужно суетиться и кидаться в панику, там в ЧАТ-БОТЕ, куда будут"
                       "приходить коды будет кнопка " + " ПОМОЩЬ " + ", вы обязательно"
                       "найдете свой ответ на вопрос или свяжетесь с АДМИНОМ, и"
                       "вам обязательно ответят и помогут, или заменят, или дадут другой.\n\n"
                       "И не начинайте с негатива😉️\n"
                       .format(call.message.from_user), reply_markup=okk2)

    elif call.data == "l.en":
        await bot.send_photo(call.message.chat.id, res_data1[7],
                       "If you have a problem or a question, then there is no need to fuss"
                       "and panic, there in the CHAT-BOT where the codes will come there"
                       "will be a " + " HELP " + " button, you will definitely find your answer to the"
                       "question or contact the ADMIN, and they will definitely answer you"
                       "and help, or replace, or give another.\n\n"
                       "And don't start with the negative😉️\n"
                       .format(call.message.from_user), reply_markup=okk3)

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.callback_query_handler(text_contains='ko.')
async def okkey(call):
    username = call.message.chat.first_name
    if call.data == "ko.ok3":
        await bot.send_photo(call.message.chat.id, res_data1[8],
                       "Thank you very much " + username + " for doing everything right👍️❗️\n\n"
                       "Press the " + "GO" + " button👇️ you will be taken to the BOTA where "
                       "only CODES come, you do not need to enter anything there, you "
                       "enter the login and password in STEAM itself, as above in the "
                       "picture, and the CODE will come to the BOTA. After the transition,"
                       "click RUN (at the bottom of the screen).\n\n"
                       "And do not forget about the " + "HELP" + " button,"
                       " press it when you need it and they will help you. Good luck❗️️\n"
                       .format(call.message.from_user), reply_markup=go)

    elif call.data == "ko.ok2":
        await bot.send_photo(call.message.chat.id, res_data1[8],
                       "Спасибо большое  " + username + " , что все сделали правильно👍️❗️\n\n"
                       "Нажимайте на кнопку" + " ПЕРЕЙТИ" + "👇️ вы попадете в БОТА куда"
                       "приходят только КОДЫ, вводить туда ничего не нужно, логин и "
                       "пароль вы вводите в сам STEAM, как выше на картинке, а в "
                       "БОТА придет КОД. После перехода нажмите ЗАПУСТИТЬ\n (внизу экрана)\n\n"
                       "И не забывайте про кнопку" + "ПОМОЩЬ" + ", нажмёте её когда вам она"
                       "понадобится и вам помогут. Удачи❗️\n"
                       .format(call.message.from_user), reply_markup=go)

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

    await bot.send_message(call.message.chat.id, "👇Меню", reply_markup = Help_Steam_Guard)

@dp.message_handler(content_types='text')
async def start(message: types.Message):
    if message.text.lower() == 'меню' and str(message.chat.id) != config['Chat']['chat_id']:
        await bot.send_photo(
            message.chat.id, res_data2[0],
            "Сейчас ответим на все твои вопросы❗️\n\n"
            "Выберите нужный из списка ниже и нажмите КНОПКУ👇️"
            .format(message.from_user), reply_markup=Help)
        await bot.delete_message(message.chat.id, message.message_id)

    elif str(message.chat.id) == config['Chat']['chat_id']:
        chat_id = config['Chat']['chat_id']
        await bot.send_photo(
            chat_id, res_data2[9],
            "{0.first_name},не нужно здесь писать, здесь всё уже продумали за вас.\n\n"
            "Достаточно читать и делать как написано❗️"
            "-----------------------------------------------------------\n"
            "{0.first_name}, no need to write here, everything has already been thought out for you.\n\n"
            "It is enough to read and do as it is written❗️".format(message.from_user))

        await bot.delete_message(chat_id, message.message_id)
        await asyncio.sleep(3)
        await bot.delete_message(chat_id, message.message_id + 1)

        await bot.restrict_chat_member(message.chat.id, message.from_id, types.ChatPermissions(False), until_date = 10)

    elif message.text == "/all_inf":
        if str(message.chat.id) == str(config['meid']['id']):
            with open("settings/user_data.json", "rb") as file:
                await bot.send_document(config['meid']['id'], document=file)

        else:
            await bot.send_message(
                message.chat.id,
                "Вас разве это попросили сделать⁉️")

            await bot.delete_message(message.chat.id, message.message_id)
            await asyncio.sleep(5)
            await bot.delete_message(message.chat.id, message.message_id + 1)

    else:
        await bot.send_message(
            message.chat.id,
            "Вас разве это попросили сделать⁉️")

        await bot.delete_message(message.chat.id, message.message_id)
        await asyncio.sleep(5)
        await bot.delete_message(message.chat.id, message.message_id + 1)