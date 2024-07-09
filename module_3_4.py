
def single_root_words(root_word, *other_words):                                  # Создаем функцию single_root_words
    same_words = []                                                              # Создаем пустой список

# Функция составляет новый список same_words из тех слов списка other_words,
# которые содержат root_word и наоборот root_word содержит одно из этих слов.

    for i in other_words:                                                         # Функция ищет слова содержащие
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():      # root_word в other_words и если
            same_words.append(i)                                                  # элементы other_words находятся
    return same_words                                                             # в root_word

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
