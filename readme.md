# Дипломная работа. Профессия python-разработчик

Написать небольшой проект на Django и Django Rest Framework с моделью "Образовательные модули". В них есть:

- порядковый номер
- название
- описание

## Задача

<aside>
👾 При создании проекта  нужно:

1. реализовать для модели (моделей) все методы CRUD

2. Полностью покрыть автоматизированными юнит-тестами все модели, сериализаторы, виды.

</aside>

## Требуемый стэк

- python 3.11
- Docker
- Django

### Условия приемки

- код размещен в открытом репозитории
- доступна документация
- код покрыт автоматизированными юнит-тестами
- код оформлен согласно pep8
- оформлен Readme файл
- в проекте использован Docker

# Развертывание проекта:

```bash
python3 -m venv venv
```
Активировать виртуальное окружение
```bash
source venv/bin/activate
```
Установить зависимости проекта, указанные в файле `requirements.txt`
```bash
pip install -r requirements.txt
```
Применить миграции
```bash
python manage.py migrate
```
Наполнить БД
```bash
python manage.py loaddata data.json
```
Создать пользователей
```bash
python3 manage.py create_user
```
Запустить сервер
```bash
python manage.py runserver
```
Собрать и запустить образ docker-compose
```bash
 docker-compose up -d --build
```