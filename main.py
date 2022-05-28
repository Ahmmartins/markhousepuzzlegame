print("welcome to the house puzzle game")
print("your mission is to find the way to marks house from prince house")
task_1 = input("from prince compound junction take 'left' or 'right' to main junction").lower()
if task_1 == 'right':
    task_2 = input("you are correct. from junction , type 'keke'  or 'trek' to plaza" ).lower()
    if task_2 == 'keke':
        task_3 = input("from plaza, type 'keke' or 'bus' to water fountain")
        if task_3 == 'bus':
            task_4 = input("from fountain,type 'keke' or 'trek' to his junction")
            if task_4 == 'keke':
                task_5 = input("from his junction, type 'left' or 'right' to enter").lower()
                if task_5 == 'left':
                    task_6 = input("from street are you to take the second street by 'left' or 'right'").lower()
                    if task_6 == 'right':
                        task_7 = input("from the end of that junction, take 'left' or 'right' ")
                        if task_7 == 'left':
                            task_8 = input(" youre alost there.from that point type  's' to go straight or 'r' to go right" ).lower()
                            if task_8 == 'r':
                                task_9 = input("from there type 'l' to take next left or 's' to continue going straight").lower()
                                if task_9 == 'l':
                                    task_10 = input("from that street type 'one' for gate1 or 'two' for gate2 ")
                                    if task_10 == 'one':
                                        print("you have arrived marks house.you have won 5 bitcoin")
                                    else:
                                        print("sorry . you lost. try again next time")
                                else: print("you are wrong. game over")

                            else:print("you are going to senators house .game over")

                        else:
                            print(" you have missed it. game over")
                    else:
                        print("sorry you missed it. game over")
                else:
                    print("you have missed it. start over again")

            else:
                print("you are wrong. game over")
        else:
            print("sorry keke are not allowed from plaza to water fountain.you lost.start again")

    else:
        print("you will suffer. game over")
else:
    print("game over . start cover again")

