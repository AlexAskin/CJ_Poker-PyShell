#   15/11/2022 CJ Poker for Python Shell


# Modules:
import csv
import random

from datetime import datetime


# App start greeting:
def greeting(user_name, _user_bank):
    print('Wellcome to CJ-Poker!\n')
    print(f'{user_name}: {_user_bank}$')
    print(f'\nBet: {_user_bet}$')
    print()


#  Show Menu def:
def show_menu():
    print('\n____ MENU ____')
    print('0 - Show Menu')
    print('1 - Play Round!')
    print('2 -  ')
    print('3 -  ')    
    print('4 -  ')
    print('5 -  ')    
    print('6 -  ')
    
    #print('\n00 - Show Extended Menu')
    print('\n98 - Show deck_list')
    print('01 - Show Games Rules')
    
    print('\n9 - Exit')


#    Show Games Rules:    |
def show_rules():
    with open("app_data\\game_rules.txt", "r") as file:
        for message in file: print(message, end="")
            




#    CARDS DECK LOADING:
def deck_init():
    with open('app_data\\cards_data_df.csv', "r",  encoding='utf-8' ) as file:
        reader = csv.reader(file)
        deck_list = []
        for row in reader:
            row[1] = row[1].replace('\ufeff', '')
            deck_list.append([row[1],row[2]])
    return deck_list





def new_round():
    pass






#                                                     |
#                      MENU                           |
#                                                     |


def menu():
    global run_flag
    
    
    menu_select = input('\nSelect>>>')
    

#                                 |
    if menu_select == '0':
        show_menu()

#                                 |
    if menu_select == '01':
        show_rules()


#                                 |
    if menu_select == '1':
        print('NEW ROUND\n')
        #if debit_bet(_user_bet):
            #new_round()
        
        new_round()






#                                 |
    if menu_select == '9':
        exit_confirm = input('Sure for Exit?(1/else)>>>')
        if exit_confirm == '1':
            print('Goodbye!')
            run_flag = False
            
            return
        else:
            print('Let\'s Roll to Continue!') 

            
#         Admin Service                 |
    if menu_select == '98':
        print('Show deck_list:')        
        #random.shuffle(deck_list)
        for i in deck_list:
            print(i)





#    Main Function:  |
def main():
    menu()





#          Start App:        |


#        Run Start Time:       
now = datetime.now()
now_datatime = now.strftime("%d/%m/%Y %H:%M:%S")
print(now_datatime,'\n')




#    Loading (Initialization) of the Cards Deck:
deck_list = deck_init()

#    Defoult Bet:
_user_bet = 50




#greeting(user_name, _user_bank)
greeting('Alex', 5000)


show_menu()




#          Run App:        |
run_flag = True

while run_flag == True: main()


#exit()
