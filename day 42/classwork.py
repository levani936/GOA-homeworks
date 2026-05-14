dictionary1 = {
    "Student": "Zviada",
    "Age": 90,
    "Points": 97
}
print(dictionary1["Points"])


dictionary2 = {
    "Brand": "Buggatti",
    "Model": "Divo",
    "Release": 2018

}
dictionary2.update({"Color": "Blue"})


dictionary3 = {
    "Idk": "Smbd",
    "Idk2": "Smbd2",
    "Idk3": "Smbd3"
}
dictionary3.pop("Idk3")
dictionary3.update ({"idk4": "SOMETHING"})


dictionary4 = {
    "Apple": "Red",
    "Orange": "Orange",
    "Grapes": "Purple"
}
for i in dictionary4:
    print(dictionary4.items())


    store = {
    "laptop": {
        "price": 3200,
        "stock": 5,
        "rating": 4.7
    },
    "phone": {
        "price": 1800,
        "stock": 8,
        "rating": 4.5
    },
    "tablet": {
        "price": 1200,
        "stock": 3,
        "rating": 4.2
    }
}
store.update(Headphones = {
    "Price": 400,
    "Stock": 12,
    "Rating": 4.8
})


store.items() * 1.1

store.update(High_rated = {
    "pc": 5.0
    "smartphone": 4.9
})