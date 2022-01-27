import random
a = random.randint(1,101)
print(a)

list1=[0]
no_of_guesses=0
while True:

    guess = int(input())
    if guess <1 or guess > 100:
        print('OUT OF BOUNDS')
        continue
    if guess == a:
        print('you have guessed it right')
        break
    else:
        list1.append(guess)
        print(list1)
        if abs(a-guess)  in range(1,10):
            print('warmer')
        else:
            print('colder')
        no_of_guesses = no_of_guesses+1

        print('chances left= ', 5 - no_of_guesses)
        if no_of_guesses==5:

            print('sorry you were not able to guess the number')
            break
print('thank you')
