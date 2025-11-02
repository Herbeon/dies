# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rod")
define dp = Character("DonutPenguins")
define cr = Character("Chicken of Rotisserie")
define iu = Character("Iunno")
define sib = Character("The Sibling")

default award_nihilism = False
default award_detective = False
define is_yolo = False
default self_talking = False
define has_trust_issues = False
define too_many_clubs = True
define dpc = 0
define is_in_robotics = False
define loves_food = False
define gets_more_nightmares = False 
# define iunnosize = 9

define lst_c3 = []

define school = 7
define clubs = 7
define happiness= 7
define health = 7
define relations = 7
define detectivechecks = 3
define totaldays = 10

# The game starts here.

label start:

    # I LIKE!! wipe! dissolve is a classic. zoomin would be cool
    # parallax would be so cool, will implement if I have time
    # or just a small zoomed in scene that moves opposite from mouse

    # chapter 1: the self that we can be 
    scene bg content warning 1
    with dissolve
    pause 
    scene bg content warning 2
    with dissolve
    pause
    scene bg content warning 3
    with dissolve 
    pause 

    scene bg ctscn sleepingdark
    with dissolve
    "march 1st, 2025,"

    scene bg ctscn sleepingdark2
    with dissolve
    "I was murdered."

    scene bg ctscn sleeping 
    with dissolve 
    "december 31st, 2024,"

    scene bg ctsn awaken 
    with wipeup
    "I reawakened."

    scene bg ctsn hny0
    with dissolve
    "numb through the day,"
    scene bg ctsn hny1
    pause 0.5
    scene bg ctsn happy new year
    with dissolve 
    "I watched the fireworks at night."
    "Happy new year."
    "This is my last one."

    scene bg blank
    $ global self_talking
    $ self_talking = True
    $ renpy.notify("chapter 1: the self that we can be")
    show rod blue bedhead
    "."
    show rod blue shocked
    pause 0.5
    show rod blue stand
    ".."
    "That was...not a dream?"
    
    show rod blue sweatsmile
    pause
    show rod blue ohno
    pause 0.5
    show rod blue questioning
    "What do I do????"
    show rod blue ohno
    "Am I going to die again?????"
    "aasdfghjkl;"
    "hhhhhhhhh."
    show rod blue sweatsmile
    "it's okay."
    "I just need to...make decisions!"
    show rod blue questioning
    jump death_decide_menu

    # code should never reach this
    return 

menu death_decide_menu:
    "am I actually going to die???"

    "my death is inevitable.":
        show rod blue ohno
        jump inevitable_death
    
    "I won't die this time":
        show rod blue thumbsup
        jump prevent_death

menu inevitable_death:
    "I've read plenty of stories about self-consistency in time travel."
    "My death is inevitable and my day is ruined."
    
    "....but maybe I can still solve my murder?":
        $ global award_detective
        $ award_detective = True
        jump detective_time
    "and...there is no point trying to solve my murder, if I'm just going to die anyway...":
        $ global award_nihilism
        $ award_nihilism = True
        show rod blue pointingout
        jump yoloornot_time

menu prevent_death:
    "since I'm in the past, surely I can change it."
    "I will try to solve my murder."

    "I'll look for clues...":
        $ global award_detective
        $ award_detective = True 
        jump detective_time
    "I'll trust nobody...":
        show rod blue secretive
        "and that will keep me safe."
        $ global has_trust_issues 
        $ has_trust_issues = True
        jump restofwinter_time

label detective_time:
    show rod blue detective
    "TIME TO BE A DETECTIVE!"
    jump restofwinter_time

menu yoloornot_time:
    "I just can't change a thing."

    "I just have to relive this life of suffering.":
        jump bonus_scene_time
    "So I should live my life to the fullest!!":
        jump yolo_time

label yolo_time:
    $ global is_yolo
    $ is_yolo = True
    show rod blue thumbsup
    "I will join ALL the clubs."
    "I will make a bucket list."
    "And I will do EVERYTHING ON IT!!"
    "I will stop worrying about my grades!"
    show rod blue bittersweet
    "This is the last time I'll live, after all!"

    jump restofwinter_time

label restofwinter_time:
    show rod blue secretive
    "for the rest of winter break, I didn't do anything productive."
    scene bg ctsn itsfood
    with dissolve
    "wake, eat, sleep, repeat"
    scene bg ctsn itssleep
    with dissolve
    "I used to love having breaks from work, but I find myself in need of things to do."
    scene bg blank 
    with dissolve
    show rod blue bored 
    "School starts again tomorrow."
    jump chapter_2

