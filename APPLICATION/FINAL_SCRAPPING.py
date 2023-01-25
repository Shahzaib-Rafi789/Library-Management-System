from ast import Continue, Global
import functools
from operator import index
from pickle import GLOBAL, TRUE
from attr import attrs
from matplotlib.path import Path
from matplotlib.pyplot import cla, title
from regex import D
from scipy.misc import electrocardiogram
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import csv
import pandas as pd #install chrom webdriver
import concurrent.futures
import time
from threading import *
from multiprocessing import Pool
from sympy import div
from BookClass import Book
from googletrans import Translator
isRuning=False
PATH = os.path.dirname(os.path.realpath(__file__))
stop=False;
isScrappping=True;
isPause=False;
isContinue=False;
booksScrapped=0;
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
    global stop,isContinue,lstBook,booksScrapped
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content)
    lstBook=[]
    lstBook+=getBookData(soup)
    booksScrapped+=50;
    lstPages=getAllPagesofCatagory(driver,soup)
    if(isContinue==True):
        file=open('pause.txt',mode='r')
        linkStopped=file.readline().split(',')[1]
        file.close()
        for link in lstPages.copy():
            if(link==linkStopped):
                isContinue=False
                break
            lstPages.remove(link)
    for i in lstPages:
        if not(i.endswith('page=1')):
            Soup  = getSoup(driver,i)
            book=getBookData(Soup)
            lstBook+=book
            booksScrapped+=50;
            
            if (stop==True or isPause==True):
                try:
                    print("Catagory,",link,"Page,",lstPages[lstPages.index(i)+1],'\n',book[-1])
                except:
                    print(print("Catagory,",link,"Page,",lstPages[lstPages.index(i)],'\n',book[-1]))
                if(isPause==True):
                    file=open('pause.txt',mode='w+')
                    file.write(link+','+i)
                    file.close()
                driver.close()
                break
            
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
        # os.system('cls')
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
            author="Shahzaib Rafi"
        try:
            publisher=i.find('a',attrs={'title':"Publisher"}).text
        except:
            publisher="UET PUBLICATIONS"
        publishYear=GetPropertyValue(i.find('div',attrs={'class':"bookProperty property_year"}))
        language=GetPropertyValue(i.find('div',attrs={'class':"bookProperty property_language"}))
        TypeNSize=GetPropertyValue(i.find('div',attrs={'class':"bookProperty property__file"}))
        lst=TypeNSize.split(',')
        fileFormat=lst[0]
        fileSize=lst[1]
        oneBook=Book(title,author,publisher,publishYear,language,fileFormat,fileSize)
        lstBooks.append(oneBook)
    df = pd.DataFrame(ConvertClassListToMulLists(lstBooks), columns=["Title", "Author(s)", "Language", "Publisher", "Publish Year", "File Size","File Format"])
    df.to_csv('Books.csv', mode = 'a',  index=False, header=False)
    return lstBooks

def translate1(Book):
    # print(Book.title,"Subhan")
    gt=Translator()
    # Book.title=gt.translate(Book.title).text
    # Book.author=gt.translate(Book.author).text
    # Book.publisher=gt.translate(Book.publisher).text
    c=gt.translate(Book,'en')
    a=c.text
    # print(Book,"Subhan2)
    print(a,"Subhan2")
    # return Book
def GetPropertyValue(div):
    if(div!=None):
        div=div.find('div',attrs={'class':"property_value"}) 
        return div.text
    return 2000
def csvtoList():
    df=pd.read_csv('Books.csv')
    lst=[]
    for i in range(len(df)):
        lst.append(df.loc[i].tolist())
    return lst
def ConvertClassListToMulLists(ClassList):
    NestedList = []

    for Instance in ClassList:
        NestedList.append([Instance.title, Instance.authors, Instance.language, Instance.publisher, Instance.publishYear, Instance.fileFormat, Instance.fileSize])

    return NestedList
def ConvertMulListsToClassList(lstPublisher,lstPublishYear,lstLanguage,lstauthors,lstTitle,lstFileFormat,lstFileSize):
    NestedList = []

    for i in range(0,len(lstTitle)):
        NestedList.append(lstTitle[i],lstauthors[i],lstLanguage[i],lstPublisher[i],lstPublishYear[i],lstFileFormat[i],lstFileSize[i])
        # Turns class List into Parallel lists.

    return NestedList
#########################################################################################################


###################################     MAIN  ##########################################################
def scrapData():
    global isRuning,stop,isContinue
    if(isRuning==True and isPause==False):
        # ###################### DATA STRUCTURE #############
        linkofAllCatagories="https://b-ok.asia/category-list"
        lstSubCatagoriesLnk=[] 
        # ###################################################
        driver = webdriver.Chrome(executable_path=PATH+'\chromedriver.exe')
        lstSubCatagoriesLnk=getAllSubCatagories(driver,linkofAllCatagories)
        # os.system('cls')
        if(isContinue==True):
            file=open('pause.txt',mode='r')
            linkStopped=file.readline()
            linkStopped=linkStopped.split(',')[0]
            file.close()
            for link in lstSubCatagoriesLnk.copy():
                if(link==linkStopped):
                    break
                lstSubCatagoriesLnk.remove(link)
                
        for link in lstSubCatagoriesLnk:
            getAllBooksofaCatagory(driver, link)
            if(stop==True or isPause==True):
                if(stop==True):
                   isRuning=False
                break
def startScraping():
    global isRuning
    isRuning=True
def stopScraping():
    global stop
    stop=True
def pauseScraping():
    global isPause,isContinue,isRuning
    if(isPause==True):
        isContinue,isPause=True,False
    else:
        isContinue,isPause=False,True
    # if(isContinue==True):
    #     scrapData()
# driver = webdriver.Chrome(executable_path=PATH+'\chromedriver.exe')
# getBookData(getSoup(driver,'https://b-ok.asia/category/300/History-Asian-History'))
# translate1('二十四史：文白对照版（全12册）【线装书局出品！以“武英殿二十四史”为底本，参考“百衲本二十四史”，历时数年数位史学专家精心校订！原文+白话译文，文白对照，阅读无障碍！一套书读通中华上下五千年历 史！】')