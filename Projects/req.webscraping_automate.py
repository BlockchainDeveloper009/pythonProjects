import webbrowser, sys, pyperclip
import requests as req

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

def getTicker():
    try:
        base_url = "http://www.google.com/finance?q="
        ticker = input()

        urltext = req.get(base_url)


    except as e:
        print(e)
