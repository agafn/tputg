from create_tgbot import dp, bot
from aiogram import types, Dispatcher
from keyboards import kb_student, kb_tvor4,kb_ucheba, urlkb,kb_korpusa,nazad
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text


#class number(StatesGroup):
 #   number_of_korpus = State()
  #  number_audit = State()

class InputClassroomNumber(StatesGroup):
    number_classroom = State()

@dp.callback_query_handler(text='/Назад')
async def func_return(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer('Главное меню',reply_markup=kb_student)

#################приветствие##################################
#@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    await message.answer(f'Привет!\n'
                        'Я - твой личный помощник.\n'
                        'И я помогу тебе в твоей адаптации.\n',reply_markup=kb_student)
    await message.delete()

##############################################################
@dp.callback_query_handler(text='culture')
async def culture_call(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer('Студенчество – это не только учеба.\n'
                         ' ТПУ создает безграничные возможности для активной, творческой жизни студентов!',reply_markup=kb_tvor4)

###################################################Учебный процесс
@dp.callback_query_handler(text='ucheba')
async def ucheba_call(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id) ##удаляет сообщение предыдущие
    await callback.message.answer('Что именно интересует?',reply_markup=kb_ucheba)
    #await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

@dp.callback_query_handler(text='lk')#########личный кабинет
async def lk_call(callback:types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer('<b>В твоем личном кабинете доступны следующие сервисы:</b>\n'
                                  '\n'
                                  '&#9725;Личное дело\n'
                                  '&#9725;Аттестация\n'
                                  '&#9725;Успеваемость\n'
                                  '&#9725;Учебный план\n'
                                  '\n'
                                  '1. Для доступа в личный кабинет необходимо перейти по адресу desktop.tpu.ru или открыть «Корпоративный портал ТПУ» (portal.tpu.ru) и нажать на кнопку <b>Личный кабинет</b>\n'
                                  '\n'
                                  '2. В открывшемся окне вводи имя пользователя (логин) и пароль, затем жми кнопку <b>Регистрация</b>(При правильном введении логина и пароля ты получишь доступ в свой ЛИЧНЫЙ КАБИНЕТ)',parse_mode='HTML',reply_markup=nazad)

@dp.callback_query_handler(text='cash')
async def cash_call(callback:types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer('<b>Государственная стипендия</b>\n'
                                  'Поступление на бюджет само по себе гарантирует получение минимальной стипендии. В Томском политехе эта сумма для бакалавров и специалистов составляет примерно 3 250 рублей. В первом семестре первого года обучения стипендию получают все. Затем, для ее получения нужно закрыть сессию без "троек" и не иметь академической задолженности.\n'
                                  '\n<b>Повышенная государственная академическая стипендия</b>\n'
                                  'Это надбавка за успехи в учебной, исследовательской, общественной, культурно-творческой и спортивной деятельности. Устанавливается решением Ученого совета ТПУ каждый семестр с учетом мнения Совета студентов ТПУ и Первичной профсоюзной организации студентов и аспирантов ТПУ. Следи за объявлениями (на сайте ТПУ, в системе «Фламинго» flamingo.tpu.ru) и участвуй в конкурсах!\n'
                                  '\n<b>Государственная социальная стипендия</b>\n'
                                  'Назначается студентам, являющимся детьми-сиротами, детьми, оставшимися без попечения родителей и др. Подробнее о возможности получения социальной стипендии можно узнать в Центре социальной работы ТПУ: пр. Ленина, 45 (вход со стороны пр. Ленина), телефон: (3822) 60 64 64.\n'
                                  '\n<b>Именные стипендии</b>\n'
                                  '\nНазначаются студентам очной формы обучения. Об объявленных конкурсах на назначение именных стипендий можно узнать в Едином деканате, в Центре научной карьеры или на цифровой коммуникационной площадке «Фламинго» (flamingo.tpu.ru).\n'
                                  '\n<b>Стипендии Президента Российской Федерации и Правительства Российской Федерации</b>\n\n'
                                  '<b>Стипендии из средств от приносящей доход деятельности университета</b>\n\n'
                                  '<i>Студенты имеют право на несколько видов стипендий одновременно. Если быть активным, следить за информацией, участвовать в конкурсах, можно получать несколько десятков тысяч рублей в месяц.</i>',parse_mode='HTML',reply_markup=nazad)

@dp.callback_query_handler(text='exam')
async def exam_call(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer('https://www.youtube.com/watch?v=CVJggFVXPxM&t',reply_markup=nazad)

@dp.callback_query_handler(text='lessons')
async def lessons_call(callback:types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer('https://www.youtube.com/watch?v=9a7bdfl0XJw&t',reply_markup=nazad)

@dp.callback_query_handler(text='points')
async def points_call(callback:types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer('https://www.youtube.com/watch?v=MBh6PjOp58c',reply_markup=nazad)

@dp.callback_query_handler(text='rasp')
async def rasp_call(callback:types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer(f"Расписание занятий расположено <a href='rasp.tpu.ru'>здесь</a>",parse_mode='HTML',reply_markup=nazad)
###################################################Карта кампуса
@dp.callback_query_handler(text='gps')

async def gps_call(callback: types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer('Карта кампуса по кнопке ниже',reply_markup=urlkb)


##################################################в корпусах
@dp.callback_query_handler(text='nav')
async def nav_call(callback:types.CallbackQuery):
    await callback.message.answer('Выберите корпус',reply_markup=kb_korpusa)


@dp.callback_query_handler(text_startswith='korp:')
async def corp_choise(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['corpus_name'] = callback.data
    await callback.message.answer('С помощью клавиатуры введите номер аудитории')
    await InputClassroomNumber.number_classroom.set()

@dp.message_handler(state=InputClassroomNumber.number_classroom)
async def naviga(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['classroom_number'] = message.text

        # в data["corpus_name"] у вас будет korp:gk или korp:1, помните это
        #await message.answer(text=f'Вы выбрали аудиторию корпуса {data["corpus_name"]} '
                              #    f'{data["classroom_number"]}')
        # так как нужно просто отсекать число то вот так
        floor = message.text[:1]
        # Как вы храните свои изображения я хз, потому вот как вариант для вас
       # data_with_img = {
        ##    "korp:gk": "path",
          #  "korp:1": "path2",
        #}
        await message.answer_photo(photo=open(f'Карта корпусов/{data["corpus_name"].split(":")[1]}/{floor} этаж.png','rb'),reply_markup=nazad)
        await state.reset_state(with_data=False)



##############Студ жизнь
@dp.callback_query_handler(text='tvor4')
async def tvor4_call(callback:types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer('<b>МЕЖДУНАРОДНЫЙ КУЛЬТУРНЫЙ ЦЕНТР (МКЦ)</b>\n'
                                  'Готов развить все твои таланты. Здесь можно реализовать свои идеи, попробовать себя в роли координатора мероприятия, ведущего, администратора, аниматора, идейного лидера, дизайнера, артиста и так далее. Для этого в МКЦ работает ряд творческих коллективов.\n'
                                  '<b>Адрес</b>: ул. Усова, 13в, МКЦ\n'
                                  '<b>Телефон:</b> (3822)606261, 606263\n'
                                  '<b>Сайт:</b> vk.com/mkc_tpu\n'
                                  '<b>E-mail:</b> Icc.tpu@gmail.com\n\n\n'
                                  
                                  '<b>СТУДЕНЧЕСКОЕ МУЗЫКАЛЬНОЕ ОБЪЕДИНЕНИЕ «ДОМИНАНТА»</b>\n'
                                  'Создано для тех, кто хочет заниматься музыкой и принимать активное участие в различных мероприятиях, концертах и конкурсах.\n'
                                  '<b>Руководитель:</b> Максим Михайлович Мясоедов\n'
                                  '<b>Контактный телефон:</b> (3822) 60 62 61\n\n\n'
                                  ''
                                  '<b>ШКОЛА КЛАССИЧЕСКОГО ВОКАЛА НАРОДНОЙ АРТИСТКИ РОССИИ Л.Ф. ТРАВКИНОЙ</b>\n'
                                  'В школе ведется индивидуальная работа со студентами по развитию вокальных данных, подбираются программы с учетом индивидуальных особенностей. Многие из вокалистов блистают на сцене в разных городах России.\n'
                                  '<b>Руководитель:</b> Людмила Федоровна Травкина\n'
                                  '<b>Контактный телефон:</b> (3822) 60 62 61\n\n\n'
                                  ''
                                  '<b>СТУДИЯ ЭСТРАДНОГО ВОКАЛА «ОТРАЖЕНИЕ»</b>\n'
                                  'Здесь ты сможешь петь и ярко выступать на конкурсах и фестивалях самого разного уровня.\n'
                                  '<b>Руководитель:</b> Татьяна Николаевна Виноградова\n'
                                  '<b>Контактный телефон:</b> (3822) 60 62 61\n\n\n'
                                  ''
                                  '<b>TАНЦЕВАЛЬНАЯ СБОРНАЯ ТПУ</b>\n'
                                  'Вместо слов можно танцевать! Студенты сборной участвуют в самых ярких мероприятиях ТПУ, выступают на городских площадках, принимают участие в конкурсах и различных проектах\n'
                                  '<b>Руководитель:</b> Екатерина Сулема\n'
                                  '<b>Контактный телефон:</b> +7 903 954 73 96\n\n\n'
                                  ''
                                  '<b>СТУДЕНЧЕСКОЕ ТВОРЧЕСКОЕ ОБЪЕДИНЕНИЕ ТПУ</b>\n'
                                  'Здесь самые креативные, яркие, талантливые студенты ТПУ (и ты можешь быть в их числе) делают творческие мероприятия, развивают и создают новые творческие коллективы на базе МКЦ и на базе общежитий ТПУ.\n'
                                  '<b>Руководитель:</b> Наталья Климова\n'
                                  '<b>Контактный телефон:</b> +7 962 792 75 10\n\n\n'
                                  ''
                                  '<b>СТУДОТРЯДЫ ТПУ</b>\n'
                                  'Движение студенческих отрядов ТПУ — это реальная сила! Строители, энергетики, проводники, вожатые, работники сервиса и сельского хозяйства. Только в этом году ребята трудятся в Крыму и Иркутской области, на всероссийских студенческих стройках в Северске и Озерске, на международной студенческой стройке в Кемерове и даже за рубежом! В студотрядах ТПУ ты точно найдешь себе занятие по душе, заработаешь, а также обеспечишь интересную жизнь, ведь мероприятия у ребят идут круглый год.\n'
                                  '<b>Адрес:</b> пр. Кирова, 2, вход с торца\n'
                                  '<b>Группа «ВКонтакте»:</b> vk.com/vshsotpu\n\n\n'
                                  ''
                                  '<b>МЕДИАЦЕНТР ТПУ</b>\n'
                                  'Студенческое объединение, которое работает на бренд ТПУ, создает лучший вузовский ТикТок страны (@tpu.house — более 12,5 тыс. подписчиков и более 1,8 млн просмотров), проекты на YouTube и ведет Инстаграм @media.tpu.\n'
                                  'Ты можешь стать частью этой креативной команды и вместе с единомышленниками реализовывать свои крутые проекты!\n'
                                  '<b>Сайт:</b> https://vk.com/media_tpu\n'
                                  '<b>Адрес:</b> ул. Усова, 13б, вход с торца',parse_mode='HTML',reply_markup=nazad)
    #await callback.message.answer('<b>СТУДЕНЧЕСКОЕ МУЗЫКАЛЬНОЕ ОБЪЕДИНЕНИЕ «ДОМИНАНТА»</b>\n'
    #                              'Создано для тех, кто хочет заниматься музыкой и принимать активное участие в различных мероприятиях, концертах и конкурсах.\n'
    #                              '<b>Руководитель:</b> Максим Михайлович Мясоедов\n'
    #                              '<b>Контактный телефон:</b> (3822) 60 62 61', parse_mode='HTML')
    #await callback.message.answer('<b>ШКОЛА КЛАССИЧЕСКОГО ВОКАЛА НАРОДНОЙ АРТИСТКИ РОССИИ Л.Ф. ТРАВКИНОЙ</b>\n'
    #                              'В школе ведется индивидуальная работа со студентами по развитию вокальных данных, подбираются программы с учетом индивидуальных особенностей. Многие из вокалистов блистают на сцене в разных городах России.\n'
    #                              '<b>Руководитель:</b> Людмила Федоровна Травкина\n'
    #                              '<b>Контактный телефон:</b> (3822) 60 62 61', parse_mode='HTML')
    #await callback.message.answer('<b>СТУДИЯ ЭСТРАДНОГО ВОКАЛА «ОТРАЖЕНИЕ»</b>\n'
    #                              'Здесь ты сможешь петь и ярко выступать на конкурсах и фестивалях самого разного уровня.\n'
    #                              '<b>Руководитель:</b> Татьяна Николаевна Виноградова\n'
    #                              '<b>Контактный телефон:</b> (3822) 60 62 61', parse_mode='HTML')
   # await callback.message.answer('<b>TАНЦЕВАЛЬНАЯ СБОРНАЯ ТПУ</b>\n'
   #                               'Вместо слов можно танцевать! Студенты сборной участвуют в самых ярких мероприятиях ТПУ, выступают на городских площадках, принимают участие в конкурсах и различных проектах\n'
   #                               '<b>Руководитель:</b> Екатерина Сулема\n'
    #                              '<b>Контактный телефон:</b> +7 903 954 73 96', parse_mode='HTML')
    #await callback.message.answer('<b>СТУДЕНЧЕСКОЕ ТВОРЧЕСКОЕ ОБЪЕДИНЕНИЕ ТПУ</b>\n'
    #                              'Здесь самые креативные, яркие, талантливые студенты ТПУ (и ты можешь быть в их числе) делают творческие мероприятия, развивают и создают новые творческие коллективы на базе МКЦ и на базе общежитий ТПУ.\n'
    #                              '<b>Руководитель:</b> Наталья Климова\n'
    #                              '<b>Контактный телефон:</b> +7 962 792 75 10', parse_mode='HTML')
    #await callback.message.answer('<b>СТУДОТРЯДЫ ТПУ</b>\n'
    #                              'Движение студенческих отрядов ТПУ — это реальная сила! Строители, энергетики, проводники, вожатые, работники сервиса и сельского хозяйства. Только в этом году ребята трудятся в Крыму и Иркутской области, на всероссийских студенческих стройках в Северске и Озерске, на международной студенческой стройке в Кемерове и даже за рубежом! В студотрядах ТПУ ты точно найдешь себе занятие по душе, заработаешь, а также обеспечишь интересную жизнь, ведь мероприятия у ребят идут круглый год.\n'
    #                              '<b>Адрес:</b> пр. Кирова, 2, вход с торца\n'
    #                              '<b>Группа «ВКонтакте»:</b> vk.com/vshsotpu', parse_mode='HTML')
    #await callback.message.answer('<b>МЕДИАЦЕНТР ТПУ</b>\n'
    #                              'Студенческое объединение, которое работает на бренд ТПУ, создает лучший вузовский ТикТок страны (@tpu.house — более 12,5 тыс. подписчиков и более 1,8 млн просмотров), проекты на YouTube и ведет Инстаграм @media.tpu.\n'
    #                              'Ты можешь стать частью этой креативной команды и вместе с единомышленниками реализовывать свои крутые проекты!\n'
     #                             '<b>Сайт:</b> https://vk.com/media_tpu\n'
     #                             '<b>Адрес:</b> ул. Усова, 13б, вход с торца', parse_mode='HTML',reply_markup=nazad)
@dp.callback_query_handler(text='sport')
async def sport_call(callback:types.CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer('<b>С первых дней учебы ты познакомишься со спортивными корпусами ТПУ (ул. Карпова, 4, ул. А. Иванова, 4)</b>\n\n'
                                  'Современные игровые залы, в которых проходят академические занятия, тренировки сборных команд и спортивные соревнования. Кстати, сборная команда ТПУ по баскетболу – участник и призер соревнований АСБ России, с сборная по спортивной аэробике – призеры Чемпионата России.\n'
                                  'Тренажерный зал, залы кардионагрузки, бокса, гиревого спорта, аэробики, тяжелой атлетики, единоборств, настольного тенниса.\n\n'
                                  'Всего в ТПУ культивируется 21 вид спорта.\n'
                                  'В течение года тебя ждут более 150 спортивных мероприятий и проектов различного уровня.\n\n'
                                  '<b>СПОРТИВНЫЙ КЛУБ «ПОЛИТЕХНИК»</b>\n'
                                  '<b>Председатель:</b> Наталья Николаевна Ткаченко\n'
                                  '<b>Адрес</b> ул. Карпова, 4\n\n'
                                  
                                  '<b>СТУДЕНЧЕСКИЙ СПОРТИВНЫЙ КЛУБ «СИБИРСКИЕ ЛЬВЫ»</b>\n'
                                  'Информация о мероприятиях клуба в группе «ВКонтакте»: vk.com/sib_lions\n\n'

                                  '<b>СПОРТИВНО-ТЕХНИЧЕСКИЙ КЛУБ «АФАЛИНА»</b>\n'
                                  'Обучение дайвингу и погружения.\n'
                                  '<b>Председатель:</b> Денис Евгеньевич Николаев.\n'
                                  '<b>Адрес</b> ул. Савиных, 5\n'
                                  '<b>Группа «ВКонтакте»:</b> vk.com/afalinatomsk\n\n'
                                  
                                  '<b>СПОРТИВНО-ТУРИСТИЧЕСКИЙ КЛУБ «АМАЗОНКИ»</b>\n'
                                  'Все виды туризма (авто, лыжный, водный, пеший, горный, спелеология и альпинизм), походы по родному краю, спортивные походы и путешествия.\n'
                                  '<b>Председатель:</b> Любовь Викторовна Кучумова\n'
                                  '<b>Адрес</b> ул. Карпова, 4, ауд. 130\n'
                                  '<b>Группа «ВКонтакте»:</b> vk.com/amazonki_tpu\n\n'
                                  ''
                                  '<b>СПОРТИВНЫЙ КОМПЛЕКС «ПОЛИТЕХНИК»</b>\n'
                                  'Твой стадион расположен в районе Южной площади по ул. 19 Гвардейской дивизии, 13. Здесь же находится лыжная база «Политехник». На стадионе есть футбольное поле, лыжероллерная трасса, беговая дорожка, городошная площадка. Летом действует прокат велосипедов, зимой устраивается освещенная лыжная трасса.\n'
                                  'В кампусе ТПУ находятся три игровые площадки: для мини-футбола, баскетбола, волейбола.\n\n'
                                  ''
                                  '<b>ФИЗКУЛЬТУРНО-СПОРТИВНЫЙ КОМПЛЕКС С ПЛАВАТЕЛЬНЫМ БАССЕЙНОМ «ПОЛИТЕХНИК»</b>\n'
                                  'Это классный 25-метровый бассейн на шесть дорожек. В комплексе также есть тренажерный зал (оборудованный силовыми и кардиотренажерами); зал для занятий лечебной физкультурой, аэробикой (фитбол, степ, танцевальная, силовая), йогой; массажный кабинет; инфракрасная сауна; солярий.\n'
                                  '<b>Группа «ВКонтакте»:</b> vk.com/sportpolitech\n\n',parse_mode='HTML',reply_markup=nazad)

def register_handlers_student(dp: Dispatcher):
    dp.register_message_handler(command_start,commands=['start','help'])

