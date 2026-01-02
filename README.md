# Proyecto Urban Grocers 
## _Las pruebas realizadas en este proyecto del 8vo Sprint se enfoca en realizar pruebas de la lista de comprobacion para el parametro 'name' de un kit body al momento de crear un nuevo kit._

## Fuentes utilizadas
- Revision de proyecto.
- Webinar - Sprint 7 - Introduccion a la automatizacion de pruebas.

## Tecnologias y tecnicas utilizadas
- Pruebas negativas
- Analisis de valores limite.
- libreras importadas:
- Instalacion de la libreria requests.
- Instalacion de la libreria pytest para cada funcion creada para cada prueba de la lista de comprobacion.

## Los métodos GET , POST , PUT , y DELETE están todos cubiertos.
- Solo se cubren los metodos GET y POST en este proyecto.

## Pruebas que coinciden con la documentacion 

Prueba 1. El número permitido de caracteres (1) > Código de respuesta: 201 
> El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
```sh
test_create_kit_with_1_letter_name():
create_kit_name_kit_test.py::test_create_kit_with_1_letter_name PASSED   [100%]
```
Prueba 2. El número permitido de caracteres (511) > Código de respuesta: 201 
> El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
```sh
test_create_kit_with_511_letter_name():
create_kit_name_kit_test.py::test_create_kit_with_511_letter_name PASSED [100%]
```
Prueba 5. Se permiten caracteres especiales > Código de respuesta: 201
> El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
```sh
test_create_kit_with_special_char_allowed():
create_kit_name_kit_test.py::test_create_kit_with_special_char_allowed PASSED [100%]
```
Prueba 6. Se permiten espacios > Código de respuesta: 201
> El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
```sh
test_create_kit_with_spaces_allowed():
create_kit_name_kit_test.py::test_create_kit_with_spaces_allowed PASSED  [100%]
```
Prueba 7. Se permiten números > Código de respuesta: 201
> El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
```sh
test_create_kit_with_numbers_allowed():
create_kit_name_kit_test.py::test_create_kit_with_numbers_allowed PASSED [100%]
```
Prueba 8. El parámetro no se pasa en la solicitud 
> Código de respuesta: 400
```sh
test_create_no_input_name_parameter_kit_error():
create_kit_name_kit_test.py::test_create_no_input_name_parameter_kit_error FAILED [100%]
create_kit_name_kit_test.py:49 (test_create_no_input_name_parameter_kit_error)
def test_create_no_input_name_parameter_kit_error():
>       new_kit_body = get_kit_body()
                       ^^^^^^^^^^^^^^
E       TypeError: get_kit_body() missing 1 required positional argument: 'kit_name'
```

## Pruebas que no coinciden con la documentacion
Prueba 3. El número de caracteres es menor que la cantidad permitida (0) > Código de respuesta: 400
```sh
 test_create_user_empty_kit_name_get_error_response():
 create_kit_name_kit_test.py::test_create_user_empty_kit_name_get_error_response FAILED [100%]
 create_kit_name_kit_test.py::test_create_user_empty_kit_name_get_error_response FAILED [100%]
create_kit_name_kit_test.py:32 (test_create_user_empty_kit_name_get_error_response)
201 != 400

Expected :400
Actual   :201
```
Prueba 4. El número de caracteres es mayor que la cantidad permitida (512)
> Código de respuesta: 400
```sh
test_create_kit_with_512_letter_name():
create_kit_name_kit_test.py::test_create_kit_with_512_letter_name FAILED [100%]
create_kit_name_kit_test.py:36 (test_create_kit_with_512_letter_name)
201 != 400

Expected :400
Actual   :201
```
Prueba 9. Se ha pasado un tipo de parámetro diferente (número) 
> Código de respuesta: 400
```sh
test_create_with_numeric_name_error():
create_kit_name_kit_test.py::test_create_with_numeric_name_error FAILED  [100%]
create_kit_name_kit_test.py:56 (test_create_with_numeric_name_error)
201 != 400

Expected :400
Actual   :201
```
