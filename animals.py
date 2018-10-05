import re
import requests
from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)

db = client.bigdata
collection = db.artists

text_file = open("output.txt", 'a')
jsonfile = open("data.json", 'w')

jsondata = {}
jsondata["data"] = []

url = 'https://a-z-animals.com/animals/'
page = requests.get(url)
text_file.write(page.text)

animalLinks = re.findall(r'<li class="az-phobia-link-(.*?)"><a href="/animals/(.*?)/" title="(.*?)"><b>(.*?)</b></a></li>',page.text,flags=0)
# profileNames = re.findall(r'<a class="btn btn-profile-show bottom-20" href="/(.*?)">VIEW PROFILE</a>',page.text,flags=0)


for j in range(0,len(animalLinks)):

    urlProfile = 'https://a-z-animals.com/animals/' + animalLinks[j][1]

    pageProfile = requests.get(urlProfile)

    print(urlProfile)

    # names = re.findall(r'<a href="/animals/(.*?)/" title="(.*?)">(.*?)</a>',pageProfile.text,flags=0)
    # print(names[0])

    nameOfAnimal = re.findall(r'<h2 class="az-article-title">(.*?)</h2>', pageProfile.text,flags=0)

    print(nameOfAnimal)

    facts = re.findall(r'</td><td>(.*?)</td></tr>', pageProfile.text, flags=0)

    print(len(facts))

    if not facts[2]:
        facts[2] = "Kingdom unknown"
    else:
        Kingdom = facts[2]

    if not facts[3]:
        facts[3] = "Phylum unknown"
    else:
        Phylum = facts[3]

    if not facts[4]:
        facts[4] = "Class unknown"
    else:
        Class = facts[4]

    if not facts[5]:
        facts[5] = "Order unknown"
    else:
        Order = facts[5]

    if not facts[6]:
        facts[6] = "CommonName unknown"
    else:
        CommonName = facts[6]

    if not facts[7]:
        facts[7] = "ScientificName unknown"
    else:
        ScientificName = facts[7]

    if not facts[8]:
        facts[8] = "Location unknown"
    else:
        Location = facts[8]

    if not facts[9]:
        facts[9] = "Diet unknown"
    else:
        Diet = facts[9]

    if not facts[10]:
        facts[10] = "Size unknown"
    else:
        Size = facts[10]

    if not facts[11]:
        facts[11] = "Number Of Spicies unknown"
    else:
        NumberOfSpicies = facts[11]

    if not facts[12]:
        facts[12] = "Average Life Span unknown"
    else:
        AverageLifeSpan = facts[12]

    if not facts[13]:
        facts[13] = "Conservation Status unknown"
    else:
        ConservationStatus = facts[13]

    if not facts[14]:
        facts[14] = "Colour unknown"
    else:
        Colour = facts[14]

    if not facts[15]:
        facts[15] = "SkinType unknown"
    else:
        SkinType = facts[15]

    if not facts[16]:
        facts[16] = "FavouriteFood unknown"
    else:
        FavouriteFood = facts[16]

    if not facts[14]:
        facts[14] = "Colour unknown"
    else:
        Colour = facts[14]



    # Habitat = facts[17]
    # AverageLitterSize = facts[18]
    # MainPrey = facts[19]
    # Predators = facts[20]
    # SpecialFeatures = facts[21]

    animal = {}



    # art = {}
    #
    # if not names:
    #     art["name"] = "No name"
    # else:
    #     art["name"] = names[0]
    #
    # if not locations:
    #     art["location"] = "No location"
    # else:
    #     art["location"] = locations[0]
    #
    # if not profileViews:
    #     art["views"] = 0
    # else:
    #     art["views"] = int(profileViews[0])
    #
    # if not followers:
    #     art["followers"] = 0
    # else:
    #     art["followers"] = int(followers[0])
    #
    # if not availables:
    #     art["available"] = 0
    # else:
    #     art["available"] = int(availables[0])
    #
    # if not solds:
    #     art["sold"] = 0
    # else:
    #     art["sold"] = int(solds[0])
    #
    pprint.pprint(art, jsonfile)
    collection.insert_one(art)


text_file.close()
jsonfile.close()

print("end")
