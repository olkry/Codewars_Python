# Создайте функцию, которая отвечает на вопрос «Вы играете на банджо?».
# Если ваше имя начинается с буквы «R» или строчной «r», вы играете на банджо!
#
# Функция принимает имя в качестве единственного аргумента и возвращает одну из следующих строк:
#
# name + " plays banjo"
# name + " does not play banjo"
# Указанные имена всегда являются допустимыми строками.
name = 'Tocky'


def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name


print(are_you_playing_banjo(name))

# Ещё варианты:

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'


def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";

def areYouPlayingBanjo(name):
   return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"