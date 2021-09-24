# notion_api
___
## Установка
1. Склонировать репозиторий 
2. Установить библиотеку для notion:
   1. ```
      pip install requirements
   2. либо 
      ```
      pip install git+https://github.com/jamalex/notion-py.git@refs/pull/294/merge
3. `pip install python-dotenv` для env файла
4. Проверить что файл `notion/client.py` после установки совпадает с файлом, который лежит в репозитории, если нет, 
то заменить на файл из репо.
5. Создать .env file с содержимым `token_v2=<token_v2>`. [Как получить токен?](https://www.redgregory.com/notion/2020/6/15/9zuzav95gwzwewdu1dspweqbv481s5)


## Запуск
Пока просто запустить программу
