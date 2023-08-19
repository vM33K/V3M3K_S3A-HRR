import os
import subprocess
import time
import sys

def open_in_chrome(url):
    chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    subprocess.run([chrome_path, url], check=True)

def printtext(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.005)

def print_ascii_art(text):
    for character in text:
        if character == " ":
            print("\033[95m", end="")
        elif character == "_":
            print("\033[95m", end="")  # purple
        elif character == "/":
            print("\033[91m", end="")  # yellow
        elif character == "o":
            print("\033[92m", end="")  # red
        elif character == "\\":
            print("\033[92m", end="")  # cyan
        elif character == "D":
            print("\033[95m", end="")
        elif character == "|":
            if text.count("D") % 2 == 0:
                print("\033[92m", end="")  # green
            else:
                print("\033[95m", end="")  # blue
        print(character, end="")
        time.sleep(0.0001)

def search():
    user_query = input("$3@X¢H: ")
    search_url = f"https://www.google.com/search?q={user_query}"
    open_in_chrome(search_url)

def youtube_search():
    user_query = input("$3@X¢H: ")
    search_url = f"https://www.youtube.com/results?search_query={user_query}"
    open_in_chrome(search_url)

def url_search():
    website_url = input("$ URL ")
    open_in_chrome(website_url)




def print_intro():
    text = r"""
    
-                                                                           -
-       _     _          _       _   _          _                  _        -
-     /\ \   /\ \    _ / /\     /\_\/\_\ _    /\ \                /\_\      -
-    /  \ \  \ \ \  /_/ / /    / / / / //\_\ /  \ \              / / /  _   -
-   / /\ \ \  \ \ \ \___\/    /\ \/ \ \/ / // /\ \ \            / / /  /\_\ -
-  / / /\ \ \ / / /  \ \ \   /  \____\__/ // / /\ \ \          / / /__/ / / -
-  \/_//_\ \ \\ \ \   \_\ \ / /\/________/ \/_//_\ \ \        / /\_____/ /  -
-    __\___ \ \\ \ \  / / // / /\/_// / /    __\___ \ \      / /\_______/   -
-   / /\   \ \ \\ \ \/ / // / /    / / /    / /\   \ \ \    / / /\ \ \      -
-  / /_/____\ \ \\ \ \/ // / /    / / /    / /_/____\ \ \  / / /  \ \ \     -
- /__________\ \ \\ \  / \/_/    / / /    /__________\ \ \/ / /    \ \ \    -
- \_____________\/ \_\/          \/_/     \_____________\/\/_/      \_\_\   -
-                                                                           -
-                                                                           -
-                                                                           -

"""

    os.system('cls')
    time.sleep(0.9)
    print_ascii_art(text)
    time.sleep(1)

def print_help():
    msg = r"""
    
$ search - search your fukin shit on google
$ youtube - search shit jack on youtube
$ url - type yo nigg ass url to search

"""

    time.sleep(0.9)
    print_ascii_art(msg)  # Print the help message
    time.sleep(1)





if __name__ == "__main__":
    print_intro()

    while True:
        start_prompt = input("\033[95m$ \033[0m")  # Set the input prompt to red

        start_prompt = start_prompt.lower()

        if start_prompt == "search":
            print_intro()  
            search()
        elif start_prompt == "qs":
            search()
        elif start_prompt == "youtube":
            print_intro()  
            youtube_search()
        elif start_prompt == "qy":
            os.system('cls')
            youtube_search()
        elif start_prompt == "url":
            print_intro()  
            url_search()
        elif start_prompt == "qud":
            os.system('cls')
            url_search()
        elif start_prompt == "help":
            print_help()
        else:
            print("\033[97mMXTHA FX#KA TYPE 'help' \033[0m")
            
            
            
            
            
      