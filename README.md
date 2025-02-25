# LinkCut

<img width="1131" alt="image" src="https://github.com/user-attachments/assets/768e6f05-fcf7-48e8-b860-6e14035d5228" />



### Cервис на Flask ассоциирующий длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.  Взаимодействует с БД (SQLite) при помощи ORM (SQLAlchemy). Шаблоны страниц и форм настроены через Jinja2

---

### Инструкция по развертыванию:
**Клонируйте репозиторий:**

```
git clone git@github.com:shft1/LinkCut.git
```

**Cоздайте и активируйте виртуальное окружение:**

```
python3 -m venv venv
```

* _Если у вас Linux/macOS_

    ```
    source venv/bin/activate
    ```
* _Если у вас Windows_

    ```
    source venv/scripts/activate
    ```

**Установите зависимости из файла requirements.txt:**

```
pip install -r requirements.txt
```

**Заполните файл .env**
```
FLASK_APP - имя вашего приложения
FLASK_DEBUG - режим debug (True/False)
SECRET_KEY - ключ для CSRF-защиты
DATABASE_URI - sqlite:///db.sqlite3
```

**Запустите тесты, для проверки корректности работы приложения**
```
pytest
```

**Запустите приложение на локальном хосте**
```
flask run
```
