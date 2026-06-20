print("Create yout own Hotel")

name = str(input("Please enter your Hotel name: "))
stars = float(input("Please enter how many stars your hotel have: "))
rooms = int(input("Please enter how many rooms: "))

hotel = {
    "Name": name,
    "Stars": stars,
    "Rooms": []
}

for i in range(1, rooms+1):
    print(f"""Per room please add the extra information
    {i}. 
    """)
    number = int(input("Please enter the number of the room: "))
    floor = int(input("Please enter where floor is that room: "))
    price = float(input("Please enter what is the price per night: "))

    room = {
        "Number": number,
        "Floor": floor,
        "Price per night": price
    }

    hotel.get("Rooms").append(room)

print(hotel)
