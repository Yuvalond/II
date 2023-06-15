import requests
import os
from datetime import datetime, timedelta

api_key = '3c0d9f3715a8bf127d531ae50e173816'
def get_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Moscow&units=metric&lang=ru&appid={api_key}'
    
    # получаем данные о погоде
    response = requests.get(url)
    data = response.json()
    
    # получаем нужные данные из ответа
    weather = data['weather'][0]['description']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    wind_dir = data['wind']['deg']
    
    # получаем и сохраняем иконку
    icon_url = f"http://openweathermap.org/img/w/{data['weather'][0]['icon']}.png"
    icon_path = os.path.join('II', 'Oznokom praktika', 'BlockF', 'photo_for_weather', f"{data['weather'][0]['icon']}.png")
    icon_response = requests.get(icon_url)
    with open(icon_path, 'wb') as f:
        f.write(icon_response.content)
    
    # определяем направление ветра и его скорость
    wind_speed_text, wind_dir_text = get_wind_info(wind_speed, wind_dir)
    
    # создаем строку с данными о погоде
    weather_str = f"{weather.capitalize()}, Температура {int(temp_min)}-{int(temp_max)} C\nДавление {pressure} мм. рт. ст., влажность: {humidity}%\nВетер: {wind_speed_text}, {wind_dir_text}"
    
    # возвращаем строку и список путей к иконкам
    icon_paths = [icon_path]
    return weather_str, icon_paths



def get_wind_info(wind_speed, wind_dir):
    # определяем направление ветра
    if wind_dir >= 337.5 or wind_dir < 22.5:
        wind_dir = 'северный'
    elif wind_dir >= 22.5 and wind_dir < 67.5:
        wind_dir = 'северо-восточный'
    elif wind_dir >= 67.5 and wind_dir < 112.5:
        wind_dir = 'восточный'
    elif wind_dir >= 112.5 and wind_dir < 157.5:
        wind_dir = 'юго-восточный'
    elif wind_dir >= 157.5 and wind_dir < 202.5:
        wind_dir = 'южный'
    elif wind_dir >= 202.5 and wind_dir < 247.5:
        wind_dir = 'юго-западный'
    elif wind_dir >= 247.5 and wind_dir < 292.5:
        wind_dir = 'западный'
    elif wind_dir >= 292.5 and wind_dir < 337.5:
        wind_dir = 'северо-западный'
    
    # определяем скорость ветра
    if wind_speed < 1:
        wind_speed_text = 'штиль'
    elif wind_speed < 6:
        wind_speed_text = f'легкий, {wind_speed} м/с'
    elif wind_speed < 12:
        wind_speed_text = f'умеренный, {wind_speed} м/с'
    else:
        wind_speed_text = f'сильный, {wind_speed} м/с'
    
    return wind_speed_text, wind_dir



