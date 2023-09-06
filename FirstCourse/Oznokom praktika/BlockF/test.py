import os
import openpyxl
import re

def select_teacher_from_keyboard(teachers):
    print("Multiple teachers found with the same last name:")
    for i, teacher in enumerate(teachers, start=1):
        print(f"{i}. {teacher}")
    choice = input("Enter the number corresponding to the desired teacher: ")
    return teachers[int(choice) - 1]

def parse_schedule(document_path, surname_prepod):
    workbook = openpyxl.load_workbook(document_path)
    sheet = workbook.active

    teachers = {}

    for row in sheet.iter_rows(values_only=True):
        for cell in row:
            if cell is None:
                continue

            print(f"Processing cell: {cell}")

            if surname_prepod in cell:
                teacher_name = cell.value

                subject = row[cell.column - 1] if cell.column > 1 else ''

                if teacher_name in teachers:
                    continue
                else:
                    teachers[teacher_last_name] = [(teacher_name, subject)]

    return teachers



def display_teacher_schedule(teacher_schedule):
    for teacher, schedule in teacher_schedule.items():
        print(f"\nSchedule for {teacher}:")
        for i, (teacher_name, subject) in enumerate(schedule, start=1):
            print(f"{i}. Subject: {subject}")
            print(f"   Teacher: {teacher_name}")

def main():
    document_path = r'II\Oznokom praktika\BlockF\XLSX_files\IIT_1-kurs_22_23_vesna_27.04.2023.xlsx'
    surname_prepod = input("Enter the name of the teacher you want to find: ")

    # Extract the surname from the teacher's name

    # ...
    teacher_schedule = parse_schedule(document_path, surname_prepod)

    matching_teachers = [
        teacher for teacher in teacher_schedule if any(
            re.match(fr".*\b{re.escape(surname_prepod)}\b", name) for name, _ in teacher_schedule[teacher]
        )
    ]

    if len(matching_teachers) == 1:
        selected_teacher = matching_teachers[0]
    elif len(matching_teachers) > 1:
        selected_teacher = select_teacher_from_keyboard(matching_teachers)
    else:
        print("No matching teachers found.")
        return

    display_teacher_schedule(teacher_schedule[selected_teacher])
    # ...

    if len(matching_teachers) == 1:
        selected_teacher = matching_teachers[0]
    elif len(matching_teachers) > 1:
        selected_teacher = select_teacher_from_keyboard(matching_teachers)
    else:
        print("No matching teachers found.")
        return

    display_teacher_schedule(teacher_schedule[selected_teacher])

    # Ask for the desired schedule timeframe
    timeframe = input("Enter the desired schedule timeframe (today, tomorrow, this week, next week): ")
    # TODO: Implement logic to display the schedule for the specified timeframe

if __name__ == "__main__":
    main()




#НАЙТИ ПРЕПОДОВ

#Парсим и находим препода
#Если нашли препода:
    #если он в списке
        #continue
    #если его нет в спике
        #добавить в список с преподами 

#вернуть список с преподами


#БОТ

#если препод 1 
    #РАСПИСАНИЕ
#если преподов > 1
    #выбор препода
    #РАСПИСАНИЕ
#если преподов 0 
    #Препод в файлах не найден



#РАСПИСАНИЕ

#парсим файл и ищем препода 
