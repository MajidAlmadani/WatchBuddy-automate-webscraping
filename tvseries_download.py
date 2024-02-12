from common import *


## TV Series
def download_series(driver):
    read_from_ytstv(driver)
    return

def read_from_ytstv(driver):
    url = "https://ytstv.me/"
    driver.get(url)
    driver.find_element(By.XPATH, "//div[@class='mobile-search']").click()
    # # add try finally in the future
    search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='form-control search-input']")))
    search_bar.send_keys(reading_input_search("Series"))
    search_bar.send_keys(Keys.RETURN)
    # # add Try Finally in the future
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-lg-4 footer-copyright']")))
    choose_series_number_ytstv(driver)
    season_wrap = driver.find_elements(By.CLASS_NAME,"tvseason")
    flag_download_main_page = False
    if(len(season_wrap) == 1):
        num_season = 1
        flag_full_bulk = season_wrap[0].find_elements(By.TAG_NAME,"a")
        if(len(flag_full_bulk) == 1):
            flag_full_bulk[0].click()
        else:
            flag_download_main_page = True

    elif(len(season_wrap) > 1):
        num_season = reading_num_season(len(season_wrap))
        flag_full_bulk = season_wrap[num_season-1].find_elements(By.TAG_NAME,"a")
        if(len(flag_full_bulk) == 1):
            flag_full_bulk[0].click()
        else:
            flag_download_main_page = True
    else:
        print("This is an error")
    
    if(flag_download_main_page):
        download_episodes_main_page_ytstv(driver,flag_full_bulk,num_season)
        print("Downloading ...")
    else:
        download_wrap = driver.find_element(By.XPATH, "//div[@class='btn-group btn-group-justified embed-selector']")
        flag_episode_possible = download_wrap.find_element(By.XPATH,"//a/span[@class='lnk lnk-dl']/span[@class='serv_tit']").text
        if(flag_episode_possible == "Complete"):
            possible_qualities = driver.find_elements(By.XPATH,"//div[@class='tab-pane active']/div[@id='lnk list-downloads']/div[@class='btn-group btn-group-justified embed-selector']/a")
            choose_quality_ytstv(driver,possible_qualities)
            print("Downloading ...")
        else:
            download_episodes_ytstv(driver)
            print("Downloading ...")
    

    time.sleep(100000)
    return

def choose_series_number_ytstv(driver):
    series_wrap = driver.find_elements(By.CLASS_NAME,"ml-item")
    print("Choose depend on the Number on The Left:")
    print("[Number]: Series Name ")
    for i,series in enumerate(series_wrap):
        series_title = series.find_element(By.TAG_NAME,"h2").text
        print(f"[{i+1}]: Series Name: {series_title}")

    print("")
    choice = input("Enter the Number of the Series, you want to download: \nIf the Series is not here and want to see other choices type 0. ")
    while True:
        if(choice.isdigit()):
            choice = int(choice)
            if(int(choice) == 0):
                # Need to be checked again to go between pages
                print("Go to Next Page")
                break
            elif( 1 <= int(choice) <= 20):
                series_wrap[choice-1].click()
                break
            else:
                print("There is no Series with this number, Choose Again")
                choice = input("Enter the Number of the Series, you want to download: \nIf the Series is not here and want to see other choices type 0. ")
        else:
            print("Wrong Choice Choose Again")
            choice = input("Enter the Number of the Series, you want to download: \nIf the Series is not here and want to see other choices type 0. ")
    return

def choose_quality_ytstv(driver,possible_qualities):
    print("Choose depend on the Number on The Left:")
    print("[Number]: Series Quality ")
    for i,quality in enumerate(possible_qualities):
        titles = quality.find_elements(By.CLASS_NAME,"lnk")
        quality_title = titles[2].text
        # if(quality_title == ""):
        #     possible_qualities.pop(i)
        # else:
        print(f"[{i+1}]: Quality: {quality_title}")

    print("")
    choice = input("Enter the Number of the Quality, you want to download: ")
    while True:
        if(choice.isdigit()):
            choice = int(choice)
            if( 1 <= int(choice) <= len(possible_qualities)):
                possible_qualities[choice-1].click()
                break
            else:
                print("There is no Quality with this number, Choose Again")
                choice = input("Enter the Number of the Quality, you want to download: ")
        else:
            print("Wrong Choice Choose Again")
            choice = input("Enter the Number of the Quality, you want to download: ")
    return

