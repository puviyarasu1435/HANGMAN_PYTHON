import random
from draw import hang,animals,Fruits

def wordset():
    c=int(input("1) animals\n2) Fruits\n"))
    word_list= animals if c==1 else Fruits
    word= random.choice(word_list)
    enter=[]
    for i in word:
        enter.append("_")
    return (word,enter)
def enter_print(enter):
    var=""
    for i in enter:
        var+=i
        var+=" "
    print(var)
    if "_" not in enter:
        return True


def word_find(word,find,enter):
    if find in word:
        w_index=word.index(find)
        enter[w_index]=find
        return(enter_print(enter))
    else:
        return False
word,enter=wordset()
n=0
find=""
while True:
    print(word)
    if (n>=len(hang)-1):
        print(hang[n])
        print("game over!")
        if (int(input("replay(y/n)")=="y")):
            word,enter=wordset()
            n=0
            find=""
        else:break
    else:
        print(hang[n])
    find=str(input("Enter the word : ")).upper()
    run=word_find(word,find,enter)
    if (run==False):
        n+=1
    elif(run==True):
        print("won!")
        if (int(input("replay(y/n)")=="y")):
            word,enter=wordset()
            n=0
            find=""
        else:break
    else:
        print("great!")
