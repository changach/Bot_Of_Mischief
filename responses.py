import numpy as np
import random

def bot_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("yes"):
        return """
        A pick-up line a day,keeps the loneliness away :)
           what is your pick for today?
           /best
           /cute
           /funny
           /cheesy
           /dirty
        
       """
       
    if user_message in ("/cute"):
        
        cute_array=np.array([ 'I’d never play hide and seek with you because someone like you is impossible to find',

        'You may fall from the sky, you may fall from a tree, but the best way to fall… is in love with me.',

        'Roses are red, my face is too, that only happens when I’m around you',

        'Do you have a name or can I call you mine?',

        'I am going to complain to Spotify about you not being this weeks hottest single.',
        
        'If being in love was illegal, will you be my partner in crime?',
        
        'Roses are red, violets are blue, I’m not that pretty but damn look at you.',
        
        'Roses are red violets are blue I didn’t know what perfect was until I met you',
        
        'Your hand looks heavy can i hold it for you?',
        
        'Can I follow you? Cause my mom told me to follow my dreams',
        
        'Are you a camera? Because every time I look at you, I smile.',
        
        'Guess what I’m wearing? The smile you gave me!',
        
        'There’s only one thing I want to change about you. Your last name.',
        
        'I’m no organ donor but I’d be happy to give you my heart.',
        
        '(Holds out hand) Hey I’m going for a walk. Will you hold this for me?',
        
        'I would take you to the movies but they don’t allow snacks',
        
        'If kisses were snowflakes, I’d send you a blizzard.',
        
        'Roses are red, violets are blue, lava is hot and so are you.'
        
        'You know you’re in love when you can’t fall asleep because reality is finally better than your dreams.',
        
        'You know what’s beautiful? Read the first word.']) 
        
        return random.choice(cute_array)
    
    
    if user_message in ("/best"):

        best_array=np.array ([
          ' I’d never play hide and seek with you because someone like you is impossible to find',
            
           ' You may fall from the sky, you may fall from a tree, but the best way to fall… is in love with me.',
            
            'Roses are red, my face is too, that only happens when I’m around you',
            
           ' If being in love was illegal, will you be my partner in crime?',
            
            'Your hand looks heavy can i hold it for you?',
            
           ' On a scale of 1 to 10, you’re a 9. I’m the 1 you need.',
            
           ' Roses are red violets are blue I didn’t know what perfect was until I met you',
        
           ' Roses are red, violets are blue, I’m not that pretty but damn look at you.'
            
           ' Are you busy tonight at 3:00 A.M.?',
    
           ' People are catching Coronavirus but the only thing I’m catching is feelings for you.',
        
            'I’d never play hide and seek with you because someone like you is impossible to find',
            
            'Let me tie your shoes, cause I dont want you falling for anyone else.',
            
            'You may fall from the sky, you may fall from a tree, but the best way to fall… is in love with me.',
            
            'Roses are red, my face is too, that only happens when I’m around you',
            
            'Your hand looks heavy can i hold it for you?',
            
            'Roses are red violets are blue I didn’t know what perfect was until I met you',
            
            'Can I have your picture so I can show Santa what I want for Christmas?',
            
            'Can I follow you? Cause my mom told me to follow my dreams',
            
            'Roses are red, violets are blue, I’m not that pretty but damn look at you.',
            
            'I am going to complain to Spotify about you not being this weeks hottest single.',
            
           ' If being in love was illegal, will you be my partner in crime?',
            
           ' Do you have a name or can I call you mine?',
            
            'Are you a camera? Because every time I look at you, I smile.',
            
           ' On a scale of 1 to 10, you’re a 9. I’m the 1 you need.',
            
            'Covid 19 cancelling everything, except my feelings for you.',
            
            'Even if there wasn’t any gravity on earth, I would still fall for you!',
            
            'There’s only one thing I want to change about you. Your last name.',
            
            'You can’t spell Quarantine without u r a q t',
            
            'I would take you to the movies but they don’t allow snacks',
        
            'Would you grab my arm so I can tell my friends I’ve been touched by an angel?',
            
            'Can I borrow your cell phone? I need to call animal control, because I just saw a fox!',
            
           ' my dick is so polite… it stands up so you can sit down.',
        
            'I’m not actually this tall. I’m sitting on my wallet.',
            
            'Was you father an alien? Because there’s nothing else like you on Earth!',
            
            'Do you smoke pot because i have a kush on you.',
            
            'When I first saw you I looked for a signature, because every masterpiece has one.',
            
            'You know what’s the cutest thing I’ve ever seen…? Read the first word again.',
            
            'Hey girl, are you an architect? cos I can imagine building a relationship with you.',
            
            'are you today’s date? cos you’re 10/10',
            
            'Should I smile because we are friends, or cry because I know that is what we will ever be?',
            
           ' You’re kinda, sorta, basically, pretty much always on my mind.',
        
            'Are you as beautiful on the inside as you are on the outside?',
            
            'My friend thinks you’re kinda cute, but I don’t… I think you’re absolutely gorgeous!',
            
            'If you were a virus you would be CUTIE-19',
            
            'I wish I was your differential because then I’d be touching all your curves.',
            
           ' Baby, you’re body is like a hyperbola',
            
            'You fascinate me more than the fundamental theorem of calculus.',
            
           ' You must be the square root of two cause I feel irrational around you.',
            
           ' I want our love to be like pi, irrational and never ending.'])  
           
        return random.choice(best_array) 
    
   
    if user_message in ("/funny"):
        funny_array= np.array([
            'When I first saw you I looked for a signature, because every masterpiece has one.',
            
            'You like sleeping? Me too! We should do it together sometime.',
            
            ' If you were my homework, i’d do you everyday.',
            
            'Did it hurt when you fell from the vending machine? Cause you look like a snack!',
            
            'I wanna be superhero, should I be Spiderman, Batman or Yourman?',
            
            'Let’s play a game, winner dates loser.',
            
            'Hey Baby, you want to come to my house and work on your math skills? We can add the bed, subtract the cloths, divide the legs and multiply!',
            
            'Baby, you make my floppy disk turn into a hard drive',
            
            'Hey, how did you do that? (What?) Look so good?',
            
            'If I had a penny for every time I thought of you, I’d have exactly one cent, because you never leave my mind.',
            
            'Will you be my girlfrien? I left out the ‘d’ cause you’ll get that later!',
            
            'Are you terms and conditions? Cause whatever you say I’ll always agree with you.',
            
            'If I were to ask you out on a date, would your answer be the same as the answer to this question?',
            
            'If kisses were snowflakes, I’d send you a blizzard.',
            
            'Four plus four equals eight, but you plus me equals fate.',
            
            'I’m writing a term paper on the finer things in life, and I was wondering if I could interview you?',
            
            'Your body is 75% water, and I’m thirsty.',
        
            'F**k me if I am wrong, but haven’t we met before?',
            
            'Are you harembes enclosure? Cause i’ll drop a kid inside of you!',
            
            'Kissing is a language of love….so how about a conversation?']) 
        return random.choice(funny_array)


    
    if user_message in ("/cheesy"):
        cheesy_array= np.array([
       'Let me tie your shoes, cause I dont want you falling for anyone else.',
       ' Can I have your picture so I can show Santa what I want for Christmas?',
        'Even if there wasn’t any gravity on earth, I would still fall for you!',
       ' Let’s commit the perfect crime: I’ll steal you’re heart, and you’ll steal mine.',
        'If nothing lasts forever, will you be my nothing?',
        'What time do you have to be back in heaven?',
        'If a thousand painters worked for a thousand years, they could not create a work of art as beautiful as you.',
       ' No wonder the sky is grey today, all the blue is in your eyes.',
       ' I’m no photographer, but I can picture us together.',
        'Stop, drop, and roll, baby. You are on fire.',
        'Most people like to watch the Olympics, because they only happen once every 4 years, but I’d rather talk to you cause the chance of meeting someone so special only happens once in a lifetime.',
        'I never need to see the sun again because your eyes light up my world.',
        'Hi, I’m writing a term paper on the finer things in life, and I was wondering if I could interview you?',
        'I sneezed because God blessed me with you.',
        'My love for you is like dividing by zero– it cannot be defined.',
       ' How is your fever? [What fever?] Oh… you just look hot to me.',
       ' Was that an earthquake or did you just rock my world?',
        'I must be dancing with the devil, because you’re hot as hell.',
       ' If you stood in front of a mirror and help up 11 roses, you would see 12 of the most beautiful things in the world.',
        'I have to show you the prettiest girl I’ve ever seen. (show phone with frontcam)'])
       
        return random.choice(cheesy_array)
    

    if user_message in ("/dirty"):

        dirty_array=np.array([
           'When I saw you, I lost my tongue. Can I put yours in my mouth?',
            'Do you believe in evolution? Cause my homo is erectus.',
            'Are you a thief? Cause I want you to steal my virginity tonight!',
           ' You’re like my little toe, because I’m going to bang you on every piece of furniture in my home.',
            'You look so innocent, you look so sweet, as long as I have a face, you will always have a seat.',
           ' I love my bed but I’d rather be in yours.',
            'Roses are red, violets are twisted, bend over you’re about to get fisted',
            'Are you a poster? Because I want to pin you on a wall',
            'I like every bone in your body, especially mine.',
           ' Hey! Wanna play war? (replies) WHAT? (you) Yea, I lay on the ground and you blow the fuck outta me!',
            'Are you a blanket? cos I love it when you’re on top of me.',
            'You know why they call me the cat whisperer? Cause I know exactly what that pussy needs.',
            'Your body is a Wonderland an I’d like to be Alice',
           ' Damn, if being sexy was a crime, you’d be guilty as charged!',
            'Lets play titanic youll be the ocean and ill go down on you',
            'Life is like a dick. When it gets hard, “Fuck it”.',
            'My dick’s been feeling a little dead lately. Wanna give it some mouth-to-mouth?',
            'I’ll treat you like my homework: Slam you on the table and do you all night long!',
            'If your left leg was Christmas and your right was Thanksgiving, could I visit between the holidays?',
            'I’m like a Rubik’s Cube, the more you play with me the harder I get!',
            'I`m no weatherman, but you can expect a few inches tonight.',
            'Would you like to try an Australian kiss? It is just like a French kiss, but down under',
            'Fuck me if I’m wrong, but dinosaurs still exist right?',
            'Is there a cellphone in your backpocket? Cause that ass is calling me!',
            'Baby, I’m like a firefighter, I find ’em hot and leave ’em wet!',
            'The only reason I would kick you out of bed would be to fck you on the floor.',
            'Pizza is my second favourite thing to eat in bed.',
            'You work at a post office? Cause I saw you checking out my package.',
            'That dress looks really good on you but, it would look better on my bedroom floor.',
            'Hey baby, let’s play house, you can be the door and I’ll slam you all night long!',
           ' I hope you got a pet insurance, cause tonight I’m gonna destroy that pussy.',
            'You must be Medusa because you make me rock hard.',
            'Do you want to go on a ate? I’ll give you the D later',
           ' I’m no weather man, but you can expect more than a few inches tonight.',
            'I’m not too good at algebra, but doesn’t U+I = 69?',
           ' Are you a light switch? ‘Cause you turn me on!',
           ' Sex is evil; Evil is sin; Sin is forgiven; so let’s begin.',
            'How do you spell “me”? (M-E) You forgot the D (There’s no D in ME) Not yet ;)',
            'Look out in the night sky. You see that bright light to the right of that red one? That is a comet that is streaking toward here at 34546 miles per hour. At that rate, it will be here in about an hour. So, wanna fuck?',
            'Girl, I’m jealous of your heart. ‘Cause it’s pumping inside you and I’m not.'])
    return random.choice(dirty_array)

    
    

