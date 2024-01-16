# the fire burn the Earth | the water put off fire

# | the Earth absorbs the water.

# those three elements will affect you or your enemy based on who has what.

# also if you chose to train you will train but if you chose to

# train again a message will appear saying you are strong enough.

# the same thing happens for the other two options

# (going to the temple or fighting when you are strong).

# if you are not strong you can't go to the temple of elements.

# if you are strong you still can't

# fight the dragon but you can go to the temple of elements.

import time
import random
before = []


def pau(message):  # a function for printing then pause
    print(message + "\n")
    time.sleep(3)


dragon = []
dragon.append(random.choice(["Fire", "Water", "Earth"]))


def choice(stat, option1, option2, option3):
    # a function to detect valid inputs
    while True:
        response = input(stat).lower()
        if option1 in response:
            break
        if option2 in response:
            break
        if option3 in response:
            break
        else:
            pau("You have to do something")
    return response


def play_again():  # a function to check if player wants to play again
    before.clear()
    response = choice("Do you want to play again ?\n"
                      "You may find another dragon that require another"
                      "way to beat it\n"
                      "type (yes) to play again or (no) to exit\n",
                      "yes", "no", "smth")
    if "yes" in response:
        pau("Focus on the dragon's power so you can choose the "
            "right element")
        pau("Restarting the game...")
        dragon.clear()
        dragon.append(random.choice(["Fire", "Water", "Earth"]))
        play_game()
    if "no" in response:
        exit()
    else:
        pau("Please type yes or no")
        play_again()


def the_fight():
    # a function for the fight that happen between you and the dragon
    pau("Once you enterd your village")
    pau("the dragon attacked you")
    if "Fire" in dragon:
        pau("The fire dragon attacked you with flames of fire but")
        if "1" in before:
            pau("You threw flames into the dragon's "
                "flames and the flames vanished each other")
            pau("It seems like your flames are "
                "much stronger than the dragon flames")
            pau("You think this happens because the ULTIMATE power of fire")
            pau("The dragon tried to attack again but you were prepared")
            pau("You threw flames with all you got of "
                "power against the dragon's flames")
            pau("It seems like you are winning")
            pau("The dragon was hit with your flames "
                "and it seems like it is stunned")
            pau("You attacked the dragon right "
                "in his heart and ended his life")
            pau("Congratulations!, you beated the dragon and won the game")
            play_again()
        elif "2" in before:
            pau("You sent waves of water into his flames that "
                "immediately made his flames like nothing")
            pau("It seems like you chose the "
                "right element to fight the dragon")
            pau("You attacked the dragon with another wave of water")
            pau("Once the attack reached the dragon "
                "the dragon became so weak")
            pau("You attacked the dragon right "
                "in his heart and ended his life")
            pau("Congratulations!, you beated the dragon and won the game")
            play_again()
        elif "3" in before:
            pau("You tried to shield yourself with "
                "the growing plants around you")
            pau("the dragon's flames burnt your plants")
            pau("It seems like you chose the wrong "
                "element to fight the dragon")
            pau("when you try to use the power of your "
                "element the dragon burn it")
            pau("You can't fight this kind of dragons "
                "with an element like this")
            pau("Eventually, you became so weak and the dragon defeated you")
            pau("You lost the fight and failed your father and your people")
            play_again()
    elif "Water" in dragon:
        pau("The water dragon attacked you with huge waves of water but")
        if "1" in before:
            pau("You threw flames into the dragon's waves of water")
            pau("It seems like his water attack has put off your flames")
            pau("When the dragon attacked again you "
                "tried to resist with your power")
            pau("But the same thing happened again")
            pau("It seems like you chose the wrong "
                "element to fight the dragon")
            pau("You can't fight this kind of dragons "
                "with an element like this")
            pau("Eventually, you became so weak and the dragon defeated you")
            pau("You lost the fight and failed your father and your people")
            play_again()
        elif "2" in before:
            pau("You sent a huge wave of water too into the dragon's attack")
            pau("It seems like your waves are much "
                "stronger than the dragon's waves")
            pau("You think this happens because the ULTIMATE power of water")
            pau("The dragon tried to attack again but you were prepared")
            pau("You threw huge water waves with all you "
                "got of power against the dragon's waves")
            pau("It seems like you are winning")
            pau("The dragon was hit with your water waves "
                "and it seems like it is stunned")
            pau("You attacked the dragon right in "
                "his heart and ended his life")
            pau("Congratulations!, you beated the dragon and won the game")
            play_again()
        elif "3" in before:
            pau("You ordered huge number of plants to defend you")
            pau("Your move was succesful and the plants "
                "absorbed the dragon's waves")
            pau("You attacked the dragon with a huge number of plants")
            pau("The dragon tried to attack but his attacks "
                "do nothing against your plants")
            pau("After your attack the dragon became so weak")
            pau("You attacked the dragon right in "
                "his heart and ended his life")
            pau("Congratulations!, you beated the dragon and won the game")
            play_again()
    elif "Earth" in dragon:
        pau("The dragon orderd huge number of plants to attack you")
        if "1" in before:
            pau("But you threw flames all around you that burnt "
                "any plant could come near you")
            pau("The dragon tried to attack again but you attacked "
                "him first with your flames")
            pau("The dragon can do nothing against your fire power")
            pau("It seems like you chose the right "
                "element to fight the dargon")
            pau("You threw flames right into the dragon that weaken it")
            pau("You attacked the dragon right in "
                "his heart and ended his life")
            pau("Congratulations!, you beated the dragon and won the game")
            play_again()
        elif "2" in before:
            pau("You sent a huge wave of water into his plants")
            pau("It seems like the plants have absorbed "
                "your water and your attack was useless")
            pau("You think you chose the wrong element")
            pau("After some attacks you became weak")
            pau("The dragon defeated")
            pau("You lost the fight and failed your father and your people")
            play_again()
        elif "3" in before:
            pau("You also orderd alot of plants to defend you")
            pau("It seems like your plants are much "
                "stronger than the dragon's")
            pau("You think this happened because of "
                "your ULTIMATE power of earth")
            pau("It seems like you chose the right element power")
            pau("Before the dragon could attack you again")
            pau("You created a powerful earth attack "
                "that made the dragon weak")
            pau("You attacked the dragon right "
                "in his heart and ended his life")
            pau("Congratulations!, you beated the dragon and won the game")
            play_again()


