main = '''
<b>Магазин кастомной одежды Spat</b>

<b>У нас в наличии есть</b>:
1. Новинки
2. Футболки
3. Худи
4. Джерси
5. Велюр
6. Штаны
7. Кепки
8. Шарфы
'''

first_join = '''
<b>Новый пользователь:</b>
id: {}
t.me/{}
'''


def order(page: str, page_max: int, list_catalog: list):
    result = ['id  |     Название товара      | Цена']
    for a, b, c in list_catalog:
        a = str(a)
        if len(a) < 2:
            a += '  '
        result.append(f'\n--------------------------------------------------------\n{a} | {b} | {c} р.')
    return f'<b>Каталог | Страница {page} из {page_max}</b>\n{" ".join([i for i in result])}\n' \
           f'--------------------------------------------------------\n<b>Оформить заказ</b>           👇👇👇'


lk = '''
Клиент <b>{} {}</b>
--- Ваш последний заказ ---:
ID заказа:       <b>{}</b>
Дата заказа:  <b>{}</b>
Стоимость:   <b>{} р.</b>
Менеджер:       <b>{}</b>
Детали заказа:
<b>{}</b>
'''

user_data = '''
Ваши данные:
ID: {}
Имя: {}
Фамилия: {}
Телефон: {}
E-mail: {}
Количество заказов: {}
'''

setting_ch = '''
Заявка на смену личных данных
id: {}
Дата: {}
url: t.me/{}
'''

setting = '''
<b>Ваша заявка принята</b>
С вами свяжутся для смены данных

Можете написать нам:
{}
'''


def user_history(page: str, page_max: str, list_history: list):
    result = [' id |  Менеджер  | Цена']
    for a, b, c in list_history:
        a = str(a)
        if len(a) < 2:
            a += '  '
        result.append(f'\n--------------------------------------------------------\n{a} | {b} | {c}')
    return f'История заказов | Страница {page} из {page_max}\n{" ".join([i for i in result])}\n'


a_main = '''
<b>Меню админа</b>
Ваш id: {}
Проверка: /sql | /pay
'''

a_updatecatalog_1 = '''
Загрузите <b>{}</b> в папку с ботом.
Формат, в котором там должны храниться данные:
id | название товара | цена
1  |    Футболка     | 1000
2  |     Худи        | 1500

Если всё верно, можете обновить каталог
'''

a_updatecatalog_2 = '''
<b>Обновление каталога...</b>

{}
Товаров в каталоге: {}
'''


def a_userlist(page: str, page_max: str, list_user: list):
    result = ['          id          |  Фамилия  |  Имя  | Заказы']
    for one_user in list_user:
        result.append(f'\n---------------------------------------------------------------------\n{one_user[0]} |'
                      f' {one_user[3]} | {one_user[2]} | {one_user[9]}')
    return f'<b>Пользователи | Страница {page} из {page_max}</b>\n{" ".join([i for i in result])}\n'


a_updateuser = '''
<b>Смена данных пользователя</b>
Отправьте данные в формате:
updateuser; user_id; username; first_name; last_name; phone; email

Не забывайте, данные делятся знаком "<b>;</b>",
если менять не надо, то "-"

Пример: <i>updateuser; 123456; ivanov; -; Иванов; +791234567890; -</i>
'''

a_neworder = '''
<b>Оформление нового заказа</b>
Отправьте данные в формате:
neworder; id-клиента; Цену; %-скидки; Менеджер;
Список услуг в заказе (1, 5, 12, 12, 20)

Не забывайте, данные делятся знаком "<b>;</b>"

Пример: <i>neworder; 123456; 2500; 10; Иванов Иван; 1, 2, 5</i>
'''

a_userhistory = '''
<b> Список заказов пользователя </b>
Отправьте данные в формате:
<i>listorder; id-клиента; №-страницы</i>

Пример: <i>listorder; 123456; 1</i>
'''


def db_w_update_user_t(data):
    return f'''<b>Данные пользователя обновлены:</b>
    id       | {data[0]}
    Ник      | {data[1]}
    Фамилия  | {data[2]}
    Имя      | {data[3]}
    Тел      | {data[4]}
    Mail     | {data[5]}
    Дата рег | {data[6]}
    Реф. код | {data[7]}
    Подписка | {data[8]}
    Заказов  | {data[9]}'''


db_w_update_user_f = '''
<b>Ошибка.</b> Проверьте правильность введённых данных

Отправьте данные в формате:
updateuser; user_id; username; first_name; last_name; phone; email

Не забывайте, данные разделяются знаком "<b>;</b>", если меня не надо, "-"
Пример:
<i>updateuser; 123456; ivanov; -; Иванов; +791234567890; -</i>
'''


def check_database(data):
    result = ['<b>Проверка базы данных...</b>\n']
    for i in data:
        result.append(f'\n{i}')
    return f'{" ".join([i for i in result])}'
