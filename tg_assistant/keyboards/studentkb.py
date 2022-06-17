from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

##################row insert #######################################

kb_korpusa = InlineKeyboardMarkup(row_width=4).row(InlineKeyboardButton(text='Главный корпус',callback_data='korp:gk')).row(InlineKeyboardButton(text='Корпус №1',callback_data='korp:1')).add(InlineKeyboardButton(text='Назад',callback_data='/Назад'))


nazad = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Назад',callback_data='/Назад'))

urlkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Карта',url='https://clck.ru/rPz8V')).add(InlineKeyboardButton(text='Назад',callback_data='/Назад'))

kb_ucheba=InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Личный кабинет💼',callback_data='lk'))\
    .add(InlineKeyboardButton(text='Стипендия💰',callback_data='cash')).add(InlineKeyboardButton(text='Виды учебных занятий📒',callback_data='lessons'))\
    .add(InlineKeyboardButton(text='Рейтинг план(Система оценивания)📈',callback_data='points')).add(InlineKeyboardButton(text='Сессия😱', callback_data='exam'))\
    .add(InlineKeyboardButton(text='Расписание📅',callback_data='rasp')).add(InlineKeyboardButton(text='Назад',callback_data='/Назад'))


kb_tvor4 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Творчество',callback_data='tvor4'))\
    .add(InlineKeyboardButton(text='Спорт',callback_data='sport')).add(InlineKeyboardButton(text='Назад',callback_data='/Назад'))

kb_student= InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Студенческая жизнь в ТПУ',callback_data='culture'))\
                                            .add(InlineKeyboardButton(text='Учебный процесс🎓',callback_data='ucheba'))\
                                            .add(InlineKeyboardButton(text='Навигация в кампусе',callback_data='gps'))\
                                            .add(InlineKeyboardButton(text='Навигация в корпусах',callback_data='nav'))

