major_rivers={'ganga':'india','Amazon':'Brazil','Nile':'Egypt'}

for river,country in major_rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")