# ddt-geodata
Data driven тесты для 2 api - search и reverse.

Ссылка на документацию - https://nominatim.org/release-docs/develop/

Для запуска всех тестов использовать команду:

    pytest -s -v python -m pytest [...]

Для запуска конкретного модуля с тестами использовать команду:

    pytest -s -v ./test_*.py
  
Для запуска тестов с пометкой "xfail" использовать команду:

    pytest -s -v -m "xfail" ./test_*.py

Для запуска определенного теста из модуля использовать команду:

    pytest test_*.py::Test*Api::test_*
