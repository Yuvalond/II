import vk_api
from Parsing_raspisania import *
from Parsing_weather import *
from Parsing_teacher import *
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api import VkUpload
from PIL import Image
#api-key = vk1.a.t9U8dwwX7L2XFyqrz6Iwq8bRIW8BQsOodLpd5DGVqDmrEpLylPEGfdFp8VGdjYjw_XdSkjTo1QdIg3fG6kMTaWo7aQMjXN9WOCoEitzvlm_pL2pJ4fji81xUvg6Q_dsIO8CObCySsBmUKoOF9_h9u_ULUFQHdYEbboV1dyL9TwVzy296wNfUEmRd3VcNej5CyC41Hye6HFQ1TNFk1eMe2Q
import xml.etree.ElementTree as ET

#ОБРАЩЕНИЕ К LONGPOLL
vk_session = vk_api.VkApi(token='vk1.a.t9U8dwwX7L2XFyqrz6Iwq8bRIW8BQsOodLpd5DGVqDmrEpLylPEGfdFp8VGdjYjw_XdSkjTo1QdIg3fG6kMTaWo7aQMjXN9WOCoEitzvlm_pL2pJ4fji81xUvg6Q_dsIO8CObCySsBmUKoOF9_h9u_ULUFQHdYEbboV1dyL9TwVzy296wNfUEmRd3VcNej5CyC41Hye6HFQ1TNFk1eMe2Q')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def instruction_bot(event):
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Погода', color =VkKeyboardColor.PRIMARY)
    keyboard.add_button('Бот', color =VkKeyboardColor.PRIMARY)
    vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Привет, ' +
                            vk.users.get(user_id=event.user_id)[0]['first_name'] + 
                            "! Это инструкция к боту , для того что бы выполнить команду , нажми на кнопку(если таковая имеется), либо введи\nКоманды:\n\n"+
                            "1) «Погода» - показывает погоду в Москве\n"+
                            "2) «Номер группы» - сохранение группы, сохраняет номер твоей группы для дальнейшего использования\n"+
                            "3) «Бот» - показывает расписание для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "4) «Бот + номер группы» - показывает расписание для заданной группе \n"
                            "5) «Бот + день недели» - показывает расписание на день недели (четную и нечетную) для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "6) «Бот + день недели + группа» - показывает расписани на день недели(четную и нечетную) для заданной группы\n"
                            "7) «Найти + Фамилия преподавателя» - показывает расписание заданного преподавателя \n",
                    keyboard=keyboard.get_keyboard()
                )
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_user and not event.from_me:
            pattern_group = r'[а-яА-Я]{4}-\d{2}-\d{2}$' 
            pattern_bot_group = r'^бот\s+[а-яА-Я]{4}-\d{2}-\d{2}$' 
            pattern_find = r"^найти [А-Яа-я]{3,12}$"
            if event.text.lower() == 'погода':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                pogoda_bot(event)
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= "Команды:\n\n"+
                            "1) «Погода» - показывает погоду в Москве\n"+
                            "2) «Номер группы» - сохранение группы, сохраняет номер твоей группы для дальнейшего использования\n"+
                            "3) «Бот» - показывает расписание для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "4) «Бот + номер группы» - показывает расписание для заданной группе \n"
                            "5) «Бот + день недели» - показывает расписание на день недели (четную и нечетную) для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "6) «Бот + день недели + группа» - показывает расписани на день недели(четную и нечетную) для заданной группы\n"
                            "7) «Найти + Фамилия преподавателя» - показывает расписание заданного преподавателя \n",
                    keyboard=keyboard.get_keyboard())

            # *COMPLETE
            elif event.text.lower() == 'бот':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                bot_bot(event)
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= "Команды:\n\n"+
                            "1) «Погода» - показывает погоду в Москве\n"+
                            "2) «Номер группы» - сохранение группы, сохраняет номер твоей группы для дальнейшего использования\n"+
                            "3) «Бот» - показывает расписание для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "4) «Бот + номер группы» - показывает расписание для заданной группе \n"
                            "5) «Бот + день недели» - показывает расписание на день недели (четную и нечетную) для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "6) «Бот + день недели + группа» - показывает расписани на день недели(четную и нечетную) для заданной группы\n"
                            "7) «Найти + Фамилия преподавателя» - показывает расписание заданного преподавателя \n",
                    keyboard=keyboard.get_keyboard())


            # *COMPLETE 
            elif re.search(pattern_bot_group, event.text.lower()):
                print('New from {}, text = {}'.format(event.user_id, event.text))
                group = event.text.lower().split("бот ")[1]
                bot_group_bot(event,group.upper())
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= "Команды:\n\n"+
                            "1) «Погода» - показывает погоду в Москве\n"+
                            "2) «Номер группы» - сохранение группы, сохраняет номер твоей группы для дальнейшего использования\n"+
                            "3) «Бот» - показывает расписание для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "4) «Бот + номер группы» - показывает расписание для заданной группе \n"
                            "5) «Бот + день недели» - показывает расписание на день недели (четную и нечетную) для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "6) «Бот + день недели + группа» - показывает расписани на день недели(четную и нечетную) для заданной группы\n"
                            "7) «Найти + Фамилия преподавателя» - показывает расписание заданного преподавателя \n",
                    keyboard=keyboard.get_keyboard())
            # *COMPLETE
            elif event.text.lower().startswith('бот') and len(event.text.lower().split()) == 3:
                day, group = event.text.lower().split()[1:]
                if day in ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота'] and re.match(r'\w{4}-\d{2}-\d{2}', group):
                    print('New from {}, text = {}'.format(event.user_id, event.text))
                    bot_day_of_the_week_group_bot(event,day,group.upper(),keyboard)

            # *COMPLETE
            elif 'бот' in event.text.lower().split():
                day = [word for word in event.text.lower().split() if word in ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']]
                if day:    
                    print('New from {}, text = {}'.format(event.user_id, event.text))
                    bot_day_of_the_week_bot(event,day[0],keyboard)

            # *COMPLETE
            elif re.search(pattern_group, event.text.lower()):
                print('New from {}, text = {}'.format(event.user_id, event.text))
                group = event.text.upper()
                group_number_bot(event,group)
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= "Команды:\n\n"+
                            "1) «Погода» - показывает погоду в Москве\n"+
                            "2) «Номер группы» - сохранение группы, сохраняет номер твоей группы для дальнейшего использования\n"+
                            "3) «Бот» - показывает расписание для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "4) «Бот + номер группы» - показывает расписание для заданной группе \n"
                            "5) «Бот + день недели» - показывает расписание на день недели (четную и нечетную) для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "6) «Бот + день недели + группа» - показывает расписани на день недели(четную и нечетную) для заданной группы\n"
                            "7) «Найти + Фамилия преподавателя» - показывает расписание заданного преподавателя \n",
                    keyboard=keyboard.get_keyboard())
            #+
            elif re.match(pattern_find, event.text.lower()):
                print('New from {}, text = {}'.format(event.user_id, event.text))
                if event.text.lower().startswith("найти "):
                    surname = event.text.lower()[len("найти "):].strip().capitalize()
                print (surname)
                find_teacher_bot(event,surname,keyboard)
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= "Команды:\n\n"+
                            "1) «Погода» - показывает погоду в Москве\n"+
                            "2) «Номер группы» - сохранение группы, сохраняет номер твоей группы для дальнейшего использования\n"+
                            "3) «Бот» - показывает расписание для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "4) «Бот + номер группы» - показывает расписание для заданной группе \n"
                            "5) «Бот + день недели» - показывает расписание на день недели (четную и нечетную) для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "6) «Бот + день недели + группа» - показывает расписани на день недели(четную и нечетную) для заданной группы\n"
                            "7) «Найти + Фамилия преподавателя» - показывает расписание заданного преподавателя \n",
                    keyboard=keyboard.get_keyboard())
            #+
            else:
                print('New from {}, text = {}'.format(event.user_id, event.text))
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= "Ошибка , такой команды нет или неверно введена\nКоманды:\n\n"+
                            "1) «Погода» - показывает погоду в Москве\n"+
                            "2) «Номер группы» - сохранение группы, сохраняет номер твоей группы для дальнейшего использования\n"+
                            "3) «Бот» - показывает расписание для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "4) «Бот + номер группы» - показывает расписание для заданной группе \n"
                            "5) «Бот + день недели» - показывает расписание на день недели (четную и нечетную) для сохраненой группы (перед этим потребуется ввести номер свой номер группы , если ты его этого не сохранял)\n"
                            "6) «Бот + день недели + группа» - показывает расписани на день недели(четную и нечетную) для заданной группы\n"
                            "7) «Найти + Фамилия преподавателя» - показывает расписание заданного преподавателя \n",
                    keyboard=keyboard.get_keyboard()
                )

