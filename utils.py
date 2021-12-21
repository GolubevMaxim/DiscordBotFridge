def time_is_not_up(time_d: dict):
    for key in time_d.keys():
        if time_d[key] != 0:
            return True
    return False


def time_str_to_sec(time_str: str):
    try:
        multi_dict = {"s": 1, "m": 60, "h": 60 ** 2, "d": 24 * (60 ** 2)}
        return int(time_str[:-1]) * multi_dict[time_str[-1]]
    except KeyError:
        return None
    except ValueError:
        return None
    except TypeError:
        return None


def translit_translate(word):
    for prep in ".,!?":
        word = word.replace(prep, " ")
    word = word.strip()
    d = {'щ': ['щ', 'sch'],
         'ч': ['ч', 'ch'],
         'ш': ['ш', 'sh'],
         'ы': ['ы', 'bi'],
         'ю': ['ю', 'io', "юю"],
         'ж': ['ж', 'zh', '*'],
         'я': ['ya', "уа", "yа", "яя"],
         'а': ['а', 'a', '@', 'аа'],
         'б': ['б', '6', 'b'],
         'в': ['в', 'b', 'v'],
         'г': ['г', 'g'],
         'д': ['д', 'd'],
         'е': ['е', 'e', "ее"],
         'ё': ['ё', 'e'],
         'з': ['з', '3', 'z'],
         'и': ['и', 'u', 'i'],
         'й': ['й', 'u', 'i'],
         'к': ['к', 'k'],
         'л': ['л', 'l'],
         'м': ['м', 'm'],
         'н': ['н', 'h', 'n'],
         'о': ['о', 'o', '0', "оо"],
         'п': ['п', 'n', 'p'],
         'р': ['р', 'r', 'p'],
         'с': ['с', 'c', 's'],
         'т': ['т', 'm', 't'],
         'у': ['у', 'y', 'u', "уу"],
         'ф': ['ф', 'f'],
         'х': ['х', 'x', 'h', '}{'],
         'ц': ['ц', 'c'],
         'ь': ['ь', 'b'],
         'ъ': ['ъ'],
         'э': ['э', 'e']
         }

    for key, value in d.items():
        for letter in value:
            while word != word.replace(letter, key):
                word = word.replace(letter, key)

    return word
