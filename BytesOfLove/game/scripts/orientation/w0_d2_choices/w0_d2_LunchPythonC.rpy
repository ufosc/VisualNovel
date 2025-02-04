label w0_d2_LunchPythonC:
    mc "\"Hey Python and C++, what did you guys get for lunch?\""
    show python_angry at left with easeinleft
    p "\"...\""
    mc "\"Look, I’m sorry about what happened earlier.\""
    mc "\"Do you think we can move past this and start over?\""
    hide python_angry
    show python_angry_talk at left
    p "\"I guess it would be nice if we all got along.\""
    p "\"What do you think, C++?\""
    hide python_angry_talk
    show python_angry at left
    show cpp_talk at right with easeinright
    c "\"I don’t care, do whatever you want.\""
    hide cpp_talk
    show cpp_normal at right
    hide python_angry
    show python_pocket_happy at left
    p "\"It’s settled then.\""
    p "\"No hard feelings, we’re all friends here.\""
    hide python_pocket_happy
    show python_pocket at left
    mc "\"Great. What did you get for lunch?\""
    hide python_pocket
    show python_pocket_happy at left
    p "\"I got a beef burrito and some plantains for lunch.\""
    p "\"It looks really good, and I am starving!\""
    hide python_pocket_happy
    show python_pocket at left
    mc "\"Yeah me too, I didn’t even get to eat breakfast.\""
    hide cpp_normal
    show cpp_talk at right
    c "\"Why not? You’re so stupid you don’t know how to cook?\""
    c "{i}Sighs{/i} \"Sorry that was mean, why didn’t you get breakfast??\""
    hide cpp_talk
    show cpp_normal at right
    mc "\"My morning was a mess.\""
    mc "\"I am from an area about 4 hours away from here and so I had to stay in a hotel.\""
    mc "\"And last night I was up way too late.\""
    mc "\"And as you can guess I didn’t wake up on time.\""
    hide cpp_normal
    show cpp_talk at right
    c "\"And that was why you barely made it to the room on time?\""
    hide cpp_talk
    show cpp_normal at right
    mc "\"Yeah, and that wasn’t even the worst part.\""
    mc "\"I rushed out the door and got to my car in like 3 minutes.\""
    mc "\"But when I started driving, I realized I didn’t even know where the school was.\""
    hide python_pocket
    show python_pocket_happy at left
    p "\"Yeah, I ran into the same problem.\""
    p "\"I have never been to Bytesborough before today.\""
    hide python_pocket_happy
    show python_pocket at left
    mc "\"Then I eventually got here and I realized I missed the start of orientation.\""
    mc "\"Luckily there was a professor there who told me where I was supposed to go.\""
    mc "\"And that’s how I ended up in the breakout room.\""
    hide cpp_normal
    show cpp_talk at right
    c "\"You met a professor?\""
    c "\"I don’t think there are any professors on campus right now.\""
    c "\"Since classes haven’t started, they have no reason to be here.\""
    hide cpp_talk
    show cpp_normal at right
    hide python_pocket
    show python_pocket_happy at left
    p "\"You’re right. Come to think of it, I haven't seen any professors either.\""
    hide python_pocket_happy
    show python_pocket at left
    mc "\"Huh, I didn’t think of that.\""
    mc "\"She was definitely older than us and seemed really knowledgeable.\""
    hide cpp_normal
    show cpp_talk at right
    c "\"You better not be trying to get ahead of me before the semester even starts.\""
    hide cpp_talk
    show cpp_normal at right
    mc "\"Don’t worry, I don’t have to try, I’m probably ahead of you already.\""
    mc "\"Anyway, what did you guys think about JavaScript?\""
    hide python_pocket
    show python_pocket_happy at left
    p "\"She seemed really nice.\""
    hide python_pocket_happy
    show python_pocket at left
    hide cpp_normal
    show cpp_talk at right
    c "\"She just does too much.\""
    c "\"She was always saying ‘slay’, or ‘queen’.\""
    
    menu w0_d2_JSAnnoying:
        c "\"Talk about being chronically online...\""

        "Make fun of JavaScript":
            hide cpp_talk
            show cpp_normal at right
            mc "\"Yeah, she is pretty annoying.\""
            # Add camera pan
            mc "\"Look over there, she’s sitting alone.\""
            mc "\"It makes sense when you think about it.\""
            mc "\"I wouldn’t want to sit with her either.\""

        "Defend JavaScript":
            hide cpp_talk
            show cpp_normal at right
            mc "\"I mean she can be a little much.\""
            mc "\"But I wouldn’t go as far as to say she is annoying.\""
            # Add camera pan
            mc "\"Look, she is sitting alone over there.\""
            mc "\"Do you guys want to go sit with her?\""
    
    hide python_pocket
    show python_pocket_happy at left
    p "\"I think we should go sit with her.\""
    p "\"She is probably feeling lonely.\""
    p "\"And we shouldn’t be mean to someone who could be our new friend.\""
    hide python_pocket_happy
    show python_pocket at left

    show js_normal with dissolve
    jump w0_d2_LunchApology
