# Example Uses of Hash Tables

# using dict.get() to see if it contains value, returns none when doesn't
voted = {}
result = voted.get("test")

print(result) # -> None 

# checker for voted 
voters = {}
def check_voter(name):
    if voters.get(name):
        print (f"{name} has already voted")
    else:
        voters[name] = True
        print (f"{name} voting..")

check_voter("tom")
check_voter("tom")
check_voter("pam")

# caching for urls
cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data

# placeholder for work
def get_data_from_server(url):
    return (f"{url} page")

