from typing import Sequence


#index[] = [Presedent, People, Environment, Treasury], scale=100

#----Group one, fire in the woods----#
{
    name: "Smoke in the Woods",
    desc: "Someone reports observing unusual smoke coming out of the woods",
    cards: [
        {
            card_name: "Do Nothing",
            card_desc: "Probobaly kids BBQ",
            card_effect:[0,0,-20,0],
            consequence:"You think it's not a big deal and decide not to worry about it",
        },
        {
            card_name: "Ask a Ranger",
            card_desc: "Hey, you know what's going on?",
            card_effect:[0,+10,0,0],
            consequence:"The ranger decide to check it out himself",
        },
        {
            card_name: "Let Me See",
            card_desc: "I'll go and have a look",
            card_effect:[0,0,0,-10],
            consequence:"You decide to travel to the woods",
        }
    ]
}

{
    name: "FIRE!",
    desc: "The smoke in the woods turns out to be a FIRE!",
    cards: [
        {
            card_name: "Do Nothing",
            card_desc: "Let it Burn",
            card_effect:[0,0,-30,0],
            consequence:"What's the big deal?",
        },
        {
            card_name: "Tries to Stop the Fire Yourself",
            card_desc: "That is very Brave of Me Indeed",
            card_effect:[+10,+10,-10,0],
            consequence:"You did your best",
        },
        {
            card_name: "Pay the Firefighters",
            card_desc: "For the heros!",
            card_effect:[0,0,0,-20],
            consequence:"You guys made it!",
        }
    ]
}

#-----------------#