def chosen_element():  # a function to detect your chosen element
    element = choice("\"what will you choose, HERO !\"\n"
                     "1. The ULTIMATE power of fire\n"
                     "2. The ULTIMATE power of water\n"
                     "3. The ULTIMATE power of earth\n", "1", "2", "3")
    pau("Everything went white...\n")
    if element == "1":
        pau("You woke up after few moments and found yourself "
            "throwing FLAMES OF FIRE from your hand")
    if element == "2":
        pau("You woke up after few moments and found yourself "
            "throwing WAVES OF WATER from your hand")
    if element == "3":
        pau("You woke up after few moments and found yourself "
            "ordring PLANTS to grow around you")
    pau("You went back home and now you think that you "
        "are ready to fight the dragon")
    before.append(element)


def revenge_time():  # a function to detect what will you do after waking up
    response = choice("what will you do:\n"
                      "1. Train hard until you become stronger and ready\n"
                      "2. Go to the elements temple\n"
                      "3. Pick up your sword and "
                      "face that dragon\n", "1", "2", "3")
    if response == "1":
        if "power" in before:
            pau("You are already strong enough")
            pau("You also have a power of an element from the elements temple")
            pau("You think you are strong enough to fight the dragon")
            revenge_time()
        if "strong" in before and "power" not in before:
            pau("You are already strong enough")
            pau("But you think you should check the "
                "temple your father talked about")
            revenge_time
        if "strong" not in before:
            pau("You trained hard for 2 years like a hero")
            pau("Motivated by your father's words and The desire for revenge")
            pau("You definitely became stronger now")
            before.append("strong")
        revenge_time()
    if response == "2":
        if "power" in before:
            pau("You already got a power from the elements temple")
            pau("There is nothing to do there")
            pau("You think you are ready to fight the dragon")
            revenge_time()
        if "strong" in before:
            pau("You are strong enough to go to the temple of elements")
            pau("You went there but a strong shock of power rushed at you")
            pau("You can barely resist but you remember "
                "your father and your family")
            pau("so you stood there with no care of what will happen to you")
            pau("Suddenly, three rockes appeard and you "
                "heared a sound saying")
            pau("\"So, you could resist the power of the temple\"")
            pau("\"You can now choose the power of an "
                "element of your choice\"")
            chosen_element()
            before.append("power")
            revenge_time()
        if "yes" in before and "strong" not in before:
            pau("You remember how you were thrown from the temple")
            pau("You think that you need to become "
                "stronger before you can go there")
            revenge_time()
        before.append("yes")
        if "strong" not in before:
            pau("You think that you are not strong enough but "
                "you are going there anyway")
            pau("when you became there, a strong shock "
                "of power threw you back")
            pau("after some time you woke up")
            pau("You know for sure now that you need to become stronger")
            revenge_time()
    if response == "3":
        if "yes4" in before and "power" not in before and "strong"\
         not in before:
            pau("You need to become stronger to face the dragon")
            revenge_time()
        before.append("yes4")
        if "power" in before:
            pau("So, you are strong enough")
            pau("Got a huge power from the elements temple")
            pau("and well prepared")
            pau("You are ready to face the dragon")
            pau("You went to your destroyed village where "
                "the dragon is staying")
            the_fight()
            time.sleep(5)
        if "strong" in before and "power" not in before:
            pau("Yes you trained for two years, and you think "
                "you are strong to face the dragon")
            pau("But you think you should check the temple your "
                "father talked about first")
            revenge_time()
        if "strong" not in before:
            pau("You hold your sword in your hand strongly")
            pau("You remembered your father and cried and "
                "remembered that you should be stronger to revenge")
            pau("You leave the sword and decide that facing dragon "
                "now will not do any good")
            pau("You decided to do something else")
            revenge_time()


