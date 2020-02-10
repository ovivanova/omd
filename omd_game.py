def my_step(step,tree):
    
    my_tree = tree.copy()
    print('{}'.format(my_tree[step]['text']))
    
    if my_tree[step].get('нет') is None and my_tree[step].get('каркаде') is None:
        return 0
    else:
        user_input = input().lower()

    counter = 0
    if my_tree[step].get('каркаде') is None:
        answer_list = {'да', 'нет'}
    else:
        answer_list = {'фруктовый', 'зеленый', 'каркаде'}
    while user_input not in answer_list:
        counter+=1
        if counter< 5:
            print('Проверьте правильность ввода ответа на вопрос    {}'.format(my_tree[step]['text']))
            user_input = input().lower()
        else:
            print('Я так не играю..')
            return 0

    next_step = my_tree[step].get(user_input)
    return next_step

if __name__ == '__main__':
    current_step = 1
    question_tree = {
        1: {'text': 'Привет! Может чаю?', 'да' : 10, 'нет' : 11},
        2: {'text': 'Ммм, может добавить лимон?',  'да': 4, 'нет': 3},
        3: {'text': 'А булочку с изюмом хочешь?', 'да': 6, 'нет': 4},
        4: {'text': 'Может дольку горького шоколада?', 'да':6 , 'нет': 5},
        5: {'text': 'Ты на диете?', 'да': 7, 'нет': 8},
        6: {'text': 'Ой, а этого у меня как раз нет. Сходим в магазин?', 'да': 9, 'нет': 8},
        7: {'text': 'Так держать! Держи свой напиток!'},
        8: {'text': 'Ну воть..'},
        9: {'text': 'Уиии. Тогда возьмем еще и тортик!'},
        10 :{'text': 'Какой чай ты хочешь? (фруктовый, зеленый, каркаде)', 'фруктовый': 3, 'зеленый' : 2 ,'каркаде': 4},
        11 :{'text': 'Тогда кофе', 'да': 4, 'нет': 8}
    }

while current_step != 0:
    current_step = my_step(current_step, question_tree)