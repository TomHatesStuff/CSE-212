# 1. Name:
#      Luke Marshall
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      Purchase houses and a hotel on the properties.
# 4. What was the hardest part? Be as specific as possible.
#     The hardest part of this was the submission the time on the video is hard to get.
# 5. How long did it take for you to complete the assignment?
#      4 Hours
#first prompts
def monopoly_property_purchase():
    print ("Hello Welcome to Monopoly! If you are trying to purchase a hotel for Pensylvania AVE then look no further, all you need to do is answer a few questions.")
    color_group = input ("Do you own all the green properties? (y/n)")
    # color prompt
    if color_group == ("y") :
            PA = int(input("What is on Pensylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel)"))
            if PA == (5):
                print("You cannot purchase a hotel if the property already has one.")
            elif PA in (0,1,2,3,4):
                NC = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel)"))
                if NC == (5):
                    print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
                elif NC in (0,1,2,3,4):
                    PC = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel)"))
                    if PC == (5):
                        print ("Swap Pacific's hotel with Pennsylvania's 4 houses.")
                    elif PC in (0,1,2,3,4):
                         houses_hotels (PA,NC,PC)
                    else:
                        print("Invalid input.")
                else:
                    print("Invalid input.")
            else:
                print("Invalid input.") 
    elif color_group == ("n"):
            print ("You cannot purchase a hotel until you own all the properties of a given color group.")
    else:
        print ("Invalid input")
# this is now to calculate all prices and how many houses on each property
def houses_hotels(PA,NC,PC):
    hotels = int(input("How many hotels are there to purchase?"))
    houses_total = PA+NC+PC

    PC_HN = (5) - PC
    PA_HN = (5) - PC
    NC_HN = (5) - PC
    PC_HP = PA_HN * 200
    NC_HP = NC_HN * 200
    PA_HP = PC_HN * 200
    price_PA_PC = (PC_HP + PA_HP)
    total_H = (PA_HN + NC_HN + PC_HN + 1)
    total_H_PA_PC = (PA_HN + PC_HN)
    

    price = ((15*200) - (houses_total * 200))
    # begin if statement for final print
    if hotels > (0):
        cash = int(input("How much cash do you have to spend? "))
        if cash >= price:
            houses = int(input("How many houses are there to purchase? "))
            if houses > (0):
                if NC_HN > 0 :
                    print (f"This will cost ${price:,.2f} \nPurchase 1 hotel and {total_H} house(s). \nPut 1 hotel on Pennsylvania and return any houses to the bank. \nPut {NC_HN} house(s) on North Carolina. \nPut {PC_HN} house(s) on Pacific.")
                elif PC_HN > 0 :
                    print (f"This will cost ${price_PA_PC:,.2f}. \nPurchase 1 hotel and {total_H_PA_PC} house(s). \nPut 1 hotel on Pennsylvania and return any houses to the bank. \nPut {PC_HN} house(s) on Pacific.")
                else:
                    print ("something went wrong")
        elif cash < price:
            print ("You do not have sufficient funds to purchase a hotel at this time.")
    elif hotels == (0):
        print("There are not enough hotels available for purchase at this time.")
        
    else:
        ("invalid input")
      
    
monopoly_property_purchase()