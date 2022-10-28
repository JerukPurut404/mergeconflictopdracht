import oldgreeting
import random
print("merge oefening leuk!")

oldgreeting.greet()




def basicHaiku():
    return ["Toward those big trees","We saw a bird descending","On a night in spring."]

def student1haiku():
    return ["Jouw ogen zijn als vuur", "\nHet verbrandt mijn hart door en door", "\nDe hitte is voor altijd"]  

#zet hier je haiku functie neer, zie https://github.com/progsen/haikugitopdracht voor ideeen

haikus = [
    basicHaiku()
    student1haiku()
]

def randomHaiku():
    return random.choice(haikus)

def start():
    print("starting main")
    
    print(randomHaiku())

    pass


start()