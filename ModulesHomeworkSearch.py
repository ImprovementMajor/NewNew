#Steps:
#importing module webbrowser
import webbrowser
import urllib.parse

def wikipedia(): #The LANGUAGE and the PAGE are entered by the user. Writing input method below:
    #Why it gives me an error?
    page_name= input("Please enter the page name")
    page_language = input("Please enter preffered language")
    page_name=urllib.parse.quote_plus(page_name)
    url = "https://"+page_language+".wikipedia.org/wiki/"+ page_name
    webbrowser.open_new_tab(url) #opens anythng in a browser 
wikipedia()

def google(inquiry_request):
    inquiry_request = urllib.parse.quote_plus(inquiry_request)
    url = "https://www.google.com/search?q=" + inquiry_request
    webbrowser.open_new_tab(url)
user_input=input("Please enter search request")
google(user_input)



# Applying quote_plus to the page to encode it. How do we apply it? Where do we write it? https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse
#Do we have to apply this part somewhere? urllib.parse.quote()
#Then just use + to construct a final URL, like "https://" + LANGUAGE + "wikipedia.org" etc. Finally, use open_new_tab to open this URL.
#How do I use it? Is it a part of the function?





#import urlib.parse # importing urlib.parse to apply quote_plus() later
#creating module search,
#def wikipedia(page_name, page_language) # defining arguments one is "page_name" and another "page_language"
# not sure  how to make this function work
# should I enter this url for wikipedia https://ЯЗЫКОВОЙ_КОД.wikipedia.org/wiki/НАЗВАНИЕ_СТРАНИЦЫ
# quote_plus()
# Some of the functions from the previous homework go here?
# raw_data to be changed on page_name? = urllib.request.urlopen(url).read()
# should we use parsed data somewhere as well? parsed_data['rates']

#def google(search_inquiry) ## defining an argument "search_inquiry"
