def kontrol_fonksiyonu(degisken):
    if "@" in degisken:
        return 1
    elif degisken.startswith("0"):
        return 0
    else:
        return -1  # Eğer ne "@" var ne de "0" ile başlıyorsa -1 döndürülebilir
def var_mi_kontrol_fonksiyonu(email_dizisi, aranan_email):
    if aranan_email in email_dizisi:
        return 0
    else:
        return 1
import time

web_baglantilari_listesi = []
kacIletisimBilgisiIstiyorsunuz = input("Kac Sayfanin Taranmasini Istiyorsunuz ")
kacIletisimBilgisiIstiyorsunuz = int(kacIletisimBilgisiIstiyorsunuz)
time.sleep(2)
from sifre import Passw
from selenium import webdriver
password = Passw()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
cepTelefonlariDizisi = []
emailDizisi = []
browser.get("https://www.facebook.com")
browser.maximize_window()
eMailInputXPATH = '//*[@id="email"]'
passwInputXPATH = '//*[@id="pass"]'
eMailInputXPATH = browser.find_element(By.XPATH,eMailInputXPATH)
time.sleep(3)
eMailInputXPATH.send_keys(password.getMail())
time.sleep(3)
passwInputXPATH = browser.find_element(By.XPATH,passwInputXPATH)
time.sleep(3)
passwInputXPATH.send_keys(password.getPass())
time.sleep(3)
passwInputXPATH.send_keys(Keys.RETURN)
time.sleep(8)
browser.get("https://www.facebook.com/search/top/?q=Hurdac%C4%B1&locale=tr_TR")
time.sleep(4)
browser.get("https://www.facebook.com/search/pages/?q=Hurdac%C4%B1&locale=tr_TR")
y = 1
time.sleep(5)
def sayfaKaydir(_sayfaKaydirmaParametresi):
    denememXPATHIM = f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[{_sayfaKaydirmaParametresi}]/div/div/div/div/div/div/div/div/div/div/div[1]/div/a'
    denemeXPATH = browser.find_element(By.XPATH,denememXPATHIM) 
    try:
        print("sayfa scroll ediliyor . . .")
        time.sleep(1)
        browser.execute_script("arguments[0].scrollIntoView();",denemeXPATH)
        print("Sayfa Scroll Edildi . . .")
        time.sleep(1)
    except:
        print("scroll edilemedi X X X X")

def getBaglantilar(kacaKadar):
    sayfaKaydirmaParametresi = 16
    icerideKactaKaldin = 17 #href almaak icindidr
    for i in range(1, 17):
        try:
            print("")
            time.sleep(1)
            aTAGXPATH = f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[{str(i)}]/div/div/div/div/div/div/div/div/div/div/div[1]/div/a'
            a_tag = browser.find_element(By.XPATH,aTAGXPATH)
            href = a_tag.get_attribute("href")
            print(href)
            web_baglantilari_listesi.append(href)
        except:
            print("bu tag hatalidir")
    sayfaKaydir(sayfaKaydirmaParametresi)
    sayfaKaydirmaParametresi = sayfaKaydirmaParametresi + 9
    kactaneDokuzVar1 = kacaKadar - 16
    kactaneDokuzVar1 = int(kacaKadar / 9)
    denememXPATHIM = f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[{str(sayfaKaydirmaParametresi)}]/div/div/div/div/div/div/div/div/div/div/div[1]/div/a'
    denemeXPATH = browser.find_element(By.XPATH,denememXPATHIM) 
    try:
        print("sayfa scroll ediliyor . . .")
        time.sleep(2)
        browser.execute_script("arguments[0].scrollIntoView();",denemeXPATH)
        print("Sayfa Scroll Edildi . . .")
        time.sleep(2)
        sayfaKaydirmaParametresi = sayfaKaydirmaParametresi + 9
    except:
        print("scroll edilemedi . . .")
    for i in range(1, int(kactaneDokuzVar1)):
        print(i)
        for y in range(icerideKactaKaldin, icerideKactaKaldin + 9):
            try:
                print("")
                time.sleep(1)
                aTAGXPATH = f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[{str(y)}]/div/div/div/div/div/div/div/div/div/div/div[1]/div/a'
                a_tag = browser.find_element(By.XPATH,aTAGXPATH)
                href = a_tag.get_attribute("href")
                print(href)
                web_baglantilari_listesi.append(href)
            except:
                print("bu tag hatalidir")
        icerideKactaKaldin = icerideKactaKaldin + 9
        denememXPATHIM = f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[{str(sayfaKaydirmaParametresi)}]/div/div/div/div/div/div/div/div/div/div/div[1]/div/a'
        denemeXPATH = browser.find_element(By.XPATH,denememXPATHIM) 
        try:
            print("sayfa scroll ediliyor . . .")
            time.sleep(1)
            browser.execute_script("arguments[0].scrollIntoView();",denemeXPATH)
            print("Sayfa Scroll Edildi . . .")
            time.sleep(1)
            sayfaKaydirmaParametresi = sayfaKaydirmaParametresi + 9
        except:
            print("scroll edilemedi . . .")
        denememXPATHIM = f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[{str(sayfaKaydirmaParametresi)}]/div/div/div/div/div/div/div/div/div/div/div[1]/div/a'
        denemeXPATH = browser.find_element(By.XPATH,denememXPATHIM) 
        try:
            print("sayfa scroll ediliyor . . .")
            time.sleep(1)
            browser.execute_script("arguments[0].scrollIntoView();",denemeXPATH)
            print("Sayfa Scroll Edildi . . .")
            time.sleep(1)
            sayfaKaydirmaParametresi = sayfaKaydirmaParametresi + 9
        except:
            print("scroll edilemedi . . .")   
