from pandas import read_csv
from random import randint

csv = read_csv('resources/thousand_most_popular_spanish_words.csv', sep=',', encoding='utf-8').to_dict()

while True:
    random_index = randint(0, len(csv['Spanish']) - 1)
    random_word = csv["Spanish"][random_index]
    print(random_word)
    answer = input("Type translation: ")
    if answer.lower() == csv["in English"][random_index].lower():
        print("Correct!")
    else:
        print("Wrong! The answer is:", csv["in English"][random_index])
