#   15/11/2022 CJ Poker for Python Shell


# Python Modules:
import csv
import random

from datetime import datetime

# App Modules:

import CHECK_Module as checker # Combination Checker



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



#       GAMES DEFS          |

#     NEW ROUND GAME:       |
# to Get 5 Random Cards:
def new_round():
    global user_hand
    
    #if len(except_nums_list) == len(deck_list)-1:
        #print('THE DECK IS ALREADY EMPTY!')
        #return
    
    #user_hand = []
    #except_nums_list = []
    
    except_nums_list.clear()
    user_hand.clear()
    
    for i in range(5):
        a = random.randint(0,51)
        
        while a in except_nums_list:
            a = random.randint(0,51)

                
        
        except_nums_list.append(a)
        user_hand.append(deck_list[a])



    #print('1!',user_hand)
    #  SORT FUNC   ??????????????   Before or After....
    #user_hand = sorted(user_hand, reverse=True, key=lambda x: int(x[1]))

    #sort_user_hand()


    message = 'user_hand: '
    for i in range(len(user_hand)):
        
        message += user_hand[i][0] + ' '
            
        #print('user_hand:', user_hand)
    print(user_hand)
        
    print()
    print(message)
    print()

    

    




    # ВЫБОР ПУША

    push_select = input('For PUSH (1-5) -> ')

    if push_select == '':
        pass
    else:
        print('PUSH:',push_select)


        for i in push_select:        
            print(user_hand[int(i) -1 ])             
            a = random.randint(0,51)       
            while a in except_nums_list:
                a = random.randint(0,51)
            except_nums_list.append(a)
            #user_hand.append(deck_list[a])
            user_hand[int(i) -1 ] = deck_list[a]
            
        print(user_hand)


        message = 'user_hand: '
        for i in range(len(user_hand)):
        
            message += user_hand[i][0] + ' '
            
        #print('user_hand:', user_hand)
        #print(user_hand)
        
        print()
        print(message)
        print()
    


    # Для отправки на ранюю криво написанную функцию Проверки:

    
    user_hand_score.clear()
    user_hand_suit.clear()

    suit_converted = []

    # SORT FUNC!!!
    user_hand = sorted(user_hand, reverse=True, key=lambda x: int(x[1]))
    
    for i in range(len(user_hand)):
        user_hand_score.append(int(user_hand[i][1]))
        user_hand_suit.append(user_hand[i][0][-1])


    #   Stop it....
    message = ''
    for i in range(len(user_hand)):
        
        message += user_hand[i][0] + ' '
            
        #print('user_hand:', user_hand)
        #print(user_hand)
        
    #print()
    #print(message)
    #print()
    
    print('\nДля отправки на Проверку:')
    print(message)
    print()
    print(user_hand_score)
    #print(user_hand_suit)

    # Еще более кривая обработка под ранее написанную функцию Проверки:

    for i in user_hand_suit:
        # [ '♥', '♦', '♣', '♠' ]
        if i == '♥': suit_converted.append('a')
        if i == '♦': suit_converted.append('b')             
        if i == '♣': suit_converted.append('c')
        if i == '♠': suit_converted.append('d')
    print(suit_converted)
    print()
    
    print(user_hand_score,',',suit_converted)

    # !!!!!!!!!! ОТПРАВЛЯЕМ В МОДУЛЬ НА ПРОВЕРКУ
    send_list = [ user_hand_score, suit_converted ] 
    
    checker.match_check(send_list)
    
    pass





def sort_user_hand():
    global user_hand
    user_hand = sorted(user_hand, reverse=True, key=lambda x: int(x[1]))
    #user_hand = sorted_user_hand   
    print('res:',user_hand)
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

        
        new_round()


        #print(user_hand_score)
        #print(user_hand_suit)



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

#for i in range(len(deck_list)):
    #print(deck_list[i][0][-1])

#    Empty User Hand:
user_hand = []
user_hand_score = []
user_hand_suit = []

#    Empty List for Exceptions Cards:
except_nums_list = []


#    Defoult Bet:
_user_bet = 50




#greeting(user_name, _user_bank)
greeting('Alex', 5000)


show_menu()




#          Run App:        |
run_flag = True

while run_flag == True: main()


#exit()
