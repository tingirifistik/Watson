from sendRequest import UserChecker
from os import system
from time import sleep
from colorama import Fore, Style

while 1:
    system("cls||clear")
    with open("config", "r") as f:
        r = f.read()
    if r == " ":
        try:
            lang = int(input("\n1- Türkçe\n2- English\n\nChoose: "))
        except ValueError:
            system("cls||clear")
            print("Please enter integer..")
            sleep(2)
            system("cls||clear")
            continue
        if lang != 1 and lang != 2:
            system("cls||clear")
            print("Please enter valid input..")
            sleep(2)
            system("cls||clear")
            continue
        if lang == 1:
            with open("config", "w") as f:
                f.write("language:tr")
        if lang == 2:
            with open("config", "w") as f:
                f.write("language:en")
    with open("config", "r") as f:
        r = f.read()
    language = r.split(":")[1]
    if language == "tr":
        username = "Kullanıcı Adı: "
        error = "Lütfen kullanıcı adı girin.."
        enter = "\n\nDevam etmek için enter'a basın.."
    elif language == "en":
        username = "Username: "
        error = "Please enter username.."
        enter = "\n\nPress enter to continue.."
    system("cls||clear")
    print(r"""
    ____            _       __      __
   / __ \_____     | |     / /___ _/ /__________  ____
  / / / / ___/     | | /| / / __ `/ __/ ___/ __ \/ __ \
 / /_/ / /  _      | |/ |/ / /_/ / /_(__  ) /_/ / / / /
/_____/_/  (_)     |__/|__/\__,_/\__/____/\____/_/ /_/

                                  by {}@_tingirifistik
""".format(Fore.LIGHTMAGENTA_EX))
    print(Style.RESET_ALL+username+ Fore.LIGHTYELLOW_EX, end="")
    username = input()
    if len(username) == 0:
        system("cls||clear")
        print(f"{Fore.LIGHTRED_EX}{error}{Style.RESET_ALL}")
        sleep(3)
        continue
    print(Style.RESET_ALL)
    system("cls||clear")
    with open(f"{username}-profile.txt", "w", encoding="utf-8") as f:
        for attribute in dir(UserChecker):
            attribute_value = getattr(UserChecker, attribute)
            if callable(attribute_value):
                if attribute.startswith('__') == False:
                    att = str(eval("UserChecker('{}').{}('{}')".format(language, attribute, username)))
                    if att == "None":
                        pass
                    else:
                        f.write(att+"\n")
        input(enter)