def find_teacher_bot(event,surname,keyboard):
    list_with_teachers = parse_schedule(surname)
    if list_with_teachers == None:
        vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message= "Такого преподавателя нету в файлах",
            keyboard=keyboard.get_keyboard()
            )
        return
    
    if len(list_with_teachers) == 1:
        show_keyboard_for_teacher(list_with_teachers[0], event)
    else:
        choose_teacher(event,list_with_teachers)
    return

def choose_teacher(event,list_with_teachers):
    keyboard = VkKeyboard(one_time=True)
    for teacher in list_with_teachers:
        keyboard.add_button(teacher, color =VkKeyboardColor.PRIMARY)
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message= "Выберите Преподавателя:",
        keyboard=keyboard.get_keyboard()
    )
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_user and not event.from_me:
            if event.text in list_with_teachers:
                show_keyboard_for_teacher(event.text,event)
                return
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= "Выберите Преподавателя:",
                    keyboard=keyboard.get_keyboard()
                )


def show_keyboard_for_teacher(teacher,event):
    global vk
    global longpoll
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('На сегодня', color =VkKeyboardColor.POSITIVE)
    keyboard.add_button('На завтра', color =VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('На эту неделю', color =VkKeyboardColor.PRIMARY)
    keyboard.add_button('На следующую неделю', color =VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color =VkKeyboardColor.NEGATIVE)
    cl_teacher = Teacher(teacher)
    vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= '«Меню Расписание»',
                    keyboard=keyboard.get_keyboard()
                )
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_user and not event.from_me:
            if event.text.lower() == 'на сегодня':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                teacher_schedule_today(event,cl_teacher,keyboard)
            elif event.text.lower() == 'на завтра':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                teacher_schedule_tommorow(event,cl_teacher,keyboard)
            elif event.text.lower() == 'на эту неделю':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                teacher_schedule_this_week(event,cl_teacher,keyboard)
            elif event.text.lower() == 'на следующую неделю':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                teacher_schedule_next_week(event,cl_teacher,keyboard)
            elif event.text.lower() == 'назад':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                return
            else:
                print('New from {}, text = {}'.format(event.user_id, event.text))
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= '«Неверная команда»',
                    keyboard=keyboard.get_keyboard()
                )
    
