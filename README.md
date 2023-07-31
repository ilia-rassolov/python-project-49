### Hexlet tests and linter status:
[![Actions Status](https://github.com/ilia-rassolov/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/ilia-rassolov/python-project-49/actions)
<a href="https://codeclimate.com/github/ilia-rassolov/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/f315eb1f909eb7b075f2/maintainability" /></a>

Привет, меня зовут Илья

Здесь я создал свой первый проект, он учебный, от Hexlet.io, называется Игры разума (Brain games)

Описание:
Начать можно с **brain-games** - это просто приветствие!
Далее необходимо решить пять логических задач, по три вопроса в каждой:
1. В **brain-even** нужно определить является ли предлагаемое число чётным
2. Игра **brain-calc** попросит выполнить вас простейшие арифметические действия
3. А в **brain-gcd** чуть сложнее: необходимо определить наибольший общий делитель двух чисел
4. **brain-progression**: здесь вам будет предложена прогрессия, но не полная, задача её восстановить
5. И, наконец, в **brain-prime** вы, надеюсь, с лёгкостью определите является ли число простым или нет

Примеры решений указаны ниже в плеере asciinema

[![asciicast](https://asciinema.org/a/ZzHIhGThu8wVnTeOA5JVkRism.svg)](https://asciinema.org/a/ZzHIhGThu8wVnTeOA5JVkRism)


Готово! Можно запускать игры следующими командами:

brain-games

[![asciicast](https://asciinema.org/a/iQ2hBOQ6BpJQTQ0omn8PGJsAC.svg)](https://asciinema.org/a/iQ2hBOQ6BpJQTQ0omn8PGJsAC)


brain-even

[![asciicast](https://asciinema.org/a/Qltn8cPLpfb2o9OehuShKsGbm.svg)](https://asciinema.org/a/Qltn8cPLpfb2o9OehuShKsGbm)


brain-calc

[![asciicast](https://asciinema.org/a/PBQIBYdG9osCseVqaMy6884Hw.svg)](https://asciinema.org/a/PBQIBYdG9osCseVqaMy6884Hw)


brain-gcd

[![asciicast](https://asciinema.org/a/RQGU14N3qpHawQ7JqwNVB7eXK.svg)](https://asciinema.org/a/RQGU14N3qpHawQ7JqwNVB7eXK)


brain-progression

[![asciicast](https://asciinema.org/a/564451.svg)](https://asciinema.org/a/564451)


brain-prime

[![asciicast](https://asciinema.org/a/TWI6GTq3JiwSVxBJ3R9C9Wcq5.svg)](https://asciinema.org/a/TWI6GTq3JiwSVxBJ3R9C9Wcq5)



Чтобы установить игру и запустить необходимо:
1. Установить Python 3.6 или выше: 
python -m pip install
2. Установить poetry 1.2.0 или выше:
poetry -m pip install
3. Настроить poetry для создания виртуального окружения:
poetry config virtualenvs.in-project true
4. Склонируйте пакет:
git clone git@github.com:ilia-rassolov/python-project-49.git
5. Установите пакет:
poetry install
6. Выполните сборку пакета, отладку публикации и установку в систему:
make build
make publish
make package-install
