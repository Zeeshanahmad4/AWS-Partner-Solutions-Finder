# coding: utf-8
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
# import csv
import random
import unicodecsv as csv



def link_assembler(file_path, name):
    fieldnames = ['Grade']

    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "Grade": name,
        })

def end_data(file_path, Name, Category, Address, Phone, Price_range, Health_rating, Info, Working_hours, Ratings, Ratings_histogram, Claimed_status, Reviews, Website, Url,Amazon):
    fieldnames = ['name', 'category', 'address', 'phone', 'price_range', 'health_rating', 'info',
                  'working_hours', 'ratings', 'ratings_histogram', 'claimed_status', 'reviews', 'website', 'url',"amazon"]

    with open(file_path, "ab") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "name": Name,
            "category": Category,
            "address": Address,
         			"phone": Phone,
         			"price_range": Price_range,
         			"health_rating": Health_rating,
         			"info": Info,
         			"working_hours": Working_hours,
            "ratings": Ratings,
         			"ratings_histogram": Ratings_histogram,
         			"claimed_status": Claimed_status,
         			"reviews": Reviews,
         			"website": Website,
         			"url": Url,
                     "amazon":Amazon
        })


options = Options()
options.headless = False
#PROXY = "36.67.23.117:8888" # IP:PORT or HOST:PORT
#options.add_argument('--proxy-server=%s' % PROXY)
driver = selenium.webdriver.Chrome(chrome_options=options)
driver.set_page_load_timeout(10000)
a = 0
b = 1
list_name_of_competence = []
with open("links.csv", "rb") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        url = row[0]
        # a = 0
        # while True:
        #     a += b
        #     if a==3:
        #         break
        print(url)
        driver.get(url)
        # sec = random.randint(0,2)
        # sleep(sec)
        header = driver.find_element_by_class_name("psf-header")
        try:
            name = header.find_element_by_xpath("//*[@id='aws-page-content']/div/div/main/section/div/div/div[2]/div[1]/div/span").text
        except:
            name = ""
        try:
            Headquarters = driver.find_element_by_xpath("//*[@id='aws-page-content']/div/div/main/section/div/div/div[2]/div[2]/div[1]/div/a[2]/span").text
        except:
            Headquarters = ""
        try:
            Webstite = driver.find_element_by_xpath("//*[@id='aws-page-content']/div/div/main/section/div/div/div[2]/div[2]/div[2]/div/a").text
        except:
            Webstite = ""
        try:
            Partner_type = driver.find_element_by_xpath("//*[@id='aws-page-content']/div/div/main/section/div/div/div[2]/div[2]/div[3]/div/div").text
        except:
            Partner_type = ""
        try:
            Overview  = driver.find_element_by_xpath("//*[@id='psf-overview']/div[1]/div/div").text    
        except:
            Overview = ""
        try:
            head_all = driver.find_elements_by_class_name("psf-competencies")
            AWS_Competencies  = head_all[0].find_elements_by_tag_name("ul")
        except:
            pass
        # print (head_all[0].text)
        
        try:
            childs_competencies = AWS_Competencies[0].find_elements_by_tag_name("li")
            for competence in childs_competencies:
                name_of_competence = competence.text
                list_name_of_competence.append(name_of_competence)
            all_competenceies = ",".join(list_name_of_competence)
            list_name_of_competence = []
            # print(all_competenceies)
        except:
            all_competenceies = ""
        try:

            AWS_Services  = AWS_Competencies[1].find_element_by_xpath("//*[@id='psf-overview']/div[3]/div/div[2]/ul").text
            all_Services = AWS_Services.split("\n")
            all_Services = ",".join(all_Services)
        except:
            all_Services = ""
        # for Services in childs_AWS_Services:
        #     name_of_Services = Services.text.encode('utf-8')
        #     list_name_of_competence.append(name_of_Services)
        # all_Services = ",".join(list_name_of_competence)
        # list_name_of_competence = []
        # print(all_Services)
        try:
            AWS_Programs  = AWS_Competencies[2].find_element_by_xpath("//*[@id='psf-overview']/div[3]/div/div[3]/ul").text
            Program = AWS_Programs.split("\n")
            final_Program = ",".join(Program)
        except:
            final_Program = ""

        # print(final_Program)
        # childs_AWS_Programs = AWS_Programs.find_elements_by_tag_name("li")
        # for Programs in childs_AWS_Programs:
        #     name_of_Programs = Programs.text.encode('utf-8')
        #     list_name_of_competence.append(name_of_Programs)
        # # all_Programs = ",".join((list_name_of_competence))
        #     for pro in list_name_of_competence:
        #         program += str(pro)
        #         program += ","
        # program = program[:-1]
        # list_name_of_competence = []

        
        try:
            AWS_Competencies  = head_all[4].find_elements_by_tag_name("ul")
            # AWS_CERTIFICATIONS  = AWS_Competencies[0].find_element_by_xpath("//*[@id='psf-overview']/div[3]/div/div[4]/ul").text
            AWS_CERTIFICATIONS = AWS_Competencies[0].text
            CERTIFICAT = AWS_CERTIFICATIONS.split("\n")
            final_certificate = ",".join(CERTIFICAT)
        except:
            final_certificate = ""

        # print(final_certificate)
        # childs_AWS_CERTIFICATIONS = AWS_CERTIFICATIONS.find_elements_by_tag_name("li")
        # for CERTIFICATs in childs_AWS_CERTIFICATIONS:
        #     name_of_CERTIFICATs = CERTIFICATs.text.encode('utf-8')
        #     list_name_of_competence.append(name_of_CERTIFICATs)
        # # all_CERTIFICATs = ",".join(list_name_of_competence)
        # # print(all_CERTIFICATs)
        #     for cerf in list_name_of_competence:
        #         CERTIFICAT += str(cerf)
        #         CERTIFICAT += ","
        # CERTIFICAT = CERTIFICAT[:-1]
        # print(CERTIFICAT)
        # list_name_of_competence = []
        # print("z"*1000)

        # Solution = ""                       
        # Solution_Areas  = driver.find_element_by_xpath("//*[@id='psf-overview']/div[5]/div/div[1]/ul").text
        try:

            Solution_Areas = AWS_Competencies[1].text
            Solution        =Solution_Areas.split("\n")
            final_solution = ",".join(Solution)
        except:
            final_solution = ""
        # childs_Solution_Areas = Solution_Areas.find_elements_by_tag_name("li")
        # for Solution in childs_Solution_Areas:
        #     name_of_Solution = Solution.text
        #     list_name_of_competence.append(name_of_Solution)
        #     print(list_name_of_competence)
        #     # for sol in list_name_of_competence:
        #     #     try:
        #     #         Solution += str(sol)
        #     #         Solution += ","
        #     #     except:
        #     #         pass
                
        # # Solution = Solution[:-1]
        # # print(Solution)
        # # all_Solution = ",".join(list_name_of_competence)
        # # print(all_Solution)
        # list_name_of_competence = []


        
        # Industry_Areas  = driver.find_element_by_xpath("//*[@id='psf-overview']/div[5]/div/div[2]/ul").text
        try:
            Industry_Areas = AWS_Competencies[2].text
            Industry        =Industry_Areas.split("\n")
            final_Industry = ",".join(Industry)
        except:
            final_Industry = ""