def teacher_schedule_today(event,cl_teacher,keyboard):
    today = datetime.date.today()
    cl_teacher.date = today.strftime("%d.%m.%Y")
    string = cl_teacher.found_teacher()
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )
    return

def teacher_schedule_tommorow(event,cl_teacher,keyboard):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    cl_teacher.date = tomorrow.strftime("%d.%m.%Y")
    string = cl_teacher.found_teacher()
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )
    return

def teacher_schedule_this_week(event,cl_teacher,keyboard):
    today = datetime.date.today()
    day_of_week = today.weekday()
    start_date = today - datetime.timedelta(days=day_of_week)
    week_dates = [start_date + datetime.timedelta(days=i) for i in range(6)]
    string = ''
    for date in week_dates:
        cl_teacher.date = date.strftime("%d.%m.%Y")
        string += f'{cl_teacher.found_teacher()}\n'
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )
    return
    
def teacher_schedule_next_week(event,cl_teacher,keyboard):
    today = datetime.date.today()
    day_of_week = today.weekday()
    start_date = today - datetime.timedelta(days=day_of_week)
    next_week_start_date = start_date + datetime.timedelta(days=7)
    next_week_dates = [next_week_start_date + datetime.timedelta(days=i) for i in range(6)]
    string = ''
    for date in next_week_dates:
        cl_teacher.date = date.strftime("%d.%m.%Y")
        string += f'{cl_teacher.found_teacher()}\n'
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )
    return

