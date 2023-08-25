from settings import *
from .buttons import *
from .correct_mail import *
from .States import *
from .message import *


@dp.message_handler(content_types=["new_chat_members"])
async def new_member(message: types.Message):
    neme = message.new_chat_members[0].first_name
    chat_id = config['Chat']['chat_id']
    await bot.send_photo(chat_id, res_data1[8],
            "❗️ ПРОЧТИ ЭТО ВАЖНО⚠️\n\n"
            "❌️Если у вас открыт STEAM,\n то закройте его ПОЛНОСТЬЮ и откройте заново.\n\n"
            "✅️Вводите полученные ЛОГИН и ПАРОЛЬ в STEAM, как выше на картинке, а сюда в ЧАТ придет КОД.\n\n"
            "🆘️Если код не пришел или у вас появился вопрос или проблема,\n"
            "нажми на кнопку 'ПОМОЩЬ' или просто напишите в чат слово 'ПОМОЩЬ'❗️"
            , reply_markup=Suport_back)


@dp.callback_query_handler(text_contains='H.')
async def Menu1(call):
    if call.data == "H.1":
        await bot.send_photo(call.message.chat.id, res_data2[1],
            "❌️Если у вас открыт STEAM, то закройте его ПОЛНОСТЬЮ и откройте заново.\n\n"
            "✅️Вводите полученные ЛОГИН и ПАРОЛЬ в STEAM, как выше на картинке, а в ЧАТ придет КОД.\n\n"
            "Сделайте ИМЕННО ТАК, нужно ЗАКРЫТЬ СТИМ полностью (на крестик ❌️)"
            "и открыть его занаво и ввести снова ЛОГИН и ПАРОЛЬ.\n\n"

            "Код приходит от 2х до 5и секунд, не нужно его ждать по 30 минут \n\n"

            "Если и так не пришел то жмите кнопку ПОДДЕРЖКА👇️"
            .format(call.message.from_user), reply_markup=not_all)

    elif call.data == "H.2":
        await bot.send_photo(call.message.chat.id, res_data2[2],
            "Если у вас вот такая ОШИБКА, то это ошибка не КОДА который вы получили , а вашего СТИМА. \n\n"

            "1.Нажмите кнопку ПОВТОРИТЬ➯ВВОД➯ТОТ ЖЕ КОД.\n\n"

            "2.И чистите КЕШ вашего СТИМА"
            .format(call.message.from_user), reply_markup=Backk)

    elif call.data == "H.3":
        await bot.send_photo(call.message.chat.id, res_data2[3],
            "Вы купили 2а и более или вы купили с другом и вам попался\n"
            "одинаковый аккаунт, не истерить и не бить ногами в пол, так и\n"
            "должно быть, так настроена выдача товара.😉️\n\n"

            "Нажмите кнопку АДМИНИСТРАТОР👇️ и Вам дадут другой аккаунт, в этом нет проблемы❗️"
            .format(call.message.from_user), reply_markup=Sup_inf)

    elif call.data == "H.4":
        await bot.send_photo(call.message.chat.id, res_data2[4],
            "У Вас открылось окно что Служба потдержки сбросила пароль🆘️\n\n"

            "Просто закройте его и на этом всё, никто пароль не сбросил и не сбросит, все данные те же❗️"
            .format(call.message.from_user), reply_markup=back_SG)

    elif call.data == "H.5":
        await bot.send_photo(call.message.chat.id, res_data2[5],
            "Если вы не можете найти игру в библиотеке нужно:\n\n"

            "1. Ввести ее название в ПОИСК (слева в аккаунте СТИМ)\n\n"

            "2. Она может быть в скрытой папке\n\n"

            "3. Если и там нет, то смотрите это видео прикрепленное здесь.☝️"
            .format(call.message.from_user), reply_markup=back_SG)

    elif call.data == "H.6":
        await bot.send_photo(call.message.chat.id, res_data2[6],
            "Это не личный аккаунт с полным доступом и почтой и доступ не только у вас👍️\n\n"

            "Отключите у себя в аккаунте СТИМ функцию Steam Remote Play"
            "(https://store.steampowered.com/remoteplay?l=russian)  это для вашей же безопасности🆘️"
            .format(call.message.from_user), reply_markup=back_SG)

    elif call.data == "H.7":
        await bot.send_photo(call.message.chat.id, res_data2[7],
            "Family Library Sharing не предоставляем к сожалению, может быть в дальнейшем, но пока нет.❗️"
            .format(call.message.from_user), reply_markup=back_SG)

    elif call.data == "H.8":
        await bot.send_photo(call.message.chat.id, res_data2[10],
            "Нажмите АДМИНИСТРАТОР для связи с АДМИНОМ,\n"
            "после перехода сразу пишите Ваш вопрос или оставьте заявку,\n"
            "что бы АДМИНИСТРАТОР вам сразу мог ответить. 🆘️\n"
            "Не паникуйте, вам ответят 💯️% как только увидят ваш вапрос,\n"
            "оператор может быть просто не онлайн и обязательно ответит позже.👍️\n\n"

            "Время работы потдержки с 9:00-21:00 ,но это не значит"
            "что вы не можете оставить вопрос, так что пишите смело."
            .format(call.message.from_user), reply_markup=Suport)

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text_contains='Not.')
async def Menu2(call):
    await bot.send_photo(
        call.message.chat.id, res_data2[14],
        "✅️ДЛЯ ПОНИМАНИЯ\n\n"
        "КОД приходит сразу же как вы ввели логин и пароль в СТИМ \n"
        "и при вступлении в ЧАТ куда приходят КОДЫ все что было до \n"
        "вашего вступления ВАМ не видно, ВЫ можете видеть все что \n"
        "после того как вы вступили, а КОД пришел до, следовательно \n"
        "что бы он пришел еще раз нужно сделать как вам написали:👇️ \n"
        "и не нужно пытаться обмануть систему😀️ \n\n"
        "❌️Если у вас открыт STEAM, то закройте его ПОЛНОСТЬЮ и откройте заново.\n"
        "✅️Вводите полученные ЛОГИН и ПАРОЛЬ в STEAM,\n как выше на картинке, а в ЧАТ придет КОД."
        .format(call.message.from_user), reply_markup=Sup_inf)

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.callback_query_handler(text_contains='Sup.')
async def Menu2(call):
    await bot.send_photo(
        call.message.chat.id, res_data2[10],
        "Нажмите АДМИНИСТРАТОР для связи с АДМИНОМ,\n"
        "после перехода сразу пишите Ваш вопрос или оставьте заявку,\n"
        "что бы АДМИНИСТРАТОР вам сразу мог ответить.\n"
        "🆘️ Не паникуйте, вам ответят 💯️% как только увидят ваш вапрос,"
        "оператор может быть просто не онлайн и обязательно ответит позже.👍️\n\n"

        "Время работы потдержки с 9:00-21:00 , но это не значит что вы\n"
        "не можете оставить вопрос, так что пишите смело."
        .format(call.message.from_user), reply_markup=Suport)

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)



