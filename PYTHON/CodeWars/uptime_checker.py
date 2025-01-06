def checker(website):
    import requests 
    try:
        requests.head(website)
        return True
    except:
        return False

