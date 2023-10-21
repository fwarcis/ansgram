# AnsGram как QA-сервис в телеграм-боте

## Проблема

---
**Генеральная совокупность** — 29 человек

### При использовании в целом различных источников информации выделяется нехватка

1. Анонимности (мало выбравших)
2. Оповещений об ответах (мало выбравших)
3. Быстрых ответов

### Причины неиспользования телеграм-чатов в качестве источника информации по предметам

1. Неудобства: сообщений не по теме, реклама и подписки
2. Незаинтересованность людей в помощи
3. Риск недостоверности информации

### Люди довольны при поиске в источниках информации

- Быстроте нахождения
- Надежности
- Объяснениям
- Обилию информации (хотя есть и недовольство по поводу лишних слов) и ответов
- Заинтересованностью людей в помощи

## Решение

---
**Телеграм-бот с использованием aiogram_dialog, предоставляющий возможность:**

- Задавать вопросы по предметам
  - ИИ может сгенерировать/перегенерировать ответ
  - В ответах от пользователей требуется объяснение
- Искать вопросы и людей для:
  - Помощи
  - Нахождения ответов
- Иметь свой профиль соответственно
- Получать оповещения об ответах