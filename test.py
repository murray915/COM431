

# Load Kaggle POI dataset
import csv

points_of_interest = []

with open("C:/Users/katie/Downloads/poi.csv/poi.csv", mode ='r')as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        print(lines)
        points_of_interest.append(lines)



print(points_of_interest[0])

# # Your full list
# points_of_interest = [
#         "Eiffel Tower", "Statue of Liberty", "Great Wall of China", "Machu Picchu", "Colosseum",
#         "Taj Mahal", "Christ the Redeemer", "Stonehenge", "Grand Canyon", "Niagara Falls",
#         "Mount Everest", "Pyramids of Giza", "Sydney Opera House", "Big Ben", "Tokyo Tower",
#         "Acropolis of Athens", "Petra", "Burj Khalifa", "Louvre Museum", "Times Square",
#         "Central Park", "Golden Gate Bridge", "Mount Fuji", "Santorini", "Banff National Park",
#         "Yellowstone National Park", "Yosemite National Park", "Redwood National Park", "Victoria Falls", "Angel Falls",
#         "Great Barrier Reef", "Serengeti National Park", "Galápagos Islands", "Antelope Canyon", "Alhambra",
#         "Mont Saint-Michel", "Neuschwanstein Castle", "Prague Castle", "Brandenburg Gate", "Berlin Wall",
#         "Versailles Palace", "Buckingham Palace", "Tower of London", "St. Peters Basilica", "Vatican Museums",
#         "Sagrada Familia", "Park Güell", "La Rambla", "Leaning Tower of Pisa", "Trevi Fountain",
#         "The Shard", "Empire State Building", "Brooklyn Bridge", "Chicago Riverwalk", "CN Tower",
#         "Banaras Ghats", "Meenakshi Temple", "Amber Fort", "Red Fort", "Qutub Minar",
#         "Gateway of India", "Marina Beach", "Charminar", "Hampi Ruins", "Ajanta Caves",
#         "Borobudur Temple", "Ubud Monkey Forest", "Ha Long Bay", "Angkor Wat", "Bagan Temples",
#         "Blue Lagoon", "Reykjavik Church", "Thingvellir National Park", "Geysir", "Skógafoss",
#         "Plitvice Lakes", "Dubrovnik Old Town", "Diocletians Palace", "Lake Bled", "Matterhorn",
#         "Zermatt", "Lake Geneva", "Château de Chillon", "Lake Como", "Cinque Terre",
#         "Amalfi Coast", "Pompeii", "Mt. Vesuvius", "Blue Mosque", "Hagia Sophia",
#         "Topkapi Palace", "Cappadocia", "Pamukkale", "Ephesus", "Mount Kilimanjaro",
#         "Table Mountain", "Robben Island", "Cape of Good Hope", "Kruger National Park", "Victoria & Alfred Waterfront",
#         "Dubai Mall", "Dubai Marina", "Palm Jumeirah", "Sheikh Zayed Mosque", "Abu Dhabi Louvre",
#         "Jerusalem Old City", "Western Wall", "Dome of the Rock", "Dead Sea", "Masada",
#         "Petronas Towers", "Batu Caves", "Cameron Highlands", "Marina Bay Sands", "Gardens by the Bay",
#         "Sentosa Island", "Merlion Park", "Namsan Tower", "Gyeongbokgung Palace", "Jeju Island",
#         "Great Ocean Road", "Twelve Apostles", "Uluru", "Bondi Beach", "Fraser Island",
#         "Christchurch Botanic Gardens", "Milford Sound", "Hobbiton Movie Set", "Rotorua Geothermal Park", "Queenstown",
#         "Chichen Itza", "Tulum Ruins", "Teotihuacan", "Cancún Beaches", "Frida Kahlo Museum",
#         "Christ the Redeemer", "Iguazu Falls", "Sugarloaf Mountain", "Copacabana Beach", "Amazon Rainforest",
#         "Cusco", "Sacred Valley", "Nazca Lines", "Lake Titicaca", "Arequipa",
#         "Moai Statues of Easter Island", "Mount Rushmore", "Walt Disney World", "Universal Studios", "Smithsonian Institution"
#     ]

# results = []

# # Step 1: Lookup in Kaggle CSV
# for place in points_of_interest:
#     subset = points_of_interest[[0].str.lower() in place.lower()]
    
#     if not subset.empty:
#         lat, lng = subset.iloc[0][["latitude", "longitude"]]
#         results.append([place, lat, lng])
#     else:
#         results.append([place, '', ''])
