#Greeting the user and introducing him/her about the game
print("Welcome to AK quiz!")
print("This is a game of knowledge. You earn based on your level of history's knowledge and awareness about past facts.")

#Importing required modules
import sys
import requests
from selenium import webdriver

#Creating a function for opening webpages
def open_web_page(url):
    try:
        driver = webdriver.Chrome("C:\\Users\\capta\\Documents\\chromedriver") #Setting up the webdriver
        driver.get(url) #Opening the webpage
    except Exception as e:
        print("Sorry, we are unable to reach the webpage.")
        print("Following exception occured:-")
        print(str(e)) #Printing the exception 

#Creating a function to validate crypto address
def validate_address(wallet_choice, wallet_address):
    url = "https://crypto-wallet-address-validator.p.rapidapi.com/validate/" + wallet_address

    querystring = {"currency":wallet_choice ,"network":"prod"}

    headers = {
        'x-rapidapi-host': "crypto-wallet-address-validator.p.rapidapi.com",
        'x-rapidapi-key': "c9a50d71bbmsh986ce6928856767p1381e8jsn95185302faab"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text

print("Do you want to make a crypto wallet account? (y/n) ")
choice = input()

if choice == "y":
    try:
        open_web_page("https://www.mathwallet.org") #Opening mathwallet webpage
    except Exception as e:
        print("Sorry, we are unable to reach the webpage.")
        print("Following exception occured:-")
        print(str(e)) #Printing the exception
elif choice == "n":
    pass
else:
    print("Invalid input")
    print("System exiting....")
    print("Press enter to exit....")

    input()

    sys.exit() #Exiting the system

#Taking user input of the wallet of his choice 
wallet_choice = int(input('''
Please enter your choice of wallet.
Input 1 for Bitcoin 
Input 2 for Ethereum
Press Enter after giving the input to continue....\n
'''))

if wallet_choice == 1:
    wallet_address = input("Press enter your BTC wallet address: ") #Taking user input of the wallet address

    print("Validating wallet address....")

    response = validate_address("btc", wallet_address) #Getting the validator response

    if "true" in response:
        print("Wallet address is valid.") #Wallet address valid
    elif "false" in response: 
        print("Wallet address is not valid.") #Wallet address invalid
        print("System exiting....")

        sys.exit() #Exiting the system
    else:
        pass 

elif wallet_choice == 2:
    wallet_address = input("Press enter your ETH wallet address: ") #Taking user input of the wallet address

    print("Validating wallet address....")

    response = validate_address("ETH", wallet_address) #Getting the validator response

    if "true" in response:
        print("Wallet address is valid.") #Wallet address valid
    elif "false" in response: 
        print("Wallet address is not valid.") #Wallet address invalid
        print("System exiting....")

        sys.exit() #Exiting the system
    else:
        pass 

print('''
Input 1 to get study material for the quiz
Input 2 to begin first round of the quiz
''')

choice = int(input()) #Getting user input

if choice == 1:
    choice2 = int(input(
'''
Input 1 for first round's material
Input 2 for second round's material
'''
    ))

    if choice2 == 1:
        open_web_page(r"https://www.gutenberg.org/cache/epub/56836/pg56836-images.html")

    elif choice2 == 2:
        open_web_page(r"https://www.gutenberg.org/cache/epub/30624/pg30624-images.html")

    else:
        print("Invalid input")
        print("System exiting....")
        print("Press enter to exit....")

        input()

        sys.exit() #Exiting the system

elif choice == 2:
    print("The first round of the quiz has started.")

    print("Instructions:-")
    print("Type the number of the correct option and press enter after typing.")
    print("You will get -2 points for each wrong answer and +4 point for each correct answer.")
    print("Good Luck!")

    points = 0

    q1 = int(input(
'''
Q1. Who conquered Constantinople?
1. Mehmed I
2. Mehmed II
3. Bayezid II
3. Bayezid I
'''
    ))

    if q1 == 2:
        print("Correct answer! You have gained 4 points!")

        points += 4
    else:
        print("Wrong answer. You have lost 2 points.")

        points -= 2

    q2 = int(input(
'''
Q2. When was constantinople conquered?
1. 1453
2. 1467
3. 1598
4. 1287
'''
    ))

    if q2 == 1:
        print("Correct answer! You have gained 4 points!")

        points += 4
    else:
        print("Wrong answer. You have lost 2 points.")

        points -= 2

    q3 = int(input(
'''
Q3. Pick Selim I's son from the following.
1. Ahmed Shah Abdali
2. Ertugrul
3. Bayezid I
4. Suleiman the Magnificent
'''
    ))

    if q3 == 4:
        print("Correct answer! You have gained 4 points!")

        points += 4
    else:
        print("Wrong answer. You have lost 2 points.")

        points -= 2

    q4 = int(input(
'''
Q4. Where did the ottoman sultans keep their brothers?
1. Golden Jail
2. Rose Bath
3. Brother's Jail
4. Royal Garden
'''
    ))

    if q4 == 1:
        print("Correct answer! You have gained 4 points!")

        points += 4
    else:
        print("Wrong answer. You have lost 2 points.")

        points -= 2

    if points >= 14:
        print("Congrats! You have passed the first round of the quiz.")
        print("You have earned ", points, " points.")
        print("You will get 1 usd in your wallet.")
        print("You are now eligible for the second round of the quiz.")

        print("Second round of the quiz begins now.")

        points = 0

        q1 = int(input(
'''
Q1. What was the name of Alexander the Great's horse?
1. Agamemnon
2. Bucephalus
3, Gimsky
4. Odysseus
'''
        ))

        if q1 == 2:
            print("Correct answer! You have gained 4 points!")

            points += 4
        else:
            print("Wrong answer. You have lost 2 points.")

            points -= 2

        q2 = int(input(
'''
Q2. Which territory was not under Alexander the Great?
1. Tyre
2. Egypt
3. Persia
4. Rome
'''
        ))

        if q2 == 4:
            print("Correct answer! You have gained 4 points!")

            points += 4
        else:
            print("Wrong answer. You have lost 2 points.")

            points -= 2

        q3 = int(input(
'''
Q3. What was the name of Alexander the Great's father?
1. Hamen
2. Philip
3. Gassetty
4. Olympio
'''
        ))

        if q3 == 2:
            print("Correct answer! You have gained 4 points!")

            points += 4
        else:
            print("Wrong answer. You have lost 2 points.")

            points -= 2

        q4 = int(input(
'''
Q4. Alexander is said to have cut which knot?
1. Gordian Knot
2. Olympian Knot
3. Greek Knot
4. Great Mesopotamian Knot
'''
        ))

        if q4 == 1:
            print("Correct answer! You have gained 4 points!")

            points += 4
        else:
            print("Wrong answer. You have lost 2 points.")

            points -= 2

        if points >= 14:
            print("Congrats! You have passed the first round of the quiz.")
            print("You have earned ", points, " points.")
            print("You will get 1 usd in your wallet.")
            print("You are now eligible for the second round of the quiz.")
        else:
            print("You have failed the quiz. You are not eligible for playing second round or getting prizes.")
            print("System exiting....")
            print("Press Enter to exit....")

            input()

            sys.exit() #Exiting the system

    else:
        print("You have failed the quiz. You are not eligible for playing second round or getting prizes.")
        print("System exiting....")
        print("Press Enter to exit....")

        input()

        sys.exit() #Exiting the system

else:
    pass
