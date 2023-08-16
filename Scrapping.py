import requests
from bs4 import BeautifulSoup

def scrapeinstagram(soup1):
    #Empty List
    Data = [0]

    #Melakukan Looping
    for meta in soup1.find_all (name="meta", attrs={"property" : "og:description"}):
        #Menyimpan di List Data
        Data = meta["content"].split()
        pengikut = Data [0]
        diikuti = Data [2]
        post = Data [4]

        #Menampilkan Hasil
        print("Jumlah Postingan :", post)
        print("Jumlah yang diikuti :", diikuti)
        print("Jumlah pengikut :", pengikut)

if __name__ == "__main__":
    user=input("Masukkan Username :")
    url="https://www.instagram.com/"+user
    page=requests.get(url)
    soup=BeautifulSoup(page.text, "html.parser")
    scrapeinstagram(soup)
