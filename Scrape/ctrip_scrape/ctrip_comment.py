'''
@Description: This file is used to scrape comment data from https://you.ctrip.com/countrysightlist/australia100048.html
@Author:      Shanyue
@Time:        2019-10-02
'''

#%%
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Ctrip urls
ctrip_url = 'https://you.ctrip.com'
url = 'https://you.ctrip.com/countrysightlist/australia100048.html'

father_page = BeautifulSoup(urlopen(url).read(), "lxml")
href_list = []
attraction_list = []
div_list = []
comment_list = []
df = pd.DataFrame(columns=["city","place","rating","comments","user+time","url"])

'''
example
{"悉尼"：{'place': ['悉尼歌剧院', '悉尼海港大桥', '达令港', '悉尼水族馆', '塔龙加动物园'],
 'url': ['https://you.ctrip.com/sight/sydney236/13607.html',... 'https://you.ctrip.com/sight/sydney236/67649.html']}
'''

# To store city information: city, place, href
city_dict = {}
city_list = father_page.find_all("div", {"class":"list_mod1"})
for city in city_list:
    city_name=city.find("dl").find("dt").text
    city_detail = {}
    place_list=[]
    url_list=[]
    for a in city.find("dd").find_all("a"):
        if(not a.attrs["href"].startswith("http") and ("sight" in a.attrs["href"] \
                                                       and (not "sightlist" in a.attrs["href"]))):
            place_list.append(a.text)
            url_list.append(ctrip_url+a.attrs["href"])
    city_detail["place"]=place_list
    city_detail["url"]=url_list
    city_dict[city_name]=city_detail


#%%
for item in city_dict.items():
    city_name = item[0]
    place_list=item[1]['place']
    url_list=item[1]['url']

    for i in range(len(url_list)):
        href=url_list[i]
        place_name=place_list[i]
        # Inport chrome driver
        browser = webdriver.Chrome('chromedriver')
        browser.get(href)
        html = browser.page_source
        body = BeautifulSoup(html, "html.parser")
        user_list = body.find('ul', {"class": "comments"})

        # Get user_list: One scrape format
        if (user_list is None):
            comment_single_list = body.find_all("div", {"class": "comment_single"})

        # If no user_list: try another scrape format
        if (user_list):
            try:
                page=1
                # Set comments page 5
                while(page<=5):
                    user_list = body.find('ul', {"class": "comments"})
                    for user_info in user_list:
                        for li in user_list:
                            # Entry is one comment
                            entry = {}
                            h4 = li.find("h4")
                            p = li.find("p")
                            user_time = li.find("div", {'class': 'user-date'}).find('span')
                            entry["city"] = city_name
                            entry["place"] = place_name
                            entry["rating"] = h4.text
                            entry["comments"] = p.text
                            entry["user_time"] = user_time.text
                            entry["url"] = href
                            df = df.append(entry, ignore_index=True)

                    # Simulate clicking
                    next_page = browser.find_element_by_class_name("down ")
                    next_page.click()
                    print(href + " page " + str(page) + " has been finished.")
                    page += 1
            except:
                print(href+"has error.")
        elif (comment_single_list):
                page=1

                # Set comments page 5
                while(page<=5):
                    comment_single_list = body.find_all("div", {"class": "comment_single"})
                    for comment_single in comment_single_list:
                        # Entry is one comment
                        entry = {}
                        user = comment_single.find("div", {"class": "userimg"})
                        user = "" if user == None else user.text
                        rating = comment_single.find("ul").find("li", {"class": "title cf"})
                        rating = "" if rating == None else rating.text
                        comment = comment_single.find("ul").find("li", {"class": "main_con"})
                        comment = "" if comment == None else comment.text
                        time = comment_single.find("ul").find("li", {"class": "from_link"}).find("span",
                                                                                                 {"class": "f_left"})
                        time = "" if time == None else time.text
                        entry["city"] = city_name
                        entry["place"] = place_name
                        entry["rating"] = rating.strip()
                        entry["comments"] = comment.strip()
                        entry["user_time"] = time.strip() + user.strip()
                        entry["url"] = href
                        df = df.append(entry, ignore_index=True)
                    # Simulate clicking
                    try:
                        next_page = browser.find_element_by_class_name("nextpage")
                        browser.execute_script("GoCommentPage({0});".format(page), next_page)
                        print(href + " page " + str(page) + " has been finished.")
                        page += 1
                    except:
                        print(href+" "+str(page)+" has error.")
                        break
        else:
            print(href+" does not fall in either category.")

        print(href + " has been finished.")

# store all the data in csv
df.to_csv("raw_data.csv",index=False)