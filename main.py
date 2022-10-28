import re
import newgreeting
import random
print("merge oefening leuk!")

newgreeting.greet()




def basicHaiku():
    return ["Toward those big trees","We saw a bird descending","On a night in spring."]

def student1haiku():
    return ["Jouw ogen zijn als vuur", "\nHet verbrandt mijn hart door en door", "\nDe hitte is voor altijd"]  

def student2haiku():
    return["Mijn naam is Ryan Schorel","Ik ben twee meter en aan half lang", " Mijn broer is korter lol"]

haikus = [
    basicHaiku(),
    student1haiku(),
    student2haiku()
]

def randomHaiku():
    return random.choice(haikus)

def start():
    print("starting main")
    
    print(randomHaiku())

    pass


start()