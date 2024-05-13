# Тестовое задание: Разработка консольного приложения "Личный финансовый кошелек"

### Задача:
Создать приложение для учета личных доходов и расходов.

## Запуск проекта
> [!NOTE]
> Для запуска программы необходим [интерпертатор python](https://www.python.org/downloads/) v. 3.10 или выше
 - Клонируйте репозиторий и перейдите в него в командной строке:
 ```
 git clone git@github.com:acunathink/personal_console_wallet.git && cd personal_console_wallet
 ```
 <br>

 - Запустите программу используя интерпретатор pyhton 
 <br>  <sub>(вторым аргументом можно указать файл для хранения данных - по умолчанию создаётся wallet.json или data.json)</sub>
```
python wallet.py data.json
```


### Использование программы:
> [!TIP]
> Если ввести неправильную команду появится следующая подсказка:
>
> ```
> Usage: Wallet-> [COMMAND] [OPTIONS]
>
>    COMMANDS:
>        show balance - shows the total income, total expenses and
>                       balance between total income and total expenses\n
> 
>        add [OPTION] - adds record with OPTIONS:
>            income  <amount> "description" - adds income  record
>            expense <amount> "description" - adds expense record
> 
>        edit [OPTION] - edit record by id with OPTIONS:
>            income  <id> <amount> "description" - adds income  record
>            expense <id> <amount> "description" - adds expense record
> 
>        search [FILTERS] - shows list of records corresponding by FILTERS:
>            -c [income|expense] - filter by category
>            -a <amount> - filter by equal amount
>            -g <amount> - filter by greater amount
>            -l <amount> - filter by lower amount
>            -d <date> - filter by date
>            -p <date:date> - filter by period behind two dates
>            * all filters may be use together with others
>            example usage: search -с income -a 25 -g 30 -l 10 -d 2024-05-02
> ```
___

<h4 align="left">тестовое задание выполнил <a href="https://github.com/acunathink" target="_blank">Тимофей Карпов</a><a href="https://t.me/timofey_the_hiker" target="_blank">  🛒</a></h4>