label chapter_2:
# show proper transition
    $ renpy.notify("chapter 2: the friends that be")
    

    "The Reliable Transport Commission had a delay in the morning."
    "Other than that, the beginning of school was fine."
    "It's lunchtime now."
    scene bg treefrock
    $ global has_trust_issues
    if has_trust_issues:
        "I can't reveal too much to my friends. Any of them might have been my murderer."
    if award_detective:
        "I have to talk to my friends a lot, and figure out whether they are related to my murder."
    jump donut_penguins_time

label donut_penguins_time:
    # python if donut_penguins_count %= 0, it is even -> show one sprite. else, show the other
    # need to make donutpenguins sprite
    "It's DonutPenguins!!"
    $ global is_yolo
    if is_yolo:
        "I've always admired DonutPenguins' whimsy."
    $ self_talking = False
    show dpeven
    dp "yo rod!!!"
    $ global dpc 
    $ dpc += 1
    jump get_sushi
    # ...... I will NOT regret not making a function for this.

menu get_sushi:
    dp "wanna come get sushi with me?"    
    "yeah!":
        $ global loves_food 
        $ loves_food = True
        $ global dpc 
        if(dpc%2 == 0):
            hide dpodd
            show dpeven 
        else:
            hide dpeven
            show dpodd
        dp "alright!"
        $ dpc += 1
        jump sushi_time
    "nah!":
        $ global dpc 
        if(dpc%2 == 0):
            hide dpodd
            show dpeven
        else:
            hide dpeven 
            show dpodd
        $ dpc += 1
        dp "okayy cya!"
        scene bg treezoom
        show crnormal
        jump rotisserie_chicken_time

label sushi_time:
    scene bg streetview2
    $ global dpc 
    if(dpc%2 == 0):
        hide dpodd
        show dpeven 
    else:
        hide dpeven
        show dpodd
    dp "you look like you slept all winter break and still woke up tired."
    $ dpc += 1
    if(dpc%2 == 0):
        hide dpodd
        show dpeven 
    else:
        hide dpeven
        show dpodd
    dp "but that's chill. good food will energize us!"
    $ dpc += 1
    scene bg dark
    with dissolve 
    scene bg ctsn sushi
    with dissolve 
    pause 
    scene bg streetview1 
    with dissolve 
    if(dpc%2 == 0):
        hide dpodd
        show dpeven 
    else:
        hide dpeven
        show dpodd
    dp "yumm sushi! let's head back."
    $ dpc += 1
    if(dpc%2 == 0):
        hide dpodd
        show dpeven 
    else:
        hide dpeven
        show dpodd
    $ dpc += 1
    jump murder_mystery_manga_time

menu murder_mystery_manga_time:
    dp "there's this really good murdery and mysterious horror manga that I've been reading..."

    "(enthusiastic) wow, tell me about it!":
        $ global dpc 
        if(dpc%2 == 0):
            hide dpodd
            show dpeven 
        else:
            hide dpeven
            show dpodd
        dp "I'm SO GLAD YOU ASKED >:3"
        dp "(insert passionate rambling here)"
        $ dpc += 1

        $ global has_trust_issues, is_yolo, award_detective
        if has_trust_issues:
            scene bg dark
            with dissolve 
            scene bg susdp 
            with dissolve 
            show rod blue pointingout 
            "(they were reading murder mystery??)"
            "(they cannot be trusted.)"
            jump chapter_3 
        if is_yolo:
            show rod blue thumbsup
            r "I might have nightmares, but I gotta read that manga too! (don't want to die without having read it)"
            jump manga_nightmare_time
        if award_detective:
            show rod blue detective 
            "(interesting. must analyze this manga...)"
            show rod blue sweatsmile 
            r "ummmmm"
            r "I kinda want to read it!!"
            jump manga_nightmare_time

        jump chapter_3 # code should never reach this ?

    "(back away) wait, WHAT.":
        $ global dpc 
        if(dpc%2 == 0):
            hide dpodd
            show dpeven 
        else:
            hide dpeven
            show dpodd
        dp "oh yeah, I forgot you don't like horror."
        $ dpc += 1
        $ global has_trust_issues, is_yolo, award_detective
        if(has_trust_issues):
            show rod blue shocked 
            "oh no, THEY KNOW MY WEAKNESS"
            show rod blue secretive 
            r "hahaha... yeah, I probably shouldn't get near it"
            jump chapter_3
        if(is_yolo):
            show rod blue sweatsmile 
            r "nah!! I'm going to read this manga anyway!"
            show rod blue thumbsup
            r "it sounds SUPER INTERESTING (and I don't want to die without having read it)"
            jump manga_nightmare_time
        if(award_detective):
            show rod blue secretive 
            r "I don't like horror... but maybe I'll try a bit? (I need to analyze this manga!!)"
            jump manga_nightmare_time

    "(shock)":
        show rod blue shocked 
        $ global dpc 
        if(dpc%2 == 0):
            hide dpodd
            show dpeven 
        else:
            hide dpeven
            show dpodd
        dp "...based on the fact that you're scared of the THOUGHT of a horror manga,"
        dp "maybe I won't recommend that one to you."
        $ dpc += 1
        jump chapter_3

