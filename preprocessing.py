import csv
import random
# List of national Identities
country_IDs = "Afghan,Albanian,Algerian,USA,Andorran,Angolan,Antiguan,Barbudan,Argentine,Armenian,Aruban,Australian,Austrian,Azerbaijani,Bahamian,Bahraini,Bangladeshi,Barbadian,Basques,Belarusian,Belgian,Belizean,Beninese,Bermudian,Bhutanese,Bolivian,Bosniak,Bosnian-and-Herzegovinian,Botswanan,Brazilian,Breton,British,British-Virgin-Islander,Bruneian,Bulgarian,Burkinabé,Burmese,Burundian,Cambodian,Cameroonian,Canadian,Cape-Verdean,Chaldean,Chadians,Chilean,Chinese,Colombian,Comorian,Congolese (DRC),Congolese (RotC),Costa-Rican,Croat,Cuban,Cypriot,Czech,Dane,Greenlander,Djiboutian,Dominican,Dutch,East-Timorese,Ecuadorian,Egyptian,Emirati,English,Equatoguinean,Eritrean,Estonian,Ethiopian,Falkland-Islander,Faroese,Fijians,Finnish,Filipino,French,Gabonese,Gambian,Georgian,German,Baltic-German,Ghanaian,Gibraltarian,Greeks,Macedonian,Grenadian,Guatemalan,Guianese,Guinean,Guinea-Bissauan,Guyanese,Haitian,Honduran,Hong-Kong,Hungarian,Icelander,I-Kiribati,Indians,Indonesian,Iranian,Iraqi,Irish,Israeli,Italian,Ivoirian,Jamaican,Japanese,Jordanian,Kazakh,Kenyan,Kosovar,Kuwaiti,Kyrgyz,Lao,Latvian,Lebanese,Liberian,Libyan,Liechtensteiner,Lithuanian,Luxembourger,Macao,Macedonian,Malagasy,Malawian,Malaysian,Maldivian,Malian,Maltese,Manx,Marshallese,Mauritanian,Mauritian,Mexican,Micronesian,Moldovan,Monégasque,Mongolian,Montenegrin,Moroccan,Mozambican,Namibian,Nauruan,Nepalese,New-Zealander,Nicaraguan,Nigerien,Nigerian,Norwegian,Omani,Pakistani,Palauan,Palestinian,Panamanian,Papua-New-Guinean,Paraguayan,Peruvian,Polish,Portuguese,,Puerto-Rican,Qatari,Romanian,Russian,Rwandans,Saint-Kitt,Nevi,Saint-Lucian,Salvadoran,Sammarinese,Samoan,São-Tomé,Príncipe,Saudis,Scottish,Senegalese,Serb,Seychellois,Sierra-Leonean,Singaporean,Slovak,Slovene,Solomon-Islander,Somali,Sotho,South-African,Spanish,Sri-Lankan,Sudanese,Surinamese,Swazi,Swedish,Swiss,Syriac,Syrian,Taiwanese,Tamil,Tajik,Tanzanian,Thai,Tibetan,Tobagonian,Togolese,Tongan,Trinidadian,Tunisian,Turkish,Tuvaluan,Ugandan,Ukrainian,Uruguayan,Uzbek,Vanuatuan,Venezuelan,Vietnamese,Vincentian,Welsh,Yemeni,Zambian,Zimbabwean".split(",");

