label w0_d2:
    scene w0_d2_sunnyhotel with longer_fade
    "You wake up in your room and look at the clock."
    "{i}It's 9:30AM, orientation started 15 minutes ago.{/i}"
    mc "WHAT THE HELL?!?!?"
    mc "WHY DIDN’T MY ALARM GO OFF?"
    mc "Where’s my phone? No no no, please don’t be dead."
    "{i}*You check your phone*{/i}"
    mc "Shoot it’s dead."
    # Add swiftly getting ready - Lazzy
    mc "Great, it’s not even the first day, and I already messed up."
    mc "Who stays up so late the night before the first day of orientation???"
     
    mc "I should just go back home, I’m not gonna succeed here…" 
    mc "What was I thinking???"
    # Sprinting out the door to his car - Lazzy
    mc "What kind of excuse can I come up with..."
    mc "I was sick? Family emergency? My car wouldn’t start?"
    "{i}*You turn the key and the car struggles to start*{/i}"
    scene w0_d2_urgentcar with shorter_fade
    mc "WAIT NOT ACTUALLY! PLEASE START!!!"
    scene w0_d2_insidecar with shorter_fade
    "*As the car starts, you sign in relief and speed off*"
    mc "I don’t even know where I’m going. This city is all new to me!"
    mc "I’m going to be so late..."

    #"*Scene fades to the lecture hall.*" Current one is temporary
    scene w0_d2_lecturehall with longer_fade
    "{i}*You burst through the doors into an nearly empty auditorium, looking around frantically in search of someone*{/i}" 
    mc "Oh look there’s somebody."
    mc "She looks old, I wonder if she is a professor..."
    show java_normal at right with dissolve 
    mc "Excuse me ma’am, I’m so sorry that I’m late."
    mc "I don’t know where to go or what to do."
    mc "My car wouldn't start and I had a family emergency, and I got lost, and..."
    hide java_normal
    show java_happy at right
    u "Hey, it’s okay. It’s just orientation, calm down." 
    hide java_happy
    show java_normal at right
    mc "{i}*Panicked*{/i} Yeah but it’s my first day and I feel like I am already messing everything up."
    hide java_normal
    show java_happy at right
    u "Oh sweetie, don’t worry about it."
    u "Every journey has its own pace; being late doesn’t mean you won’t reach your destination."

    # YOU STOPPED HERE
    
    hide java_happy
    show java_normal at right
    mc "*Stunned* Huh, I guess you're right. Well, what'd I miss?"
    hide java_normal
    show java_happy at right
    u "Sure, well the dean came in and introduced themself to the students."
    u "They said that everyone here was admitted because they are hard working, responsible, smart..."
    u "...and punctual."
    hide java_happy
    show java_normal at right
    mc "Oh. Well that's just great."
    hide java_normal
    show java_happy at right
    u "And then he dismissed them all to breakout rooms where their orientation groups will meet."
    u "You can check on the list outside of the auditorium door to see what room you’ll be in."
    hide java_happy
    show java_normal at right
    mc "Well how will I know where my room is? I don’t know anything about this school!"
    hide java_normal
    show java_happy at right
    u "I am not sure, but you seem smart. I’m sure you'll figure it out."
    u "Anyway I have to go"
    u "It was nice to meet you [mc]."
    hide java_happy
    show java_normal at right
    u "*Winks*"
    u "Turns around and leaves*"
    hide java_normal with fade
    mc "*shouts (still flustered)* Thank you!!"
    mc "Man, I hope all of my professors are as nice as her!"
    mc "So, where am I supposed to be…"
    mc "*looking a list* Room 283. Now to find room 283…"
    
    # Insert transition to breakout room - Lazzy
    # currently put a temp one in - Anton
    scene w0_d2_breakout with fade 

    mc "Jeez, everyone’s here already, where am I going to sit?"
    mc "Oh! There’s a seat! And the company is not that bad either…"
    mc "*Sits down at a table with 3 girls.*"
    mc "Sorry I’m late, I got lost on the wa-"
    
    show cpp_normal with easeinright #moves cpp in from the right to the middle 

    hide cpp_normal
    show cpp_talk
    c "*interrupting* Shut up, did it ever occur to you that maybe everyone is quiet for a reason?"
    hide cpp_talk
    show cpp_normal
    mc "*Obediently stops talking and sits down, flustered.*"
    bsl "Alright, it looks like everyone is here."
    bsl "Go ahead and take some time to introduce yourself to those around you."

    hide cpp_normal
    show python_normal with dissolve
    hide python_normal
    show python_happy

    p "Hi guys!"
    p "My name is Python."
    p "I just moved here from Logicburg."
    p "I’m a computer science major."
    p "I really like playing tennis and reading books."

    hide python_happy
    show js_normal with dissolve
    hide js_normal
    show js_talk
    js "Oh my gosh, that is so cool, Python!"
    js "I am actually from Syntax Springs, but I played tennis in high school!"
    hide js_talk
    show js_smirk
    js "I’m also a computer science major, that’s really cool! Slay!"

    hide js_smirk
    show cpp_talk with dissolve

    c "*grossed out* Uhm, anyway… My name is C++."
    c "I’m a computer science major with a lot of experience."
    c "I did a lot of coding in high school so I’m probably a lot better than you guys."
    c "What about you?"
    # Short interaction decided not to put in choices lmk if this is changed - Lazzy
    menu w0_d2_LateReason:
        c "Why were you so late?" 

        "Honest":
            hide cpp_talk
            show cpp_normal
            mc "I was up really late last night and my phone died before I fell asleep, so I missed my alarm."
            mc "Then this morning, I got lost on the way here and struggled to find the room."
            mc "It was a mess."

        "Cool":
            hide cpp_talk
            show cpp_normal
            mc "So, I was on the way here this morning, and as I was getting to my car I heard a faint meow."
            mc "I looked up and saw a cat 20 feet up a tree."
            mc "I had to help this cat get down so I climbed the tree."
            mc "When I got to the top I noticed that the cat wasn’t afraid of the fall, but instead of the vulture a few feet away from it."
            mc "And then, after I rescued the cat, I had to stop by a women’s right protest, for more rights of course, and that took up a lot of my time."
            mc "I’m 6 foot by the way."
    
    mc "Anyway, my name is [mc]."
    mc "I’m also a computer science major, and I’m really excited to get my college experience started."
    mc "Why do you guys want to do computer science?"
    
    hide cpp_normal
    show cpp_talk

    c "My mom is a software developer for iClicker and my Dad is a software developer for MentiMeter, so you could say it’s in my blood."
    c "I have been coding for as long as I can remember."

    hide cpp_talk
    show cpp_normal
    show js_talk at left with easeinleft
    js "Well aren’t you lucky."
    js "My mom is the worst person in the world."
    js "She is such a helicopter Mom, and won’t leave me alone."
    js "Even though I’m in college now she still won’t butt out of my life."
    js "She even came here with me."
    hide js_talk
    show js_normal at left

    show python_pocket at right with easeinright
    hide python_pocket
    show python_pocket_happy at right
    p "I mean at least you moved out of Syntax Springs, right?"
    hide python_pocket_happy
    show python_pocket at right

    hide js_normal
    show js_talk at left
    js "That’s just it! She’s here in Byteborough with me! UGH!!!"
    js "Anyway that’s irrelevant, I’m in computer science because of its recent growth in popularity!"
    js "I’m so excited to meet new people and make a lot of friends!"
    js "What about you tennis queen?"
    
    hide js_talk
    show js_normal at left

    hide python_pocket
    show python_pocket_happy at right

    p "Well it’s nice that your mom loves you that much. But I definitely get how that is."
    p "I think it is the future and I like learning new stuff."
    p "I’m not super passionate about a career in it but, I bet I will grow to love it."
    p "I think it will be a good choice."
    hide python_pocket_happy
    show python_pocket at right

    # Another short interaction not worth seperating files. Temporarily named everything "Respond to X" since I didnt know what to put - Lazzy
    menu w0_d2_BreakoutResponse1:
        "Respond to Javascript":
            $ js_rep = reputation(js_rep, 2)
            mc "Yeah, it is pretty annoying that your mom won’t leave you alone."
            mc "Parents can be so annoying."
            mc "I wish my mom had cared enough to come with me to orientation though."
            hide js_normal
            show js_talk at left
            js "Well actually…"
            hide js_talk
            show js_normal at left

        "Respond to Python":
            $ p_rep = reputation(p_rep, 2)
            mc "Yeah I agree with Python, computer science definitely seems cool."
            mc "I’m just like you, I don’t have much experience in programming, but I am definitely excited to learn."
            mc "I am also ready to make some money!!"

        "Respond to C++":
            $ c_rep = reputation(c_rep, 2)
            mc "I think it’s really cool that your parents work for those companies, C++."
            mc "I have never heard of iClicker or Mentimeter."
            mc "I don’t know much when it comes to coding, but you sound really experienced."
            mc "Maybe you could show me the ropes sometime..?"
    
    bsl "Alright now, we’re gonna wrap up these conversations and start our guided tour of campus!"
     
    #tour just started put scene change
    scene w0_d2_statue with fade

    "*The group tours campus as the guide talks about random trivia*"
    bsl "And if you look to your left you will see the Half-A-Century Tower…"
    c "Gosh this is so boring."
    c "Who doesn’t know all of this stuff already?"
    c "I mean did anybody really come to this school without already taking a tour."
    p "Wow this is interesting, I am enjoying this tour."


    show python_pocket_happy at left with dissolve
    p "Look at that cool statue over there."
    p "Don’t you guys think he looks cool?"
    hide python_pocket_happy
    show python_pocket at left
    show cpp_talk with dissolve
    c "Oh? You think that’s cool?"
    c "That statue is actually Thomas ‘Firewall’ Jackson."
    c "He was a general in a huge war a while ago and he killed a lot of people."
    c "You really think that someone like that is cool??"
    
    hide cpp_talk
    show cpp_normal

    hide python_pocket
    show python_pocket_happy at left
    p "Oh, well I didn’t realize that…"

    hide cpp_normal
    show cpp_talk
    c "Yeah, I wouldn’t expect someone like you to know something like that."
    show js_normal at right with dissolve
    js "Well I thought he was cool looking too, it was just an honest mistake."
    js "There's no need to be so aggressive C++..."

    menu w0_d2_StatueChoice:
        js "Do you agree with what I'm saying [mc] or are you on C++’s side?"

        "Side with C++":
            jump w0_d2_StatueC
        
        "Side with JavaScript":
            jump w0_d2_StatueJS
        
        "Point out the cute girl across the street":
            jump w0_d2_StatueDB

