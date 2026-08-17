# Наш Маркетплейс (Бэкенд)

### Как запустить проект локально:
1. Создать виртуальное окружение: `python -m venv venv`
2. Включить его: `source venv/bin/activate` (или `venv\Scripts\activate` на Windows)
3. Установить библиотеки: `pip install -r requirements.txt`
4. Скопировать `.env.example` в `.env` и вписать свои настройки базы данных.
5. Запустить сервер: `uvicorn app.main:app --reload`