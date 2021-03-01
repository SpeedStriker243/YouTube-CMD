import webbrowser, sys

try:
    option = sys.argv[1]
    query = sys.argv[2]
except IndexError:
    print("Usage: youtube search <search term> | youtube id <video id>")
    print("Example: youtube search holo+no+graffiti | youtube id PJf3XZ636-0")
    print("If a search term contains spaces, insert '+' where a space would be.")
    exit()

if option == "search":
    if sys.argv[3] != None:
        print("This search function contains spaces.")
        print("Please insert a '+' where the spaces should be.")
    else:
        webbrowser.open("https://www.youtube.com/results?search_query=" + query)
elif option == "id":
    if sys.argv[3] != None or sys.argv[3] != "":
        print("A video ID should not contain spaces.")
        print("Please retype or repaste the video ID.")
        print("Remember, the video ID is the random assortment of letters and numbers at the end of the URL.")
    else:
        webbrowser.open("https://www.youtube.com/results?search_query=" + query)
else:
    print("Usage: youtube search <search term> | youtube id <video id>")
    print("Example: youtube search holo+no+graffiti | youtube id PJf3XZ636-0")
    print("If a search term contains spaces, insert '+' where a space would be.")