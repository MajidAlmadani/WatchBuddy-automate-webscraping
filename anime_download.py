from common import *
   
def download_anime(driver):
    # read_from_animepahe(driver)
    read_from_anime4up(driver)
    return

###### Anime4up ######    
def read_from_anime4up(driver):
    url = "https://fghfg.anim4yw.shop/"
    driver.get(url)
    wait_click_XPATH(driver,'//*[@id="showSearch"]')
    search_bar = wait_find_XPATH(driver,'//*[@id="searchform"]/div/input[2]')
    search_bar.send_keys(reading_input_search("Anime"))
    search_bar.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "anime-list-content")))
    anime_search_result = wait_find_XPATH(driver,'/html/body/div[4]/div')
    choose_anime_number_anime4up(driver)
    wait_click_XPATH(driver,'//*[@id="DivEpisodesList"]/div[1]/div/div')
    download_anime_anime4up(driver)
    time.sleep(10000)
    return   

def choose_anime_number_anime4up(driver):
    anime_wrap = wait_finds_XPATH(driver,'/html/body/div[4]/div/div/div[1]/div')
    print("Choose depend on the Number on The Left:")
    print("[Number]: Anime Name")
    for i,anime in enumerate(anime_wrap):
        anime_title = anime.find_element(By.TAG_NAME,"h3").text
        print(f"[{i+1}]: Anime Name: {anime_title}")
    print("")
    choice = input("Enter the Number of the Anime, you want to download: \nIf the Anime is not here and want to see other choices type 0. ")
    while True:
        if(choice.isdigit()):
            choice = int(choice)
            if(int(choice) == 0):
                # Need to be checked again to go between pages
                print("Go to Next Page")
                break
            elif( 1 <= int(choice) <= len(anime_wrap)):
                anime_wrap[choice-1].click()
                break
            else:
                print("There is no Anime with this number, Choose Again")
                choice = input("Enter the Number of the Anime, you want to download: \nIf the Anime is not here and want to see other choices type 0. ")
        else:
            print("Wrong Choice Choose Again")
            choice = input("Enter the Number of the Anime, you want to download: \nIf the Anime is not here and want to see other choices type 0. ")
    return

def download_anime_anime4up(driver):
    anime_series_episodes = wait_finds_XPATH(driver,'//*[@id="mCSB_1_container"]/li/a')
    episodes_links = [i.get_attribute('href') for i in anime_series_episodes]
    # download_episode_anime4up(driver,episodes_links[0])
    first_episode = episodes_links.pop(0)
    count = 0
    for i in episodes_links:
        print(f"this is {i}.")
        download_episode_anime4up(driver,i)
        count += 1
        if count == 100:
            break
        time.sleep(5)
    download_episode_anime4up(driver,first_episode)
    return

def download_episode_anime4up(driver,link):
    driver.get(link)
    wait_click_XPATH(driver,'/html/body/div[4]/div/div/center/center/div/div/a')
    wait_click_XPATH(driver,'//*[@id="app"]/div/div/div/main/div/div[2]/div[1]/div/div[2]/div[3]/button')
    wait_get_XPATH(driver,'//*[@id="app"]/div/div/div/main/div/div[2]/div/div/div/div[1]/div/div[3]/a')
    wait_get_XPATH(driver,'/html/body/main/div/section/center/div/div/div/a[1]')
    wait_click_XPATH(driver,'//*[@id="F1"]/button')
    wait_get_XPATH(driver,'/html/body/main/div/section/div/div/div/div/a')
    return


###### Animepahe ######  
def read_from_animepahe(driver):
    url = "https://animepahe.ru/"
    driver.get(url)
    
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.CLASS_NAME, "navbar-toggler-icon")))
    driver.find_element(By.XPATH,"//nav[@class='navbar navbar-expand-lg']/button[@class='navbar-toggler navbar-toggler-right']").click()

    search_bar = WebDriverWait(driver,10000).until(visibility_of_element_located((By.XPATH, "//input[@name='q']")))
    search = reading_input_search("Anime")
    search_bar.send_keys(search)
    WebDriverWait(driver,10000).until(visibility_of_element_located((By.CLASS_NAME, "search-results")))

    search_results = driver.find_elements(By.XPATH,"//div[@class='search-results-wrap']/ul[@class='search-results']/li")
    for i,result in enumerate(search_results):
        result_title = result.find_element(By.CLASS_NAME,"result-title").text
        print(f"[{i+1}]: {result_title}")
    
    choice = int(input("Choose one: "))
    search_results[choice-1].click()
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.CLASS_NAME, "episode-wrap")))

    driver.find_element(By.XPATH,"//div[@class='episode-list row']/div[@class='episode-wrap col-12 col-sm-4']").click()

    episodes_links_driver = driver.find_elements(By.XPATH,"//div[@id='scrollArea']/a")
    episodes_links = [i.get_attribute('href') for i in episodes_links_driver]
    count = 1
    print("Downloading ...")
    for i in episodes_links:
        print(f"episode: {count}")
        download_episode_from_animepahe(driver,i)
        count += 1
    
    time.sleep(10)
    return

def download_episode_from_animepahe(driver,link):
    driver.get(link)
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.ID, "downloadMenu")))
    driver.find_element(By.ID, "downloadMenu").click()
    download_options = driver.find_elements(By.XPATH,"//div[@class='dropup show']/div[@id='pickDownload']/a")
    if len(download_options) > 5:
        link_link = download_options[len(download_options)-4].get_attribute('href')
    else:
        link_link = download_options[len(download_options)-1].get_attribute('href')
    driver.get(link_link)
    WebDriverWait(driver, 10000).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='row']/div[@class='col-sm-6']/a[@class='btn btn-secondary btn-block redirect']"), "Continue"))
    download_link = driver.find_element(By.XPATH,"//div[@class='row']/div[@class='col-sm-6']/a[@class='btn btn-secondary btn-block redirect']").get_attribute('href')
    driver.get(download_link)
    form = driver.find_element(By.CSS_SELECTOR, "button[type='" + "submit" + "']")
    driver.execute_script("arguments[0].click();", form)
    time.sleep(1)
    return