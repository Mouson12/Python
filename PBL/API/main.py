# List of avaiable websites
websites = {
    '1': 'https://www.meteo.waw.pl/',
    '2': 'https://www.meteo.pl/',
    '3': 'https://www.ladybug.tools/epwmap/',
    '4': 'https://www.meteomatics.com/en/weather-api/',
    '5': 'https://stormglass.io/',
    '6': 'https://rapidapi.com/auth/sign-up?referral=/weatherbit/api/weather',
    '7': 'https://climate.onebuilding.org/',
    '8': 'https://agdatashop.csiro.au/',
    '9': 'https://www.timeanddate.com/weather/poland/warsaw/historic',
    '10': 'https://www.wunderground.com/history/daily/pl/warsaw',
    '11': 'https://www.wetterzentrale.de/en/topkarten.php?map=41&model=alap&var=2&time=21&run=0&lid=OP&h=0&mv=0&tr=3',
    '12': 'https://pl.climate-data.org/europa/polska/masovian-voivodeship/warszawa-4560/',
}

# Website selection by the user
print("Avaiable websites:")
for key, value in websites.items():
    print(f"{key}: {value}")

selected_website = input("Choose website from 1 to 12: ")

# Sprawdzamy, czy wybór jest poprawny
if selected_website in websites:
    wybrana_strona = websites[selected_website]
    #dane = pobierz_dane_z_strony(wybrana_strona)
    #print(f"Pobrane dane ze strony {wybor}:\n{dane}")
else:
    print("Make sure that the selected number is in the range from 1 to 12.")