@dp.callback_query_handler(text_contains='SUP.')
async def Menu2(call):
    await bot.send_photo(
        call.message.chat.id, res_data2[0],
        "Сейчас ответим на все твои вопросы❗️\n\n"
        "Выберите нужный из списка ниже и нажмите КНОПКУ👇️"
        .format(call.message.from_user), reply_markup=Help)

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)



@dp.callback_query_handler(text_contains='F.')
async def Menu3(call):
    if call.data == "F.1":
        message = await bot.send_photo(call.message.chat.id, res_data2[11],
            "1.{0.first_name} Вставьте любой КОД\n\n"
            "2. Он покажет что код не верный\n\n"
            "3. Введите ЛОГИН и ПАРОЛЬ еще раз\n\n"
            "4. Код должен придти\n\n"
            "5. Если снова не пришел, пишите ПОМОЩЬ в чат"
            .format(call.message.from_user))

    elif call.data == "F.2":
        message = await bot.send_photo(call.message.chat.id, res_data2[12],
            "1. Здесь нет зависимости почему эта ошибка появляеться\n\n"
            "2. Такое происходит с любым аккаунтом, даже в который не заходили очень давно\n\n"
            "3. Вам может помочь VPN, очистка КЕША, оно реагирует на IP адрес\n\n"
            "4. С другого IP вы зайдете без проблем"
            .format(call.message.from_user))

    elif call.data == "F.3":
        message = await bot.send_photo(call.message.chat.id, res_data2[13],
            "1.Если у вас вот такая ОШИБКА, то это ошибка не КОДА который вы получили, а вашего СТИМА\n\n"
            "2.И чистите КЕШ вашего СТИМА"
            .format(call.message.from_user))

    await asyncio.sleep(10)
    await message.delete()