def intro_dream():
    # the very first function that tells you what kind of
    # dragons you are facing
    pau("You attacked with all you have got of power")
    pau("But the dragon...\n")
    pau("The dragon is so powerful")
    if "Fire" in dragon:
        pau("You tried to resist his attacks with your shield but\n\n"
            "his fire breathing made your sheild too hot"
            " that you couldn't grab it anymore as your sword")
    elif "Water" in dragon:
        pau("You tried to resist his attacks with your shield but\n\n"
            "the water dragon has sent a large wave of water")
        pau("that threw you away and dismantled your shield"
            " too as your sword")
    elif "Earth" in dragon:
        pau("You tried to resist his attacks with your shield but\n\n"
            "the earth dragon has summoned plants underneath you")
        pau("that rooted you to the ground and summoned some plants\n\n"
            "to attack you and dismantled your shield")
    pau("The only thing that you have got now is your bare hands")
    response = choice("what will you do:\n"
                      "1. Stand like a man\n"
                      "2. Try to escape\n"
                      "3. Try to grab your shield again\n", "1", "2", "3")
    if response == "1":
        pau("You stood like a man"
            " facing your death as you don't care anymore ")
    elif response == "2":
        pau("You thought of escaping...")
        pau("But you rememberd how you failed your father "
            "and your people and couldn't kill the dargon")
        pau("So you stood in disappointment waiting for your death")
    else:
        pau("You tried to go and grab your shield but "
            "you got no time to grab it")
        pau("You know if you turned your back to grab your "
            "shield the dragon will end your life")
        pau("So you stood in disappointment waiting for your death")


def after_dream():  # the story of the father and also you waking up
    pau("The dragon is getting closer to attack you"
        " and you know for sure this will end your life")
    pau("The dragon is so close to you....\n")
    pau("But\n")
    time.sleep(5)
    pau("You wake up in fear")
    pau("You breathe fast for a few moments then")
    pau("You remember your father's last words before "
        "he dies from the dragon's attacks")
    pau("\"Son you should escape our village for now")
    pau("you should take your mother and brothers away")
    pau("away from here to somewhere safe")
    pau("but I want you to put an end for this dragon")
    pau("when you are ready son...(some coughs)")
    pau("when you are ready go to the elements temple")
    pau("elements temple will give you the true power of a natural element")
    pau("when you go there you can choose an element of your choice")
    pau("BUT only if you are STRONG enough")
    pau("choose wisly...(some coughs)... son\"")
    time.sleep(3)
    pau("You got off bed angry and decided to stop that dragon")


def play_game():
    intro_dream()
    after_dream()
    revenge_time()


play_game()
