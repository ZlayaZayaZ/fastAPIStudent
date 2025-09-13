from fastapi import FastAPI, Depends, HTTPException
# from utils import json_to_dict_list
# import os
from typing import Optional, List

from models import Student, RBStudent, SUpdateFilter, SStudentUpdate, SDeleteFilter

from json_db_lite import JSONDatabase
#
# # Получаем путь к директории текущего скрипта
# script_dir = os.path.dirname(os.path.abspath(__file__))
#
# # Переходим на уровень выше
# parent_dir = os.path.dirname(script_dir)
#
# # Получаем путь к JSON
# path_to_json = os.path.join(parent_dir, 'students.json')

# path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'students.json')

app = FastAPI()
# инициализация объекта
small_db = JSONDatabase(file_path='students.json')


# получаем все записи
def json_to_dict_list():
    return small_db.get_all_records()


@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}


# через параметр пути: http://127.0.0.1:8000/students/2
@app.get("/students/{course}")
def get_all_students_course(request_body: RBStudent = Depends()) -> List[Student]:
    # students = json_to_dict_list(path_to_json)
    students = json_to_dict_list()
    filtered_students = []
    for student in students:
        if student["course"] == request_body.course:
            filtered_students.append(student)

    if request_body.major:
        filtered_students = [student for student in filtered_students if
                             student['major'].lower() == request_body.major.lower()]

    if request_body.enrollment_year:
        filtered_students = [student for student in filtered_students if
                             student['enrollment_year'] == request_body.enrollment_year]

    return filtered_students


# через параметр запроса имеющий вид: http://127.0.0.1:8000/students?course=2
@app.get("/students")
def get_all_students(course: Optional[int] = None):
    # students = json_to_dict_list(path_to_json)
    students = json_to_dict_list()
    if course is None:
        return students
    else:
        return_list = []
        for student in students:
            if student["course"] == course:
                return_list.append(student)
        return return_list


@app.get("/student", response_model=Student)
def get_student_by_query_id(student_id: int):
    # students = json_to_dict_list(path_to_json)
    students = json_to_dict_list()
    for student in students:
        if student["student_id"] == student_id:
            return student
    return {"error": "Student not found"}


# Для параметра пути: /student/3
@app.get("/student/{student_id}", response_model=Student)
def get_student_by_path_id(student_id: int):
    # students = json_to_dict_list(path_to_json)
    students = json_to_dict_list()
    for student in students:
        if student["student_id"] == student_id:
            return student
    return {"error": "Student not found"}


# добавляем студента
def add_student(student: dict):
    student['date_of_birth'] = student['date_of_birth'].strftime('%Y-%m-%d')
    small_db.add_records(student)
    return True


# обновляем данные по студенту
def upd_student(upd_filter: dict, new_data: dict):
    small_db.update_record_by_key(upd_filter, new_data)
    return True


# удаляем студента
def dell_student(key: str, value):
    small_db.delete_record_by_key(key, value)
    return True


@app.post("/add_student")
def add_student_handler(student: Student):
    student_dict = student.dict()
    check = add_student(student_dict)
    if check:
        return {"message": "Студент успешно добавлен!"}
    else:
        return {"message": "Ошибка при добавлении студента"}


@app.put("/update_student")
def update_student_handler(filter_student: SUpdateFilter, new_data: SStudentUpdate):
    check = upd_student(filter_student.dict(), new_data.dict())
    if check:
        return {"message": "Информация о студенте успешно обновлена!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при обновлении информации о студенте")


@app.delete("/delete_student")
def delete_student_handler(filter_student: SDeleteFilter):
    check = dell_student(filter_student.key, filter_student.value)
    if check:
        return {"message": "Студент успешно удален!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при удалении студента")

