label w0_d3:
    scene hotel_room_day with longer_fade  
    "{i}You wake up{/i}"
    mc"Uh oh, don’t tell me I slept through my alarm again!"
    "{i}You alarm goes off{/i}"
    mc"...Looks like I woke up right before it."
    mc"Much better than yesterday, let me start getting ready..."
    "{i}You brush your teeth, take a shower, and get dressed.{/i}"
    mc"All set! And I actually have enough time to eat breakfast this time!"
    scene hotel_buffet with shorter_fade
    mc"Oh wow! Everything looks so good!"
    "{i}While holding your food you notice that there is only one seat available, and it’s next to a boy who looks about your age.{/i}"
    mc"Well, I guess I’m eating with him."
    jump w0_d3_MeetingRust


label w0_d3_AfterMeetingRust:
    scene full_lecture_hall with longer_fade

    dc"\"Welcome to day 2 of orientation!\""
    dc"\"Yesterday we introduced you to the campus, and you got to meet some of your peers.\""
    dc"\"Today, you will all be picking your classes!\""
    dc"\"The choices you make today, will set the tone for the rest of your college career…\""
    dc"\"So choose wisely!\""

    mc"Oh man, this is a lot of pressure…"
    mc"I really hope I don’t mess anything up."
    mc"And I hope I’m able to get classes with all of the people I just met!"

    dc"\"Hello again, students!\""
    dc"\"If you are NOT in the College of Computing,\""
    dc"\"You are in the WRONG room!\""
    dc"\"From here, you will all go to your break out rooms from yesterday.\""
    dc"\"Then, your breakout room leaders will give you further instructions.\""

    scene empty_lecture_hall with shorter_fade

    mc"Well, at least I know where I’m going this time…"
    mc"And, I’m not late!"
    mc"This day is already off to a better start, let’s hope I can get the classes I want."

    scene breakout_room with fade

    bsl"\"Okay, as we found out yesterday, most of us here are computer science majors.\""
    bsl"\"So, before we go to the administration building, I will give you some tips on picking classes.\""

    c"\"Ugh, I wish we could just pick classes already.\""
    c"\"I don’t want to sit through this lady talking about stuff I already know.\""

    mc"\"You already know what classes you want to take?\""
    mc"\"I didn’t realize we were supposed to do research and stuff…\""

    p"\"I didn’t do any research either…\""
    p"\"I kinda figured they would just tell us what to pick.\""

    c"\"Jeez, you guys are hopeless.\""

    bsl"\"Okay, since most of you are freshmen in computer science, here are the classes you want to take.\""

    mc"I wonder if I really need to pay attention…"
    mc"Surely, I can just copy whatever C++ does?"
    mc"It seems like she always has it figured out…"
    jump w0_d3_CppCopy
    

