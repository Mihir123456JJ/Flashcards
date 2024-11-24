class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word + '-->' +self.meaning
flash = []
print("Welcome to the Flashcards app")
while True:
    word=input("Enter word:")
    meaning=input("Enter Meaning:")
    flash.append(flashcard(word,meaning))
    option=int(input("Enter 0 to continue and 1 to stop:"))
    if(option):
        break
print("\n Your Flashcards are:")
for i in flash:
    print("-->",i)    










        
        