def cel_to_fahr(celsius):
    fahr = (celsius * 1.8)+32
    return fahr

cel = int(input("enter temperature in celsius to convert it into fahrenheit:"))
print("temperature in fahrenheit is:",cel_to_fahr(cel))
     
