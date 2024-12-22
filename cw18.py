def defining(a):
    def doublefining():
        print('Перед виконанням функції')
        a()
        print('Після виконання функції')
    return doublefining

@defining
def triplefining():
    print('Привіт')
triplefining()