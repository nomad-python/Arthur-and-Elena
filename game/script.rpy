# --- CHARACTER DEFINITIONS ---
define a = Character("Arthur", color="#a6a6a6") # Grey for his mood
define e = Character("Elena", color="#ffcc66")  # Warmth for her role


# --- IMAGES (Placeholders) ---
# image bg apartment_rain = "apartment_night.jpg"
# image arthur sitting = "arthur_tired.png"
# image elena concern = "elena_sit.png"

# --- START GAME ---
label start:
    play music "rainy_jazz.mp3"
    $ renpy.movie_cutscene("movie/roomwithtitle.webm", stop_music=False)
 
   
    #scene black with fade
      
    scene bg room with fade
  
    
    
    "The rain has been tapping against the window for three hours. It’s a rhythmic, insistent sound."
    "Inside, the apartment smells of stale woodsmoke and fresh coffee."

    
    "Arthur stares at his mug. He hasn't taken a sip in twenty minutes."
    e "It's getting cold, Arthur."
    a "The coffee?"
    e "The room. The coffee. Everything."

    "Arthur offers a faint, dry smile. It doesn't reach his eyes."

    a "Entropy, Elena. Everything cools down eventually. That's the one rule we can't break."

    e "You could turn the heater on. Or drink the coffee."

    "Arthur finally picks up the mug. He holds it with both hands, warming his palms, but he doesn't drink."

    scene bg artherlooking with fade

    a "I've done the math, you know. I woke up today, went to the office, moved the papers, came home. I pushed the rock up the hill."
    
    a "Tomorrow, it rolls back down. I just... I don't see the point in pushing it back up again. It’s not sad. It’s just logic."

    "Elena shifts in her chair. She crosses her legs, trying to look relaxed, but her fingers are gripping her own knee."

    # --- INTERNAL THOUGHTS ---

    scene bg elenaserious
    "Elena (Thinking)" "He’s retreated into pure logic. If I cry, he'll shut down. If I lecture him, he'll tune out. I need to choose my approach carefully."


    menu:
        #"Strategy: How do you dismantle his nihilism and embrace absurdism?"
        "Strategy: How do you dismantle his {a=https://en.wikipedia.org/wiki/Nihilism}Nihilism{/a} and make him embrace {a=https://en.wikipedia.org/wiki/Absurdism}Absurdism?{/a}. He also needs to understand {a=https://www.politicsphere.com/difference-between-absurdism-and-nihilism}difference between nihilism and absurdism{/a}"

        "Attack his Logic":
            # This appeals to his intellect
            jump path_logic

        "Pivot to the Senses (The Physical Argument)":
            # This appeals to his experience/feelings
            jump path_senses

# ------------------------------------------------------------------
# PATH A: LOGIC & REBELLION
# ------------------------------------------------------------------
label path_logic:

    scene bg closeup

    e "You talk about logic, but you're making a category error."

     
    "Elena leans forward, placing her elbows on her knees."

    e "You think realizing the pointlessness of the rock is the end of the story. Camus says that's just the beginning."

    a "Camus didn't work in corporate accounting, Elena."

    e "No. But he knew that giving up isn't a solution. It’s a surrender. You’re letting the silence win."

    "Arthur swirls the cold coffee in his mug."

    a "Maybe I want to surrender. The silence is heavy. Why carry the weight if there's no prize at the end?"

    "Elena watches him closely. She needs to define why he should carry it."


label choice1:


    menu:
        "What is the motivation for staying alive?"

        "Offer him Hope: 'Things might get better tomorrow.'":
            jump ending_bad_faith

        "Offer him Spite: 'Carry it to rebel against the silence.'":
            jump ending_rebel

label ending_bad_faith:
    # BAD ENDING
    e "Because you don't know what happens tomorrow, Arthur. Maybe the rock stays up. Maybe you meet someone. You can't quit before the miracle happens."

    "Arthur laughs. It’s a sharp, unpleasant sound."

    a "Miracles? Now you're selling me fairy tales. I don't want hope, Elena. Hope is just the carrot on the stick to keep the donkey walking."

    "He sets the mug down on the table with a final clack."

    a "I think you should leave. I'm tired of waiting for miracles."
    
    "The conversation dies. The rain sounds louder than before."

    # INTERNAL THOUGHTS
    
    scene bg elenaserious
    
    "Elena (Thinking)" "This did not work...I must try other approach."
    
    jump choice1

