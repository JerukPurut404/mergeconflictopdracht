import re
import oldgreeting
import random
print("merge oefening leuk!")

oldgreeting.greet()




def basicHaiku():
    return ["Toward those short trees","We saw a hawk descending","On a night in spring."]

def student2haiku():
    return["Mijn naam is Ryan Schorel","Ik ben twee meter en aan half lang", " Mijn broer is korter lol"]

haikus = [
    basicHaiku()
    student2haiku()
]

def randomHaiku():
    return random.choice(haikus)

def start():
    print("starting main")
    
    print(randomHaiku())

    pass


start()