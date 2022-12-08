# ddt-geodata
Data driven тесты для 2 api - search и reverse.

Ссылка на документацию - https://nominatim.org/release-docs/develop/

Для запуска всех тестов использовать команду:

    pytest -v python -m pytest [...]

Для запуска конкретного модуля с тестами использовать команду:

    pytest -v ./test_*.py
  
Для запуска тестов с пометкой "xfail" использовать команду:

    pytest -v -m "xfail" ./test_*.py

Для запуска определенного теста из модуля использовать команду:

    pytest test_*.py::Test*Api::test_*
