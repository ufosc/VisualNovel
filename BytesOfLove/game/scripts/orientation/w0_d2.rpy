label w0_d2:
    scene w0_d2_sunnyhotel with longer_fade
    "*You wake up in your hotel room and look at the clock. It's 9:30, orientation started 15 minutes ago.*"
    mc "WHAT THE HELL?!?!?"
    "*Checks phone, sees that its dead*"
    
    #scene change
    mc "Good going [mc], its not even the first day and you already messed up." 
    #scene is supposed to change for every sentence here
    mc "Who stays up for hours the night before college orientation??? I should just go back home," 
    mc "I’m not gonna succeed here." 
    mc "What was I thinking?!?!?"
    mc "Better late than never I guess, DANG IT!"
    "*Sprinting out the door to the car*"
    scene w0_d2_urgentcar with shorter_fade
    mc "What's my excuse, what's my excuse?"
    mc "I was sick? Family emergency? My car wouldn't start?"
    "*Turns key, car struggles*"
    mc "WAIT WAIT NOT ACTUALLY PLEASE START!!!"
    scene w0_d2_insidecar with shorter_fade
    "*Car starts, [mc] sighs from relief, speeds off*"
    mc "And I don't even know where I’m going. This city is all new to me!"
    mc "I am going to be so late."
    #"*Scene fades to the lecture hall.*" Current one is temporary
    scene w0_d2_lecturehall with longer_fade
    "*Bursts through the doors into a nearly empty auditorium, looks around frantically, notices Java.*" 
    #Java should not be known yet prob.

    #about to meet java on the script document
    "*Walks up to Java*"
    show java_temp at left with fade 

    mc "Excuse me ma’am, I’m so sorry that I’m late but I don’t know where to go or what to do."
    mc "My car wouldn't start and I had a family emergency and I got lost and …"
    j "Hey, it's okay. It's just orientation, calm down." 
    mc "*Panicked* Yeah but it's my first day and I feel like I am already messing everything up. What am I going to do??"
    j "Oh sweetie, don’t worry about it. Every journey has its own pace; being late doesn’t mean you won’t reach your destination."
    mc "*Stunned* Huh I guess you're right. Well, what'd I miss?"
    j "Sure, well the dean came in and introduced themself to the students"
    j "They said that everyone here was admitted because they are hard working, responsible, smart, and punctual."
    mc "Oh. Well that's just great"
    j "And then he dismissed them to go to all the different rooms where their orientation breakout groups will meet."
    j "You can go check on the list outside of the auditorium door to see what room you will be in."
    mc "Well how will I know where the room is? I don’t know anything about this school!"
    j "I am not sure, but you seem smart. I’m sure you will figure it out."
    j "Anyway I have to go, it was nice to meet you [mc]."
    j "*Winks before swiftly turning away and leaving*"
    hide java_temp with fade
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
    
    show cpp_temp with easeinright #moves cpp in from the right to the middle 

    c "*interrupting* Shut up, did it ever occur to you that maybe everyone is quiet for a reason?"
    mc "*Obediently stops talking and sits down, flustered.*"
    bsl "Alright, it looks like everyone is here."
    bsl "Go ahead and take some time to introduce yourself to those around you."

    show cpp_temp at left with move
    show python_temp with dissolve

    p "Hi guys!"
    p "My name is Python."
    p "I just moved here from Logicburg."
    p "I’m a computer science major."
    p "I really like playing tennis and reading books."

    show js_temp at right with easeinleft

    js "Oh my gosh, that is so cool, Python!"
    js "I am actually from Syntax Springs, but I played tennis in high school!"
    js "I’m also a computer science major, that’s really cool! Slay!"
    c "*grossed out* Uhm, anyway… My name is C++."
    c "I’m a computer science major with a lot of experience."
    c "I did a lot of coding in high school so I’m probably a lot better than you guys."
    c "What about you?"
    
    # Short interaction decided not to put in choices lmk if this is changed - Lazzy
    menu w0_d2_LateReason:
        c "Why were you so late?"

        "Honest":
            mc "I was up really late last night and my phone died before I fell asleep, so I missed my alarm."
            mc "Then this morning, I got lost on the way here and struggled to find the room."
            mc "It was a mess."

        "Cool":
            mc "So, I was on the way here this morning, and as I was getting to my car I heard a faint meow."
            mc "I looked up and saw a cat 20 feet up a tree."
            mc "I had to help this cat get down so I climbed the tree."
            mc "When I got to the top I noticed that the cat wasn’t afraid of the fall, but instead of the vulture a few feet away from it."
            mc "And then, after I rescued the cat, I had to stop by a women’s right protest, for more rights of course, and that took up a lot of my time."
            mc "I’m 6 foot by the way."
    
    mc "Anyway, my name is [mc]."
    mc "I’m also a computer science major, and I’m really excited to get my college experience started."
    mc "Why do you guys want to do computer science?"
    c "My mom is a software developer for iClicker and my Dad is a software developer for MentiMeter, so you could say it’s in my blood."
    c "I have been coding for as long as I can remember."
    js "Well aren’t you lucky."
    js "My mom is the worst person in the world."
    js "She is such a helicopter Mom, and won’t leave me alone."
    js "Even though I’m in college now she still won’t butt out of my life."
    js "She even came here with me."
    p "I mean at least you moved out of Syntax Springs, right?"
    js "That’s just it! She’s here in Byteborough with me! UGH!!!"
    js "Anyway that’s irrelevant, I’m in computer science because of its recent growth in popularity!"
    js "I’m so excited to meet new people and make a lot of friends!"
    js "What about you tennis queen?"
    p "Well it’s nice that your mom loves you that much. But I definitely get how that is."
    p "I think it is the future and I like learning new stuff."
    p "I’m not super passionate about a career in it but, I bet I will grow to love it."
    p "I think it will be a good choice."
    
    # Another short interaction not worth seperating files. Temporarily named everything "Respond to X" since I didnt know what to put - Lazzy
    menu w0_d2_BreakoutResponse1:
        "Respond to Javascript":
            mc "Yeah, it is pretty annoying that your mom won’t leave you alone."
            mc "Parents can be so annoying."
            mc "I wish my mom had cared enough to come with me to orientation though."
            js "Well actually…"

        "Respond to Python":
            mc "Yeah I agree with Python, computer science definitely seems cool."
            mc "I’m just like you, I don’t have much experience in programming, but I am definitely excited to learn."
            mc "I am also ready to make some money!!"

        "Respond to C++":
            c "I think it’s really cool that your parents work for those companies, C++."
            c "I have never heard of iClicker or Mentimeter."
            c "I don’t know much when it comes to coding, but you sound really experienced."
            c "Maybe you could show me the ropes sometime..?"
    
    bsl "Alright now, we’re gonna wrap up these conversations and start our guided tour of campus!"
     
    #tour just started put scene change

    "*The group tours campus as the guide talks about random trivia*"
    bsl "And if you look to your left you will see the Half-A-Century Tower…"
    c "Gosh this is so boring."
    c "Who doesn’t know all of this stuff already?"
    c "I mean did anybody really come to this school without already taking a tour."
    p "Wow this is interesting, I am enjoying this tour."

    #insert statuev1
    scene w0_d2_statue with fade

    p "Look at that cool statue over there."
    p "Don’t you guys think he looks cool?"
    c "Oh? You think that’s cool?"
    c "That statue is actually Thomas ‘Firewall’ Jackson."
    c "He was a general in a huge war a while ago and he killed a lot of people."
    c "You really think that someone like that is cool??"
    p "Oh, well I didn’t realize that…"
    c "Yeah, I wouldn’t expect someone like you to know something like that."
    js "Well I thought he was cool looking too, it was just an honest mistake."
    js "There's no need to be so aggressive C++..."

    menu w0_d2_StatueChoice:
        js "Do you agree with what im saying [mc] or are you on C++’s side?"

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
    "[mc] sees 3 tables. One is Python and C++, another is just JavaScript, and the last is a table of one guy."

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


jump w0_d3

