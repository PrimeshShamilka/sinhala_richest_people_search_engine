from bs4 import BeautifulSoup
import os
import sys
import csv
import requests
from bs4 import BeautifulSoup 
import bs4
import translator
from es_send import send_data

URL = "https://www.celebritynetworth.com/list/top-100-richest-people-in-the-world/"
page = requests.get(URL)

def create_corpus():
    data = []
    soup = BeautifulSoup(page.content, "html.parser")
    people = soup.find(id="top_100_list")
    # get links 
    links = []
    for idx, li in enumerate(people.findChildren('li')):
        links.append(li.find('a')['href'])

    for link in links:
        person_page = requests.get(link)
        person_soup = BeautifulSoup(person_page.content, "html.parser")
        person_facts = person_soup.find(id='single__facts')
        person_content = person_soup.find(id='single__post_content')
        person_name = ' '.join(person_soup.find(id='single__header').find('h1').getText().split(' ')[:2])
        facts_table = person_facts.find('table')
        rows = facts_table.find_all('tr')

        # person metadata
        dic = {}
        for row in rows:
            cols = row.find_all('td')
            dic[cols[0].getText()] = cols[1].getText()


        if "Gender:" in dic:
            person_gender = dic["Gender:"]
        else:
            person_gender = ""
        
        if "Date of Birth:" in dic:
            person_dob = dic["Date of Birth:"]
        else:
            person_dob = ""

        if "Net Worth:" in dic:
            person_net_worth = dic["Net Worth:"]
        else:
            person_net_worth = ""

        if "Salary:" in dic:
            person_salary = dic["Salary:"]
        else:
            person_salary = ""
        
        if "Profession:" in dic:
            person_profession = dic["Profession:"]
        else:
            person_profession = ""

        if "Nationality:" in dic:
            person_nationality = dic["Nationality:"]
        else:
            person_nationality = ""

        data_item = [person_name, person_gender, person_dob, person_net_worth, person_salary, person_profession, person_nationality]
        key_facts = ''
        try:
            fact_rows = person_content.find('ul').find_all('li')
            for fact_row in fact_rows:
                key_facts += fact_row.getText() + '. '
            data_item.append(key_facts)
        except AttributeError:
            data_item.append(key_facts)

        data.append(data_item)
    
    header = ['person_name', 'gender', 'age', 'net_worth', 'salary', 'profession', 'nationality', 'key_facts']
    with open ('richest_people.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)


def translate_corpus():
    df = translator.translate()
    df.to_csv('richest_people_sinhala.csv', encoding='utf-8', index=False)
    print("translate done")

if __name__ == '__main__':
    if os.path.isfile("richest_people.csv"):
        if os.path.isfile("./richest_people_sinhala.csv"):
            send_data()
        else:
            translate_corpus()
    else:
        create_corpus()
        translate_corpus()
        send_data()


