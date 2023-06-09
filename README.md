# Как собрать

1. Стянуть репозиторий
2. Установить python и pip
`sudo apt install python3 python3-pip`
3. Перейти в директорию, установить и активировать виртуальное окружение
`python3 -m venv env`
`source env/bin/activate`
4. Установить библиотеки из requirements.txt
`pip3 install -r requirements.txt`
5. Запустить тесты
`pytest`






# Пусть инфа ниже тоже будет пока тут:

cd /.../integration-tests/tests

export PYTHONPATH=$PYTHONPATH:/.../integration-tests/tests

pytest test_create_order.py