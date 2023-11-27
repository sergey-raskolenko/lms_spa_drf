Команды ля запуска приложения с помощью Docker:
```bash
docker-compose build
docker-compose up
```
Во втором терминале применить миграции для проекта:
```bash
docker-compose exec app python manage.py migrate
```