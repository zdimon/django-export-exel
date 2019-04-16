# Экспорт данных из Django в exel.

Необходимо экспортировать каталог продукции из существующей базы данных в формат Exel.

## Входные данные.

Наполненная база данных MySQL.

## Выходные данные

Файл xls с двумя листами заданной структуры.

## Деплой.

    git clone git@github.com:zdimon/django-export-exel.git
    cd django-export-exel
    virtualenv -p python3 venv
    . ./venv/bin/activate
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py export_data
    

**В проекте использована библиотка xlwt.**

[Ссылка на документацию](https://pypi.org/project/xlwt/)
