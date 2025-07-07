def get_item(items, x):
    if x > len(items):
        return None
    else: 
        return items[x]


items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
y = get_item(items, x)
print(y)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
y = get_item(items, x)
print(y)
