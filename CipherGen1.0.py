#Ceaser Cipher Generator
#Haden Eagland 3/12/26 
#hadenmeagland@gmail.com

#The purpose of this is to refamiluize myself with python with a series of small projects.
#This code is not the most efficiant, I will not be importing anything or expanding it with a GUI.
#I will recreate it in java, where I am much more comfortable and compare.

#By the end of this project the user should be able to input a string to encrypt it. 

#Defining the alphbet with an Array our formula is (f(p) = (p + 3) mod 26)
Alphebet = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 

#MANUALLY defining each letter, I know there is a better method by putting the array in a variable 
#by using an string.index("x") to full out the desired character but I want to write it out
#I will obviously take that way in a professional environment.
A = Alphebet[0] 
B = Alphebet[1]
C = Alphebet[2]
D = Alphebet[3]
E = Alphebet[4]
F = Alphebet[5]
G = Alphebet[6]
H = Alphebet[7]
I = Alphebet[8]
J = Alphebet[9]
K = Alphebet[10]
L = Alphebet[11]
M = Alphebet[12]
N = Alphebet[13]
O = Alphebet[14]
P = Alphebet[15]
Q = Alphebet[16]
R = Alphebet[17]
S = Alphebet[18]
T = Alphebet[19]
U = Alphebet[20]
V = Alphebet[21]
W = Alphebet[22]
X = Alphebet[23]
Y = Alphebet[24]
Z = Alphebet[25]
#while this is extremly ugly, it was purposeful and intentionally made this way. 


#(f(p) = (p + 3) mod 26) formula used


print(r"""
▄█████ ▄▄ ▄▄▄▄  ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄     ▄████  ▄▄▄▄▄ ▄▄  ▄▄ 
██     ██ ██▄█▀ ██▄██ ██▄▄  ██▄█▄   ██  ▄▄▄ ██▄▄  ███▄██ 
▀█████ ██ ██    ██ ██ ██▄▄▄ ██ ██    ▀███▀  ██▄▄▄ ██ ▀██
""")

print("Welcome to my Cipher gen, this was made in 20 minutes; DO NOT include spaces or special characters in your text")
print("This is using a Ceaser Cipher shifted by 3, you can change this on line 85 to shift more.")
print("Source Code avaliable on GitHub, Thank you.")
Choice = "Y"
while Choice == "Y":
    UserInput = input("Please Enter You're String   ") #getting the input from user
    UserInput = UserInput.upper() #setting the input to uppercase 

    Splitter = list(UserInput) #splitting each letter into a list. 

    #Mapping the user inputs to the defined variables above; 
    SplitterCheck = {
        "A": A, "B": B, "C": C, "D": D, "E": E, "F": F,
        "G": G, "H": H, "I": I, "J": J, "K": K, "L": L,
        "M": M, "N": N, "O": O, "P": P, "Q": Q, "R": R,
        "S": S, "T": T, "U": U, "V": V, "W": W, "X": X,
        "Y": Y, "Z": Z
    }

    #I need to store each loop into a new list 
    Pass1Encryption = []
    for letter in Splitter: #Looping over each letter in the list I created, however, I could have just used UserInput.
                                    #Instead of making a seperate list and the outcome would have been the same.
                                        #Using my created list makes it easier to know what im working with. 
        #I wanted to see the original values 
       # Original = SplitterCheck[letter]
       # print("Original", Original)

        #Getting out first pass
        Pass1 = SplitterCheck[letter]
        Pass1 = ((Pass1 + 3) % 26) #"shifting" it 3 spaces and mod 26
        #print(Pass1)
        Pass1Encryption.append(Pass1) #appending each loop to the dictionary; it should store each value. 

    print(Pass1Encryption)

    #The next step is to convert our new dictonary back to letters
    Pass2List = {}
    for new, value in SplitterCheck.items():
        Pass2List[value] = new

    FinalEncryption = [] #The final Loop, this is comparing each number and giving it its new letter
    for number in Pass1Encryption:
        Final = Pass2List[number]
        FinalEncryption.append(Final)
    
    print(" -- Final String is --")
    print("".join(FinalEncryption)) #Printing the Final Cypher as a string

    Choice = input("Continue? Y/N   ") #prompts to go again.
    Choice = Choice.upper() 