label manga_nightmare_time:
    if(dpc%2 == 0):
        hide dpodd
        show dpeven 
    else:
        hide dpeven
        show dpodd
    dp "uhhh, are you still rod??"
    dp "haha, just kidding."
    dp "the series is called ****. it's in the library!"
    $ dpc += 1
    scene bg dark 
    with dissolve 
    show rod blue ohno 
    "..."
    "I shouldn't have read that."
    $ global gets_more_nightmares
    $ gets_more_nightmares = True 
    jump chapter_3

menu rotisserie_chicken_time:
    cr "yayy, you're outside today!"

    "yayy":
        hide crnormal 
        show crsmiley
        jump rest_of_lunch_time
    "is that surprising?":
        $ global is_yolo 
        if is_yolo:
            jump soo_busy_yolo
        else:
            jump soo_busy

menu soo_busy:
    cr "yeah, you're so busy with extracurriculars all the time!"

    "(smile a bit) yeah, that's sort of true":
        jump should_focus
    "(smile wide) I can manage it though!":
        jump not_managed_lol

menu soo_busy_yolo:
    cr "yeah, you're so busy with extracurriculars all the time!"

    "(smile a bit) yeah, that's sort of true":
        $ global has_trust_issues
        if has_trust_issues:
            jump should_focus_untrust
        else:
            jump should_focus
    "(smile wide) I can manage it though!":
        jump not_managed_lol
    "(grin) yeah, I should join MORE!":
        hide crnormal 
        show crwaitwhat
        cr "wait, what?"
        pause 0.2
        jump extra_ecs_time

label extra_ecs_time:
    scene bg frock 
    show rod blue secretive
    r "hi Iunno!"
    show rod blue thumbsup
    r "I want to join more clubs! what should I try?"
    hide rod blue thumbsup
    show iunnobanana
    jump join_robotics 

menu join_robotics:
    iu "you should join robotics!"

    "hmmm... I dunno....":
        # $ global iunnosize
        # $ iunnosize += 1
        # $ renpy.notify(str(iunnosize))
        # hide dpeven 
        # show dpeven:
        #     zoom iunnosize/10
        jump join_robotics
    "YEAH, okay!!":
        $ global is_in_robotics
        $ is_in_robotics = True  
        jump chapter_3


label not_managed_lol:
    scene bg ctsn didntmanage
    show rod blue bedhead
    "..."
    "I did not manage it :("
    "why am I double booked all the time?!"
    jump chapter_3

menu should_focus_untrust:
    cr "you should try to focus on the most important ones!"
    
    "yeah, you're right. I'll see what I can do.":
        $ global too_many_clubs
        $ too_many_clubs = False 
        jump chapter_3
    "(is she trying to make me abandon my favourite things to make me more ready to die??) nah, it's fine!!":
        jump not_managed_lol

menu should_focus:
    cr "you should try to focus on the most important ones!"
    
    "yeah, you're right. I'll see what I can do.":
        $ global too_many_clubs
        $ too_many_clubs = False 
        jump chapter_3
    "(smile wide) nah, it's fine!!":
        jump not_managed_lol

label rest_of_lunch_time:
    "lunch is fun."
    jump chapter_3

