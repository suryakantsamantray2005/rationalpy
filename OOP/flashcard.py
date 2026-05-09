class FlashCard:

    def __init__(self):
        pass

    def frontpage(self):
        print("Welcome to Fruit Quiz!!")

    def dict(self):
        fruits={"banana":"yellow","strawberry":"pink","orange":"orange"
        ,"watermelon":"green","apple":"red","mango":"yellow",
        "blueberry":"blue"}
        import random
        key = random.choice(list(fruits.keys()))
        print("what is the colour of",key,"?")
        ans = input("enter the answer ")
        if ans.lower()==fruits[key]:
            print("correct answer")
            print("want to play again? PRESS 0")
            self.user_input=int(input(""))
            if self.user_input==0:
                return self.dict()

        else:
            print("wrong answer",fruits[key],"is correct answer")

        

f1=FlashCard()
f1.frontpage()
f1.dict()