# importing the modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pg
import pandas as pd
import time

link = "https://www.justdial.com/Nagpur/Car-Dealers-Tata-Sumo-Gold-Authorised/nct-11018241"

pagenum = 2

for i in range(5):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
 

    time.sleep(5)
    print(pg.position())
    pg.moveTo(1044, 175)
    pg.drag(0, 600, 5)
    pg.press('end')

    # the user-defined function
    def strings_to_num(argument):
        switcher = {
            'dc': '+',
            'fe': '(',
            'hg': ')',
            'ba': '-',
            'acb': '0',
            'yz': '1',
            'wx': '2',
            'vu': '3',
            'ts': '4',
            'rq': '5',
            'po': '6',
            'nm': '7',
            'lk': '8',
            'ji': '9'
        }
        return switcher.get(argument, "nothing")


    # fetching all the store details
    storeDetails = driver.find_elements_by_class_name('store-details')

    # instatiating empty lists
    nameList = []
    addressList = []
    numbersList = []

    # iterating the storeDetails
    for i in range(len(storeDetails)):
        # fetching the name, address and contact for each entry
        name = storeDetails[i].find_element_by_class_name('lng_cont_name').text
        address = storeDetails[i].find_element_by_class_name('cont_sw_addr').text
        contactList = storeDetails[i].find_elements_by_class_name('mobilesv')

        myList = []

        for j in range(len(contactList)):
            myString = contactList[j].get_attribute('class').split("-")[1]

            myList.append(strings_to_num(myString))

        nameList.append(name)
        addressList.append(address)
        numbersList.append("".join(myList))

    # intialise data of lists.
    data = {'Company Name': nameList,
            'Address': addressList,
            'Phone': numbersList}

    # Create DataFrame
    df = pd.DataFrame(data)
    print(df)

    # Save Data as .csv
    df.to_csv('Nagpur Hotels.csv', mode='a', header=False)
    print(f"=================={pagenum}==================")
    pagenum += 1
    time.sleep(1)


