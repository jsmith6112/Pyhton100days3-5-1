# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
tscore = 0
lscore = 0
TLove1 = name1.lower()
TLove2 = name2.lower()
Truelovecheck = TLove1 + TLove2
print(Truelovecheck)
T = int(Truelovecheck.count("t"))
tscore += T
R = int(Truelovecheck.count("r"))
tscore += R
U = int(Truelovecheck.count("u"))
tscore += U
E = int(Truelovecheck.count("e"))
tscore += E
L = int(Truelovecheck.count("l"))
lscore += L
O = int(Truelovecheck.count("o"))
lscore += O
V = int(Truelovecheck.count("v"))
lscore += V
textlscore = str(lscore)
texttscore = str(tscore)
Lovescore = int(texttscore + textlscore)
#print(Lovescore)
if Lovescore <= 10 or Lovescore > 90:
  print(f"Your score is {Lovescore}, you go together like coke and mentos.")
  if Lovescore >= 40 and Lovescore <=50:
    print(f"Your score is {Lovescore}, you are alright together.")
else:
  print(f"Your score is {Lovescore}")



