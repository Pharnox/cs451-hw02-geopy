from geopy.geocoders import Nominatim
from geopy.distance import geodesic, great_circle

# Create a geolocator object to access geo data using Nominatum
geolocator = Nominatim(user_agent="Geopy Test")

loop = True
while(loop):
# A query address
    #query1 = '1314 chavez st, las vegas, nm'
    #query2 = '1701 bryant st, denver, co'
    while(True):
        try:
            query1 = input("Please enter the start address: ")
            start = geolocator.geocode(query1)
            s_Loc = start.latitude, start.longitude
        except AttributeError:
            print("That was not an address I was able to find. Please try again.")
        else:
            break
    while(True):
        try:
            query2 = input("Please enter the destination address: ")
            end = geolocator.geocode(query2)
            e_Loc = end.latitude, end.longitude
        except AttributeError:
            print("That was not an address I was able to find. Please try again.")
        else:
            break


    GD = geodesic(s_Loc, e_Loc).miles

    print("The distance from\n",start,"\nto\n",end,"\nis %5.2f miles." % (GD))
    again = True
    while(again):
        UIn = input("Search again?(y/n): ")
        if (UIn.lower() == "y"):
            loop = True
            again = False
        elif (UIn.lower() == "n"):
            print("Goodbye!")
            loop = False
            again = False
        else:
            print("I didn't understand that. Would you like to search again?(y/n): ")
        