"""
    Caution: Never Modify a List While Iterating Over It!

    Modifying a list during iteration can lead to unpredictable behavior, such as:
    - Skipped elements: Removing or adding elements affects the iterator's index, potentially skipping elements or processing them multiple times.
    - Logical errors: The shifting of indices may cause the program's logic to break.
    - Bugs and exceptions: Can result in difficult-to-debug errors in your code.

    Safe alternatives:
    1. Iterate over a copy of the list (e.g., `list[:]`).
    2. Use a list comprehension to create a new list.
    3. Collect changes in a separate list and apply them later.
    4. Use filtering methods like `filter()` for element removal.

    Example of an issue:
        my_list = [1, 2, 3, 4]
        for item in my_list:
            if item % 2 == 0:
                my_list.remove(item)
        print(my_list)  # Output: [1, 3] (Unexpected result due to skipping)

    Always use safe practices to ensure reliable and predictable behavior!
"""


print('Unfortunately you are allowed to invite only two people')

people_to_invite =[
    "Alice", "Bob", "Charlie", "Diana", "Eve",
    "Frank", "Grace", "Hannah", "Ivan", "Julia",
    "Kevin", "Liam", "Mia", "Noah", "Olivia",
    "Peter", "Quincy", "Rachel", "Steve", "Tracy"
]



for people in people_to_invite:
    
    if len(people_to_invite)> 4:
     place_holder=people_to_invite.pop()
    else:
     break

for person in people_to_invite:
    print(f">>Dear {person.title()}, I would like to invite you to a dinner gathering at my home on Saturday, \nthe 15th, at 7 PM. It would be wonderful to have you with us!"
)