def pogoda_bot(event):
    global vk
    global longpoll
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Сейчас', color =VkKeyboardColor.PRIMARY)
    keyboard.add_button('Сегодня', color =VkKeyboardColor.POSITIVE)
    keyboard.add_button('Завтра', color =VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('На 5 дней', color =VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color =VkKeyboardColor.NEGATIVE)
    vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= '«Меню Погода»',
                    keyboard=keyboard.get_keyboard()
                )
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_user and not event.from_me:
            if event.text.lower() == 'сейчас':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                get_weather_now(event,keyboard)
                pass
            elif event.text.lower() == 'сегодня':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                get_weather_segodnya(event,keyboard)

            elif event.text.lower() == 'завтра':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                get_weather_zavtra(event,keyboard)

            elif event.text.lower() == 'на 5 дней':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                get_weather_five_days(event,keyboard)

            elif event.text.lower() == 'назад':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                return
            
            else:
                print('New from {}, text = {}'.format(event.user_id, event.text))
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= '«Неизвестная команда»',
                    keyboard=keyboard.get_keyboard()
                )


def get_weather_now(event,keyboard):
    weather_string, path_icons = get_weather()
    icons = mergepng(path_icons)
    photo_id = upload_on_server_vk(icons)
    vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message= f'Погода в Москве\n',
            attachment= photo_id
            )
    vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message= f'\n{weather_string}',
            keyboard=keyboard.get_keyboard()
            )

def get_weather_segodnya(event,keyboard):
    weather_string, path_icons = get_weather_today()
    icons = mergepng(path_icons)
    photo_id = upload_on_server_vk(icons)
    vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message= f'Погода в Москве\n',
            attachment= photo_id
            )
    vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message= f'\n{weather_string}',
            keyboard=keyboard.get_keyboard()
            )
    
def get_weather_zavtra(event,keyboard):
    weather_string, path_icons = get_weather_tommorow()
    icons = mergepng(path_icons)
    photo_id = upload_on_server_vk(icons)
    vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message= f'Погода в Москве\n',
            attachment= photo_id
            )
    vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message= f'\n{weather_string}',
            keyboard=keyboard.get_keyboard()
            )

def get_weather_five_days(event,keyboard):
    weather_string, path_icons = get_weather_five_day()
    icons = mergepng(path_icons)
    photo_id = upload_on_server_vk(icons)
    start_date = datetime.date.today().strftime('%d.%m')
    end_date = (datetime.date.today() + timedelta(days=5)).strftime('%d.%m')

    weather = f"Погода в Москве с {start_date} по {end_date}"
    vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message= weather,
            attachment= photo_id
            )
    vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message= f'\n{weather_string}',
            keyboard=keyboard.get_keyboard()
            )

def upload_on_server_vk(path):
    upload = VkUpload(vk_session)
    photo = upload.photo_messages(path)
    photo_id = f'photo{photo[0]["owner_id"]}_{photo[0]["id"]}'
    return photo_id

def mergepng(image_paths):
    # Создание пустого холста для объединения картинок
    canvas_width = 0
    canvas_height = 0
    images = []
    for path in image_paths:
        image = Image.open(path)
        images.append(image)
        canvas_width += image.width  # изменение ширины холста
        canvas_height = max(canvas_height, image.height)

    canvas = Image.new('RGBA', (canvas_width, canvas_height), (0, 0, 0, 0))

    # Объединение картинок на холсте
    x_offset = 0  # новый счетчик
    y_offset = 0
    for image in images:
        canvas.paste(image, (x_offset, y_offset))
        x_offset += image.width  # увеличение счетчика по горизонтали
        if x_offset >= canvas_width:  # перенос на новую строку
            x_offset = 0
            y_offset += image.height

    path_png = "II\Oznokom praktika\BlockF\many_png_in_one\manypngs.png"
    # Сохранение объединенной картинки
    canvas.save(path_png)
    return path_png

