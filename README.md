**Cервис на Flask ассоциирующий длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.  Взаимодействует с БД (SQLite) при помощи ORM (SQLAlchemy). Шаблоны страниц и форм настроены через Jinja2.**
  
  

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
