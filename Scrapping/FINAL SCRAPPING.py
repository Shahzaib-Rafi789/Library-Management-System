from asyncio.windows_events import NULL
import functools
from attr import attrs
from matplotlib.path import Path
from matplotlib.pyplot import cla, title
from regex import D
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import csv
import pandas as pd #install chrom webdriver
import concurrent.futures
import time
from multiprocessing import Pool

from sympy import div
from BookClass import Book

PATH = os.path.dirname(os.path.realpath(__file__))
###################################     FUNCTIONS  #####################################################
def getAllSubCatagories(driver, link):
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content)

    lstSubCatagories=[]
    lstLi = soup.findAll('li', attrs={'class': 'subcategory-name'})
    for i in lstLi:
        lstSubCatagories.append("https://b-ok.asia"+i.find('a', href=True)['href'])        

    return lstSubCatagories


def getAllPagesofCatagory(driver, soup):
    paginator = soup.findAll('div',attrs={'class':'paginator'})
    lstAllTD=[]
    lstAllPages=[]

    for i in paginator:
        lstAllTD = i.findAll('td',attrs={'width':'9%'})
    for i in lstAllTD:
        b=i.find('a', href=True)
        if(b!=None):
            lstAllPages.append("https://b-ok.asia"+b['href'],)
    return lstAllPages


def getAllBooksofaCatagory(driver, link):
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content)
    lstBook=[]
    lstBook+=getBookData(soup)
    lstPages=getAllPagesofCatagory(driver,soup)
    for i in lstPages:
        if not(i.endswith('page=1')):
            Soup  = getSoup(driver,i)
            lstBook+=getBookData(Soup)
    return lstBook
def getSoup(driver,link):
    driver.get(link)
    content=driver.page_source
    soup = BeautifulSoup(content)
    return soup


def getBookData(soup):
    lstBooks=[]
    bookData=soup.findAll('tr',attrs={'class':"bookRow"})
    for i in bookData:
        os.system('cls')
        title=i.find('h3',attrs={'itemprop':"name"})
        try:
            title=title.text.replace('\n', '')
        except:
            title=None
        author=''
        lstauthors=i.findAll('div',attrs={'class':"authors"})
        try:
            for j in lstauthors:
                author+=j.text
                author+='' if(author[-1]==j) else ','
        except:
            author=None
        try:
            publisher=i.find('a',attrs={'title':"Publisher"}).text
        except:
            publisher=None
        publishYear=GetPropertyValue(i.find('div',attrs={'class':"bookProperty property_year"}))
        language=GetPropertyValue(i.find('div',attrs={'class':"bookProperty property_language"}))
        TypeNSize=GetPropertyValue(i.find('div',attrs={'class':"bookProperty property__file"}))
        lst=TypeNSize.split(',')
        fileFormat=lst[0]
        fileSize=lst[1]
        print(title,author,publisher,publishYear,language,fileFormat,fileSize,"subhan")
        lstBooks.append(Book(title,author,publisher,publishYear,language,fileFormat,fileSize))
    df = pd.DataFrame(ConvertClassListToMulLists(lstBooks), columns=["Title", "Author(s)", "Language", "Publisher", "Publish Year", "File Size","File Format"])
    df.to_csv('Books.csv', mode = 'a',  index=False, header=False)
    return lstBooks


def GetPropertyValue(div):
    if(div!=None):
        div=div.find('div',attrs={'class':"property_value"}) 
        return div.text
    return None

def ConvertClassListToMulLists(ClassList):
    NestedList = []

    for Instance in ClassList:
        NestedList.append([Instance.title, Instance.authors, Instance.language, Instance.publisher, Instance.publishYear, Instance.fileFormat, Instance.fileSize])
        # Turns class List into Parallel lists.

    return NestedList
def ConvertMulListsToClassList(lstPublisher,lstPublishYear,lstLanguage,lstauthors,lstTitle,lstFileFormat,lstFileSize):
    NestedList = []

    for i in range(0,len(lstTitle)):
        NestedList.append(lstTitle[i],lstauthors[i],lstLanguage[i],lstPublisher[i],lstPublishYear[i],lstFileFormat[i],lstFileSize[i])
        # Turns class List into Parallel lists.

    return NestedList


def StoreDataToFile(lstAllBookLnk):
    fil1 = open("D:\\DSA PROJECt\\SubCategories2.txt", 'a')
    fil2 = open("D:\\DSA PROJECt\\Counter.txt", 'a')

    for i in lstAllBookLnk:
        fil1.write(str(i) + '\n')

    fil1.close()
    fil2.close()
#########################################################################################################


###################################     MAIN  ##########################################################
def main():
    # ###################### DATA STRUCTURE #############
    linkofAllCatagories="https://b-ok.asia/category-list"
    lstSubCatagoriesLnk=[] 
    # ###################################################
    driver = webdriver.Chrome(executable_path=PATH+'\chromedriver.exe')
    lstSubCatagoriesLnk=getAllSubCatagories(driver,linkofAllCatagories)
    os.system('cls')
    for link in lstSubCatagoriesLnk:
        getAllBooksofaCatagory(driver, link)   
        
            

if __name__ == "__main__":
    main()