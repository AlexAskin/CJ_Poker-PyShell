import random


coups = 0


STRAIGHT_comb = [
[1,2,3,4,5],
[2,3,4,5,6],
[3,4,5,6,7],
[4,5,6,7,8],
[5,6,7,8,9],
[6,7,8,9,10],
[7,8,9,10,11],
[8,9,10,11,12],
[9,10,11,12,13],
[1,10,11,12,13], # 10 J Q K A
]



FLUSH_comb = [
    
['a','a','a','a','a'],
['b','b','b','b','b'],
['c','c','c','c','c'],
['d','d','d','d','d'],

]

straight_check = 0

#-----------CHECK FUNCTION-------------
def match_check(some_list):
    global coups, straight_check

    #print(some_list)
    masti = some_list[1]
    some_list = some_list[0]




        
    some_list.sort()
    
    card_list = some_list
    matches_dict = {}
    matches = 0
    index = 0


    flush_detected_flag = False

    if masti in FLUSH_comb:
        #print('FLUSH! in...', masti)
        flush_detected_flag = True

    

    if some_list in STRAIGHT_comb and flush_detected_flag == False:

        
        
        print('\n','!'*50)
        print('!'*50)
        
        print(some_list)
        
        print(masti)
        
        print('!!! STRAIGHT !!!' * 3)

        print(' Wins Bet x4 ') 

        print('!'*50)
        print('!'*50,'\n')

        coups += 1
        print('coups:', coups)
        straight_check += 1
        
    elif some_list in STRAIGHT_comb and flush_detected_flag == True:


        
        print()
        print('!'*50)
        print('!'*50)
        
        print(some_list)
        
        print(masti)

        if some_list == STRAIGHT_comb[9]:
            print('!!! ROYAL FLUSH!!!' * 3)
            print(' Wins Bet x800 ')
            
        else:
        
            print('!!! STRAIGHT FLUSH!!!' * 3)

            print(' Wins Bet x50 ') 



        print('!'*50)
        print('!'*50)
        print()
        
        coups += 1
        print('coups:', coups)
        straight_check += 1


    fullhouse_flag = False    
    for item in card_list:
        #print(item, index)
        for j in card_list:
            if item == j:
                matches+=1

                
            #if matches > 1 and item > 10  or matches > 1 and item == 1 or matches > 2:
                #matches_dict[item] = matches

            # Тонкая настройка условий!:

            if matches > 1 and item > 1  or matches > 1 and item == 1: # and item > 10
                matches_dict[item] = matches
                
            if matches > 2:
                matches_dict[item] = matches

            
        matches = 0
        index += 1

    if (matches_dict):

        
        if len(matches_dict) == 1: #!!!!!!!!!!!!!!!!1
            for i in matches_dict:
                #print(i, matches_dict[i])

                if i == 13:nick = 'Kings'
                elif i == 12: nick = 'Queens'
                elif i == 11: nick = 'Jacks'
                elif i == 1: nick = 'Aces'
                else: nick = i


                if matches_dict[i] == 2 and i > 10:
                  
                    print(some_list,'=',matches_dict,f'одна пара (вальты и выше) - "{nick}" x1')

                    
                if matches_dict[i] == 3:
                    
                    print('\n',some_list,'=',matches_dict, f'ТРОЙКА - "{nick}"! TRIPS x3','\n')

                    
                if matches_dict[i] == 4:
                    
                    
                    print('\n\n',some_list,'=',matches_dict, f'!!! ЧЕТВЕРКА - "{nick}" KARE!!! x25','\n\n')
                    


        if len(matches_dict) == 2:

                    
                   

                    step = 0
                    detect=''
                    for i in matches_dict:
                        step += 1

                        if step == 1:
                            if i == 13: nick1 = 'Kings'
                            elif i == 12: nick1 = 'Queens'
                            elif i == 11: nick1 = 'Jacks'
                            elif i == 1: nick1 = 'Aces'
                            else: nick1 = i
                            
                        if step == 2:
                            if i == 13: nick2 = 'Kings'
                            elif i == 12: nick2 = 'Queens'
                            elif i == 11: nick2 = 'Jacks'
                            elif i == 1: nick2 = 'Aces'
                            else: nick2 = i                        

                        
                        #print( i, matches_dict[i] )
                        
                        if matches_dict[i] == 3:
                            fullhouse_flag = True

                    step = 0
                    for i in matches_dict:
                        step += 1
                        if matches_dict[i] == 3:
                            if step == 1: detect = f'{nick1} is Triple and {nick2} is Pair'
                            if step == 2: detect = f'{nick2} is Triple and {nick1} is Pair'
                            


                    if fullhouse_flag:
                        
                        print('-'*30)
                        print('\n\n', some_list,'=',matches_dict, f'!!! FULL HOUSE {detect}!!! x8','\n\n')
                        print('-'*30)
                        
                    else:
                        print('',some_list,'=',matches_dict, f'!!! ДВЕ ПАРЫ {nick1} & {nick2}!!! x2')
                        
                        
                           
                    
        if matches_dict[i] == 2 and i > 10 or matches_dict[i] > 2 or  fullhouse_flag or len(matches_dict) == 2:        
                        
            coups += 1
            print('coups:', coups)
    
#______________________________________


#card_list1 = [2,11,8,8,2]

#pool_lists = []
#masti_lists = []
#pool_and_masti_lists = []

#num = 1




#print('\n')

#match_check([[1,10,11,12,13],['a','a','a','a','a']])



#a_list = [[13, 3, 2, 2, 2] , ['b', 'b', 'd', 'b', 'c']]


#match_check(a_list)


