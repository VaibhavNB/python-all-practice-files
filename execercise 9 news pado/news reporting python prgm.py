#akhbar padke sunao

def speak(str):
   from win32com.client import Dispatch
   speak=Dispatch("SAPI.SpVoice")
   speak.Speak(str)

if __name__ == '__main__':
    speak("Today's News,Let's begin")
    import requests
    import json

    url = ('http://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=d52fc49713654b22b3bc5ea537b40ad3')
    news = requests.get(url).text
    news_dict=json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news,")
    speak("Thanks for listening, Have a good day.")
