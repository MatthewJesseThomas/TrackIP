from geopy.geocoders import Nominatim

# Create a geolocator object
geolocator = Nominatim(user_agent="geoapiExercises")

# Get the IP address
ip = "Your_IP_Address"  # Replace this with the actual IP address you want to use

# Get the location details based on IP
location = geolocator.geocode(ip)

if location:
    print(f"The IP is: {ip}")
    print(f"Latitude: {location.latitude}")
    print(f"Longitude: {location.longitude}")
    print(f"Country: {location.address}")
else:
    print("Location not found for the given IP.")

# Prompt user to enter an IP address and get its details
show_IpDetails = input("Enter an IP address to get details: ")
location = geolocator.geocode(show_IpDetails)
if location:
    print(f"Location details for IP {show_IpDetails}:")
    print(f"Latitude: {location.latitude}")
    print(f"Longitude: {location.longitude}")
    print(f"Country: {location.address}")
else:
    print("Location not found for the given IP.")

# Prompt user to enter a country name and get its details
show_countryDetails = input("Enter a country name to get details: ")
location = geolocator.geocode(show_countryDetails)
if location:
    print(f"Location details for {show_countryDetails}:")
    print(f"Latitude: {location.latitude}")
    print(f"Longitude: {location.longitude}")
    print(f"Country: {location.address}")
else:
    print("Location not found for the given country.")