def get_weather_today():
    # Функция для получения прогноза погоды

    url = f"http://api.openweathermap.org/data/2.5/forecast?q=Moscow,ru&appid=3c0d9f3715a8bf127d531ae50e173816&units=metric&lang=ru&start=0&cnt=8"

    response = requests.get(url)
    data = response.json()

    weather_data = data['list']
    weather_icons = []
    weather_forecast = ""

    today = datetime.now().date()

    morning_temp = None
    day_temp = None
    evening_temp = None
    night_temp = None

    for weather in weather_data:
        # Получаем данные о погоде для каждого времени дня

        timestamp = weather['dt']
        date_time = datetime.fromtimestamp(timestamp)
        forecast_date = date_time.date()

        if forecast_date != today:
            continue

        time = date_time.strftime("%H:%M")

        if time == "06:00":
            morning_temp = round(weather['main']['temp'])
        elif time == "12:00":
            day_temp = round(weather['main']['temp'])
        elif time == "18:00":
            evening_temp = round(weather['main']['temp'])
        elif time == "21:00":
            night_temp = round(weather['main']['temp'])

        if morning_temp is not None and day_temp is not None and evening_temp is not None and night_temp is not None:
            break

    weather_forecast += f"\n/{morning_temp} C"
    weather_forecast += f"//{day_temp} C"
    weather_forecast += f"//{evening_temp} C"
    weather_forecast += f"//{night_temp} C/\n"

    for weather in weather_data:
        # Получаем данные о погоде для каждого времени дня

        timestamp = weather['dt']
        date_time = datetime.fromtimestamp(timestamp)
        forecast_date = date_time.date()

        if forecast_date != today:
            continue

        time = date_time.strftime("%H:%M")

        if time == "06:00":
            weather_forecast += "\nУТРО\n"
        elif time == "12:00":
            weather_forecast += "\nДЕНЬ\n"
        elif time == "18:00":
            weather_forecast += "\nВЕЧЕР\n"
        elif time == "21:00":
            weather_forecast += "\nНОЧЬ\n"
        else:
            continue

        weather_conditions = weather['weather'][0]['description']
        temperature_min = round(weather['main']['temp_min'])
        temperature_max = round(weather['main']['temp_max'])
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']
        wind_direction = weather['wind']['deg']

        # Получаем путь к иконке погоды и сохраняем ее

        icon_id = weather['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"
        icon_path = f"II/Oznokom praktika/BlockF/photo_for_weather/{icon_id}.png"

        with open(icon_path, "wb") as icon_file:
            icon_response = requests.get(icon_url)
            icon_file.write(icon_response.content)

        weather_icons.append(icon_path)

        # Формируем строку с данными о погоде

        weather_forecast += f"//{weather_conditions}, температура:{temperature_min}-{temperature_max} С\n"
        weather_forecast += f"//Давление: {pressure} мм рт. ст., влажность: {humidity}%\n"
        weather_forecast += f"//Ветер: легкий, {wind_speed} м/с, {get_wind_direction(wind_direction)}"

    return weather_forecast, weather_icons

def get_wind_direction(deg):
    # Функция для определения направления ветра по градусам

    if deg >= 337.5 or deg < 22.5:
        return "северный"
    elif 22.5 <= deg < 67.5:
        return "северо-восточный"
    elif 67.5 <= deg < 112.5:
        return "восточный"
    elif 112.5 <= deg < 157.5:
        return "юго-восточный"
    elif 157.5 <= deg < 202.5:
        return "южный"
    elif 202.5 <= deg < 247.5:
        return "юго-западный"
    elif 247.5 <= deg < 292.5:
        return "западный"
    elif 292.5 <= deg < 337.5:
        return "северо-западный"

# Использование функции

def get_weather_tommorow():
    # Функция для получения прогноза погоды на следующий день

    url = f"http://api.openweathermap.org/data/2.5/forecast?q=Moscow,ru&appid=3c0d9f3715a8bf127d531ae50e173816&units=metric&lang=ru&"

    response = requests.get(url)
    data = response.json()

    weather_data = data['list']
    weather_icons = []
    weather_forecast = ""

    tomorrow = datetime.now().date() + timedelta(days=1)

    morning_temp = None
    day_temp = None
    evening_temp = None
    night_temp = None

    for weather in weather_data:
        # Получаем данные о погоде для каждого времени дня

        timestamp = weather['dt']
        date_time = datetime.fromtimestamp(timestamp)
        forecast_date = date_time.date()

        if forecast_date != tomorrow:
            continue

        time = date_time.strftime("%H:%M")

        if time == "06:00":
            morning_temp = round(weather['main']['temp'])
        elif time == "12:00":
            day_temp = round(weather['main']['temp'])
        elif time == "18:00":
            evening_temp = round(weather['main']['temp'])
        elif time == "21:00":
            night_temp = round(weather['main']['temp'])

        if morning_temp is not None and day_temp is not None and evening_temp is not None and night_temp is not None:
            break

    weather_forecast += f"\n/{morning_temp} C"
    weather_forecast += f"//{day_temp} C"
    weather_forecast += f"//{evening_temp} C"
    weather_forecast += f"//{night_temp} C/\n"

    for weather in weather_data:
        # Получаем данные о погоде для каждого времени дня

        timestamp = weather['dt']
        date_time = datetime.fromtimestamp(timestamp)
        forecast_date = date_time.date()

        if forecast_date != tomorrow:
            continue

        time = date_time.strftime("%H:%M")

        if time == "06:00":
            weather_forecast += "\nУТРО\n"
        elif time == "12:00":
            weather_forecast += "\nДЕНЬ\n"
        elif time == "18:00":
            weather_forecast += "\nВЕЧЕР\n"
        elif time == "21:00":
            weather_forecast += "\nНОЧЬ\n"
        else:
            continue

        weather_conditions = weather['weather'][0]['description']
        temperature_min = round(weather['main']['temp_min'])
        temperature_max = round(weather['main']['temp_max'])
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']
        wind_direction = weather['wind']['deg']

        # Получаем путь к иконке погоды и сохраняем ее

        icon_id = weather['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"
        icon_path = f"II/Oznokom praktika/BlockF/photo_for_weather/{icon_id}.png"

        with open(icon_path, "wb") as icon_file:
            icon_response = requests.get(icon_url)
            icon_file.write(icon_response.content)

        weather_icons.append(icon_path)

        # Формируем строку с данными о погоде

        weather_forecast += f"//{weather_conditions}, температура:{temperature_min}-{temperature_max} С\n"
        weather_forecast += f"//Давление: {pressure} мм рт. ст., влажность: {humidity}%\n"
        weather_forecast += f"//Ветер: легкий, {wind_speed} м/с, {get_wind_direction(wind_direction)}"

    return weather_forecast, weather_icons

def get_weather_five_day():
    url = "http://api.openweathermap.org/data/2.5/forecast?q=Moscow,ru&appid=" + "3c0d9f3715a8bf127d531ae50e173816" + "&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()

    temperatures_day = []
    temperatures_night = []
    icon_paths = []

    previous_date = ""
    for forecast in data["list"]:
        # Получаем дату прогноза
        date = forecast["dt_txt"].split(" ")[0]

        # Пропускаем повторяющиеся даты
        if date == previous_date:
            continue

        previous_date = date

        # Получаем температуру днем и ночью
        temperature_day = None
        temperature_night = None

        # Находим прогнозы на день и ночь для данного дня
        for forecast_hour in data["list"]:
            forecast_date = forecast_hour["dt_txt"].split(" ")[0]
            if forecast_date == date:
                if "09:00:00" <= forecast_hour["dt_txt"].split(" ")[1] <= "15:00:00":
                    temperature_day = forecast_hour["main"]["temp"]
                elif "21:00:00" <= forecast_hour["dt_txt"].split(" ")[1] <= "23:59:59" or "00:00:00" <= forecast_hour["dt_txt"].split(" ")[1] <= "03:00:00":
                    temperature_night = forecast_hour["main"]["temp"]

        # Если есть прогнозы на день и ночь, добавляем их в списки температур и сохраняем иконку
        if temperature_day is not None and temperature_night is not None:
            temperatures_day.append(temperature_day)
            temperatures_night.append(temperature_night)

            # Получаем иконку погоды
            icon_code = forecast["weather"][0]["icon"]
            icon_url = "http://openweathermap.org/img/w/" + icon_code + ".png"
            icon_response = requests.get(icon_url)
            icon_path = f"II\\Oznokom praktika\\BlockF\\photo_for_weather\\icon_{date}.png"
            icon_paths.append(icon_path)

            with open(icon_path, "wb") as f:
                f.write(icon_response.content)

    # Создаем строку прогноза погоды
    weather_forecast = "/".join([f"{temperature} C" for temperature in temperatures_day]) + " ДЕНЬ\n"
    weather_forecast += "/".join([f"{temperature} C" for temperature in temperatures_night]) + " НОЧЬ"

    return weather_forecast, icon_paths