label w0_d2_AfterStatue:
    bsl "Now we will be taking a breaking for lunch."

    #change scene to cafeteria
    scene w0_d2_cafeteria with longer_fade 


    bsl "The different food stations are around the room."
    bsl "We will be meeting back in the classroom in one hour."
    bsl "Feel free to sit wherever you want."
    mc "Oh jeez, I was going to the bathroom and now everyone is already sitting with each other."
    mc "Where are the girls I was talking to earlier?"
    mc "I hope I didn’t hurt anyone’s feelings."
    mc "I really don’t want to sit alone at orientation."
    "[mc] sees 2 tables. One is Python and C++, another is just JavaScript."

    menu w0_d2_LunchChoice:
        mc "Who should I sit with?"

        "Python and C++":
            jump w0_d2_LunchPythonC

        "JavaScript":
            jump w0_d2_LunchJava

label w0_d2_AfterLunch:
    bsl "Okay guys, lunch is over."
    bsl "Everyone, make sure you are back in the original room in 10 minutes."
    bsl "Okay guys, we are now going to be playing a game to get to know each other better."
    bsl "We are going to be splitting the room up into groups of 2."
    bsl "The game we will be playing is…"
    bsl "TRIVIA!"
    bsl "Since The University of ByteBorough is renowned for its CS program,"
    bsl "all of the trivia will be related to computer science!"
    bsl "The teams you are on for this will be whoever you are sitting with right now."
    bsl "Everybody ready?"
    mc "Okay guys, I am really good at trivia"
    mc "And we are team 1, and one is my lucky number."
    mc "I don’t know much about computer science stuff yet, but I am really good at guessing."
    c "Well, we definitely won’t be guessing."
    c "We want to win, not get by with luck."
    js "I’m sure we won’t need luck, we all seem pretty smart!"
    bsl "Okay here is the first question"
    #display on screen
    #what will the following python code print? ...

    c "Okay guys this one is really easy."
    c "We have to get this one right, it's obviously-"
    js "Hey, don't be rude C++."
    js "Not all of us have programming experience and so it might not be as obvious."
    c "Whatever, take your time figuring it out."
    c "I am writing down our answer now because I want to win."
    p "What are you guys thinking?"
    p "I can tell that num1 is an integer, but num2 is a string by the single quotations surrounding it."
    p "That definitely means something."

    menu w0_d2_q1:
        "Disagree with Python":
            #tech score goes down
            mc "No, I don't think so."
            mc "They are both numbers and the asterisk has to mean multiply."
            mc "Surely the answer is just 15."

            js "Yeah, I don't know if your guess is as good as mine."
            js "I trust you to get it right, but what Python said makes sense."
            js "What do you think we should go with, [mc]?"


        "Agree with Python":
            #tech score +
            mc "Yeah I definitely agree."
            mc "I am not sure what it will change, though."
            mc "What do you think JavaScript?"

            js "Yeah, I am not sure either."
            js "I think we should leave this one up to you, [mc]."

    menu w0_d2_q1answer:
        #
        "15":
            #techscore -
            mc "I think it’s 15 because 3 times 5 is 15."
            mc "It’s as simple as that, let’s not overthink this."

            c "Oh my god."
            c "There is now way you just said that right now."
            c "The 5 OBVIOUSLY has quotations around it, making it a string."
            c "And when you multiply a string and an integer in Python,"
            c "It just prints the string, integer number of times."
            c "Literally EVERYONE knows that."
            js "Hey I didn’t know that."
            js "C++, you are kind of mean sometimes."
            js "You should really lay off, we are still going to get the question right."
            js "Since our string is ‘5’, the asterisk means that we repeat it 3 times making the answer ‘555’."
            p "C++, just because you have more experience than us doesn’t make you smarter than us."
            p "You have just been doing it for longer."
            c "Oh my gosh you guys are so sensitive."
            c "Whatever, I am sorry you got hurt by me stating facts."
            c "Let’s just see what everyone else said."
        "'15'":
            #tech score -
            mc "I think it's ‘15’ because 3 times 5 is 15."
            mc "But since the 5 has quotes around it, the answer will have quotes around it too."
            mc "It's as simple as that, let's not overthink this."

            c "Oh my god."
            c "There is now way you just said that right now."
            c "5 is a STRING, you can’t treat it like an INTEGER!!"
            c "So when you multiply a string and an integer in Python,"
            c "It just prints the string, integer number of times."
            c "Literally EVERYONE knows that."

            js "Hey I didn’t know that."
            js "C++, you are kind of mean sometimes."
            js "You should really lay off, we are still going to get the question right."
            js "Now we know that the answer is ‘555’, since we’re repeating the string ‘5’, 3 times."

            p "C++, just because you have more experience than us doesn’t make you smarter than us."
            p "You have just been doing it for longer."

            c "Oh my gosh you guys are so sensitive."
            c "Whatever, I am sorry you got hurt by me stating facts."
            c "Let’s just see what everyone else said."
        "'33333'":
            #tech score -
            mc "I think it’s ‘33333’ because the 5 has quotes around it and the 3 is just a normal number."
            mc "So something weird will have to happen."
            mc "I think that it will print num1, num2 number of times."
            mc "It’s as simple as that, let’s not overthink this."

            c "Oh my god."
            c "There is now way you just said that right now."
            c "The code might look confusing, but it's not trying to trick you."
            c "5 is a STRING, you can’t treat it like an INTEGER!!"
            c "And when you multiply a string and an integer in Python,"
            c "It just prints the string, integer number of times."
            c "Literally EVERYONE knows that."

            js "Hey I didn’t know that."
            js "C++, you are kind of mean sometimes."
            js "You should really lay off, we got the basic idea right."
            js "Something is getting repeated a number of times."
            js "We just switch the ‘numbers’ around and get '555'."

            p "C++, just because you have more experience than us doesn’t make you smarter than us."
            p "You have just been doing it for longer."

            c "Oh my gosh you guys are so sensitive."
            c "Whatever, I am sorry you got hurt by me stating facts."
            c "Let’s just see what everyone else said."
        "'555'":
            #tech score+ (CORRECT ANSWER)
            mc "Okay, wait. I think I actually know this one."
            mc "Since the 5 has quotations around it, the variables won’t just multiply normally."
            mc "So I think that it will print the variable that is a string once for each time it is multiplied by the integer."
            mc "So the answer should be ‘555’ since we’ll be printing ‘5’ three times."
            mc "Does that make sense?"

            js "I don’t really get it, why wouldn’t it be an error?"
            js "How can you multiply a string and an integer??"
            "Be Mean":
                #affects js -2x
                mc "Jesus Christ, I just explained it."
                mc "This really isn’t that hard, how do you not understand?"
                mc "It is just something that programming languages know how to do."
                mc "It makes printing something repeatedly quick and easy."
                mc "You really need to study before school even starts."
                mc "It seems like me and C++ might be the only smart people here..."

                js "Oh sorry..."

            "Be Nice":
                #affects js +
                mc "Its okay, I get it. It is a little confusing."
                mc "It is just something that programming languages know how to do."
                mc "It makes printing something repeatedly quick and easy."
                mc "This stuff can be confusing at first."
                mc "You might be thinking, how would I ever know that"
                mc "But with practice, and lots of repetition, it will start to click."

                js "Yeah, you’re right."
                js "Thanks for the explanation, I think I get it now."

            c "Jeez you guys are taking forever."
            c "Maybe try to think a little faster next round, I don’t want you guys to slow me down."
            c "Let’s see what everyone else said."
        "ERROR":
            #tech score -
            mc "I think it's going to be an error."
            mc "There’s no way you can multiply a number by a string."
            mc "That just doesn’t make any sense."
            mc "How will the computer know what to do?"
            mc "It’s as simple as that, let’s not overthink this."

            c "Oh my god."
            c "There is now way you just said that right now."
            c "The 5 OBVIOUSLY has quotations around it making it a string."
            c "And when you multiply a string and an integer in Python,"
            c "It just prints the string, integer number of times."
            c "Literally EVERYONE knows that."

            js "Hey I didn’t know that."
            js "C++, you are kind of mean sometimes."
            js "You should really lay off, we are still going to get the question right."
            js "So, now we know that, we need to repeat ‘5’ three times to get the answer ‘555’."

            p "C++, just because you have more experience than us doesn’t make you smarter than us."
            p "You have just been doing it for longer."

            c "Oh my gosh you guys are so sensitive."
            c "Whatever, I am sorry you got hurt by me stating facts."
            c "Let’s just see what everyone else said."

    bsl "Time’s up everyone!"
    bsl "Write your answers down and hold them up."
    "..."
    bsl "Wow! It looks like every team got that first question right!"
    bsl "This next one will be a little bit harder, get ready."
    bsl "What does the following Python code print?"

    #DISPLAY:
     #x = 4
     #for i in range(x):
     #x += 1
     #print(x, end=‘’)

     p "Well I think I have some idea about this one."
     p "The first thing I see is that this might be an infinite loop."
     p "Because we iterate x times, but x keeps increasing."
     p "But, maybe that loop range only references x one time."
     p "What do you think C++?"
     p "You seem to know everything..."

     c "Uhm, well actually I am not too sure."
     c "I was thinking it would be infinite as well."
     c "But I am really not sure."





jump w0_d3