def bot_bot(event):
    if student_in_json("II\Oznokom praktika\BlockF\SerealizeData\data.json",event.user_id):
        print(f"Пользователь {event.user_id} найден в json")
        show_keyboard_for_the_schedule(event)
        return 
    else:
        save = save_group(event)
        if save == 0:
            return
        show_keyboard_for_the_schedule(event)
        return 



def student_in_json(file_path, user_id):
    # Проверка наличия файла
    try:
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                if not data:
                    return False
                # Проверка наличия id_user в данных JSON
                elif "id_user" in data and data["id_user"] == user_id:
                    return True
                else:
                    return False
            except json.JSONDecodeError:
                print("ERR: Ошибка декодирования JSON. Файл содержит некорректные данные.")
                return False
                # Выполнение функции или кода для некорректного JSON
    except FileNotFoundError:
        print("ERR: Файл не найден или там еще никто не записан.")
        return False

def data_for_parsing_schedule(event):
    if student_in_json("II\Oznokom praktika\BlockF\SerealizeData\data.json",event.user_id):
        with open('II\Oznokom praktika\BlockF\SerealizeData\data.json') as file:
            data = json.loads(file.read())
        if isinstance(data, dict):
            data = [data]
        for i in data:
            if i['id_user'] == event.user_id:
                group = i['group']

        data = Raspisanie(group, event.user_id)
        return data

def show_keyboard_for_the_schedule(event, group = None):
    #получили класс расписание Для дальнейшей работы
    if group != None:
        cl_raspisanie = Raspisanie(group, event.user_id)
    else:
        cl_raspisanie = data_for_parsing_schedule(event)

    global vk
    global longpoll
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('На сегодня', color =VkKeyboardColor.POSITIVE)
    keyboard.add_button('На завтра', color =VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('На эту неделю', color =VkKeyboardColor.PRIMARY)
    keyboard.add_button('На следующую неделю', color =VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Какая неделя?', color =VkKeyboardColor.SECONDARY)
    keyboard.add_button('Какая группа?', color =VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color =VkKeyboardColor.NEGATIVE)
    vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= '«Меню Расписание»',
                    keyboard=keyboard.get_keyboard()
                )
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_user and not event.from_me:
            if event.text.lower() == 'на сегодня':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                schedule_today(event,cl_raspisanie, keyboard)

            elif event.text.lower() == 'на завтра':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                schedule_tommorow(event,cl_raspisanie, keyboard)

            elif event.text.lower() == 'на эту неделю':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                schedule_on_this_week(event,cl_raspisanie,keyboard)
            elif event.text.lower() == 'на следующую неделю':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                schedule_on_next_week(event,cl_raspisanie,keyboard)
            elif event.text.lower() == 'какая неделя?':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                what_a_week(event,cl_raspisanie,keyboard)
            elif event.text.lower() == 'какая группа?':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                what_a_group(event,cl_raspisanie,keyboard)
            elif event.text.lower() == 'назад':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                return 0
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message= 'Неверная команда',
                    keyboard=keyboard.get_keyboard()
                )

def schedule_today(event,cl_schedule,keyboard):
    today = datetime.date.today()
    cl_schedule.date = today.strftime("%d.%m.%Y") 
    string = cl_schedule.get_raspisanie_moment()
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )

def schedule_tommorow(event,cl_schedule, keyboard):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    cl_schedule.date = tomorrow.strftime("%d.%m.%Y") 
    string = cl_schedule.get_raspisanie_moment()
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )

def schedule_on_this_week(event,cl_schedule,keyboard):
    #получение дней недель для парсинга
    today = datetime.date.today()
    cl_schedule.date = today
    string = cl_schedule.get_raspisanie_moment_for_week()
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )

def schedule_on_next_week(event,cl_schedule,keyboard):
    #получение дней недель для парсинга
    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=7)
    cl_schedule.date = next_week
    string = cl_schedule.get_raspisanie_moment_for_week()
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )

def what_a_week(event,cl_schedule,keyboard):
    string = cl_schedule.get_number_of_week()
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )

