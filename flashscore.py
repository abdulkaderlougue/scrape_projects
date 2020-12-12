#selenium can make the browser act automaticaly
from selenium import webdriver
#able to use the keyboard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains #for actions in queue
from selenium.webdriver.common.alert import Alert
import time 


#time.sleep(5)
ligue1 = "france/ligue-1"
liga = "espagne/laliga"
bundesliga = "allemagne/bundesliga"
seri_a = "italie/seirie-a"
pr_league = "angleterre/premier-ligue"

leagues = []
"""
#Results
isround = False
roundedWanted = 5 # number of rounds you want to have the games
usefulRounds = []
rounds = driver.find_elements_by_css_selector(".event__round") # rounds names
for i in range(roundedWanted):
    #get the rounds name and append them to the usefulRound
    usefulRounds.append(rounds[i].text)

#games = driver.find_elements_by_css_selector(".event__match--oneLine")[0].find_elements_by_css_selector(".event__scores")[0].text
"""

for league in leagues:
    driver = webdriver.Chrome()
    url = "https://www.flashscore.fr/football/"+league+"/resultats/"
    print(url)
    driver.get(url)
    games = driver.find_elements_by_css_selector(".event__match--oneLine")
    for i in range(2):
    #for i in range(len(games)):
        g_time = games[i].find_elements_by_css_selector(".event__time")[0].text
        homeTeam = games[i].find_elements_by_css_selector(".event__participant--home")[0].text
        awayTeam = games[i].find_elements_by_css_selector(".event__participant--away")[0].text
        score = games[i].find_elements_by_css_selector(".event__scores")[0].text.strip('\n')
        print(f"time {g_time} -- {homeTeam} {score} {awayTeam}")
    
#driver.close()
#lines = driver.find_elements_by_css_selector(".sportName")
