geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [x for x in birds if x not in geese]

print(goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]))
# ['Mallard', 'Barbary', 'Hook Bill', 'Blue Swedish', 'Crested']