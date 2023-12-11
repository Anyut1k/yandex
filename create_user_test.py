import sender_stand_request
import data

# Функция для изменения значения в параметре firstName в теле запроса
def get_user_body(first_name):
    # Копируется словарь с телом запроса из файла data
    current_body = data.user_body.copy()
    # Изменение значения в поле firstName
    current_body["firstName"] = first_name
    # Возвращается новый словарь с нужным значением firstName
    return current_body

    # Функция для негативной проверки
def negative_assert_symbol(first_name):
        # В переменную user_body сохраняется обновлённое тело запроса
        user_body = get_user_body(first_name)

        # В переменную response сохраняется результат запроса
        response = sender_stand_request.post_new_user(user_body)

        # Проверка, что код ответа равен 400
        assert response.status_code == 400

        # Проверка, что в теле ответа атрибут "code" равен 400
        assert response.json()["code"] == 400


def test_create_user_number_type_first_name_get_error_response():
    # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body(12)
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    response = sender_stand_request.post_new_user(user_body)

    # Проверка кода ответа
    assert response.status_code == 400