Homework-2

1. Установлен UV
2. Установлен HomeBrew
3. Создано виртуально окружение
4. Создана директория проекта
5. Установлен Django
5. Создан Django проект
6. Инициализирован репозиториий ГИТ
7. Создан makefile
8. Создано правило защиты для ветки main на Гитхаб

Homework24012026
Поменял в шаблонах:
1. base.html -  <nav class="navbar navbar-expand-lg navbar-dark bg-success mb-4"> цвет фона меню на зеленый
2. category_list.html -  <div class="col-md-12 mb-1"> уменьшил отсутпы
3. category_list.html -  <a class="btn btn-outline-primary btn-sm" href="{% url "blog:category_detail" category.id %}">Перейти к категории</a> - Кнопки сделал контурными
4. category_detail.html -  <h6 class="card-subtitle text-success-emphasis mb-2">Опубликована</h6>
<h6 class="card-subtitle text-danger-emphasis mb-2">Неопубликована</h6> - изменил цвет в зависисмости от Опубликовано/неопубликовано

## 🚀 Быстрый старт

Для запуска проекта локально выполните следующие шаги:

1.  **Настройка переменных окружения**:
    Скопируйте файл с примером настроек в рабочий файл `.env`:
    ```bash
    cp .env.example .env
    ```

2.  **Запуск Docker-контейнеров**:
    Запустите Docker в фоновом режиме
    ```

3.  **Применение миграций**:
    Выполните запуск сервера базы данных:
    ```bash
    make start_db
    ```
    Подготовьте миграции:
    ```bash
    make makemigrations
    ```
    Примените миграции:
    ```bash
    make migrate
    ```
