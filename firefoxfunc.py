import webbrowser
def Firefox(URL):
    webbrowser.open(URL)
    
Fav_menu= {"google":"http://www.google.com",
         "youtube":"https://www.youtube.com",
         "github":"https://github.com"}
favweb=str(input("Write the website you want to open "+str(Fav_menu.keys()))).lower()
Firefox(Fav_menu[favweb])