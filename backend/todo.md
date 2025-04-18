✅ 1. Подготовка и базовая настройка

   [✅] Настроить структуру проекта (FastAPI + SQLAlchemy 2.0 + Alembic).

   [✅] Установить зависимости (FastAPI, Uvicorn, SQLAlchemy, Alembic, Pydantic, passlib, python-jose и др.).

   [✅] Настроить подключение к базе данных.

   [✅] Инициализировать Alembic и настроить миграции.

   [✅] Настроить CORS и базовую конфигурацию проекта.

✅ 2. Реализация авторизации и ролей

   [✅] Создать enum UserRole (admin, hr, candidate).

   [✅] Создать модель User с полями: id, email, пароль, роль.

   [] Реализовать регистрацию пользователя.

   [ ] Реализовать вход с JWT-авторизацией.

   [ ] Настроить защиту маршрутов в зависимости от роли.

✅ 3. Кандидат

   [ ] Создать модель CandidateProfile (имя, опыт, стек, образование, портфолио и т.п.).

   [ ] Связать профиль с пользователем (кандидатом).

   [ ] Реализовать API для создания и обновления профиля кандидата.

   [ ] Реализовать API для получения списка всех вакансий.

   [ ] Реализовать отклик на вакансию.

   [ ] Реализовать автоматическую проверку совпадения стека с вакансией.

   [ ] При совпадении ≥ 70% — отправка тестового задания кандидату (либо отображение его в личном кабинете).

   [ ] Реализовать просмотр своих откликов и их статусов.

✅ 4. HR

   [ ] Регистрация пользователя с ролью HR.

   [ ] Создание профиля компании (название, описание, сайт и др.).

   [ ] Реализовать модель Vacancy (название, описание, стек, минимальный процент совпадения).

   [ ] Реализовать API для создания, редактирования и удаления вакансий (только для HR).

   [ ] Реализовать API просмотра откликов на свои вакансии.

   [ ] Возможность менять статус откликов (например: “на рассмотрении”, “отклонён”, “приглашён”).

   [ ] Добавить тестовые задания к вакансиям.

✅ 5. Администратор

   [ ] Возможность просмотра всех пользователей.

   [ ] Возможность редактирования и удаления пользователей.

   [ ] Возможность просматривать и управлять всеми вакансиями.

   [ ] Возможность просматривать все отклики.

✅ 6. Интерфейс (Frontend или Swagger)

   [ ] Подключение фронтенда.

   [ ] Кандидат: профиль, список вакансий, отклики, тесты.

   [ ] HR: профиль, список вакансий, отклики.

   [ ] Админ: панель управления.
