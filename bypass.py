import webbrowser
import os

print("-BYPASS-")
print("by. Griphly")
print("1. Bypass discord and any site [FREE]")
print("2. Bypass YouTube [FREE]")
print("3. Tor Mosts [FREE]")
print("4. Mulvad VPN [PAID]")
print("5. Exit")
bypass = input("Enter number: ")

if bypass == "1":
    print("Opened bypass...")
    url = "https://github.com/Flowseal/zapret-discord-youtube"
    webbrowser.open(url)
elif bypass == "2":
    print("Opened bypass...")
    url = "https://uboost.tube/"
    webbrowser.open(url)
elif bypass == "3":
    print("Opened mosts...")
    url = "https://torscan-ru.ntc.party/"
    webbrowser.open(url)
elif bypass == "4":
    print("Opened mulvad...")
    url = "https://mullvad.net/ru"
    webbrowser.open(url)
elif bypass == "5":
    print("Bye")