def what_a_group(event,cl_schedule,keyboard):
    group = cl_schedule.group
    string = f'Показываю расписание группы {group}.'
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )

def save_group(event):
    print('New from {}, text = {}'.format(event.user_id, event.text))
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Назад', color =VkKeyboardColor.NEGATIVE)
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message='Пожалуйста, введите группу в формате "АААА-00-00"\nили для отмены нажмите кнопку назад":',
        keyboard= keyboard.get_keyboard()
    )
    valid = valid_group(event)
    if valid == 0:
        return 0
    else:
        group = Raspisanie(valid, event.user_id)
        with open("II\Oznokom praktika\BlockF\SerealizeData\data.json","w") as f:
            json.dump(group.to_json(), f)
        return

def valid_group(event):
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Назад', color =VkKeyboardColor.NEGATIVE)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_user and not event.from_me:
            print('New from {}, text = {}'.format(event.user_id, event.text))
            if re.match(r'^[А-Я]{4}-\d{2}-\d{2}$', event.text.upper()):
                keyboard = VkKeyboard(one_time=True)
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message=f'Я запомнил, что ты из группы {event.text.upper()}',
                )
                return event.text.upper()

            if event.text.lower() == "назад":
                return 0
            
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Пожалуйста, введите группу в формате "АААА-00-00"\nили для отмены нажмите кнопку назад'
                )

def bot_group_bot(event,group):
    show_keyboard_for_the_schedule(event,group)


def bot_day_of_the_week_bot(event,day,keyboard):
    if student_in_json("II\Oznokom praktika\BlockF\SerealizeData\data.json",event.user_id):
        print(f"Пользователь {event.user_id} найден в json")
        show_day_of_week_schedule(event,day,keyboard)
        return 
    else:
        save = save_group(event)
        if save == 0:
            vk.messages.send(
                        user_id=event.user_id,
                        random_id=get_random_id(),
                        message= "«Меню выбора»",
                        keyboard=keyboard.get_keyboard()
                    )
            return
        show_day_of_week_schedule(event,day,keyboard)
        return 

def show_day_of_week_schedule(event,day,keyboard):
    cl_raspisanie = data_for_parsing_schedule(event)
    string = cl_raspisanie.get_raspisanie_moment_for_day_of_week(day)
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )



def bot_day_of_the_week_group_bot(event,day,group,keyboard):
    cl_raspisanie = Raspisanie(group, event.user_id)
    string = cl_raspisanie.get_raspisanie_moment_for_day_of_week(day)
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        message=string,
        keyboard=keyboard.get_keyboard()
    )



def group_number_bot(event,group):
    save = save_group_2(event,group)
    if save == 0:
        return

def save_group_2(event,group):
    valid = valid_group_2(event,group)
    if valid == 0:
        return 0
    else:
        group = Raspisanie(valid, event.user_id)
        delete_from_json_user_id(event)
        with open("II\Oznokom praktika\BlockF\SerealizeData\data.json","w") as f:
            json.dump(group.to_json(), f)
        return
    
def delete_from_json_user_id(event):
    with open("II\Oznokom praktika\BlockF\SerealizeData\data.json","r") as f:
        data = json.load(f)
    for obj in list(data):
        if 'user_id' in obj and obj['user_id'] == event.user_id:
            data.remove(obj)
    with open("II\Oznokom praktika\BlockF\SerealizeData\data.json","w") as f:
        json.dump(data,f)

def valid_group_2(event,group):
    if re.match(r'^[А-Я]{4}-\d{2}-\d{2}$', group):
        vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message=f'Я запомнил, что ты из группы {group}',
        )
        return event.text.upper() 
    else:
        vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message='Группа введена неверно, введите группу в формате "АААА-00-00"\n'
        )
        return 0


 
def main():
    global vk
    global longpoll
    
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_user and not event.from_me:
            if event.text.lower() == 'начать':
                print('New from {}, text = {}'.format(event.user_id, event.text))
                instruction_bot(event) #Инструкция и дальше по дереву

if __name__ ==  '__main__':
    main()

