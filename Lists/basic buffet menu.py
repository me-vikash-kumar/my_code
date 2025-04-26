basic_items=('bread','salad','rice','veg dish',"non veg dish")

print(f"our restaurant offers these items")

for i,j in enumerate(basic_items):
    print(f"{i+1}. {j.title()}")


print('\nwe are updating our menu....\n')

unchanged_items=[basic_items[0],basic_items[1],basic_items[2],]

basic_items=(*unchanged_items,'gobi munchurian','chicken butter masala')

print(f"our restaurant offers these items")

for i,j in enumerate(basic_items):
    print(f"{i+1}. {j.title()}")
