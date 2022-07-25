import urllib.request

def getStatus():
    try:
        urllib.request.urlopen('http://pudimsdfdsdfd.com.br')
    except Exception:
        print(f"\nThe website is not online!\n")
    else:
        print("\nThe website is online!\n")


getStatus()