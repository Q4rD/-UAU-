from random import random, randrange, randint, choice
from time import sleep
import os
clear = lambda: os.system('clear')
clear()

name = input('придумайте имя: ')
sleep(1)
clear()
print('DungeonQuest')
sleep(4)
clear()
i = 0
#repulse#
CD = 0
CDm = 2 #<--- max CD

x = 0
x2 = 1 #<--- max repulse
infx2 = x2
########
run = 0
loop = 0
loop2 = 0
loop3 = 0
uhp = 100
uhpPLUS = 0
uhpost = 0
udmg = 7
health = 3
Elvl = 1
Ulvl = 1
xp = 0
ehp = 0
edmg = 0
ehp2 = 0
edmg2 = 0
if name == '???':
    uhp = 99999
    udmg = 99999
    Ulvl = 999
while True:
    if i < 10:
        print(name,"отправился в данж...\n\n\n\n |BETA Version| [0.4v]")
        sleep(0.3)
        clear()
        print(name,"отправился в данж..\n\n\n\n |BETA Version| [0.4v]")
        sleep(0.3)
        clear()
        print(name,"отправился в данж.\n\n\n\n |BETA Version| [0.4v]")
        sleep(0.3)
        clear()
        i += 1
    elif i == 10:
        clear()
        while True:
            loop2 += 1
            #you#
            x = 0
            udmg = udmg
            infx2 = x2
            uhpmax = uhp
            if Ulvl >= 25:
                CDm = 1
            #####

            ##сундук##
            if loop == 5:
                if run > 2:
                    clear()
                    print('вы сбежали больше 2-х раз!!!\nнаграды не будет!!!')
                    sleep(3)
                    run -= run
                    loop -= 5
                    clear()
                elif run < 2 or run == 2:
                    clear()
                    print("вы нашли сундук!!!")
                    sleep(1)
                    clear()
                    print("выберите предмет:\n\n   [?] [?] [?]\n")
                    chest = input('выбор: ')
                    if chest == '1' or chest == '2' or chest == '3' :
                        c1 = randint(1, 3)
                        c2 = randint(1, 3)
                        c3 = randint(1, 3)
                        if c1 == 1 or c2 == 1 or c3 == 1:
                            item = randint(2, 7)
                            udmg += item
                            sleep(1)
                            clear()
                            print('+',item,' к атаке')
                            sleep(2)
                            clear()
                        elif c1 == 2 or c2 == 2 or c3 == 2:
                            item = randint(1, 3)
                            health += item
                            sleep(1)
                            clear()
                            print('+',item,' зелье')
                            sleep(2)
                            clear()
                        elif c1 == 3 or c2 == 3 or c3 == 3:
                            item = randint(20, 50)
                            uhp += item
                            sleep(1)
                            clear()
                            print('+',item,' к хп')
                            sleep(2)
                            clear() 
                    loop -= 5
                    run -= run
                    sleep(1)
                    clear()
                ###########

            #enemy#
            loop3 += 1
            ehp1 = randint(40, 70)
            edmg1 = randint(5, 8)

            ehp = ehp1
            edmg = edmg1
         
            #lvl up enemy
            if loop3 == 10:
                if Elvl >= 15:
                    edmg2 += 4
                    ehp2 += 5
                loop3 -= 10
                ehp2 += 20
                edmg2 += 4
                Elvl += 1
            edmg += edmg2
            ehp += ehp2
            ######
            
            #name enemy#
            if edmg < 20:
                enemy = ('гоблин', 'скелет', 'зомби')
            elif edmg > 20 and edmg <= 30:
                enemy = ('орк', 'Zemen', 'тёмный рыцарь')
            elif edmg >30 and edmg <= 50:
                enemy = ('жнец', 'лич', 'тёмный маг','страж данжа')
            elif edmg > 50 and edmg <= 100:
                enemy = ('высший лич', 'вампир', 'оборотень','тёмный маг','страж данжа','демон')
            elif edmg > 100 and edmg <= 999999:
                enemy = ('высший демон', 'демон генерал', 'проклятая душа','изгой','Нулевой','Смотритель')
            elif edmg > 999999:
                enemy = ('???','???????????','??????????????????????')
            namev1 = choice(enemy)
            ############
            print('вы встретили врага!!!')
            loop += 1
            sleep(2)
            clear()
            while ehp > 0:
                if uhp <= 0:
                    sleep(1)
                    clear()
                    print("смэрт!!!")
                    print("пройдено этажей: ",loop2)
                    sleep(1)
                    quit()
                clear()
                print('этаж: ',loop2,'\n')
                print('[статус врага:',namev1,' | lvl:',Elvl,']','\n[HP:',ehp,'] [dmg:',edmg,']')
                print('\n')
                print('\n[статус игрока:',name,' | lvl:',Ulvl,']','\n[HP:',uhp,'] [dmg: ',udmg,']\n')
                print('\n1. атака\n2. отражение\n   |откат[',CD,']\n3. зелье','[',health,']','\n4. сбежать','[',run,']','\n')
                shag = input('принять решение: ')
                ##атака##
                if shag == '1':
                    if CD > 0:
                        CD -= 1
                    elif CD == 0:
                        sleep(0.1)
                    print(name,'| атаковал!')
                    c1 = randint(1, 35)
                    if c1 == 5 or c1 == 15 or c1 == 25:
                        udmgcrit = udmg
                        udmgcrit *= 1.5
                        udmgcrit = int(udmgcrit)
                        print('(крит!)') 
                        ehp -= udmgcrit
                    else:
                        ehp -= udmg
                    sleep(0.5)
                    if shag == '1':
                        if ehp > 0:
                            print(namev1,'| атаковал!')
                            uhp -=  edmg
                            sleep(0.5)
                            clear()
                        elif ehp <= 0:
                            sleep(0.5)
                            clear()
                ###################

                ##отражение##
                elif shag == '2':
                    if CD > 0:
                        print('нет сил для отражения атаки!')
                        sleep(0.5)
                        print(namev1,'| атаковал!')
                        uhp -= edmg
                        sleep(0.5)
                        if CD > 0:
                            CD -= 1
                        elif CD == 0:
                            sleep(0.1)
                    elif CD == 0:
                        if x < x2:
                            CD += CDm #<--- настройка кд
                            print(namev1,'| атаковал!')
                            sleep(0.5)
                            if ehp > 0:
                                c1 = randint(1, 2)
                                if c1 == 5 or c1 == 15 or c1 == 25:
                                    ehp -= ehp
                                    xp1 = randint(20, 25)
                                    xp += xp1
                                    print(name,'| идеальное отражение!!!')
                                    sleep(0.5)
                                    clear()
                                    print('враг аннулирован!!!\n получено xp: +',xp1)
                                    sleep(3)
                                    clear()
                                else:
                                    edmg50 = edmg
                                    edmg50 /= 2
                                    edmg50 = int(edmg50)
                                    edmg50 = edmg50
                                    ehp-= edmg50
                                    print(name,'| отразил!')
                                    sleep(0.5)
                                    clear()
                            elif ehp < 0:
                                sleep(1)
                                clear()
                        elif x >= x2:
                            print('нет сил для отражения атаки!')
                            sleep(0.5)
                            if ehp > 0:
                                print(namev1,'| атаковал!')
                                uhp -= edmg
                                sleep(0.5)
                                clear()
                            elif ehp <= 0:
                                sleep(0.5)
                                clear()
                            if CD > 0:
                                CD -= 1
                            elif CD == 0:
                                sleep(0)
                    ###################       
                
                #зелье#
                elif shag == '3':
                    if CD > 0:
                        CD -= 1
                    elif CD == 0:
                        sleep(0.1)
                    if health == 0:
                        print('нет зельев!!!')
                        sleep(1)
                        print(namev1,'| атаковал!')
                        uhp -= edmg
                        sleep(1)
                        clear()
                    elif health > 0:
                        heal = randint(50, 80)
                        uhp += heal
                        print('использовано зелье: +',heal,'к hp')
                        health -= 1
                        sleep(1)
                        clear()
                #########

                ##бегство##
                elif shag == '4':
                    if CD > 0:
                        CD -= 1
                    elif CD == 0:
                        sleep(0.1)
                    xp1 = randint(5, 10)
                    xp += xp1
                    clear()
                    print('вы сбежали!!!\nполучено xp: ',xp1,'\nвсего xp: ',xp)
                    sleep(3)
                    clear()
                    run += 1
                    uhp1 = 0
                    uhp1 += uhp
                    uhp = uhp1
                    #random items#
                    c1 = randint(1, 50)
                    c2 = randint(1, 100)
                    if c1 == 22 or c1 == 37 or c1 == 48:
                        h = randint(1, 3)
                        health += h
                        print('вы нашли зелья: +',h)
                        sleep(3)
                        clear()
                    if c2 == 37 or c2 == 51 or c2 == 79:
                        print('вы нашли редкий сундук!!!')
                        sleep(1)
                        clear()
                        c1 = randint(5, 10)
                        c2 = randint(100, 200)
                        c3 = randint(50, 80)
                        print('выберите награду!!!\n\n1. атака [+',c1,']\n2. здоровье [+',c2,']\n3. xp [',c3,']')
                        bonus = input('ввод:')
                        if bonus == '1':
                            udmg += c1
                            print('1. атака [+',c1,']')
                            sleep(1)
                            clear()
                        elif bonus == '2':
                            print('2. здоровье [+',c2,']')
                            sleep(1)
                            clear()
                            uhp += c2
                        elif bonus == '3':
                            xp += c3
                            print('1. xp [+',c3,']')
                            sleep(1)
                            clear()
                    ###############
                    if xp >= 100:
                        xp -= xp
                        uhpPLUS = 0
                        uhpPLUS += 20
                        if Ulvl >= 15:
                            uhpPLUS * 2
                        uhpost += uhpPLUS
                        if uhp < 100:
                            uhp = 100
                            uhp += uhpost
                            uhpPLUS = 0
                        uhp += uhpPLUS
                        udmg += 2
                        Ulvl += 1
                        x2 += 1
                    x2 = x2
                    uhp = uhp
                    udmg = udmg
                    Ulvl = Ulvl
                    break
                ###############
            else:
                #random items#
                c1 = randint(1, 50)
                c2 = randint(1, 100)
                if c1 == 22 or c1 == 37 or c1 == 48:
                    h = randint(1, 3)
                    health += h
                    print('вы нашли зелья: +',h)
                    sleep(3)
                    clear()
                if c2 == 37 or c2 == 51 or c2 == 79:
                    print('вы нашли редкий сундук!!!')
                    sleep(1)
                    clear()
                    c1 = randint(5, 10)
                    c2 = randint(100, 200)
                    c3 = randint(50, 80)
                    print('выберите награду!!!\n\n1. атака [+',c1,']\n2. здоровье [+',c2,']\n3. xp [',c3,']')
                    bonus = input('ввод:')
                    if bonus == '1':
                        udmg += c1
                        print('1. атака [+',c1,']')
                        sleep(1)
                        clear()
                    elif bonus == '2':
                        print('2. здоровье [+',c2,']')
                        sleep(1)
                        clear()
                        uhp += c2
                    elif bonus == '3':
                        xp += c3
                        print('1. xp [+',c3,']')
                        sleep(1)
                        clear()
                ###############
                xp1 = randint(10, 20)
                xp += xp1
                print('враг побеждён!\n получено xp: ',xp1,'\n всего xp: ',xp)
                sleep(3)
                clear()
                uhp1 = 0
                uhp1 += uhp
                uhp = uhp1
                if xp >= 100:
                    xp -= xp
                    uhpPLUS = 0
                    uhpPLUS += 20
                    if Ulvl >= 15:
                        uhpPLUS * 2
                    uhpost += uhpPLUS
                    if uhp < 100:
                        uhp = 100
                        uhp += uhpost
                        uhpPLUS = 0
                    uhp += uhpPLUS
                    udmg += 2
                    Ulvl += 1
                    x2 += 1
                x2 = x2
                uhp = uhp
                udmg = udmg
                Ulvl = Ulvl
                break