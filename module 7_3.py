from string import punctuation
from pprint import pprint

class WordsFinder:
    #Объект этого класса должен принимать при создании неограниченного количество
    # названий файлов и записывать их в атрибут file_names в виде списка или кортежа.
    def __init__(self,*file_names):
        self.file_names = list(file_names)
    def get_all_words(self):
        all_words = {}
        #Переберите названия файлов и открывайте каждый из них, используя оператор with
        for file_name in self.file_names:
            with open(file_name,'r',encoding='utf-8') as file:
                words = []
                for line in file:
                    #Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
                    line = line.lower()
                    #Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
                    # (тире обособлено пробелами, это не дефис в слове).
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for symbol in punctuation:
                        line = line.replace(symbol,'' if symbol != ' - ' else ' ')
                    #Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
                    words.extend(line.split())
                #В словарь all_words запишите полученные данные, ключ - название файла,
                # значение - список из слов этого файла.
                all_words[file_name]=words
        return  all_words
    #find(self, word) - метод, где word - искомое слово.
    # Возвращает словарь, где ключ - название файла,
    # значение - позиция первого такого слова в списке слов этого файла.
    # В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
    # Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().
    def find(self,word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word)+1
        return result
    #count(self, word) - метод, где word - искомое слово. Возвращает словарь,
    # где ключ - название файла, значение - количество слова word в списке слов этого файла.
    def count(self,word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)
        return result



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