label chapter_3:
    scene bg green 
    $ renpy.notify("chapter 3: the things we can control")
    scene bg ctsn cover 
    with dissolve 
    "what can we choose, and what is left to chance?"
    ""
    "January 1st, 2025,"
    show bgo greencorner
    show rod blue questioning
    with dissolve 
    "I made a decision."
    $ global has_trust_issues, is_yolo, award_detective
    if(has_trust_issues):
        show rod blue secretive 
        with dissolve 
        "trust nobody."
    if(is_yolo):
        show rod blue bittersweet
        with dissolve 
        "live my life to the fullest."
    if(award_detective):
        show rod blue detective
        with dissolve 
        "solve my murder."
    scene bg green 
    show rod blue stand 
    "that sort of decision-making was easy,"
    show rod blue bedhead
    "wasn't it?"
    show rod blue bittersweet 
    with dissolve
    "didn't it feel so simple?"
    scene bg blank 
    show rod blue bored 
    "Just two choices at a time."
    jump choose_things

label choose_things:
    $ global self_talking 
    $ self_talking = True 
    "in this life, however," 
    scene bg inthislife1
    with wipeup 
    "our choices are daunting, crucial, limitless!"
    show bg inthislife2
    with dissolve 
    jump what_to_do

label what_to_do:

    $ global totaldays
    $ totaldays -= 1
    if totaldays <= 0:
        scene bg dark 
        with dissolve 
        jump chapter_4 
    scene bg inthislife2 
    with dissolve 
    $ lst_c3 = [
        ("do homework", "homework_time"),
        ("do extracurriculars", "extracurricular_time"),
        ("do hobbies", "hobby_time"),
        ("eat food", "food_time"),
        ("sleep","sleep_time"),
        ("dream","dream_time")
    ]
    $ global award_detective, is_yolo, has_trust_issues
    $ global too_many_clubs, is_in_robotics, loves_food, gets_more_nightmares 
    if (award_detective):
        $ lst_c3.append(("do detective investigation","invest_time"))
    if(is_yolo):
        $ lst_c3.append(("do bucket list", "bucket_time"))
    if(has_trust_issues):
        $ lst_c3.append(("test friends' trustworthiness", "trust_time"))
    # IT WORKS!!
    if(too_many_clubs):
        $ lst_c3.append(("do MORE extracurriculars", "more_extracurriculars_time"))
    if(is_in_robotics):
        $ lst_c3.append(("do robotics!" , "do_robotics_time"))
    if(loves_food):
        $ lst_c3.append(("eat MORE food", "more_food_time"))
    if(gets_more_nightmares):
        $ lst_c3.append(("read wholesome things (to get rid of nightmares)" , "wholesome_time"))
    if(totaldays == 1):
        $ renpy.notify("last day.")
    else:
        $ renpy.notify(str(totaldays) + " days left.")
    "well, what should I do?"
    $ randomcount = renpy.random.randint(2,5)
    $ the_options = renpy.random.sample(lst_c3, randomcount)
    $ chosen_thing = menu(the_options)
    $ renpy.jump(chosen_thing)

label homework_time:
    $ global school, clubs, happiness, health, relations
    scene bg homeworktime 
    "I do homework. Cool."
    $ school += 3
    $ happiness += 1
    jump what_to_do

label extracurricular_time:
    $ global school, clubs, happiness, health, relations
    scene bg extracurriculartime 
    "so many clubs!! so many extracurriculars!!"
    $ school += 1
    $ clubs += 2
    $ happiness += 2
    $ relations += 2
    jump what_to_do

label hobby_time:
    $ global school, clubs, happiness, health, relations
    scene bg hobbytime 
    "haven't found time for hobbies in a while!"
    $ happiness += 1
    $ relations += 1
    jump what_to_do

label food_time:
    $ global school, clubs, happiness, health, relations
    scene bg foodtime 
    "yum, food!"
    $ school += 1
    $ happiness += 1
    $ health += 3
    $ relations += 2
    jump what_to_do

label sleep_time:
    $ global school, clubs, happiness, health, relations
    scene bg sleeptime 
    "always a good time for a nap!"
    $ school += 3
    $ happiness += 2
    $ health += 3
    $ relations += 1
    jump what_to_do

label dream_time:
    $ global school, clubs, happiness, health, relations
    $ global gets_more_nightmares
    scene bg dreamtime 
    "it's possible to dream while awake."
    $ coinflip = renpy.random.randint(1,2)
    if(coinflip == 1):
        if(gets_more_nightmares):
            "unfortunately, it's also possible to get nightmares while awake."
            $ happiness -= 1
            $ health -= 1
    else:
        $ happiness += 1
    jump what_to_do

