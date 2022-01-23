import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

class UserChecker():
    def __init__(self, lang):
        self.sentence = "(This profile may not be the profile of the user you are looking for!)"
        self.notFound = "User not found"
        if lang == "tr":
            self.sentence = "(Bu profil, aradığınız kullanıcının profili olmayabilir!)"
            self.notFound = "Kullanıcı bulunamadı"
    
    def Twitter(self, username):
        header = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    }
        twitter = requests.get("https://api.twitter.com/graphql/P8ph10GzBbdMqWZxulqCfA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + username + "%22%2C%22withHighlightedLabel%22%3Atrue%7D", headers=header)
        try:
            twitter.json()["errors"]
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Twitter: {Style.RESET_ALL}"+ self.notFound)
        except KeyError:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Twitter: {Style.RESET_ALL}https://twitter.com/{username}")
        
    def GitHub(self, username):
        github = requests.get(f"https://github.com/{username}")
        if github.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}GitHub: {Style.RESET_ALL}"+ self.notFound)
        elif github.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}GitHub: {Style.RESET_ALL}https://github.com/{username}")
        else:
            pass
        
    def Yazbel(self, username):
        yazbel = requests.get(f"https://forum.yazbel.com/u/{username}")
        if yazbel.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}YazBel Forumu: {Style.RESET_ALL}"+ self.notFound)
        elif yazbel.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}YazBel Forumu: {Style.RESET_ALL}https://forum.yazbel.com/u/{username}")
        else:
            pass

    def Youtube(self, username):
        youtube = requests.get(f"https://www.youtube.com/c/{username}")
        if youtube.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Youtube: {Style.RESET_ALL}"+ self.notFound)
        elif youtube.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Youtube: {Style.RESET_ALL}https://www.youtube.com/c/{username}")
        else:
            pass
        
    def Replit(self, username):
        replit = requests.get(f"https://repl.it/@{username}")
        if replit.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Repl.it: {Style.RESET_ALL}"+ self.notFound)
        elif replit.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Repl.it: {Style.RESET_ALL}https://repl.it/@{username}")
        else:
            pass

    def TryHackme(self, username):
        tryhackme = requests.get(f"https://tryhackme.com/p/{username}")
        if tryhackme.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}TryHackMe: {Style.RESET_ALL}"+ self.notFound)
        elif tryhackme.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}TryHackMe: {Style.RESET_ALL}https://tryhackme.com/p/{username}")
        else:
            pass
        
    def Instagram(self, username):
        instagram = requests.get(f"https://www.instagram.com/{username}")
        if instagram.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Instagram: {Style.RESET_ALL}"+ self.notFound)
        elif instagram.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Instagram: {Style.RESET_ALL}https://www.instagram.com/{username}")
        else:
            pass

    def Reddit(self, username):
        html = BeautifulSoup((requests.get(f"https://www.reddit.com/user/{username}", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"}).content), "html.parser")
        try:
            check = html.find_all("h3", {"class":"_2XKLlvmuqdor3RvVbYZfgz"})[1].text
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Reddit: {Style.RESET_ALL}"+ self.notFound)
        except IndexError:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Reddit: {Style.RESET_ALL}https://www.reddit.com/user/{username}")
            
    def Duolingo(self, username):
        duolingo = requests.get(f"https://www.duolingo.com/2017-06-30/users?username={username}&_=1642946994401")
        if len(duolingo.json()["users"]) == 0:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Duolingo: {Style.RESET_ALL}"+ self.notFound)
        else:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Duolingo: {Style.RESET_ALL}https://www.duolingo.com/profile/{username}")

    def Steam(self, username):
        steam = requests.get(f"https://steamcommunity.com/search/SearchCommunityAjax?text={username}&filter=users&sessionid=77fea0b7b970929072567862&steamid_user=false&page=1",
                        headers={"Cookie": "sessionid=77fea0b7b970929072567862; steamCountry=TR%7Caf00fe0ae4fab79aa1cff82212541978; timezoneOffset=10800,0"})
        if steam.json()["search_result_count"] == 0:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Steam: {Style.RESET_ALL}"+ self.notFound)
        if steam.json()["search_result_count"] == 1:
            html = BeautifulSoup(steam.json()["html"], "html.parser")
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Steam: {Style.RESET_ALL}"+html.find("a", {"class":"searchPersonaName"})["href"])
        if steam.json()["search_result_count"] > 1:
            html = BeautifulSoup(steam.json()["html"], "html.parser")
            print(f"[+] {Fore.LIGHTGREEN_EX}Steam: {Style.RESET_ALL}"+html.find("a", {"class":"searchPersonaName"})["href"]+"  "+self.sentence)

    def Lichess(self, username):
        lichess = requests.get(f"https://lichess.org/@/{username}")
        if lichess.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Lichess: {Style.RESET_ALL}"+ self.notFound)
        elif lichess.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Lichess: {Style.RESET_ALL}https://lichess.org/@/{username}")
        else:
            pass

    def HackerOne(self, username):
        hackerone = requests.get(f"https://hackerone.com/{username}")
        if hackerone.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}HackerOne: {Style.RESET_ALL}"+ self.notFound)
        elif hackerone.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}HackerOne: {Style.RESET_ALL}https://hackerone.com/{username}")
        else:
            pass
        
    def SnapChat(self, username):
        snap = requests.post(f"https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={username}&xsrf_token=PlEcin8s5H600toD4Swngg",
                            headers={"Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg=="})
        if snap.json()["reference"]["status_code"] == "OK":
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}SnapChat: {Style.RESET_ALL}"+ self.notFound)
        if snap.json()["reference"]["status_code"] == "TAKEN":
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}SnapChat: {Style.RESET_ALL}https://www.snapchat.com/add/{username}")
        else:
            pass
        
    def TikTok(self, username):
        tiktok = requests.get(f"https://www.tiktok.com/@{username}")
        if tiktok.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}TikTok: {Style.RESET_ALL}"+ self.notFound)
        elif tiktok.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}TikTok: {Style.RESET_ALL}https://www.tiktok.com/@{username}")
        else:
            pass

    def StackOverFlow(self, username):
        sof = requests.get(f"https://stackoverflow.com/users/filter?search={username}")
        html = BeautifulSoup(sof.text, "html.parser")
        profiles = html.find_all("div", {"class":"user-details"})
        if len(profiles) == 0:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}StackOverFlow: {Style.RESET_ALL}"+ self.notFound)
        elif len(profiles) == 1:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}StackOverFlow: {Style.RESET_ALL}https://stackoverflow.com"+profiles[0].find("a")["href"])
        elif len(profiles) > 1:
            print(f"[+] {Fore.LIGHTGREEN_EX}StackOverFlow: {Style.RESET_ALL}https://stackoverflow.com"+profiles[0].find("a")["href"]+"  "+self.sentence)
        
    def Pinterest(self, username):
        pinterest = requests.get(f"https://pinterest.com/{username}")
        if pinterest.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Pinterest: {Style.RESET_ALL}"+ self.notFound)
        elif pinterest.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Pinterest: {Style.RESET_ALL}https://pinterest.com/{username}")
        else:
            pass
        
    def Vk(self, username):
        vk = requests.get(f"https://vk.com/{username}")
        if vk.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}VK: {Style.RESET_ALL}"+ self.notFound)
        elif vk.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}VK: {Style.RESET_ALL}https://vk.com/{username}")
        else:
            pass
        
    def Medium(self, username):
        medium = requests.get(f"https://medium.com/@{username}")
        if medium.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Medium: {Style.RESET_ALL}"+ self.notFound)
        elif medium.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Medium: {Style.RESET_ALL}https://medium.com/@{username}")
        else:
            pass