# The script of the game goes in this file.
image BG lab a = "Labratory.jpg"
image s = "scientist.png"
image BG Pyramid = "startend.png"
image BG left = "left.jpg"
image BG right = "right.jpg"
image Underworl = "underworld.jpeg"
image BG anubis = "bg anubis.jpg"
image BG isis = "bg isis.jpg"
image BG ayahotep = "bg ayahotep.jpg"
image BG sekhmet = "Sekhmet2.jpg"
image Sekhmet = "Sekhmet.png"
image Aya = "Ayahotep.png"
image Anubis = "Anubis.png"
image Isis = "Isis.png"
image Osiris = "Osiris.png"
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define p = Character("[name]")
define s = Character("Qing Zheng")
define o = Character("Osiris")
define a = Character("Anubis")
define i = Character("Isis")
define sk = Character("Sekhmet")
define q = Character("Queen Ayahotep")


# The game starts here.

label start:
    play music "Jane_Fonda.mp3"
    $ relationship = 30

    $ name = renpy.input("Before we begin, what's your name?")
    $ name = name.strip()

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene BG lab a with dissolve


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show s happy:
        xalign .5
        yalign -0.75


    # These display lines of dialogue.
    s "Hello [name]! I'm so happy to meet you. How are you?"
    menu:
        "I'm wonderful, how are you, gorgeous?":
            $ relationship +=5
            show s blushing
            s "Oh-oh my...I'm very good, thank you."
            show s happy
            s "Let me give you a bit of background, so you aren't completely oblivious to the task."
            s "You have been hired by APEX Intelligence as a Treasure Hunter. You have to retrieve the Cube of Pandemonium from the great Pharoh Ayahotep's pyramid."
            s "Legend says that it's user will not only be able to contain and release all of the chaos in the world, but will also be able to cure all sickness and destroy mosquitos in the world"
            p "Mosquitos...?"
            s "I have no idea why they had some sort of personal beef with mosquitos, but let's be honest, are we really going to disagree with them? Mosquitos do nothing except annoy everyone and spread disease."
            p "Mosquitos ARE the worst."
            s "Anyhow, APEX will be willing to pay you a large sum of cash, if you do succeed."
            p "If I succeed? Were there others?"
            s "It's best we not talk about it. I'm sure you'll be different from the other people we've hired!"
            p "But-"
            s "Let's get you to the location!"
        "Could be better.":
            $ relationship +=0
            s "Sorry to hear that. Keep fighting! You never know when today is your day to die!"
            s "Let me give you a bit of background, so you aren't completely oblivious to the task."
            s "You have been hired by APEX Intelligence as a Treasure Hunter. You have to retrieve the Cube of Pandemonium from the great Pharoh Ayahotep's pyramid."
            s "Legend says that it's user will not only be able to contain and release all of the chaos in the world, but will also be able to cure all sickness and mosquitos in the world"
            p "Mosquitos...?"
            s "I have no idea why they had some sort of personal beef with mosquitos, but let's be honest, are we really going to disagree with them? Mosquitos do nothing except annoy everyone and spread disease."
            p "Mosquitos ARE the worst."
            s "Anyhow, APEX will be willing to pay you a large sum of cash, if you do succeed."
            p "'If' I succeed? Were there others?"
            s "It's best we not talk about it. I'm sure you'll be different from the other people we've hired!"
            p "but-"
            s "Let's get you to the location!"
        "Don't bother asking me.":
            show s upset
            $ relationship -=5
            s "No need to get so snappy with me!"
            s "Since you're in such a bad mood, we'll just get started with the task at hand. Good luck."
            jump scene3
            p "Hopefully, anything she had to say to me wasn't important..."
    label scene3:
        play music "egypt.mp3"
        scene BG Pyramid with dissolve
        p "Let's get this started."
        p "Where should I start...?"
        menu:
            "Left":
                scene BG left
                "You walk into the left side of the passageway, and are greeted with a long hallway, covered in hieroglyphs, that tell a story about the Queen's legacy. There are double doors made out of jade at the end of the hall, and a lone skeleton direrectly next to it, holding a rifle, that looks like it was made in the 1800s."
                p "This looks a bit too easy."
                menu:
                    "Walk down the hallway carefully.":
                            "You walk down the hall, being sure to not step on anything that looks suspicious. You continue down the hall and step on a stone that immediatly sinks into the ground, causing the entire ceiling to collapse on you,"
                            hide BG left
                            scene black
                            play sound "Blood Splatter Sound Effect.mp3"
                            "crushing your bones and organs."
                    "Walk down the hallway casually.":
                            "*You walk down the hall, not giving it a second thought, after all, you're a professional."
                            "You continue down the hall and step on a stone that immediatly sinks into the ground, causing the entire ceiling to collapse on you,"
                            scene black
                            play sound "Blood Splatter Sound Effect.mp3"
                            "crushing your bones and organs."
            "Right":
                scene BG right
                "You walk into the left side of the passageway, and are greeted with a huge room covered top to bottom with gold coins, jewlery, and other beautiful artifacts."
                p "Amazing..."
                "Pick up a ruby?"
                menu:
                    "Pick up a ruby":
                        "In all of your awe, you decide to pick up the largest ruby you can find to examine it."
                        p "WOAH!!!!"
                        "As soon as the ruby touches you, the ground shakes and all of the coins fall on top of you. Who knew metal was so heavy?"
                        scene black
                    "Don't":
                        "You decide to be a little smarter about the things you touch"
                        "A snake comes out of a crack in the wall"
                        play sound "snake.mp3"
                        "And it bites you."
                        "You die instantly."
                        scene black

        scene underworld with dissolve

        show Osiris
        o "Well, well well. If it isn't [name]. You weren't supposed to die for another couple of years. Heart attack. You might want to lay off those big macs. What brings you here?"
        menu:
            "I'm supposed to find the Cube of Pandemonium.":
                o "Seriously? Y'know, it'll be pretty hard to get that thing, you'll need Aufaa's armor of blessings to impress Queen Ayahotep."
                o "You'll have no choice but to go through the other gods and goddesses here to protect her in order to collect everything it is that you need."
                o "Try not to be rude, and maybe they'll let you pass them! I'll lead you to your first god."
                $ relationship += 0


            "Woah! Osiris! You're the god of death! I've read so much about you! Can you help me get the Cube of Pandemonium?":
                o "How sweet."
                o "Seriously? Y'know, it'll be pretty hard to get that thing, you'll need Aufaa's armor of blessings to impress Queen Ayahotep."
                o "You'll have no choice but to go through the other gods and goddesses here to protect her in order to collect everything it is that you need."
                o "Try not to be rude, and maybe they'll let you pass them! I'll lead you to your first god."
                $ relationship +=5

            "None of your business.":
                o "Congrats, idiot, you've just earned 20 years off your lifespan. Good luck."
                "After foolishly disrespecting one of the more powerful Gods you've read about, you are forced to get to the next location by swimming through lakes filled with baby eating crocodiles, and walking through fields of grass infested with mosquitoes and scorpions."
                $ relationship -= 5
        scene BG anubis with dissolve
        show Osiris at right
        show Anubis at left:
            yalign 1.0
        a "Welcome, human. I see you are trying to get to Queen Aya, but, in order to get to her, you must go through me."
        o "You might want tot show some respect, [name]. Anubis is not what you'd call...forgiving"
        menu:
            "*bow down*":
                a "Very nice...you seem to know power when you see it."
                $ relationship +=5
            "*shake his hand eagerly*":
                a "Um...okay...?"
                $ relationship +=0
            "*Stare at his massive dog head, and yell 'Who's a good boy?!'":
                a "*His eye twitches and turns yellow*"
                $ relationship -=5
        a "In order to continue with your quest, I will give you a riddle, as only the most sophisticated men can even interact with the pharoah herself. So, try this out for size."
        $ answer = ""
        $ sdhf = False
        label Anubis:
        a "I am not alive but seem so, because I dance and breathe with no legs or lungs of my own. What am I?"
        $ answer = renpy.input("Enter your answer")
        if answer == "Fire":
            a "Hm. took you long enough. You may pass, and take this with you."
            "You recied a breast plate!"
        elif answer == "fire":
            a "Hm. took you long enough. You may pass, and take this with you."
            "You recied a breast plate!"
        else:
            a "Try again."
            jump Anubis
    hide Osiris
    hide Anubis
    scene BG isis with dissolve
    "After solving the riddle, you continue along your path, and come across a shrine  that is dimly lit and filled with insense"


    p "Hello? Is anyone here?"
    i "Hello [name]"
    show Isis:
        xalign 0.5
        yalign -2.0
    p "Isis! Goddess of magic!"
    i "Indeed."
    menu:
            "Didn't you marry your brother? Gross, man.":
                i "Gods do not follow the same rules humans are given. They hold no weight, nor meaning over our heads."
                $ relationship -=5
            "You're even more gorgeous in person, my goddess...":
                i "Bless you and those softly spoken lips of yours, my child."
                $ relationship +=5
            "I've read all about you, Isis.":
                i "No amount of books you have ever read can truly reflect what I am capable of, my child."
                $ relationship +=0
    i "I know why you are here, and what it is you seek, and just like before, you must answer a simple question. You may have gotten through my dear Anubis, but you must know that mine will be much more difficult. Are you ready?"
    menu:
            "Yes, my goddess!":
                i "*slight laugh* Alright."
                $ relationship +=0
            "Heck yea!":
                i "Excited. I like it."
                $ relationship +=5
            "It can't be that hard.":
                i "We will see about that."
                $ relationship -=5
    $ answer = ""
    $ sdhf = False
    label Isis:
    i "I'm always there, some distance away. Between land or sea, and sky I lay. You may move towards me, yet distant I stay. What am I?"
    $ answer = renpy.input("Enter your answer")
    if answer == "Horizon":
        i "Amazing! You have a gift!"
        "You recieved a shield!"
    elif answer == "horizon":
        i "Amazing! You have a gift!"
        "You recieved a shield!"
    else:
        i "Afraid not, my child..."
        jump Isis

    if relationship > 45:
        "Isis leans in, and kisses you on the lips, making you bluss, and get a warm feeling inside your stomach."
        i "Be careful, and stay strong,[name]."
    else:
        i "Now go."
    hide Isis
    scene BG sekhmet
    "You enter a room full of fire and smoke. You look around trying to find your next obstacle."

    menu:
        "What will you say?"

        "Hello?":
            show Sekhmet:
                xalign 0.5
                yalign -0.75
            sk "What do you want you mortal? I am Sekhmet, goddess of war and healing. I know why you're here and just like before you must answer my riddle to continue on your quest."
            $ relationship += 5
        "Anybody there?":
            show Sekhmet:
                xalign 0.5
                yalign -0.75
            sk "What do you want you mortal? I am Sekhmet, goddess of war and healing. I know why you're here and just like before you must answer my riddle to continue on your quest."
            $ relationship += 0
        "Man this place is a mess":
            show Sekhmet:
                xalign 0.5
                yalign -0.75
            sk "Watch your mouth. You are in the presence of the goddess of war you insolent mortal. You maybe already dead but I can still make things worse for you. Now answer my riddle so that you can leave my presence."
            $ relationship -= 5
    sk "I am the black child of a white father, a wingless bird, flying even to the clouds of heaven. I give birth to tears of mourning in pupils that meet me, even though there is no cause for grief, and at once on my birth I am dissolved into air. What am I?"
    $ answer = ""
    $ sdhf = False
    label sekh:
    sk "I am the black child of a white father, a wingless bird, flying even to the clouds of heaven. I give birth to tears of mourning in pupils that meet me, even though there is no cause for grief, and at once on my birth I am dissolved into air. What am I?"
    $ answer = renpy.input("Enter your answer")
    if answer == "smoke":
        sk "Good job. You're smarter than you look."
    elif answer == "Smoke":
        sk "Good job. You're smarter than you look."
    else:
        sk "Try again, it's easier than you think."
        jump sekh

    if relationship >= 20:
        sk "You have answered my riddle and have earned Asenath, sword of decay. Good luck on your journey, you'll need it."
    elif relationship < 20:
        sk "Take Asenath, sword of decay, and leave my presence you putrid mortal."
    hide Sekhmet

    scene BG ayahotep
    "With all the pieces of armor, you feel confident in yourself. You enter the Pharoah's room and Ayahotep appears"
    show Aya
    q "Hello there, I see that you've traveled long and far to get your hands on the Cube of Pandamonium. But lets see if you're truly worthy of it."
    if relationship < 20:
        q "It seems that you've treated many of those that you've encountered with disrespect and for that it's obvious that you aren't worthy of my precious treasure."
        return
    elif 20 < relationship < 40:
        q "Your behavior has been alright but I know for a fact that you can do better. I'll give you one last chance, chose carefully"
    menu:
        "What will you say?"

        "Pay her a compliment":
            $ relationship += 20
            "Has anyone ever told you that your crown looks stunning."
            q "They say flattery won't get you anywhere. Well they're wrong. You've earned this."
        "Be rude":
            $ relationship -= 20
            "I don't take orders from the dead."
            q "Is that so? Well the dead take orders from me. You just earned yourself enternity in the underworld. You fool."
            scene black
            "Anubis keeps your soul. You couldn't be nice huh?"
            return
    if relationship >= 40:
        q "You've treated the people you've encountered with kindness. You understand that every choice, every action, every word has a value. And I can tell that you are worthy of my treasure."
    q "Well done, now be sure to take care of my cube. And more importantly, make that its power is only used for good. I'm trusting you. Anubis will take you home."
    hide Ayahotep
    play music "end.mp3"
    scene BG Pyramid
    "You wake up with the cube in hand, back where you started."
    scene BG lab a
    "You go back to APEX and give the cube to the scientist."
    show s happy:
        xalign .5
        yalign -0.75
    s "My hero!"
    scene black
    "Thanks for playing our game. :)"