def getContact(_webListesi):
    for x in _webListesi:
        browser.get(x)
        time.sleep(1)
        try:
            stringim = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/ul/div[3]/div[2]/div/div/span").text
            print(stringim)
            if kontrol_fonksiyonu(stringim) == 1 and var_mi_kontrol_fonksiyonu(emailDizisi, stringim) == 1:
                emailDizisi.append(stringim)
                print(stringim)
                print("Eklendi")
            elif kontrol_fonksiyonu(stringim) == 0 and var_mi_kontrol_fonksiyonu(cepTelefonlariDizisi, stringim) == 1:
                cepTelefonlariDizisi.append(stringim)
                print(stringim)
                print("Eklendi")
            print(emailDizisi)
            print(cepTelefonlariDizisi)
        except:
            print("yok 1")
        time.sleep(1)
        try:
            stringim2 = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div/ul/div[4]/div[2]/div/div/span").text
            if kontrol_fonksiyonu(stringim2) == 1 and var_mi_kontrol_fonksiyonu(emailDizisi, stringim2) == 1:
                emailDizisi.append(stringim2)
                print(stringim2)
                print("Eklendi")   
            elif kontrol_fonksiyonu(stringim2) == 0 and var_mi_kontrol_fonksiyonu(cepTelefonlariDizisi, stringim2) ==1:
                cepTelefonlariDizisi.append(stringim2)
                print(stringim2)
                print("Eklendi")
            print(emailDizisi)
            print(cepTelefonlariDizisi)
        except:
            time.sleep(1)
            try: 
                stringim3 = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/ul/div[3]/div[2]/div/div/span").text
                if kontrol_fonksiyonu(stringim3) == 1 and var_mi_kontrol_fonksiyonu(emailDizisi, stringim3) == 1:
                    emailDizisi.append(stringim3)
                    print(stringim3)
                    print("Eklendi")   
                elif kontrol_fonksiyonu(stringim3) == 0 and var_mi_kontrol_fonksiyonu(cepTelefonlariDizisi, stringim3) ==1:
                    cepTelefonlariDizisi.append(stringim3)
                    print(stringim3)
                    print("Eklendi")
            except:
                print("Yok 2")
            print(emailDizisi)
            print(cepTelefonlariDizisi)
        print(emailDizisi)
        print(cepTelefonlariDizisi)
getBaglantilar(kacIletisimBilgisiIstiyorsunuz)
print(web_baglantilari_listesi)
print(f"kac web baglantisi var: {len(web_baglantilari_listesi)}")
getContact(web_baglantilari_listesi)
print(emailDizisi)
print(cepTelefonlariDizisi)
browser.close()

import pandas as pd

def listToDataFrame1(_telList):
    df1 = pd.DataFrame(_telList, columns=["tel Listesi"])
    print(df1)
    with pd.ExcelWriter(r"telList.xlsx") as writer:
        df1.to_excel(writer, sheet_name="telList")
listToDataFrame1(cepTelefonlariDizisi)

def listToDataFrame2(_webList):
    df1 = pd.DataFrame(_webList, columns=["Web Listesi"])
    print(df1)
    with pd.ExcelWriter(r"webListesi.xlsx") as writer:
        df1.to_excel(writer, sheet_name="weblist")
listToDataFrame2(web_baglantilari_listesi)

def listToDataFrame3(_mailList):
    df1 = pd.DataFrame(_mailList, columns=["Mail Listesi"])
    print(df1)
    with pd.ExcelWriter(r"mailListesi.xlsx") as writer:
        df1.to_excel(writer, sheet_name="mailList")
listToDataFrame3(emailDizisi)