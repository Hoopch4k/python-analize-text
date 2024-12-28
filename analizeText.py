
class AnalizeText:
    
    text: str
    textArr: list
    
    
    __tabulaions = '''\'\"\n\r\t\0\\\x0c'''
    __symbols = '''"'`~!@#$%^&*()_+=-?:;№,<.>/?|[]{}'''
    
    def __init__(self, text) -> None:
        self.text = text
        self.textArr = list(map(lambda y: y.lower(), self.__del_tabulation(list(map(lambda x: self.__del_symb(x), text.split(" "))))))
    


    # Получить длину текста в словах
    def get_len(self) -> int:
        return len(self.textArr)

    # Получить все уникальные слова в тексте
    def get_unique_words(self) -> list:
        return list(set(self.textArr))

    # Получить кол-во встречающихся слов в тексте
    def get_word_count(self, word: str) -> int:
        return self.textArr.count(word.lower())

    # Получить самое длинное слово в тексте
    def get_longest_word(self) -> str:
        return max(self.textArr, key=lambda x: len(x))

    # Получить самое короткое слово в тексте
    def get_shortest_word(self) -> str: # Самое короткое слово в тексте, проходится по вему тексту и если таких лов несколько, то запоминает самое первое
        return min(self.textArr, key=lambda x: len(x))

    # Получить часто встречающеся слово 
    def get_common_word(self) -> str:
        return self.__get_common_word_and_count()





    # метод нахождения самого частотного слова и его количества в тексте
    def __get_common_word_and_count(self) -> tuple:
        return max(self.get_unique_words(), key=lambda x: self.get_word_count(x), default=None), self.get_word_count(max(self.get_unique_words(), key=lambda x: self.get_word_count(x), default=None))



    #-----Классовые методы при инициализации текста-----------#

    # Удаление символов из слова, кроме букв и цифр
    def __del_symb(self, word) -> str:
        arrWord = list(word)
        for symbol in self.__symbols:
            arrWord = [x for x in arrWord if x!=symbol]
        return "".join(arrWord)


    # Удаление табуляции списка содержащие строки
    def __del_tabulation(self, arr: list) -> list: 
        for ind, w in enumerate(arr):
            newArr = None
            for tab in self.__tabulaions:
                if tab in w:
                    newArr = w.replace(tab, ",").split(",") # Новый массив без табуляций
                    newArr = self.__correct_null_str_in_arr(newArr) # Проверить и удалить все пустые строки
                    for indArr, wordArr in enumerate(newArr):   # перебрать этот массив, который содержит несколько слов, либо же одно слово
                        del arr[ind]                            # Удалить элемент из массива содержащий строку с табуляцией
                        arr.insert(ind+indArr, wordArr)         # Вставить новый элемент в массив за место удалёенного
                    
        return arr
                    

    # Проверка и удаление всех пустых строк в массиве
    def __correct_null_str_in_arr(self, array) -> list:
        newArr = []
        list(map(lambda word: newArr.append(word) if not (word == "" or word == " " or word == None) else word , array))
        return newArr