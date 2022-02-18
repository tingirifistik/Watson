import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from json import dumps

class UserChecker():
    def __init__(self, lang):
        self.sentence = "(This profile may not be the profile of the user you are looking for!)"
        self.notFound = "User not found"
        self.found = "User found"
        if lang == "tr":
            self.sentence = "(Bu profil, aradığınız kullanıcının profili olmayabilir!)"
            self.notFound = "Kullanıcı bulunamadı"
            self.found = "Kullanıcı bulundu"
        
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
    
    def Twitch(self, username):
        data = {"operationName":"PlaybackAccessToken_Template","query":"query PlaybackAccessToken_Template($login: String!, $isLive: Boolean!, $vodID: ID!, $isVod: Boolean!, $playerType: String!) {  streamPlaybackAccessToken(channelName: $login, params: {platform: \"web\", playerBackend: \"mediaplayer\", playerType: $playerType}) @include(if: $isLive) {    value    signature    __typename  }  videoPlaybackAccessToken(id: $vodID, params: {platform: \"web\", playerBackend: \"mediaplayer\", playerType: $playerType}) @include(if: $isVod) {    value    signature    __typename  }}","variables":{"isLive":True,"login":username,"isVod":False,"vodID":"","playerType":"site"}}
        twitch = requests.post("https://gql.twitch.tv/gql", data=dumps(data), headers={"Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko"})
        if twitch.json()["data"]["streamPlaybackAccessToken"] != None:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Twitch: {Style.RESET_ALL}https://twitch.tv/{username}")
        elif twitch.json()["data"]["streamPlaybackAccessToken"] == None:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Twitch: {Style.RESET_ALL}"+ self.notFound)
        else:
            pass
        
    def BuyMeaCoffee(self, username):
        coffee = requests.get("https://www.buymeacoffee.com/"+username)
        if coffee.status_code == 404:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}BuyMeACoffee: {Style.RESET_ALL}"+ self.notFound)
        elif coffee.status_code == 200:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}BuyMeACoffee: {Style.RESET_ALL}https://www.buymeacoffee.com/{username}")
        else:
            pass
    
    def eksi(self, username):
        eksi = BeautifulSoup(requests.get("https://eksisozluk.com:443/biri/"+username, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"}).content, "html.parser")
        try:
            eksi.find("span", {"class":"field-validation-error"}).text
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}EksiSozluk: {Style.RESET_ALL}"+ self.notFound)
        except AttributeError:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}EksiSozluk: {Style.RESET_ALL}https://eksisozluk.com/biri/{username}")
            
#     def forumDev(self, username):
#         forumdev =  requests.get(f"https://forum.dev:443/index.php?members/find&q={username}&_xfRequestUri=%2F&_xfWithData=1&_xfToken=1644158403%2C41fa4d86d31f899cf2a10b162b176e79&_xfResponseType=json",  cookies={"xf_csrf": "7bzd3JhmM19VlaRt"})    
#         try:
#             forumdev.json()["results"][0]["id"]
#             print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Forum.dev: {Style.RESET_ALL}"+ self.found)
#         except IndexError:
#             print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Forum.dev: {Style.RESET_ALL}"+ self.notFound)
            
#     def technopat(self, username):
#         technopat = requests.get(f"https://www.technopat.net:443/sosyal/index.php?members/find&q={username}&_xfRequestUri=%2F&_xfWithData=1&_xfToken=1644159616%2Cf7b8804c9fc9e843089cce7e3dfe72fe&_xfResponseType=json", cookies={"xf_csrf": "S76M7bN9JapI9hpZ"})
#         try:
#             technopat.json()["results"][0]["id"]
#             print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Technopat: {Style.RESET_ALL}"+ self.found)
#         except IndexError:
#             print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Technopat: {Style.RESET_ALL}"+ self.notFound)
    
    def inciSozluk(self, username):
        inci = BeautifulSoup(requests.get("http://incisozluk.com.tr:80/u/"+username).content, "html.parser")
        try:
            inci.find("div", {"class":"alert alert-danger"}).text
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}InciSozluk: {Style.RESET_ALL}"+ self.notFound)
        except AttributeError:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}InciSozluk: {Style.RESET_ALL}http://incisozluk.com.tr/u/{username}")