# 

        # Target_Areas  = driver.find_element_by_xpath("//*[@id='psf-overview']/div[5]/div/div[3]/ul").text
        try:

            Target_Areas = AWS_Competencies[3].text
            Target        =Target_Areas.split("\n")
            final_Target = ",".join(Target)
        except:
            final_Target = ""

# //*[@id="psf-overview"]/div[5]/div/div[4]/ul
        try:
        # Tec_Areas  = driver.find_element_by_xpath("//*[@id='psf-overview']/div[5]/div/div[4]/ul").text
            Tec_Areas = AWS_Competencies[4].text
            Technology        =Tec_Areas.split("\n")
            final_Tecnology = ",".join(Technology)
        except:
            final_Tecnology = ""

# //*[@id="psf-overview"]/div[5]/div/div[5]/ul
        try:
            # Pro_services  = driver.find_element_by_xpath("//*[@id='psf-overview']/div[5]/div/div[5]/ul").text
            Pro_services = AWS_Competencies[5].text
            pro_services_single       =Pro_services.split("\n")
            final_services = ",".join(pro_services_single)
        except:
            final_services = ""


        end_data("data2.csv",name,Headquarters,Webstite,Partner_type,Overview,all_competenceies,all_Services,final_Program,final_certificate,final_solution,final_Industry,final_Target,final_Tecnology,final_services,url)
                # break
            # except:
                # link_assembler("missed.csv",url)
                # pass
        AWS_Competencies = ""
        

