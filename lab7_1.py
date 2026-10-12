
text = input('Введіть слова: ')

text = text.replace(',', ' ')
text = text.replace('.', ' ')

words = text.split()

if words:
    max_len = max(len(word) for word in words)
    min_len = min(len(word) for word in words)

    longest = [word for word in words if len(word) == max_len]
    shortest = [word for word in words if len(word) == min_len]

    if len(longest) == 1:
        print('Найдовше слово: ', longest[0])
    
    else:
        print('Найдовші слова: ', ', ' .join(longest))

    if len(shortest) == 1:
        print('Найкоротше слово: ', shortest[0])

    else:
        print('Найкоротші слова: ', ', ' .join(shortest))

    
else:
    print('Ви не ввели жодного слова')