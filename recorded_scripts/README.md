# Записанные скрипты

Здесь хранятся сырые скрипты, записанные через `playwright codegen`.

## Структура

```
recorded_scripts/
├── auth/          # Авторизация, выход, регистрация
├── catalog/       # Каталог, поиск, фильтры
├── cart/          # Корзина
└── checkout/      # Оформление заказа
```

## Запись нового скрипта

```bash
# Запись сценария авторизации
python utils/recorder.py --page auth --name login --url /login

# Запись поиска в каталоге
python utils/recorder.py --page catalog --name search_product --url /catalog
```

## Конвертация в метод Page Object

```bash
# Конвертировать скрипт и вывести готовый метод
python utils/script_converter.py recorded_scripts/auth/login.py --method login

# Записать в файл
python utils/script_converter.py recorded_scripts/catalog/search_product.py \
    --method search \
    --output pages/catalog_page_search.py
```
