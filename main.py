import random

nouns = ['Chair', 'Laptop', 'Book', 'City', 'New York', 'Banana',  'Family', 'Ice cream', 'Table', 'Anger']
adjectives = ['Blue', 'Red', 'Purple', 'Green', 'Black', 'Cyan', 'Rainbow', 'Marin', 'Mink', 'Orange', ]
punctuations = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ]

print('---------------------------------------------------------------------------------------------------------------')
print('-*-*-*-*-*-*-*-*-*-> Welcome to password picker,this app creates a hard password to crack. <-*-*-*-*-*-*-*-*-*-')
print('---------------------------------------------------------------------------------------------------------------')
print('')

is_new_password_required = True

while is_new_password_required:
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    punctuation = random.choice(punctuations)
    number = random.randint(0, 100)

    password = f"{noun}{adjective}{number}{punctuation}"

    print(f'Your new password is {password}')
    answer = input('Do you need another password? Yes/No: ')

    if answer.lstrip().rstrip().lower() == 'yes':
        is_new_password_required = True
    elif answer.lstrip().rstrip().lower() == 'no':
        print('Thanks for using my app.')
        is_new_password_required = False

    else:
        is_new_password_required = False
        print("you've entered a wrong choice")
