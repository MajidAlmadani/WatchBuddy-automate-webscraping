from common import *

def download_movie(driver):
    read_from_yts(driver)
    return

def read_from_yts(driver):
    url = "https://yts.mx/browse-movies"
    driver.get(url)
    driver.find_element(By.ID, "mobile-search-btn").click()
    # add try finally in the future
    search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "form-control")))
    search_bar.send_keys(reading_input_search("Movie"))
    search_bar.send_keys(Keys.RETURN)
    # add Try Finally in the future
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "browse-movie-wrap")))
    choose_movie_number_yts(driver)
    choose_movie_quality_yts(driver)

    time.sleep(100000)

    return

def choose_movie_number_yts(driver):
    movie_wrap = driver.find_elements(By.CLASS_NAME,"browse-movie-wrap")
    print("Choose depend on the Number on The Left:")
    print("[Number]: Movie Name || Year ")
    for i,movie in enumerate(movie_wrap):
        header = movie.find_element(By.CLASS_NAME,"browse-movie-bottom")
        movie_title = header.find_element(By.CLASS_NAME,"browse-movie-title").text
        movie_year = header.find_element(By.CLASS_NAME,"browse-movie-year").text
        print(f"[{i+1}]: Movie Name: {movie_title} || Year: {movie_year}")
    print("")
    choice = input("Enter the Number of the movie, you want to download: \nIf the movie is not here and want to see other choices type 0. ")
    while True:
        if(choice.isdigit()):
            choice = int(choice)
            if(int(choice) == 0):
                # Need to be checked again to go between pages
                print("Go to Next Page")
                break
            elif( 1 <= int(choice) <= 20):
                header = movie_wrap[choice-1].find_element(By.CLASS_NAME,"browse-movie-link")
                movie_link = header.get_attribute("href")
                driver.get(movie_link)
                break
            else:
                print("There is no movie with this number, Choose Again")
                choice = input("Enter the Number of the movie, you want to download: \nIf the movie is not here and want to see other choices type 0. ")
        else:
            print("Wrong Choice Choose Again")
            choice = input("Enter the Number of the movie, you want to download: \nIf the movie is not here and want to see other choices type 0. ")
    return

def choose_movie_quality_yts(driver):
    movie_quality = driver.find_elements(By.XPATH,"//div[@class='bottom-info']/p[@class='hidden-md hidden-lg']/a[@rel='nofollow']")
    print("Choose depend on the Number on The Left:")
    print("[Number]: Quality of the Movie ")
    for i,quality in enumerate(movie_quality):
        print(f"[{i+1}]: Quality of the Movie: {quality.text}")
    choice = input("Enter the Number of the Quality, you want to download: ")
    while True:
        if(choice.isdigit()):
            choice = int(choice)
            if( 1 <= int(choice) <= i):
                movie_link = movie_quality[choice-1].get_attribute("href")
                driver.get(movie_link)
                break
            else:
                print("There is no Quality with this number, Choose Again")
                choice = input("Enter the Number of the Quality, you want to download:")
        else:
            print("Wrong Choose Choose Again")
            choice = input("Enter the Number of the Quality, you want to download: ")
    return

