# preinstalled python dependancies
import webbrowser

def open_url(url):
    if 'http://' not in url:
        url = 'http://' + url
    webbrowser.get().open_new_tab(url)