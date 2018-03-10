"""
Human Friendly Name: Syllable
Import Friendly Name: syllable
Package Description: Package that send a word or words set to service and get the syllabes of each phrase sent
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://tip.iatext.ulpgc.es/silabas/Default.aspx")


def sendingWords():
    with open('Diccionario.txt', 'r') as input, \
            open('output.txt', 'w') as output:
        for item in input:
            element = driver.find_element_by_id("MainContent_TextBox1")
            element.send_keys(item)

            result = driver.find_element_by_css_selector("table#MainContent_Table1 > tbody > tr > td:nth-of-type(2)").text
            # output.write(result)
            output.write("My word sent is: {item}. "
                         "The word divide in silabes is: {result}\n".format(item=item, result=result))


#sendingWords()