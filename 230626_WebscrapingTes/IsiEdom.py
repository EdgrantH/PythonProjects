from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
import pwinput

def hilangin_ssl():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return browser

def login(browser, path):
    loop = True
    while loop:
        browser.get(path)
        # input from user
        name = input("User ID anda: ")

        password = pwinput.pwinput(prompt='Password: ')


        # inpur to web
        try:
            search_bar = browser.find_element(By.NAME, "u")
            search_bar.send_keys(name)
            search_bar = browser.find_element(By.NAME, "p")
            search_bar.send_keys(password)
            search_bar.submit()
        except:
            loop = False
            break #redundency

        # # Check if login is successful
        # if login_successful(browser):
        #     loop = False
        #     break  # Break out of the loop if login is successful
        # Check if login is successful
        if True:
            loop = False
            break  # Break out of the loop if login is successful

        continue
        print("Login unsuccessful. Please try again.")

def login_successful(browser):
    # Mencari tombol logout
    try:
        browser.find_element(By.CLASS_NAME, 'linfo')
        return True
    except:
        print("gagal login")
        return False
        # return True 

def click_link(browser):
    link = browser.find_element(By.LINK_TEXT, "Isi EDOM")
    link.click()
    browser.find_element(By.ID, "proceed-button").click()

def check_dosen(browser, index_dosen):
    try:
        browser.find_element(By.XPATH, '//*[@id="pertanyaan"]/tbody/tr[1]/td[%d]' % (index_dosen + 2))
        return True
    except:
        print("Dosen sudah habis")
        return False

def ganti_row_gak(browser, index):
    try:
        button = browser.find_element(By.XPATH, '//*[@id="pertanyaan"]/tbody/tr[%s]/td[2]/input' % str(index + 3))
        return "gak ganti row"
    except:
        try:
            button = browser.find_element(By.XPATH, '//*[@id="pertanyaan"]/tbody/tr[%s]/td[2]/input' % str(index + 4))
            return "ganti row"
        except:
            return "gak ada row lagi"

def link_masih_ada(browser):
    try:
        link = browser.find_element(By.LINK_TEXT, "Isi EDOM")
        return True
    except:
        return False


# path = "C:\\Users\\Edgrant\\OneDrive - UNIVERSITAS INDONESIA\\Desktop\\UI\\Others\\PythonStudy\\230626_WebscrapingTes\\Evaluasi Dosen Oleh Mahasiswa - Isi Formulir EDOM.html"

path = "https://academic.ui.ac.id/main/Authentication/"
browser = hilangin_ssl()
login(browser, path)

linkMasihAda = True

while (linkMasihAda):
    browser.get("https://academic.ui.ac.id/main/Academic/HistoryByTerm")

    if(link_masih_ada(browser)):
        browser.find_element(By.LINK_TEXT, "Isi EDOM").click()
    else:
        break

    index_dosen = 0
    dosenMasihAda = True

    # send anyways
    browser.find_element(By.XPATH, '//*[@id="proceed-button"]').click()

    while (dosenMasihAda):
        index = 0
        
        # score = int(input("nilai professor %d: " % (index_dosen + 1)))
        score = 5

        centang_masih_ada = True
        while (centang_masih_ada):
            random_score = score + random.randint(0, 2) - 1 # random +- 1

            # nilai maksimum 6 dan minimum 1
            if (random_score > 6):
                random_score = 6
            if (random_score < 1):
                random_score = 1

            # random_score = 5

            status_ganti_row = ganti_row_gak(browser, index)

            if (status_ganti_row == "gak ada row lagi"):
                centang_masih_ada = False
                print("Dosen habis")
                continue
            elif (status_ganti_row == "gak ganti row"):
                index += 1
            else:
                print("rusak bro")
            button = browser.find_element(By.XPATH, '//*[@id="pertanyaan"]/tbody/tr[%s]/td[%s]/input' % (str(index + 3), str(6*index_dosen + (random_score + 1))))
            button.click()
            index += 1
            
        index_dosen += 1
        dosenMasihAda = check_dosen(browser, index_dosen)
        
    
    if(str(input("apakah anda ingin submit (Y/N): ")).upper() == "Y"):
        browser.find_element(By.XPATH, '//*[@id="pertanyaan"]/tbody/tr[23]/td/input').click()
    else:
        print("pencet submit sendiri")

    # linkMasihAda = False

input("Press Enter to close the window...")
browser.quit()
