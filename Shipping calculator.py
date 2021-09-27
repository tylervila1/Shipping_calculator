from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
# Shipping cost calculator


box_length = input("What is the box Length? ")
box_width = input("What is the box Width? ")
box_height = input("What is the box Height? ")
box_weight = input("How much does the package weight? ")

length = float(box_length)
width = float(box_width)
height = float(box_height)
weight = float(box_weight)

volume_ship_cost = .02
weight_ship_cost = .01

#Zip code input and converting to numbers
zip_raw1 = input("What is the starting Zip Code?: ")
zip_raw2 = input("What is the ending Zip Code?: ")
zip1 = zip_raw1
zip2 = zip_raw2

distance_ship_cost = .009
miles = open("distance", "r+")

def distance_cost ():
    driver = webdriver.Chrome()
    driver.get("https://www.zip-codes.com/distance_calculator.asp")
    sleep(2)
    driver.find_element_by_id("from").send_keys(zip1)
    driver.find_element_by_id("to").send_keys(zip2)
    driver.find_element_by_name("submit").click()
    distance_raw = driver.find_element_by_class_name("mi").text
    miles.write(distance_raw)


    driver.close()
    driver.quit()

def total_cost ():
    distance_value = miles.read()
    test = int(distance_value)
    volume = (length * width * height)
    size_cost = (volume * volume_ship_cost)
    weight_cost = (weight * weight_ship_cost)
    total_cost = (size_cost + weight_cost + test)

    print("$", total_cost)

distance_cost()
total_cost()