revamped_IDs = {'Afghan':'Afghanistan', 'Albanian': 'Albania', 'Algerian': 'Algeria', 'USA': 'USA', 'Andorran': 'Andora', 'Angolan': 'Angola', 'Antiguan': 'Antigua and Barbuda', 'Barbudan': 'Antigua and Barbuda',
                 'Argentine': 'Argentina', 'Armenian': 'Armenia', 'Australian': 'Australia', 'Austrian': 'Austria', 'Azerbaijani': 'Azerbaijan','Bahamian': 'The Bahamas', 'Bahraini': 'Bahrain', 'Bangladeshi': 'Bangladesh', 
                 'Barbadian': 'Barbados', 'Belarusian': 'Belarus', 'Belgian': 'Belgium', 'Belizean': 'Belize', 'Beninese': 'Benin', 'Bermudian': 'Bermuda', 'Bhutanese': 'Bhutan', 'Bolivian': 'Bolivia',
                 'Bosnian-and-Herzegovinian': 'Bosnia and Herzegovina', 'Botswanan': 'Botswana', 'Brazilian': 'Brazil', 'British': 'England', 'Bruneian': 'Brunei', 'Bulgarian': 'Bulgaria', 'Burkinabé': 'Burkina Faso',
                 'Burundian': 'Burundi', 'Cambodian': 'Cambodia', 'Cameroonian': 'Cameroon', 'Canadian': 'Canada', 'Chadians': 'Chad', 'Chilean': 'Chile', 'Chinese': 'China', 'Colombian': 'Columbia',
                 'Congolese (DRC)': 'Democratic Republic of the Congo', 'Congolese (RotC)': 'Republic of the Congo', 'Costa-Rican': 'Costa Rica', 'Croat': 'Croatia', 'Cuban': 'Cuba', 'Cypriot': 'Cyprus', 'N Cypriot': 'Northern Cyprus',
                 'Czech': 'Czech Republic', 'Danish': 'Denmark', 'Greenlander': 'Greenland', 'Djiboutian': 'Djibouti', 'Dominican': 'Dominican Republic', 'Dutch': 'Netherland', 'East-Timorese': "East Timor",
                 'Ecuadorian': 'Ecuador', 'Egyptian': 'Egypt', 'Emirati': 'United Arab Emirates', 'English': 'England', 'Equatoguinean': 'Equatorial Guinea', 'Eritrean': 'Eritrea', 'Estonian': 'Estonia', 'Ethiopian': 'Ethiopia',
                 'Falkland-Islander': 'Falkland Islands', 'Fijians': 'Fiji', 'Finnish': 'Finland', 'Filipino': 'Philippines', 'French': 'France', 'Gabonese': 'Gabon', 'Gambian': 'Gambia', 'Georgian': 'Georgia', 'German': 'Germany', 
                 'Ghanaian': 'Ghana', 'Greek': 'Greece', 'Macedonian': 'Macedonia', 'Guatemalan': 'Guatemala', 'Guianese': 'Guyana', 'Guinean': 'Guinea', 'Guinea-Bissauan': 'Guinea Bissau', 'Guyanese': 'Guyana', 'Haitian': 'Haiti', 
                 'Honduran': 'Honduras', 'Hungarian': 'Hungary', 'Icelander': 'Iceland', 'Indian': 'India', 'Indonesian': 'Indonesia', 'Iranian': 'Iran', 'Iraqi': 'Iraq', 'Irish': 'Ireland', 'Israeli': 'Israel', 'Italian': 'Italy',
                 'Ivoirian': 'Ivory Coast', 'Jamaican': 'Jamaica', 'Japanese': 'Japan', 'Jordanian': 'Jordan', 'Kazakh': 'Kazakhstan', 'Kenyan': 'Kenya', 'Kosovar': 'Kosovo', 'Kuwaiti': 'Kuwait', 'Kyrgyz': 'Kyrgyzstan', 'Lao': 'Laos', 
                 'Latvian': 'Latvia', 'Lebanese': 'Lebanon', 'Liberian': 'Liberia', 'Libyan': 'Libya', 'Lithuanian': 'Lithuania', 'Luxembourger': 'Luxembourg', 'Macedonian': 'Macedonia', 'Malawian': 'Malawi', 'Malaysian': 'Malaysia', 
                 'Malian': 'Mali', 'Maltese': 'Malta', 'Mauritanian': 'Mauritania', 'Mexican': 'Mexico', 'Moldovan': 'Moldova', 'Mongolian': 'Mongolia', 'Montenegrin': 'Montenegro', 'Moroccan': 'Morocco', 'Mozambican': 'Mozambique', 
                 'Namibian': 'Namibia', 'Nepalese': 'Nepal', 'New-Zealander': 'New Zealand', 'Nicaraguan': 'Nicaragua', 'Nigerien': 'Niger', 'Nigerian': 'Nigeria', 'Norwegian': 'Norway', 'Omani': 'Oman', 'Pakistani': 'Pakistan', 
                 'Panamanian': 'Panama', 'Papua-New-Guinean': 'Papua New Guinea', 'Paraguayan': 'Paraguay', 'Peruvian': 'Peru', 'Polish': 'Poland', 'Portuguese': 'Portugal', 'Puerto-Rican': 'Puerto Rico', 'Qatari': 'Qatar', 
                 'Romanian': 'Romania', 'Russian': 'Russia', 'Rwandan': 'Rwanda', 'Salvadoran': 'El Salvador','Saudis': 'Saudi Arabi', 'Scottish': 'Scotland', 'Senegalese': 'Senegal', 'Serb': 'Serbia', 'Sierra-Leonean': 'Sierra Leone',
                'Slovak': 'Slovakia', 'Slovene': 'Slovenia', 'Solomon-Islander': 'Solomon Islands', 'Somali': 'Somalia', 'Sotho': 'Lesotho', 'South-African': 'South Africa', 'Spanish': 'Spain', 'Sri-Lankan': 'Sri Lanka', 'Sudanese': 'Sudan', 
                'Surinamese': 'Suriname', 'Swazi': 'Swaziland', 'Swedish': 'Sweden', 'Swiss': 'Switzerland', 'Syrian': 'Syria', 'Taiwanese': 'Taiwan', 'Tajik': 'Tajikistan', 'Tanzanian': 'Tanzania', 'Thai': 'Thailand', 'Tibetan': 'Tibet', 
                'Tobagonian': 'Trinidad and Tobago', 'Togolese': 'Togo', 'Trinidadian': 'Trinidad and Tobago', 'Tunisian': 'Tunisia', 'Turkish': 'Turkey', 'Ugandan': 'Uganda', 'Ukrainian': 'Ukraine', 'Uruguayan': 'Uruguay', 
                'Uzbek': 'Uzbekistan', 'Vanuatuan': 'Vanuatu', 'Venezuelan': 'Venezuela', 'Vietnamese': 'Vietnam', 'Welsh': 'Wales', 'Yemeni': 'Yemen', 'Zambian': 'Zambia', 'Zimbabwean': 'Zimbabwe'}


