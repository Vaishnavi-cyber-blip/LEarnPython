import requests
import win32com.client

# Api helps to retreive data without even been aware of backend
# uses of api in situations when:
''' 1. when data s changing quickly  2. You want small piece of much larger info  '''


# Api request hits the api server
# We are using the api that doesn't requires the authentication


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    r = requests.get("http://newsapi.org/v2/everything?q=bitcoin&from=2020-10-25&sortBy=publishedAt&apiKey"
                     "=5216299770364e759c5c4013d316566b")
    print(r.json())  # output in jason format(dict encoded in string)