label ending_rebel:
    # GOOD ENDING (PHILOSOPHICAL)
    scene bg closeup
    e "There is no prize, Arthur. You carry the weight out of spite."

    "Arthur blinks, surprised. He looks at her properly for the first time tonight."

    a "Spite?"

    e "The universe is cold and indifferent. It wants you to be nothing. By living—by drinking that cold coffee and going to that stupid job, you are saying 'I exist' in spite of it all."
    
    e "Don't you want to prove you're stronger than the void?"

    "Arthur runs a hand through his hair. A genuine, crooked smile touches his lips."

    a "So... I should live just to piss off the universe?"

    e "Basically. One must imagine Sisyphus happy. Not because he likes the rock. But because the rock belongs to him."

    "Arthur picks up the coffee and finally takes a sip. He grimaces at the taste."

    a "It's terrible coffee."

    e "I know."

    a "I'll make a fresh pot. Not because it matters. But because it's mine."

    stop music fadeout 2.0
    
    scene bg good_end with fade
    
    "Elena relaxes back into the chair. He is safe for tonight."
    return


# ------------------------------------------------------------------
# PATH B: SENSES & CONNECTION
# ------------------------------------------------------------------
label path_senses:

    play music "rainy_jazz.mp3" fadein 3.0

    e "Stop doing math, Arthur. You're not a calculator."

    "Elena stands up and walks to the fireplace. She picks up a piece of wood and chucks at the fire."

    e "You live in your head. But you’re also here in this room. You can feel the chair? You can hear the rain?"

    a "Sensory data. It doesn't provide meaning. It just provides... texture."

    e "Texture is all we have! You used to love the texture of things. The ocean. The sun. Good scotch."

    a "The sun sets. The scotch runs out. It's fleeting, Elena. It's not enough to anchor a life."

    "Elena turns to face him. she comes back to sit down."

label choice2:

    menu:
        "He feels isolated. How do you anchor him? Offer {a=https://en.wikipedia.org/wiki/Hedonism}Hedonism{/a} or talk about togetherness in void"

        "Suggest Hedonism: We just need to find more pleasures.":

            jump ending_distraction

        "Offer Connection: 'We are in this void together.'":
            jump ending_anchor

label ending_distraction:
    # NEUTRAL/BAD ENDING
    e "So we find more scotch. We find new cities. We chase the sunset. If life is meaningless, we might as well have fun with it, right? Be a hedonist."

    "Arthur shakes his head slowly, looking exhausted."

    a "I don't have the energy for the chase, Elena. The Don Juan lifestyle... it requires a hunger I simply don't have."

    "He looks out the window."

    a "I think I just want to sleep."

    # INTERNAL THOUGHTS
    "Elena (Thinking)" "This did not work...I must try other approach."

   
    jump choice2

label ending_anchor:
    # GOOD ENDING (EMOTIONAL)
    e "It doesn't have to anchor a whole life. It just has to anchor tonight."

    "She walks over and sits on the ottoman right in front of him. She reaches out and covers his hand with hers."

    e "It's absurd that we are on a rock spinning in space. It's absurd that nothing means anything."
    
    e "But it's also absurd that I drove twenty minutes in the rain just to look at you. Isn't that enough of a truth for one night?"

    "Arthur looks at their joined hands. He squeezes her fingers, testing the reality of her touch."

    a "It is irrational."

    e "Completely."

    "Arthur lets out a long breath, his shoulders dropping two inches."

    a "I can't promise I'll find a reason for the next forty years."

    e "I'm not asking for forty years. I'm asking for you to stay for breakfast."

    "Arthur looks at her. His eyes are soft."

    a "Breakfast. I suppose I can manage that."


    scene bg good_end with fade

    "Elena smiles, relief washing over her. Thought of breakfast --a slice of bread with cheese cream-- makes her feel hungry and hopeful."

    return