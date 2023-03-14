username = input("What is the username? ")
password = input("What is the password? ")

ID = ["a", "b"]
PSWD = ["a1", "b2"]
d = dict(zip(ID, PSWD))

if d[username] == password:
    print("Welcome!")
else:
    print("I don't know you.")



"""
Challenges
1. Investigate how you can prevent the password from being 
displayed on the screen in clear text when typed.
--> 리눅스에서 하는 법은 배웠는데 다른 플랫폼과 언어에서는 어떻게 하는 걸까

clear 2. Create a map of usernames and passwords and ensure
the username and password combinations match.

3. Encode the passwords using Bcrypt and store the hashes in the map 
instead of the clear-text passwords. 
Then, when you prompt for the password, encrypt the password 
using Bcrypt and compare it with the value in your map.    
--> POCU에서 배운 암호화 기법 사용(JAVA). 나중에 찾아서 해보자.
"""