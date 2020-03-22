import pyautogui, mouse, keyboard, random, time, threading, os
#pip install pyautogui & pip install keyboard
#Preconditions:
##Python installed with the proper libraries
##Player is in front of NPC/item
##1920x1080 resolution
##Minimum Minecraft mouse sensitivity
##Have an empty inventory
##Have money in the purse
##Have the correct crafting format
##Face forward in intervals of 90 degrees

def delayStart():
    pyautogui.alert("When you press OK, the program will start in 5 seconds. Please open Minecraft and then stand in front of the NPC/item before the 5 seconds is up. PRESS 'p' to stop the process. HAVE the default Minecraft settings on: W to walk forwards, A to strafe left, etc. Use the correct preset crafting templates! Make sure to have an empty inventory!", "Hypixel Skyblock Item Compacting v1.0") 
    time.sleep(5)
def stop():
    while True:
        if keyboard.is_pressed('p') == True:
            pyautogui.keyUp("shift")
            os._exit(1)
def buyCraft1(x, y, z): #for normal items like enchanted carrots
    #x and y are coordinates of the item, z = # of stacks requested
    #setting up for 1st slot in inventory
    stacks = int(z)
    for a in range(stacks):
        pyautogui.press("1") #to prevent clicking with nether star
        time.sleep(0.1)
        pyautogui.rightClick()#NPC interaction
        mouse.move(x, y, absolute = True, duration = 0.3) #item coords
        pyautogui.rightClick()
        mouse.move(1100, 355, absolute = True, duration = 0.1) #64 item purchase and craft Eitems coords
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 11, interval = random.uniform(0.1,0.25))
        pyautogui.press("esc")
        mouse.move(0, 10000, absolute = False, duration = 0.3)#LOOK DOWN ALL THE WAY
        time.sleep(0.1)
        pyautogui.press("9")
        pyautogui.rightClick()
        mouse.move(950, 420, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        
        #use first 10 slots to get 4 enchanted items
        mouse.move(670, 915, absolute = True, duration = 0.1) #bottom left corner
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        
        mouse.move(740, 915, absolute = True, duration = 0.1) #2nd column
        pyautogui.keyDown("shift")
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 2)
        mouse.move(1030, 340, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click() #2 eItems for this click

        mouse.move(955, 915, absolute = True, duration = 0.1) #5th column
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 2)
        
        #RUSHED, leftovers here:
        mouse.move(1030, 340, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        pyautogui.keyUp("shift")
        pyautogui.press("esc")
        mouse.move(0, -500, absolute = False, duration = 0.2)#LOOK UP

        #4 enchanted items crafted, buy (at least) 30 more stacks
        time.sleep(0.1) #prevent skip click
        pyautogui.press("1") #to prevent clicking with nether star
        time.sleep(0.1)
        pyautogui.rightClick() #NPC interaction
        mouse.move(x, y, absolute = True, duration = 0.3) #item coords
        pyautogui.rightClick()
        mouse.move(1100, 355, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 31, interval = random.uniform(0.1,0.25)) #refill inventory
        pyautogui.press("esc")
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #MOVEMENT TO PREVENT AFK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        pyautogui.keyDown("shift")
        pyautogui.keyDown("s")
        time.sleep(0.3)
        pyautogui.keyUp("s")
        pyautogui.keyUp("shift")
        
        mouse.move(0, 10000, absolute = False, duration = 0.3)#LOOK DOWN ALL THE WAY
        time.sleep(0.1)
        pyautogui.press("9")
        pyautogui.rightClick()
        mouse.move(950, 420, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        
        #start 60 enchanted item crafting
        for b in range (5): #b starts at 0, ends at 4
            if b < 4:
                mouse.move(1180, 910, absolute = True, duration = 0.1) #8th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click() #doesn't craft here
                pyautogui.keyDown("shift")
                            
                mouse.move(1100, 915, absolute = True, duration = 0.1) #7th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                            
                mouse.move(1020, 915, absolute = True, duration = 0.1) #6th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(955, 915, absolute = True, duration = 0.1) #5th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(885, 915, absolute = True, duration = 0.1) #4th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(820, 915, absolute = True, duration = 0.1) #3rd column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(740, 915, absolute = True, duration = 0.1) #2nd column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyUp("shift")
                pyautogui.press("esc")
                mouse.move(0, -500, absolute = False, duration = 0.2)#LOOK UP
                
                #12 enchanted items made at this point
                pyautogui.press("1") #to prevent clicking with nether star
                time.sleep(0.1)
                pyautogui.rightClick()#NPC interaction
                mouse.move(x, y, absolute = True, duration = 0.3) #item coords
                pyautogui.rightClick()
                mouse.move(1100, 355, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 31, interval = random.uniform(0.1,0.25))
                pyautogui.press("esc")
                mouse.move(0, 10000, absolute = False, duration = 0.3)#LOOK DOWN ALL THE WAY
                time.sleep(0.1)
                pyautogui.press("9")
                pyautogui.rightClick()
                mouse.move(950, 420, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                #last step: just craft
            if b == 4:
                mouse.move(1180, 910, absolute = True, duration = 0.1) #8th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click() #doesn't craft here
                pyautogui.keyDown("shift")
                            
                mouse.move(1100, 915, absolute = True, duration = 0.1) #7th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                            
                mouse.move(1020, 915, absolute = True, duration = 0.1) #6th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(955, 915, absolute = True, duration = 0.1) #5th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(885, 915, absolute = True, duration = 0.1) #4th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(820, 915, absolute = True, duration = 0.1) #3rd column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(740, 915, absolute = True, duration = 0.1) #2nd column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyUp("shift")
        
                mouse.move(960, 550, absolute = True, duration = 0.1) #Back arrow
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                mouse.move(1180, 340, absolute = True, duration = 0.1) #Echest
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyDown("shift")
                mouse.move(670, 840, absolute = True, duration = 0.1) #Enchanted item stack
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyUp("shift")
                
                #now reset for next loop
                pyautogui.press("esc")
                mouse.move(0, -500, absolute = False, duration = 0.2)#LOOK UP
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #MOVEMENT TO PREVENT AFK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                pyautogui.keyDown("shift")
                pyautogui.keyDown("w")
                time.sleep(0.1)
                pyautogui.keyUp("w")
                pyautogui.keyUp("shift")

def buyCraft2(x, y, z): #for enchanted string
    #x and y are coordinates of the item, z = # of stacks requested
    #setting up for 1st slot in inventory
    stacks = int(z)
    for a in range(stacks):
        pyautogui.press("1") #to prevent clicking with nether star
        time.sleep(0.1)
        pyautogui.rightClick()#NPC interaction
        mouse.move(x, y, absolute = True, duration = 0.3) #item coords
        pyautogui.rightClick()
        mouse.move(1100, 355, absolute = True, duration = 0.1) #64 item purchase and craft Eitems coords
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 13, interval = random.uniform(0.1,0.25))
        pyautogui.press("esc")
        time.sleep(0.1) #prevent skip click
        mouse.move(0, 10000, absolute = False, duration = 0.3)#LOOK DOWN ALL THE WAY
        time.sleep(0.1)
        pyautogui.press("9")
        pyautogui.rightClick()
        mouse.move(950, 420, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        #Use first 12 slots to craft 4 enchanted string
        mouse.move(670, 915, absolute = True, duration = 0.1) #bottom left corner
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        
        mouse.move(740, 915, absolute = True, duration = 0.1) #2nd column
        pyautogui.keyDown("shift")
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 2)
        mouse.move(1030, 340, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click() #2 eItems for this click

        mouse.move(880, 915, absolute = True, duration = 0.1) #4th column
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 2)
        mouse.move(1030, 340, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        pyautogui.keyUp("shift")
        pyautogui.press("esc")
        mouse.move(0, -500, absolute = False, duration = 0.2)#LOOK UP

        #4 enchanted items crafted, buy (at least) 30 more stacks
        time.sleep(0.1) #prevent skip click
        pyautogui.press("1") #to prevent clicking with nether star
        time.sleep(0.1)
        pyautogui.rightClick() #NPC interaction
        mouse.move(x, y, absolute = True, duration = 0.3) #item coords
        pyautogui.rightClick()
        mouse.move(1100, 355, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 31, interval = random.uniform(0.1,0.25)) #refill inventory
        pyautogui.press("esc")
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #MOVEMENT TO PREVENT AFK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        pyautogui.keyDown("shift")
        pyautogui.keyDown("s")
        time.sleep(0.3)
        pyautogui.keyUp("s")
        pyautogui.keyUp("shift")
        
        mouse.move(0, 10000, absolute = False, duration = 0.3)#LOOK DOWN ALL THE WAY
        time.sleep(0.1)
        pyautogui.press("9")
        pyautogui.rightClick()
        mouse.move(950, 420, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        for b in range (6): #b starts at 0, ends at 5
            if b < 5:
                mouse.move(1180, 910, absolute = True, duration = 0.1) #8th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click() #doesn't craft here
                pyautogui.keyDown("shift")
                            
                mouse.move(1100, 915, absolute = True, duration = 0.1) #7th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                            
                mouse.move(1020, 915, absolute = True, duration = 0.1) #6th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(955, 915, absolute = True, duration = 0.1) #5th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(885, 915, absolute = True, duration = 0.1) #4th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(820, 915, absolute = True, duration = 0.1) #3rd column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                pyautogui.keyUp("shift") #to place last slot
                mouse.move(885, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click() #puts in LAST SLOT
                pyautogui.keyDown("shift")
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyUp("shift")
                pyautogui.press("esc")
                mouse.move(0, -500, absolute = False, duration = 0.2)#LOOK UP

                #10 enchanted items made at this point
                pyautogui.press("1") #to prevent clicking with nether star
                time.sleep(0.1)
                pyautogui.rightClick()#NPC interaction
                mouse.move(x, y, absolute = True, duration = 0.3) #item coords
                pyautogui.rightClick()
                mouse.move(1100, 355, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 31, interval = random.uniform(0.1,0.25))
                pyautogui.press("esc")
                mouse.move(0, 10000, absolute = False, duration = 0.3)#LOOK DOWN ALL THE WAY
                time.sleep(0.1)
                pyautogui.press("9")
                pyautogui.rightClick()
                mouse.move(950, 420, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
            if b == 5:
                mouse.move(1180, 910, absolute = True, duration = 0.1) #8th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click() #doesn't craft here
                pyautogui.keyDown("shift")
                            
                mouse.move(1100, 915, absolute = True, duration = 0.1) #7th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                            
                mouse.move(1020, 915, absolute = True, duration = 0.1) #6th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(955, 915, absolute = True, duration = 0.1) #5th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(885, 915, absolute = True, duration = 0.1) #4th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(820, 915, absolute = True, duration = 0.1) #3rd column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                pyautogui.keyUp("shift") #to place last slot
                mouse.move(885, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click() #puts in LAST SLOT
                pyautogui.keyDown("shift")
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyUp("shift")
                mouse.move(960, 550, absolute = True, duration = 0.1) #Back arrow
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                mouse.move(1180, 340, absolute = True, duration = 0.1) #Echest
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyDown("shift")
                mouse.move(670, 840, absolute = True, duration = 0.1) #Enchanted item stack
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyUp("shift")
                
                #now reset for next loop
                pyautogui.press("esc")
                mouse.move(0, -500, absolute = False, duration = 0.2)#LOOK UP
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #MOVEMENT TO PREVENT AFK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                pyautogui.keyDown("shift")
                pyautogui.keyDown("w")
                time.sleep(0.1)
                pyautogui.keyUp("w")
                pyautogui.keyUp("shift")

def buyCraft3(x, y, z): #for enchanted hay bales
    #x and y are coordinates of the item, z = # of ITEMS requested
    #setting up for 1st slot in inventory
    #NOTE: WILL CRAFT 1 ENCHANTED HAY BALE AT A TIME
    stacks = int(z)
    for a in range(stacks):
    
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #MOVEMENT TO PREVENT AFK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        pyautogui.keyDown("shift")
        pyautogui.keyDown("w")
        time.sleep(0.1)
        pyautogui.keyUp("w")
        pyautogui.keyUp("shift")
        
        pyautogui.press("1") #to prevent clicking with nether star
        time.sleep(0.1)
        pyautogui.rightClick()#NPC interaction
        mouse.move(x, y, absolute = True, duration = 0.3) #item coords
        pyautogui.rightClick()
        mouse.move(1100, 355, absolute = True, duration = 0.1) #64 item purchase and craft Eitems coords
        time.sleep(0.1) #prevent skip click
        #20 stacks + 16 wheat
        pyautogui.click(clicks = 20, interval = random.uniform(0.6,0.8))
        mouse.move(955, 335, absolute = True, duration = 0.1)
        time.sleep(0.3) #prevent skip click
        pyautogui.click()
        mouse.move(890, 335, absolute = True, duration = 0.1)
        time.sleep(0.3) #prevent skip click
        pyautogui.click()
        mouse.move(815, 335, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        
        pyautogui.press("esc")
        mouse.move(0, 10000, absolute = False, duration = 0.3)#LOOK DOWN ALL THE WAY
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #MOVEMENT TO PREVENT AFK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        pyautogui.keyDown("shift")
        pyautogui.keyDown("s")
        time.sleep(0.3)
        pyautogui.keyUp("s")
        pyautogui.keyUp("shift")
        
        time.sleep(0.1)
        pyautogui.press("9")
        pyautogui.rightClick()
        mouse.move(950, 420, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        mouse.move(670, 915, absolute = True, duration = 0.1) #bottom left corner
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        
        mouse.move(740, 915, absolute = True, duration = 0.1) #2nd column
        pyautogui.keyDown("shift")
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 2)
        mouse.move(1030, 340, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click() #64 hay bales for this click

        mouse.move(820, 915, absolute = True, duration = 0.1) #3rd column
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 2)
        mouse.move(1030, 340, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click() #64 hay bales for this click
        pyautogui.keyUp("shift") 

        mouse.move(1020, 915, absolute = True, duration = 0.1) #6th column
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        time.sleep(0.1) #prevent skip click
        pyautogui.keyDown("shift")
        pyautogui.click()
        mouse.move(1100, 915, absolute = True, duration = 0.1) #7th column
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        mouse.move(1180, 910, absolute = True, duration = 0.1) #8th column
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        pyautogui.keyUp("shift")

        mouse.move(740, 270, absolute = True, duration = 0.1) #Top left crafting
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(740, 340, absolute = True, duration = 0.1) #lower row
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(740, 410, absolute = True, duration = 0.1) #lower row
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        mouse.move(810, 270, absolute = True, duration = 0.1) #Row 1, column 2
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(810, 340, absolute = True, duration = 0.1) #lower row
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(810, 410, absolute = True, duration = 0.1) #lower row
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        mouse.move(740, 270, absolute = True, duration = 0.1) #Top left crafting
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(890, 340, absolute = True, duration = 0.1) #Row 2, column 3
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        mouse.move(810, 270, absolute = True, duration = 0.1) #Row 1, column 2
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(890, 410, absolute = True, duration = 0.1) #Row 3, column 3
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        mouse.move(1030, 340, absolute = True, duration = 0.1)
        pyautogui.keyDown("shift")
        time.sleep(0.1) #prevent skip click
        pyautogui.click() #16 hay bales for this click
        
        mouse.move(670, 915, absolute = True, duration = 0.1) #bottom left corner
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        mouse.move(740, 915, absolute = True, duration = 0.1) #2nd column
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        
        mouse.move(820, 915, absolute = True, duration = 0.1) #3rd column
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        pyautogui.keyUp("shift")
        mouse.move(740, 270, absolute = True, duration = 0.1) #Top left crafting
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(740, 340, absolute = True, duration = 0.1) #lower row
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(740, 410, absolute = True, duration = 0.1) #lower row
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        mouse.move(810, 270, absolute = True, duration = 0.1) #Row 1, column 2
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(810, 340, absolute = True, duration = 0.1) #lower row
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(810, 410, absolute = True, duration = 0.1) #lower row
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        mouse.move(740, 270, absolute = True, duration = 0.1) #Top left crafting
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(890, 340, absolute = True, duration = 0.1) #Row 2, column 3
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        mouse.move(810, 270, absolute = True, duration = 0.1) #Row 1, column 2
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(890, 410, absolute = True, duration = 0.1) #Row 3, column 3
        time.sleep(0.1) #prevent skip click
        pyautogui.click()

        mouse.move(1030, 340, absolute = True, duration = 0.1)
        pyautogui.keyDown("shift")
        time.sleep(0.1) #prevent skip click
        pyautogui.click() #Craft 1 enchanted hay bale

        pyautogui.keyUp("shift")
        mouse.move(960, 550, absolute = True, duration = 0.1) #Back arrow
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        mouse.move(1180, 340, absolute = True, duration = 0.1) #Echest
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        pyautogui.keyDown("shift")
        mouse.move(670, 840, absolute = True, duration = 0.1) #Enchanted item 
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        pyautogui.keyUp("shift")
        
        #now reset for next loop
        pyautogui.press("esc")
        mouse.move(0, -500, absolute = False, duration = 0.2)#LOOK UP
        

    
def buyCraft4(z): #for end shop items
    #z = # of stacks requested
    #setting up for 1st slot in inventory
    #NOTE: WILL SKIP SOME STEPS
    stacks = int(z)
    for a in range(stacks):
        pyautogui.press("1") #to prevent clicking with nether star
        time.sleep(0.1)
        pyautogui.rightClick()#End shop open
        mouse.move(955, 340, absolute = True, duration = 0.1) #Item
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(1100, 355, absolute = True, duration = 0.1) #64 items
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 11, interval = random.uniform(0.1,0.25))
        pyautogui.press("esc")
        mouse.move(0, 10000, absolute = False, duration = 0.3)#LOOK DOWN ALL THE WAY
        time.sleep(0.1)
        pyautogui.press("9")
        pyautogui.rightClick()
        mouse.move(950, 420, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        
        #use first 10 slots to get 4 enchanted items
        mouse.move(670, 915, absolute = True, duration = 0.1) #bottom left corner
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        
        mouse.move(740, 915, absolute = True, duration = 0.1) #2nd column
        pyautogui.keyDown("shift")
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 2)
        mouse.move(1030, 340, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click() #2 eItems for this click

        mouse.move(955, 915, absolute = True, duration = 0.1) #5th column
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 2)
        
        #RUSHED, leftovers here:
        mouse.move(1030, 340, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        pyautogui.keyUp("shift")
        pyautogui.press("esc")
        mouse.move(0, -500, absolute = False, duration = 0.2)#LOOK UP

        #4 enchanted items crafted, buy (at least) 30 more stacks
        time.sleep(0.1) #prevent skip click
        pyautogui.press("1") #to prevent clicking with nether star
        time.sleep(0.1)
        pyautogui.rightClick()#End shop open
        mouse.move(955, 340, absolute = True, duration = 0.1) #Item
        time.sleep(0.1) #prevent skip click
        pyautogui.rightClick()
        mouse.move(1100, 355, absolute = True, duration = 0.1) #64 items
        time.sleep(0.1) #prevent skip click
        pyautogui.click(clicks = 31, interval = random.uniform(0.1,0.25)) #refill inventory
        pyautogui.press("esc")
        
        mouse.move(0, 10000, absolute = False, duration = 0.3)#LOOK DOWN ALL THE WAY
        time.sleep(0.1)
        pyautogui.press("9")
        pyautogui.rightClick()
        mouse.move(950, 420, absolute = True, duration = 0.1)
        time.sleep(0.1) #prevent skip click
        pyautogui.click()
        
        #start 60 enchanted item crafting
        for b in range (5): #b starts at 0, ends at 4
            if b < 4:
                mouse.move(1180, 910, absolute = True, duration = 0.1) #8th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click() #doesn't craft here
                pyautogui.keyDown("shift")
                            
                mouse.move(1100, 915, absolute = True, duration = 0.1) #7th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                            
                mouse.move(1020, 915, absolute = True, duration = 0.1) #6th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(955, 915, absolute = True, duration = 0.1) #5th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(885, 915, absolute = True, duration = 0.1) #4th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(820, 915, absolute = True, duration = 0.1) #3rd column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(740, 915, absolute = True, duration = 0.1) #2nd column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyUp("shift")
                pyautogui.press("esc")
                mouse.move(0, -500, absolute = False, duration = 0.2)#LOOK UP
                
                #12 enchanted items made at this point
                pyautogui.press("1") #to prevent clicking with nether star
                time.sleep(0.1)
                pyautogui.rightClick()#End shop open
                mouse.move(955, 340, absolute = True, duration = 0.1) #Item
                time.sleep(0.1) #prevent skip click
                pyautogui.rightClick()
                mouse.move(1100, 355, absolute = True, duration = 0.1) #64 items
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 31, interval = random.uniform(0.1,0.25))
                pyautogui.press("esc")
                mouse.move(0, 10000, absolute = False, duration = 0.3)#LOOK DOWN ALL THE WAY
                time.sleep(0.1)
                pyautogui.press("9")
                pyautogui.rightClick()
                mouse.move(950, 420, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                #last step: just craft
            if b == 4:
                mouse.move(1180, 910, absolute = True, duration = 0.1) #8th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click() #doesn't craft here
                pyautogui.keyDown("shift")
                            
                mouse.move(1100, 915, absolute = True, duration = 0.1) #7th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                            
                mouse.move(1020, 915, absolute = True, duration = 0.1) #6th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(955, 915, absolute = True, duration = 0.1) #5th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(885, 915, absolute = True, duration = 0.1) #4th column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(820, 915, absolute = True, duration = 0.1) #3rd column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()

                mouse.move(740, 915, absolute = True, duration = 0.1) #2nd column
                time.sleep(0.1) #prevent skip click
                pyautogui.click(clicks = 2)
                mouse.move(1030, 340, absolute = True, duration = 0.1)
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyUp("shift")
        
                mouse.move(960, 550, absolute = True, duration = 0.1) #Back arrow
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                mouse.move(1180, 340, absolute = True, duration = 0.1) #Echest
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyDown("shift")
                mouse.move(670, 840, absolute = True, duration = 0.1) #Enchanted item stack
                time.sleep(0.1) #prevent skip click
                pyautogui.click()
                pyautogui.keyUp("shift")
                
                #now reset for next loop
                pyautogui.press("esc")
                mouse.move(0, -500, absolute = False, duration = 0.2)#LOOK UP
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #MOVEMENT TO PREVENT AFK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                pyautogui.keyDown("s")
                time.sleep(0.1)
                pyautogui.keyUp("s")
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #MOVEMENT TO PREVENT AFK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                pyautogui.keyDown("w")
                time.sleep(0.3)
                pyautogui.keyUp("w")
  

pyautogui.alert("Do you want to aquire NPC items and craft them into their respective enchanted items? I have the solution for you!", "Hypixel Skyblock Item Compacting v1.0", "OK")
npc = pyautogui.prompt(" Enter 1 for Lumber Merchant\n Enter 2 for Adventurer\n Enter 3 for Fish Merchant\n Enter 4 for Farm Merchant\n Enter 5 for Mine Merchant\n Enter 6 for Iron Forager\n Enter 7 for Gold Forager\n Enter 8 for End Shop\n Enter 9 for Alchemist\n Enter 10 for Pat", "Hypixel Skyblock Item Compacting v1.0") 
if npc != "1" and npc != "2" and npc != "3" and npc != "4" and npc != "5" and npc != "6" and npc != "7" and npc != "8" and npc != "9" and npc != "10":
        pyautogui.alert(text='Invalid input!', title='Hypixel Skyblock Item Compacting v1.0', button='OK')
        os._exit(1)
t1 = threading.Thread(target = stop)
#format: get npc #, then item # and stack #, finally delayStart() and t1.start() and some form of buyCraft 

if npc == "1": #Lumber Merchant
    item = pyautogui.prompt(" Enter 1 for Oak Log\n Enter 2 for Birch Log\n Enter 3 for Spruce Log\n Enter 4 for Dark Oak Log\n Enter 5 for Acacia Log\n Enter 6 for Jungle Log", "Hypixel Skyblock Item Compacting v1.0") 
    if item != "1" and item != "2" and item != "3" and item != "4" and item != "5" and item != "6":
        pyautogui.alert(text='Invalid input!', title='Hypixel Skyblock Item Compacting v1.0', button='OK')
        os._exit(1)
    stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
        
    if item == "1": #Oak
        delayStart()
        t1.start()
        buyCraft1(740, 270, stacks)
                    
    elif item == "2": #Birch
        delayStart()
        t1.start()
        buyCraft1(820, 270, stacks)

    elif item == "3": #Spruce
        delayStart()
        t1.start()
        buyCraft1(880, 270, stacks)

    elif item == "4": #Dark Oak
        delayStart()
        t1.start()
        buyCraft1(960, 270, stacks)

    elif item == "5": #Acacia 
        delayStart()
        t1.start()
        buyCraft1(1030, 270, stacks)

    elif item == "6": #Jungle
        delayStart()
        t1.start()
        buyCraft1(1100, 270, stacks)


elif npc == "2": #Adventurer 
    item = pyautogui.prompt(" Enter 1 for Rotten Flesh\n Enter 2 for Bone\n Enter 3 for String\n Enter 4 for Slime\n Enter 5 for Gunpowder")
    if item != "1" and item != "2" and item != "3" and item != "4" and item != "5":
        pyautogui.alert(text='Invalid input!', title='Hypixel Skyblock Item Compacting v1.0', button='OK')
        os._exit(1)
    stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
        
    if item == "1": #Rotten Flesh
        delayStart()
        t1.start()
        buyCraft1(740, 270, stacks)

    elif item == "2": #Bone
        delayStart()
        t1.start()
        buyCraft1(820, 270, stacks)

    elif item == "3": #String, CUSTOM
        delayStart()
        t1.start()
        buyCraft2(880, 270, stacks)

    elif item == "4": #Slime
        delayStart()
        t1.start()
        buyCraft1(960, 270, stacks)

    elif item == "5": #Gunpowder
        delayStart()
        t1.start()
        buyCraft1(1030, 270, stacks)


elif npc == "3": #Fish Merchant
    item = pyautogui.prompt(" Enter 1 for Raw Fish\n Enter 2 for Raw Salmon")
    if item != "1" and item != "2":
        pyautogui.alert(text='Invalid input!', title='Hypixel Skyblock Item Compacting v1.0', button='OK')
        os._exit(1)
    stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")

    if item == "1": #Raw Fish
        delayStart()
        t1.start()
        buyCraft1(820, 270, stacks)

    elif item == "2": #Raw Salmon
        delayStart()
        t1.start()
        buyCraft1(880, 270, stacks)


elif npc == "4": #Farm Merchant
    item = pyautogui.prompt(" Enter 1 for Wheat\n Enter 2 for Carrot\n Enter 3 for Potato\n Enter 4 for Melon\n Enter 5 for Sugarcane\n Enter 6 for Pumpkin\n Enter 7 for Cocoa Beans\n Enter 8 for Red Mushroom\n Enter 9 for Sand")
    if item != "1" and item != "2" and item != "3" and item != "4" and item != "5" and item != "6" and item != "7" and item != "8" and item != "9":
        pyautogui.alert(text='Invalid input!', title='Hypixel Skyblock Item Compacting v1.0', button='OK')
        os._exit(1)

    if item == "1": #Wheat
        wheatAmount = pyautogui.prompt(" Enter the number (NOT STACKS) of enchanted hay number to order: ", "Hypixel Skyblock Item Compacting v1.0")
        delayStart()
        t1.start()
        buyCraft3(740, 270, wheatAmount)
        
    elif item == "2": #Carrot
        stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
        delayStart()
        t1.start()
        buyCraft1(820, 270, stacks)

    elif item == "3": #Potato
        stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
        delayStart()
        t1.start()
        buyCraft1(880, 270, stacks)

    elif item == "4": #Melon
        stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
        delayStart()
        t1.start()
        buyCraft1(960, 270, stacks)

    elif item == "5": #Sugarcane
        stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
        delayStart()
        t1.start()
        buyCraft1(1030, 270, stacks)

    elif item == "6": #Pumpkin
        stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
        delayStart()
        t1.start()
        buyCraft1(1100, 270, stacks)

    elif item == "7": #Cocoa Beans
        stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
        delayStart()
        t1.start()
        buyCraft1(1175, 270, stacks)

    elif item == "8": #Red Mushroom
        stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
        delayStart()
        t1.start()
        buyCraft1(740, 335, stacks)

    elif item == "9": #Sand
        stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
        delayStart()
        t1.start()
        buyCraft1(890, 335, stacks)


elif npc == "5": #Mine Merchant 
    item = pyautogui.prompt(" Enter 1 for Coal\n Enter 2 for Cobblestone")
    if item != "1" and item != "2":
        pyautogui.alert(text='Invalid input!', title='Hypixel Skyblock Item Compacting v1.0', button='OK')
        os._exit(1)
    stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")

    if item == "1": #Coal
        delayStart()
        t1.start()
        buyCraft1(740, 270, stacks)

    elif item == "2": #Cobblestone
        delayStart()
        t1.start()
        buyCraft1(815, 340, stacks)


elif npc == "6": #Iron Forager 
    stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
    delayStart()
    t1.start()
    buyCraft1(820, 270, stacks)


elif npc == "7": #Gold Forager 
    stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")
    delayStart()
    t1.start()
    buyCraft1(740, 270, stacks)


elif npc == "8": #End Shop 
    item = pyautogui.prompt(" Enter 1 for End Stone\n Enter 2 for Obsidian")
    if item != "1" and item != "2":
        pyautogui.alert(text='Invalid input!', title='Hypixel Skyblock Item Compacting v1.0', button='OK')
        os._exit(1)
    stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")

    if item == "1": #End Stone
        delayStart()
        t1.start()
        buyCraft4(stacks)

    elif item == "2": #Obsidian
        delayStart()
        t1.start()
        buyCraft4(stacks)
    

elif npc == "9": #Alchemist
    item = pyautogui.prompt(" Enter 1 for Nether Wart\n Enter 2 for Rabbit Foot\n Enter 3 for Spider Eye\n Enter 4 for Magma Cream")
    if item != "1" and item != "2" and item != "3" and item != "4":
        pyautogui.alert(text='Invalid input!', title='Hypixel Skyblock Item Compacting v1.0', button='OK')
        os._exit(1)
    stacks = pyautogui.prompt(" Enter the number of enchanted stacks to order: ", "Hypixel Skyblock Item Compacting v1.0")

    if item == "1": #Nether Wart
        delayStart()
        t1.start()
        buyCraft1(740, 270, stacks)

    elif item == "2": #Rabbit Foot
        delayStart()
        t1.start()
        buyCraft1(1100, 270, stacks)

    elif item == "3": #Spider Eye
        delayStart()
        t1.start()
        buyCraft1(740, 335, stacks)

    elif item == "4": #Magma Cream
        delayStart()
        t1.start()
        buyCraft1(960, 335, stacks)

elif npc == "10": #Pat
    stacks = pyautogui.prompt(" Enter the number of enchanted stacks of flint to order: ", "Hypixel Skyblock Item Compacting v1.0")
    delayStart()
    t1.start()
    buyCraft1(740, 270, stacks)

