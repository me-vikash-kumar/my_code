def car_make(brand,model,**items):
    items['Brand']=brand
    items['Model']=model
    return items

car=car_make('toyota','carola',type="SUV",color="Black")

print(car)