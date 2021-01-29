def searcher():
    import time
    #some 4 sec time consuming task
    book= "this is a harry baos sf"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("ur txt is in the book")
        else:
            print("txt is not in the book")
search = searcher()
next(search)
search.send("harryyyyyyyyy")
input("press any key")
search.send("is a")

#