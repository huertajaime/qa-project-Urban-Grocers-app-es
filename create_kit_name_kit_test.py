import sender_stand_request
import data

def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400
#Prueba 1
def test_create_kit_with_1_letter_name():
    new_kit_body = get_kit_body("A")
    positive_assert(new_kit_body)
#Prueba 2
def test_create_kit_with_511_letter_name():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(new_kit_body)
#Prueba 3
def test_create_user_empty_kit_name_get_error_response():
    new_kit_body = get_kit_body("")
    negative_assert(new_kit_body)
#Prueba 4
def test_create_kit_with_512_letter_name():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(new_kit_body)
#Prueba 5
def test_create_kit_with_special_char_allowed():
    new_kit_body = get_kit_body("\"№%@\",")
    positive_assert(new_kit_body)
#Prueba 6
def test_create_kit_with_spaces_allowed():
    new_kit_body = get_kit_body("A Aaa")
    positive_assert(new_kit_body)
#Prueba 7
def test_create_kit_with_numbers_allowed():
    new_kit_body = get_kit_body("123")
    positive_assert(new_kit_body)
#Prueba 8
def test_create_no_input_name_parameter_kit_error():
    new_kit_body = get_kit_body()
    negative_assert(new_kit_body)
#Prueba 9
def test_create_with_numeric_name_error():
    new_kit_body = get_kit_body(123)
    negative_assert(new_kit_body)
