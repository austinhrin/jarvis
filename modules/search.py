### pip installed dependancies
import wolframalpha
import wikipedia

### user created dependancies
from config import WOLF_APPID

### initial variables
# wolframalpha
wolfClient = wolframalpha.Client(WOLF_APPID)

def wolf(search_term):
    try:
        response = next(wolfClient.query(search_term).results).text
        return response
    except StopIteration:
        response = wolfClient.query(search_term)
        response_pods_text = ''
        for pod in response.pod:
            for sub in pod.subpods:
                if sub.plaintext != None:
                    response_pods_text += sub.plaintext
        return response_pods_text
    except:
        error = f'Sorry I could not find {search_term} on Wolfram Alpha.'
        return error

def wiki(search_term):
    try:
        response = wikipedia.summary(search_term, sentences=4)
        return response
    except:
        error = f'Sorry I could not find {search_term} on Wikipedia.'
        return error