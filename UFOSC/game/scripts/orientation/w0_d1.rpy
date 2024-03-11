label w1_d1:
    scene w1_d1_sunnyhotel with longer_fade
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
    scene w1_d1_urgentcar with shorter_fade
    mc "What's my excuse, what's my excuse?"
    mc "I was sick? Family emergency? My car wouldn't start?"
    "*Turns key, car struggles*"
    mc "WAIT WAIT NOT ACTUALLY PLEASE START!!!"
    scene w1_d1_insidecar with shorter_fade
    "*Car starts, [mc] sighs from relief, speeds off*"
    mc "And I don't even know where I’m going. This city is all new to me!"
    mc "I am going to be so late."
    #"*Scene fades to the lecture hall.*" Current one is temporary
    scene w1_d1_lecturehall with longer_fade
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



jump w1_d2

