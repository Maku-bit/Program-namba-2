from random import randint
#my first program
#listing vegetables
global greens
greens=["sukuma_wiki","Terere","Kunde","Murenda","Speenach","Cabbage"]
fruits=["Oranges","Plums","Pears","Mangoes","Apples","Grapes","Ovacadoes"]
spices=["Onion","Pepper","Garlic","Tagawizi","Tomato","Masala"]
#using loops to display option for the user to select
def green():
    a=1
    for i in greens:
        r=randint(4,8)
        k="ksh........Per Kg."
        print(a,i,r,k)
        a=a+1
        #print(quantity,weight)
    user1=input("ENTER YOUR CHOOICE....")
    if user1=="1":
        user2=input("Enter Number Of SkumaWiki....")
    elif user1=="2":
        user2=input("Enter Number of Terere.....")
    elif user1=="3":
        user2=input("Enter number of Kunde.....")
    elif user1=="4":
        user2=input("Enter number of Murenda.....")
    elif user1=="5":
        user2=input("Enter number of Speenach....")
    elif user1=="6":
        user=input("Enter number of Cabbage....")
def fruit():
    a=1
    for i in fruits:
        r=randint(10,20)
        k="ksh........Per Kg."
        print(a,i,r,k)
        a=a+1
        #print(quantity,weight)
    user1=input("ENTER YOUR CHOOICE....")
    if user1=="1":
        user2=input("Enter Number Of orange....")
    elif user1=="2":
        user2=input("Enter Number of plums.....")
    elif user1=="3":
        user2=input("Enter number of pears.....")
    elif user1=="4":
        user2=input("Enter number of Mangoes.....")
    elif user1=="5":
        user2=input("Enter number of Apples....")
    elif user1=="6":
        user=input("Enter number of Grapes....")
def spices():
    a=1
    for i in spices:
        r=randint(30,70)
        k="ksh........Per Kg."
        print(a,i,r,k)
        a=a+1
        #print(quantity,weight)
    user1=input("ENTER YOUR CHOOICE....")
    if user1=="1":
        user2=input("Enter Number Of Onion....")
    elif user1=="2":
        user2=input("Enter Number of pepper.....")
    elif user1=="3":
        user2=input("Enter number of Garlic.....")
    elif user1=="4":
        user2=input("Enter number of Tangawizi.....")
    elif user1=="5":
        user2=input("Enter number of Tomato....")
    elif user1=="6":
        user=input("Enter number of Masala....")
print("SELECT CATEGORY....?")
print("1.GREENS")
print("2.FRUITS")
print("3.SPICES")
user3=input("SELECT CATEGORY...(1-3)")
if user3=="1":
    green()
elif user3=="2":
    fruit()
elif user3=="3":
    spices()
