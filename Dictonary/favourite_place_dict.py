manoj={'1st_Favourite_place':'victoria memorial park','2nd_Favourite_place':'jhumritik temple','3rd_Favourite_place':'Red fort'}

vinay = {'1st_Favourite_place':'patna museum','2nd_Favourite_place':'konark temple','3rd_Favourite_place':'Taj mahal'}

uday  = {'1st_Favourite_place':'ram mandir','2nd_Favourite_place':'india gate','3rd_Favourite_place':'lotus temple'}

rahul = {'1st_Favourite_place':'gwalior','2nd_Favourite_place':'jodhpur','3rd_Favourite_place':'udaipur'}

people = {
    "Manoj": manoj,
    "Vinay": vinay,
    "Uday": uday,
    "Rahul": rahul
}

for n,j in people.items():
    i=0
    print(f'\n{n} has following favourite places: \n1st favourite place is {j["1st_Favourite_place"]}, 2nd favourite place is {j["2nd_Favourite_place"]}, \nand his 3rd favourite place is {j["3rd_Favourite_place"]}')
    i+=1