artistGenreMap = {
  "Elvis Costello": "PUNK ROCK",
  "Elvis Costello & The Attractions": "PUNK ROCK",
  "Tiffany Page": "Alternative",
  "Joe Echo": "ROCK",
  "Paul McCartney": "BRITISH/ROCK",
  "Lissie": "ROCK",
  "The All-American Rejects": "INDIE/ALTERNATIVE",
  "Demi Lovato": "POP",
  "Babyshambles": "INDIE/ALTERNATIVE",
  "Lilygreen & Maguire": "POP",
  "Taylor Swift": "POP",
  "Amanda Seyfried": "SOUNDTRACK",
  "Olly Murs": "POP",
  "The Pigeon Detectives": "INDIE/ALTERNATIVE",
  "James Blunt": "POP/INDIE",
  "Luther Vandross": "R&B",
  "Glee Cast": "SOUNDTRACK",
  "Anna Kendrick": "SOUNDTRACK",
  "Daniel Powter": "POP/ALTERNATIVE",
  "Snow Patrol": "INDIE/ALTERNATIVE",
  "OneRepublic": "ROCK",
  "Allstar Weekend": "POP",
  "Ed Sheeran": "ACOUSTIC",
  "Coldplay": "ROCK/ALTERNATIVE",
  "The 1975": "INDIE/ROCK",
  "Butterfly Boucher": "INDIE/ALTERNATIVE",
  "Christina Aguilera": "POP",
  "Beans On Toast": "FOLK",
  "Cast Of 'Camp Rock 2": "SOUNDTRACK",
  "Elton John": "POP",
  "Lennon & Maisy": "COUNTRY",
  "Beyoncé": "POP",
  "One Direction": "POP",
  "Frank Turner": "FOLK",
  "S Club 7": "POP",
  "Hugh Jackman": "SOUNDTRACK",
  "Kelly Clarkson": "POP",
  "Simon & Garfunkel": "FOLK",
  "Eliza Doolittle": "POP",
  "Barenaked Ladies": "ROCK/ALTERNATIVE",
  "Boyzone": "POP",
  "Young Money": "RAP",
  "Rachael Yamagata": "INDIE/ALTERNATIVE",
  "The Twang": "INDIE",
  "Frank Turner": "FOLK",
  "Justin Bieber": "POP",
  "Lily Allen": "POP",
  "Cat Stevens": "FOLK",
  "The Pogues": "IRISH",
  "Bob Carlisle": "CHRISTIAN",
  "Newton Faulkner": "FOLK",
  "Passenger": "FOLK",
  "Mat Kearney": "ACOUSTIC",
  "Oasis": "BRITISH/ROCK",
  "A Great Big World": "INDIE/ALTERNATIVE",
  "Matt Nathanson": "ACOUSTIC",
  "Ryan O'Shaughnessy": "IRISH/ACOUSTIC",
  "The Rifles": "INDIE/ALTERNATIVE",
  "KISS": "ROCK",
  "Red Hot Chili Peppers": "ROCK/ALTERNATIVE",
  "Michael Jackson": "POP",
  "Daft Punk": "ELECTRONIC",
  "Danny Elfman": "SOUNDTRACK",
  "Joe Hisaishi": "JAPANESE/SOUNDTRACK",
  "KIRAKIRA Quartet": "JAPANESE/SOUNDTRACK",
  "Moby": "ELECTRONIC",
  "Ratatat": "ELECTRONIC",
  "All That Jazz": "JAZZ/JAPANESE",
  "Pendulum": "ELECTRONIC",
  "Justice": "ELECTRONIC/FRENCH",
  "Wolfgang Amadeus Mozart": "CLASSICAL",
  "Antonio Vivaldi": "CLASSICAL",
  "Ludwig van Beethoven": "CLASSICAL",
  "Drake": "RAP/HIP-HOP",
  "2080": "ELECTRONIC/FRENCH",
  "C418": "ELECTRONIC",
  "Glen Porter": "HIP-HOP/LOUNGE",
  "Bonobo": "ELECTRONIC/LOUNGE",
  "Schoolboy Q": "RAP/HIP-HOP",
  "Athletics": "INDIE/ALTERNATIVE",
  "Black Sabbath": "METAL",
  "Led Zeppelin": "ROCK",
  "Arctic Monkeys": "BRITISH/INDIE",
  "London Grammar": "INDIE/ELECTRONIC",
  "Otis Redding": "R&B",
  "Johnny Cash": "COUNTRY",
  "The Chainsmokers": "ELECTRONIC/POP",
  "The Rolling Stones": "ROCK/BRITISH",
  "Eminem": "RAP",
  "J Balvin": "LATIN/POP"

}
def add_country_column(file):

    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        readers = csv.DictReader(file)
        fieldnames = readers.fieldnames + ['Country']
        rows = []

        for row in readers:
            genre = row['Genre']
            # split the genre by '/'
            genre_parts = genre.split("/")
            country = 'USA' #default option for genre

            # Check if any genre part matches a country
            for part in genre_parts:
                part = part.strip()
                for key in revamped_IDs:
                    if part.lower() == key.lower():
                        print([part.lower(), key.lower()])
                        print(revamped_IDs[key])
                        country = revamped_IDs[key] #set the country
                        break

            row['Country'] = country
            rows.append(row)
    output = 'latest_data.csv'
    with open(output, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Updated data saved to {output}")

# Use the function
csv_file = 'data/updated_dataset.csv'
add_country_column(csv_file)

extra_data = [("c50566d83fba17b20697039d5824db78","Sufjan Stevens","Should Have Known Better","E."),
            ("c50566d83fba17b20697039d5824db78","The Shins","Simple Song","E."),
            ("c50566d83fba17b20697039d5824db78","Daughter","Smother","E."),
            ("c50566d83fba17b20697039d5824db78","Death Cab for Cutie","Soul Meets Body","E."),
            ("c50566d83fba17b20697039d5824db78","José González","Stay Alive","E."),
            ("c50566d83fba17b20697039d5824db78","Daughter","Still","E."),
            ("c50566d83fba17b20697039d5824db78","Junip","The Ghost Of Tom Joad","E."),
            ("c50566d83fba17b20697039d5824db78","Death Cab for Cutie","The Ice Is Getting Thinner","E."),
            ("c50566d83fba17b20697039d5824db78","Churchill","The War Within","E."),
            ("c50566d83fba17b20697039d5824db78","Sufjan Stevens","To Be Alone With You","E."),
            ("c50566d83fba17b20697039d5824db78","Hey Marseilles","To Travels and Trunks","E."),
            ("c50566d83fba17b20697039d5824db78","Daughter","Touch","E."),
            ("c50566d83fba17b20697039d5824db78","Daughter","Winter","E."),
            ("c50566d83fba17b20697039d5824db78","Keaton Henson","You Don't Know How Lucky You Are","E."),
            ("c50566d83fba17b20697039d5824db78","Peter Bjorn And John","Young Folks","E."),
            ("c50566d83fba17b20697039d5824db78","Daughter","Youth","E."),
            ("c50566d83fba17b20697039d5824db78","J Balvin","6 AM","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","J Balvin","Ay Vamos","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","Enrique Iglesias","Bailando - Spanish Version","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","Los Hijos del sol","Cariñito","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","ABBA","Chiquitita - Spanish Version","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","Don Omar","Danza Kuduro","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","Sash!","Ecuador","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","Nicky Jam","El Perdón","Ecuador"),
            ("c50566d83fba17b20697039d5824db78",'Osmani Garcia "La Voz"',"El Taxi","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","Dvicio","Enamorate","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","Pitbull","Fireball","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","Kygo","Firestone","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","Daddy Yankee","Gasolina","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","Daddy Yankee","Gasolina - DJ Buddah Remix","Ecuador"),
            ("c50566d83fba17b20697039d5824db78","Los Enanitos Verdes","Lamento Boliviano","Ecuador")]

new_data = [("c50566d83fba17b20697039d5824db78","Daddy Yankee","Limbo","Ecuador"),
    ("c50566d83fba17b20697039d5824db78","Los Del Rio","Macarena","Ecuador"),
    ("c50566d83fba17b20697039d5824db78","Natalia Lafourcade","Nunca Es Suficiente","Ecuador"),
    ("c50566d83fba17b20697039d5824db78","Thewen","Relaciones Pasajeras","Ecuador"),
    ("c50566d83fba17b20697039d5824db78","Pitbull","Time of Our Lives","Ecuador"),
    ("c50566d83fba17b20697039d5824db78","Nicky Jam","Travesuras","Ecuador"),
    ("c50566d83fba17b20697039d5824db78","Marc Anthony","Vivir Mi Vida - Versión Pop","Ecuador"),
    ("c50566d83fba17b20697039d5824db78","Nicky Jam","Voy a Beber","Ecuador"),
    ("c50566d83fba17b20697039d5824db78","Dawid Podsiadlo","!H.a.p.p.y!","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","The Gaslight Anthem",'"45"',"Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Garbage","#1 Crush","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","MNDR","#1 In Heaven","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","The Chainsmokers","#SELFIE","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","will.i.am","#thatPOWER","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Tom Waits","$29.00","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Albert Hammond, Jr.","& So We Go","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Tame Impala","'Cause I'm A Man","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Eminem","'Till I Collapse","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Arcade Fire","(Antichrist Television Blues)","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","The Offspring","(Can't Get My) Head Around You","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Blue Oyster Cult","(Don't Fear) The Reaper","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Martin","(Du Ar Sa) Yeah Yeah, Wow Wow","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","The Rolling Stones","(I Can't Get No) Satisfaction - (Original Single Mono Version)","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Cat Power","(I Can’t Get No) Satisfaction","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Humble Pie","(I'm A) Road Runner","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Weezer","(If You're Wondering If I Want You To) I Want You To","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Manic Street Preachers","(It's Not War) Just the End of Love","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","The Reddings","(Sittin' On) The Dock Of The Bay","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","The Stone Roses","(Song For My) Sugar Spun Sister - Remastered","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Marilyn Manson","(s)AINT","Everything at once"),
    ("c50566d83fba17b20697039d5824db78","Beyoncé","***Flawless","Everything at once")]


#print(formatted_list)

def add_genre(entry):
    user_id, artist, track_name, playlist_name = entry
    genre = artistGenreMap.get(artist)
    if not genre:
        # check if the country is in the name of the playlist
        if playlist_name in revamped_IDs:
            genre = revamped_IDs[playlist_name].upper()
        else:
            for key, value in revamped_IDs.items():
                if playlist_name == value:
                    genre = value.upper()
                    break
        if not genre:
            # randomly pick a genre to add to it if not a country name
            genre = random.choice(list(artistGenreMap.values()))
    return ",".join(entry) + "," + genre

# formatted_data1 = [add_genre(entry) for entry in extra_data]
# formatted_list1 = "\n".join(formatted_data1)

# formatted_data2 = [add_genre(entry) for entry in new_data]
# formatted_list2 = "\n".join(formatted_data2)

# print(formatted_list1)
# print('XXXXXXXXXXXXXXXXXXXXX')
# print(formatted_list2)