def download_episodes_ytstv(driver):
    all_links = driver.find_elements(By.XPATH,"//div[@class='tab-pane active']/div[@id='lnk list-downloads']/div[@class='btn-group btn-group-justified embed-selector']/a")
    qualities = []
    print("Choose depend on the Number on The Left:")
    print("[Number]: Series Quality ")
    for i,quality in enumerate(all_links):
        titles = quality.find_elements(By.CLASS_NAME,"lnk")
        quality_title = titles[2].text
        if(not(quality_title in qualities)):
            qualities.append(quality_title)
            print(f"[{i+1}]: Quality: {quality_title}")
        else:
            break        
    print("")
    choice = input("Enter the Number of the Quality, you want to download: ")
    while True:
        if(choice.isdigit()):
            choice = int(choice)
            if( 1 <= int(choice) <= len(qualities)):
                num_episodes = round(len(all_links)/len(qualities))
                download_iterator = choice
                for i in range(0,num_episodes):
                    quality_title = all_links[download_iterator-1].find_elements(By.CLASS_NAME,"lnk")[2].text
                    if qualities[choice-1] == quality_title:
                        all_links[download_iterator-1].click()
                        download_iterator+=len(qualities)
                    else:
                        all_links[download_iterator-2].click()
                        download_iterator+=len(qualities)
                break
            else:
                print("There is no Quality with this number, Choose Again")
                choice = input("Enter the Number of the Quality, you want to download: ")
        else:
            print("Wrong Choice Choose Again")
            choice = input("Enter the Number of the Quality, you want to download: ")
    return

def download_episodes_main_page_ytstv(driver,flag_full_bulk,num_season):
    flag_full_bulk[0].click()
    all_links = driver.find_elements(By.XPATH,"//div[@class='tab-pane active']/div[@id='lnk list-downloads']/div[@class='btn-group btn-group-justified embed-selector']/a")
    qualities = []
    print("Choose depend on the Number on The Left:")
    print("[Number]: Series Quality ")
    print(f"This is {len(flag_full_bulk)}")
    for i,quality in enumerate(all_links):
        titles = quality.find_elements(By.CLASS_NAME,"lnk")
        quality_title = titles[2].text
        if(not(quality_title in qualities)):
            qualities.append(quality_title)
            print(f"[{i+1}]: Quality: {quality_title}")
        else:
            break        
    print("")
    choice = input("Enter the Number of the Quality, you want to download: ")
    while True:
        if(choice.isdigit()):
            choice = int(choice)
            if( 1 <= int(choice) <= len(qualities)):
                num_episodes = len(flag_full_bulk)
                for i in range(1,num_episodes+1):
                    quality_title = all_links[choice-1].find_elements(By.CLASS_NAME,"lnk")[2].text
                    print(f"This is quality:{quality_title}.")
                    print(f"This is quality:{qualities[choice-1]}.")
                    if qualities[choice-1] == quality_title:
                        print("Here")
                        all_links[choice-1].click()
                    else:
                        all_links[choice-2].click()
                    driver.back()
                    if(i != len(flag_full_bulk)):
                        season_wrap = driver.find_elements(By.CLASS_NAME,"tvseason")
                        flag_full_bulk = season_wrap[num_season-1].find_elements(By.TAG_NAME,"a")
                        flag_full_bulk[i].click()
                        all_links = driver.find_elements(By.XPATH,"//div[@class='tab-pane active']/div[@id='lnk list-downloads']/div[@class='btn-group btn-group-justified embed-selector']/a")
                break
            else:
                print("There is no Quality with this number, Choose Again")
                choice = input("Enter the Number of the Quality, you want to download: ")
        else:
            print("Wrong Choice Choose Again")
            choice = input("Enter the Number of the Quality, you want to download: ")
    return














