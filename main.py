import requests
from bs4 import BeautifulSoup
import re
from Driver import Driver

def main():
    html_doc = requests.get('https://www.formula1.com/en/drivers')
    soup = BeautifulSoup(html_doc.content, "html.parser")
    x = soup.find_all('a', {'class': 'group focus-visible:outline-0'})
    drivers = []
    for data in x:
        name_re = 'font-formulaOne">(.*?)</p>'
        points_re = 'leading-none normal-case">([0-9]+)</p>'
        pos_re = 'text-fs-42px leading-none\">([0-9]+)</p>'
        racing_num_re = 'Racing Number ([0-9]+)\"'
        tmp_data = str(data)

        name = re.findall(name_re, tmp_data)
        points = re.findall(points_re, tmp_data)
        pos = re.findall(pos_re, tmp_data)
        racing_num = re.findall(racing_num_re, tmp_data) 

        driver = Driver(name[0] + " " + name[1], pos[0], points[0], racing_num[0])
        drivers.append(driver) 

    print_scores(drivers)


def print_scores(drivers):
    top_score = drivers[0].points
    final_string = "Rank".ljust(5) + "| " + "Num". ljust(5) + "| Name".ljust(25) + "| Points".ljust(7) + "| Diff from first\n" + "+"*5 + "|" + "+"*6 + "|" + "+"* 24 + "|" + "+"*7 + "|" + "+" * 18 + "\n"
    for driver in drivers:
        final_string += driver.pos.ljust(5) + "| " + driver.num.ljust(5) + "| " + driver.name.ljust(23) + "| " + driver.points.ljust(6) + "| " + str((int(top_score) - int(driver.points))) + "\n"
    print(final_string)
main()