label w0_d3_Registration:
    scene office with longer_fade
    show advisor at right with dissolve
    a"\"Hey there, sugar!\""
    a"\"Hmmm...\""
    a"\"Says 'ere your [mc]\""
    a"\"Is that right?\""

    mc"\"Yes ma’am, that’s me!\""

    a"\"Alrighty, the ‘ol machine says you’re a computer science major.\""
    a"\"I reckon you'll definitely need a programming class.\""
    a"\"Let me pull up a list of some options...\""
    a"\"Which of these catches your eye?\""

    menu choosingFirstClass:
        "Introduction to Programming I":
            mc"\"Well, I guess I've got to start somewhere. I’ll take Introduction to Programming 1.\""
            a"\"Well no duh. Let’s be honest kid, you ain't gonna make it in any of these other classes.\""
            a"\"So let's just move on along, take a gander at these next set of classes.\""

        "Introduction to Programming II":
            mc"\"I’m smart enough, I can probably test out of Introduction to Programming 1.\""
            mc"\"Let me give Introduction to Programming 2 a try.\""
            a"\"*Sighs* Oh sugar, bless your heart...\""
            a"\"You’d be as lost as a fish in a cornfield.\""
            jump choosingFirstClass

        " Data Structures and Algorithms":
            mc"\"This class sounds important, I’ll take Data Structures and Algorithms.\""
            a"\"You got that right on the button, sugar!\""
            a"\"That is one of the most important classes!\""
            a"\"But you gotta take Introduction to Programming 1 and 2 first.\""
            a"\"You’d be as lost as a fish in a cornfield.\""
            jump choosingFirstClass

        "Data Sorcery: Unveiling Secrets with Big Data Alchemy and Dark Analytics":
            mc"\"Woah, the Data Sorcery class sounds so cool!\""
            mc"\"I definitely want to take that.\""
            a"\"Well all right, sugar!\""
            a"\"I can work with that, let’s see if it’s available.\""
            mc"\"Awesome, I am so excited!\""
            mc"\"I can’t believe my first programming class is called Data Sorcery!\""
            mc"\"College is so cool!\""
            a"\"Oh my heavens...\""
            a"\"This usually doesn’t happen this early, but the class is all full!\""
            a"\"That’s crazy!\""
            mc"\"Aw man!\""
            mc"\"I was really looking forward to that...\""
            a"\"Well it’s alright sweetheart, don’t get your panties in a twist.\""
            jump choosingFirstClass

    a"\"We reckon freshmen best take 4 classes in total.\""
    a"\"How does that sit with you, sugar?\""
    mc"\"Uh, that sounds good to me.\""
    mc"\"I know I also want to take Calculus 1, is that available?\""
    a"\"Well, let’s have a look...\""
    a"\"Alright, Calculus 1 is available!\""
    mc"\"Oh, great!\""
    mc"\"So I just need two more classes...\""
    mc"\"What do you recommend?\""
    a"\"Well you ain't the first computer science kid I’ve had walk through those doors.\""
    a"\"Most of ‘em, I tell to take Professional Communication for Engineers.\""
    mc"\"Okay, I’ve heard of that.\""
    mc"\"Let’s do Professional Communication for Engineers.\""
    a"\"Alrighty, got it.\""
    a"\"The last class is all up to you, sweetheart\""
    a"\"Based on your current schedule here are some options,\""
    a"\"Pick whichever one tickles your fancy...\""

    menu choosingLastClass:
        "Women in French Literature and Cinema":
            mc"\"Well this seems pretty interesting.\""
            mc"\"I think I’ll take Women in French Literature And/Or Cinema.\""

        "Geology":
            mc"\"Well this seems pretty interesting.\""
            mc"\"I think I’ll take Geology.\""

        "First year Byteborough":
            mc"\"Well this seems pretty interesting.\""
            mc"\"I think I’ll take First Year ByteBorough.\""

        "Philosophy":
            mc"\"Well this seems pretty interesting.\""
            mc"\"I think I’ll take Philosophy.\""

    a"\"Well that settles it!\""
    a"\"Your classes for your first semester of college are now set!\""
    mc"\"Awesome!\""
    mc"\"So these will definitely be my classes?\""
    a"\"That depends, are biscuits supposed to be buttered?\""
    mc"\"Uhm, I think so?\""
    a"\"Well of course they are!\""
    a"\"I’ll just have to approve your classes and then it’ll be all set.\""
    mc"\"Okay, thank you so much!\""

    hide advisor with dissolve

    scene parking_lot with longer_fade

    mc"\"Wow, what a good day!\""
    mc"\"I made it to orientation on time and picked some good classes.\""
    mc"\"I am so excited to start college!\""
    show python_pocket   # moved this up to show python instead of later to fit next lines
    mc"\"Oh, look. There’s Python\""

    menu w0d3_talktopython:
        "Talk to Python":
            mc"\"Hey, Python!\""

            
            
            show python_pocket_happy with ease
            p"\"Oh, hey [mc]!\""
            p"\"How are you doing, did you get the classes you wanted?\""
            hide python_pocket_happy
            show python_pocket
            mc"\"Yeah, I did!\""
            mc"\"I obviously am taking Introduction to Programming 1,\""
            mc"\"And then I’m also taking Calculus 1.\""
            hide python_pocket
            #hide python_pocket
            #show python_pocket_happy at center

            show python_pocket_happy
            p"\"Oh, cool.\""
            p"\"I am taking those too.\""
            hide python_pocket_happy
            show python_pocket
            mc"\"What time is your Calculus 1 class?\""
            mc"\"Maybe we’ll have it together...\""
            hide python_pocket
            show python_pocket_happy
            # show python_pocket  ///should i have her make a neutral face here
            p"\"Hmm, let me check...\""
            hide python_pocket_happy
            show python_pocket
            hide python_pocket
            show python_pocket_happy
            p"\"Okay, it looks like mine is at 10:40 in Carlington Amphitheater.\""
            p"\"What about you?\""
            hide python_pocket_happy
            show python_pocket
            mc"\"No way, mine is too!\""
            mc"\"That’s good, at least I’ll know somebody.\""
            hide python_pocket
            p "{i}Smiles warmly{i}"
            p"\"Yeah I’m excited.\""
            p"\"Anyway I gotta run, I’ll see you in Fall!\""
            mc"\"Sure thing, bye!\""

            hide python_pocket_happy with fade

        "Go Home":
            mc"\"I can always see her another time, I don’t need to talk to her today.\""
            mc"\"Plus, I’m pretty tired, I just want to go back to the hotel.\""


    scene black with longer_fade

