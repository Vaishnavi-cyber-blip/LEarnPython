"""import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')

excel.Visible = True
_ = input("Press enter to Quit:")

excel.Application.Quit()"""
import json
import requests


def speak(write):
    from win32com.client import Dispatch
    done = Dispatch("SAPI.SpVoice")
    done.Speak(write)


url = ('http://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=5216299770364e759c5c4013d316566b')
response = requests.get(url).text
new_dict = json.loads(response)
art = new_dict['articles']
print(art)
for article in art:
    speak(article['title'])
    print(article['title'])
    speak("here is the detail")
    speak(article['description'])
    speak("moving to next news")

if __name__ == '__main__':
    speak("HII there")
