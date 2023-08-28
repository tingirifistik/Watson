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
        try:
            url = f"https://twitter.com:443/i/api/graphql/SAMkL5y_N9pmahSw8yy6gw/UserByScreenName?variables=%7B%22screen_name%22%3A%22{username}%22%2C%22withSafetyModeUserFields%22%3Atrue%7D&features=%7B%22hidden_profile_likes_enabled%22%3Afalse%2C%22hidden_profile_subscriptions_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22subscriptions_verification_info_is_identity_verified_enabled%22%3Afalse%2C%22subscriptions_verification_info_verified_since_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D&fieldToggles=%7B%22withAuxiliaryUserLabels%22%3Afalse%7D"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://twitter.com/MGokhanAhisdsd", "Content-Type": "application/json", "X-Csrf-Token": "4e1d872c3d95c029d51a9c9136a4744a", "X-Guest-Token": "1693953685385080832", "X-Twitter-Client-Language": "tr", "X-Twitter-Active-User": "yes", "X-Client-Transaction-Id": "TdzFsKO7pD/6n9CL4l+USnul+V5dbtzTiUnmvAKVW5fHREw/S3rXilcAWHjQsPcdmfFw2E3bNJO9Trok5ppYxBr7ytnPTA", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA", "Te": "trailers"}
            twitter = requests.get(url, headers=headers)
            if len(twitter.json()["data"]) != 0:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Twitter: {Style.RESET_ALL}https://twitter.com/{username}")
                return ("Twitter: https://twitter.com/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Twitter: {Style.RESET_ALL}"+ self.notFound)
             
    def GitHub(self, username):
        try:
            github = requests.get(f"https://github.com/{username}")
            if github.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}GitHub: {Style.RESET_ALL}https://github.com/{username}")
                return ("GitHub: https://github.com/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}GitHub: {Style.RESET_ALL}"+ self.notFound)
            
            
    def Yazbel(self, username):
        try:
            yazbel = requests.get(f"https://forum.yazbel.com/u/{username}")
            if yazbel.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}YazBel Forumu: {Style.RESET_ALL}https://forum.yazbel.com/u/{username}")
                return ("YazBel: https://forum.yazbel.com/u/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}YazBel Forumu: {Style.RESET_ALL}"+ self.notFound)
            

    def Youtube(self, username):
        try:
            url = f"https://www.youtube.com:443/@{username}"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Upgrade-Insecure-Requests": "1", "Service-Worker-Navigation-Preload": "true", "Dnt": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            youtube = requests.get(url, headers=headers)
            if youtube.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Youtube: {Style.RESET_ALL}https://www.youtube.com/@{username}")
                return ("Youtube: https://www.youtube.com/@" + username)  
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Youtube: {Style.RESET_ALL}"+ self.notFound)
                  
        
    def Replit(self, username):
        try:
            replit = requests.get(f"https://repl.it/@{username}")
            if replit.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Replit: {Style.RESET_ALL}https://repl.it/@{username}")
                return ("Replit: https://repl.it/@" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Replit: {Style.RESET_ALL}"+ self.notFound)
            

    def TryHackme(self, username):
        try:
            url = f"https://tryhackme.com:443/p/{username}"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Dnt": "1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Te": "trailers"}
            tryhackme = requests.get(url, headers=headers, allow_redirects=False)
            if tryhackme.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}TryHackMe: {Style.RESET_ALL}https://tryhackme.com/p/{username}")
                return ("TryHackMe: https://tryhackme.com/p/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}TryHackMe: {Style.RESET_ALL}"+ self.notFound)
            
        
    def Instagram(self, username):
        try:
            url = f"https://www.instagram.com:443/api/v1/users/web_profile_info/?username={username}"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "X-Csrftoken": "yhm91gqzYfAIV2f1hKSbz0FboHa2OYM9", "X-Ig-App-Id": "936619743392459", "X-Asbd-Id": "129477", "X-Ig-Www-Claim": "0", "X-Requested-With": "XMLHttpRequest", "Dnt": "1", "Referer": "https://www.instagram.com/042601ab/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            insta = requests.get(url, headers=headers)
            if insta.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Instagram: {Style.RESET_ALL}https://www.instagram.com/{username}")
                return ("Instagram: https://www.instagram.com/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Instagram: {Style.RESET_ALL}"+ self.notFound)
            

    def Reddit(self, username):
        try:
            headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0"}
            params = {"user": username}
            reddit = requests.get('https://www.reddit.com/api/username_available.json', params=params, headers=headers)
            if reddit.text == "false":
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Reddit: {Style.RESET_ALL}https://www.reddit.com/user/{username}")
                return ("Reddit: https://www.reddit.com/user/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Reddit: {Style.RESET_ALL}"+ self.notFound)
        
        
    def Steam(self, username):
        try:
            steam = requests.get(f"https://steamcommunity.com/search/SearchCommunityAjax?text={username}&filter=users&sessionid=77fea0b7b970929072567862&steamid_user=false&page=1",
                            headers={"Cookie": "sessionid=77fea0b7b970929072567862; steamCountry=TR%7Caf00fe0ae4fab79aa1cff82212541978; timezoneOffset=10800,0"})
            if steam.json()["search_result_count"] == 0:
                raise
            elif steam.json()["search_result_count"] == 1:
                html = BeautifulSoup(steam.json()["html"], "html.parser")
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Steam: {Style.RESET_ALL}"+html.find("a", {"class":"searchPersonaName"})["href"])
                return ("Steam: " + html.find("a", {"class":"searchPersonaName"})["href"])
            elif steam.json()["search_result_count"] > 1:
                html = BeautifulSoup(steam.json()["html"], "html.parser")
                print(f"[+] {Fore.LIGHTGREEN_EX}Steam: {Style.RESET_ALL}"+html.find("a", {"class":"searchPersonaName"})["href"]+"  "+self.sentence)
                return ("Steam: " + html.find("a", {"class":"searchPersonaName"})["href"]+"  "+self.sentence)
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Steam: {Style.RESET_ALL}"+ self.notFound)
            
            
    def Lichess(self, username):
        try:
            lichess = requests.get(f"https://lichess.org/@/{username}")
            if lichess.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Lichess: {Style.RESET_ALL}https://lichess.org/@/{username}")
                return ("Lichess: https://lichess.org/@/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Lichess: {Style.RESET_ALL}"+ self.notFound)
            
            
    def HackerOne(self, username):
        try:
            hackerone = requests.get(f"https://hackerone.com/{username}")
            if hackerone.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}HackerOne: {Style.RESET_ALL}https://hackerone.com/{username}")
                return ("HackerOne: https://hackerone.com/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}HackerOne: {Style.RESET_ALL}"+ self.notFound)
        

    def TikTok(self, username):
        try:
            tt = requests.head("https://www.tiktok.com/@"+username, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0", "accept-language": "en-US"})
            if tt.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}TikTok: {Style.RESET_ALL}https://www.tiktok.com/@{username}")
                return ("TikTok: https://www.tiktok.com/@" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}TikTok: {Style.RESET_ALL}"+ self.notFound)
            

    def StackOverFlow(self, username):
        try:
            sof = requests.get(f"https://stackoverflow.com/users/filter?search={username}")
            html = BeautifulSoup(sof.text, "html.parser")
            profiles = html.find_all("div", {"class":"user-details"})
            if len(profiles) == 0:
                raise
            elif len(profiles) == 1:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}StackOverFlow: {Style.RESET_ALL}https://stackoverflow.com"+profiles[0].find("a")["href"])
                return ("StackOverFlow: https://stackoverflow.com"+profiles[0].find("a")["href"])
            elif len(profiles) > 1:
                print(f"[+] {Fore.LIGHTGREEN_EX}StackOverFlow: {Style.RESET_ALL}https://stackoverflow.com"+profiles[0].find("a")["href"]+"  "+self.sentence)
                return ("StackOverFlow: https://stackoverflow.com"+profiles[0].find("a")["href"]+"  "+self.sentence)
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}StackOverFlow: {Style.RESET_ALL}"+ self.notFound)
            
        
    def Vk(self, username):
        try:
            url = f"https://m.vk.com:443/{username}"
            cookies = {" remixmdevice": "31"}
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Dnt": "1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Te": "trailers"}
            vk = requests.get(url, headers=headers, cookies=cookies)
            if vk.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}VK: {Style.RESET_ALL}https://vk.com/{username}")
                return ("VK: https://vk.com/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}VK: {Style.RESET_ALL}"+ self.notFound)
            
            
    def Medium(self, username):
        try:
            url = f"https://medium.com:443/@{username}"
            medium = requests.get(url)
            if "PAGE NOT FOUND" in medium.text:
                print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Medium: {Style.RESET_ALL}"+ self.notFound)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Medium: {Style.RESET_ALL}https://medium.com/@{username}")
            return ("Medium: https://medium.com/@" + username)
        
        
    def Twitch(self, username):
        try:
            data = {"operationName":"PlaybackAccessToken_Template","query":"query PlaybackAccessToken_Template($login: String!, $isLive: Boolean!, $vodID: ID!, $isVod: Boolean!, $playerType: String!) {  streamPlaybackAccessToken(channelName: $login, params: {platform: \"web\", playerBackend: \"mediaplayer\", playerType: $playerType}) @include(if: $isLive) {    value    signature    __typename  }  videoPlaybackAccessToken(id: $vodID, params: {platform: \"web\", playerBackend: \"mediaplayer\", playerType: $playerType}) @include(if: $isVod) {    value    signature    __typename  }}","variables":{"isLive":True,"login":username,"isVod":False,"vodID":"","playerType":"site"}}
            twitch = requests.post("https://gql.twitch.tv/gql", data=dumps(data), headers={"Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko"})
            if twitch.json()["data"]["streamPlaybackAccessToken"] != None:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Twitch: {Style.RESET_ALL}https://twitch.tv/{username}")
                return ("Twitch: https://twitch.tv/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Twitch: {Style.RESET_ALL}"+ self.notFound)
            
            
    def BuyMeaCoffee(self, username):
        try:
            url = f"https://www.buymeacoffee.com:443/{username}"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Dnt": "1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Te": "trailers"}
            coffee = requests.get(url, headers=headers)  
            if coffee.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}BuyMeACoffee: {Style.RESET_ALL}https://www.buymeacoffee.com/{username}")
                return ("BuyMeACoffee: https://www.buymeacoffee.com/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}BuyMeACoffee: {Style.RESET_ALL}"+ self.notFound)
            
            
    def Eksi(self, username):
        try:
            eksi = BeautifulSoup(requests.get("https://eksisozluk.com:443/biri/"+username, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"}).content, "html.parser")
            try:
                eksi.find("span", {"class":"field-validation-error"}).text
                print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}EksiSozluk: {Style.RESET_ALL}"+ self.notFound)
            except AttributeError:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}EksiSozluk: {Style.RESET_ALL}https://eksisozluk.com/biri/{username}")
                return ("EksiSozluk: https://eksisozluk.com/biri/" + username)
        except:
            pass
        
        
    def InciSozluk(self, username):
        try:
            inci = requests.get(f"http://www.incisozluk.com.tr:80/u/{username}/")
            if "ye bulunamad" in inci.text:
                print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}InciSozluk: {Style.RESET_ALL}"+ self.notFound)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}InciSozluk: {Style.RESET_ALL}http://incisozluk.com.tr/u/{username}")
            return ("InciSozluk: http://incisozluk.com.tr/u/" + username)
        

    def Genius(self, username):
        try:
            genius = requests.get("https://genius.com/"+username)
            if genius.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Genius: {Style.RESET_ALL}https://genius.com/{username}")
                return ("Genius: https://genius.com/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Genius: {Style.RESET_ALL}"+ self.notFound)
            
            
    def Soundcloud(self, username):
        try:
            sc = requests.get("https://soundcloud.com/"+username)
            if sc.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}SoundCloud: {Style.RESET_ALL}https://soundcloud.com/{username}")
                return ("Soundcloud: https://soundcloud.com/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}SoundCloud: {Style.RESET_ALL}"+ self.notFound)
            
                       
    def Vsco(self, username):
        try:
            url = f"https://vsco.co:443/{username}/gallery"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Dnt": "1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Te": "trailers"}
            vsco = requests.get(url, headers=headers)
            if vsco.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}VSCO: {Style.RESET_ALL}https://vsco.co/{username}")
                return ("VSCO: https://vsco.co/" + username)
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}VSCO: {Style.RESET_ALL}"+ self.notFound)
            
    
    def Snapchat(self, username):
        try:
            url = "https://www.snapchat.com:443/add/"+ username
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Dnt": "1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Te": "trailers"}
            snap = requests.get(url, headers=headers)
            if snap.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}SnapChat: {Style.RESET_ALL}https://www.snapchat.com/add/{username}")
                return ("SnapChat: https://www.snapchat.com/add/" + username)
            else:
                raise   
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}SnapChat: {Style.RESET_ALL}"+ self.notFound)


    def Ok(self, username):
        try:
            url = "https://ok.ru:443/web-api/v2/search/portal"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://ok.ru/search?tin", "Tkn": "undefined", "Strd": "false", "Strv": "null", "Msver": "V1", "Ok-Screen": "anonymSearchResult", "Content-Type": "text/plain;charset=UTF-8", "Origin": "https://ok.ru", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            json={"id": 5, "parameters": {"filters": {"st.grmode": "Groups", "st.mode": "Users", "st.query": username}, "query": username}}
            ok = requests.post(url, headers=headers, json=json)
            try:
                profile = ok.json()["result"]["users"]["values"]["results"][0]["user"]["href"]
                if len(ok.json()["result"]["users"]["values"]["results"]) == 1:
                    print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Ok: {Style.RESET_ALL}https://ok.ru"+profile)
                    return ("Ok: https://ok.ru" + profile)
                elif len(ok.json()["result"]["users"]["values"]["results"]) > 1:
                    print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Ok: {Style.RESET_ALL}https://ok.ru"+profile+"  "+self.sentence)
                    return ("Ok: https://ok.ru" + profile+"  "+self.sentence)
            except KeyError:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Ok: {Style.RESET_ALL}"+ self.notFound)
            
    
    def Izlesene(self, username):
        try:
            izlesene = requests.get(f"https://www.izlesene.com:443/kanal/{username}")
            if izlesene.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Izlesene: {Style.RESET_ALL}https://www.izlesene.com/kanal/{username}")
                return ("Izlesene:"+ "https://www.izlesene.com/kanal/{username}")
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Izlesene: {Style.RESET_ALL}"+ self.notFound)
            
    
    def Tumblr(self, username):
        try:
            tum = requests.get(f"https://www.tumblr.com:443/{username}", allow_redirects=False)
            if tum.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Tumblr: {Style.RESET_ALL}https://www.tumblr.com/{username}")
                return ("Tumblr:"+ "https://www.tumblr.com/{username}")
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Tumblr: {Style.RESET_ALL}"+ self.notFound)
    
    
    def Disqus(self, username):
        try:
            disqus = requests.get(f"https://disqus.com:443/by/{username}/")
            if disqus.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Disqus: {Style.RESET_ALL}https://disqus.com/by/{username}")
                return ("Disqus:"+ "https://disqus.com/by/{username}")
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Disqus: {Style.RESET_ALL}"+ self.notFound)
    
    
    def KizlarSoruyor(self, username):
        try:
            url = "https://www.kizlarsoruyor.com:443/uye/"+username
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Upgrade-Insecure-Requests": "1", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "same-origin", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            kiz = requests.get(url, headers=headers)
            if kiz.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Kizlarsoruyor: {Style.RESET_ALL}https://www.kizlarsoruyor.com/uye/{username}")
                return ("Kizlarsoruyor:"+ "https://www.kizlarsoruyor.com/uye/{username}")
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Kizlarsoruyor: {Style.RESET_ALL}"+ self.notFound)
    
    
    def Onedio(self, username):
        try:
            onedio = requests.get("https://onedio.com:443/profil/"+username)
            if onedio.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}+{Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Onedio: {Style.RESET_ALL}https://onedio.com/profil/{username}")
                return ("Onedio:"+ "https://onedio.com/profil/{username}")
            else:
                raise
        except:
            print(f"[{Fore.LIGHTRED_EX}-{Style.RESET_ALL}] {Fore.LIGHTRED_EX}Onedio: {Style.RESET_ALL}"+ self.notFound)