label invest_time:
    $ global school, clubs, happiness, health, relations
    scene bg investtime 
    "feeling like that conspiracy theory meme right now."
    $ global detectivechecks
    $ detectivechecks-= 1
    jump what_to_do

label bucket_time:
    $ global school, clubs, happiness, health, relations
    scene bg buckettime 
    $ school -= 2
    $ happiness += 2
    "gotta try something on my bucket list!"
    jump what_to_do

label trust_time:
    $ global school, clubs, happiness, health, relations
    scene bg trusttime 
    $ school -= 2
    $ happiness -= 2
    $ health -= 1
    $ relations -= 3
    "everyone is sus. donutpenguins' outfit changes every time I blink. rotisseriechicken smiles weird. iunno peels bananas the wrong way."
    jump what_to_do

label more_extracurriculars_time:
    $ global school, clubs, happiness, health, relations
    scene bg moreextracurriculartime 
    $ school -= 1
    $ clubs += 3
    $ happiness += 3
    $ relations += 3
    "MORE EXTRACURRICULARS!! (maybe too many?)"
    jump what_to_do

label do_robotics_time:
    $ global school, clubs, happiness, health, relations
    scene bg roboticstime 
    $ school += 1
    $ clubs += 1
    $ happiness += 2
    $ health -= 1
    $ relations += 2
    "robotics!! (why won't the robot go in a straight line?)"
    jump what_to_do

label more_food_time:
    $ global school, clubs, happiness, health, relations
    scene bg morefoodtime 
    $ happiness += 2
    $ health += 3
    $ relations += 3
    "YUM, MORE FOOD!"
    jump what_to_do

label wholesome_time:
    $ global school, clubs, happiness, health, relations
    scene bg wholesometime 
    "I like looking at cute cats. Makes me smile."
    $ school -= 1
    $ happiness += 2
    $ health += 1
    jump what_to_do


label chapter_4:
    scene bg green 
    $ renpy.notify("chapter 4: the things we can't control")
    show rod blue stand 
    "there are the things we can control,"
    "and the things we can't"
    show rod blue bittersweet
    with dissolve 
    "for example, my story's end."
    # okay so here is how it will work...
    ""
    $ global school, clubs, happiness, health, relations
    $ global award_detective, is_yolo, has_trust_issues

    $ renpy.notify(f"school: {school} | clubs: {clubs} | relations: {relations}")
    pause 2.0
    $ renpy.notify(f"happiness: {happiness} | health: {health}")
    pause 
    if(award_detective):
        $ global detectivechecks
        if(detectivechecks < 2):
            show rod blue detective 
            "I spent lots of time investigating my murder."
            "I think..."
            "I think I know who did it."
            show rod blue bittersweet
            ""
            "Maybe it's best if I don't think about that :)"

    if(is_yolo):
        show rod blue thumbsup 
        with dissolve 
        "I was living my life to the fullest!! was that enough?"
    if(has_trust_issues):
        show rod blue secretive 
        with dissolve
        "I wonder if my \"friends\" ever realised what happened"

    if(health < 11):
        jump the_spiralling
    if (school < 10 and (happiness < 10 or relations < 10)):
        jump the_spiralling 
    if(school < 8 and happiness < 18):
        jump the_spiralling
    if(relations > 14 and clubs < relations):
        jump the_loved
    if(happiness > 14 or clubs > 14 or school > 14):
        jump the_passionate
    else:
        jump the_spiralling


#     eeeeeeeeeeeeeeeeeee
label the_spiralling:
    scene bg dark 
    with dissolve 
    "what does it feel like to spiral?"
    "I wouldn't be able to tell you."
    "I left my world a second time."
    scene the spiralling 
    with dissolve
    pause 
    return 

label bonus_scene_time:
    scene bg dark 
    with dissolve 
    "I was murdered on March 1st, 2025"
    "Twice"
    ""
    "what puppets my life most is my mindset."
    "This is the relief from life that I wanted,"
    "right?"
    ""
    "the end."
    return

label the_passionate:
    scene bg dark 
    scene the passionate 
    with dissolve 
    "\"passionate\""
    "..is such a lively word!"
    "and my life now embodies this."
    "it's so nice to have things that I love in my life."
    window hide 
    pause 
    return 


label the_loved:
    scene bg dark 
    scene the loved 
    with dissolve 
    "\"the loved\""
    "passive, because our lives are not solely dependent on ourselves."
    "we are constantly influenced by the people around us;"
    "we are constantly loved."
    window hide 
    pause 
    return 