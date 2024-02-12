from common import *
from anime_download import *
from movie_download import *
from tvseries_download import *

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_extension('C:/Users/CornFlex/AppData/Local/Google/Chrome/User Data/Default/Extensions/cjpalhdlnbpafiamejdnhcphjbkeiagm/1.55.0_17.crx')
    options.add_extension('C:/Users/CornFlex/AppData/Local/Google/Chrome/User Data/Default/Extensions/ahmpjcflkgiildlgicmcieglgoilbfdp/3.0.57_0.crx')
    driver = webdriver.Chrome(options=options)

    # download_episode_anime4up(driver,"https://fghfg.anim4yw.shop/episode/one-piece-%d8%a7%d9%84%d8%ad%d9%84%d9%82%d8%a9-j2umq/")
    # driver.get("https://fghfg.anim4yw.shop/episode/one-piece-%d8%a7%d9%84%d8%ad%d9%84%d9%82%d8%a9-j2umq/")
    # download_anime_anime4up(driver)
    choice_type = input("Enter S => Series, M => Movie, A => Anime: ")
    while(True):
        if(choice_type.lower() == "s"):
            download_series(driver)
            driver.close()
        elif(choice_type.lower() == "m"):
            download_movie(driver)
            driver.close()
        elif(choice_type.lower() == "a"):
            download_anime(driver)
            driver.close()
        else:
            print("Wrong Choice. Please Enter Again.")
            choice_type = input("S => Series, M => Movie, A => Anime: ")
    