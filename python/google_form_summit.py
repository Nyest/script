from selenium import webdriver
from random import randint
import time

choices=[None]*46
choices[0]=[0,1]
choices[1]=[0,2]
choices[2]=[0,1]
choices[3]=[0,3]
choices[4]=[0,5]

#page2
choices[5]=[3,4]
choices[6]=[0,4]
choices[7]=[0,4]

choices[8]=[0,4]
choices[9]=[0,4]
choices[10]=[0,4]

choices[11]=[2,4]
choices[12]=[2,4]
choices[13]=[2,4]

choices[14]=[2,4]
choices[15]=[2,4]
choices[16]=[2,4]

choices[17]=[2,4]
choices[18]=[2,4]
choices[19]=[2,4]

choices[20]=[3,4]
choices[21]=[3,4]
choices[22]=[3,4]

choices[23]=[1,4]
choices[24]=[1,4]
choices[25]=[1,4]


#page3
choices[26]=[2,4]
choices[27]=[2,4]
choices[28]=[2,4]

choices[29]=[1,4]
choices[30]=[1,4]
choices[31]=[1,4]

choices[32]=[3,4]
choices[33]=[3,4]
choices[34]=[3,4]

choices[35]=[2,4]
choices[36]=[2,4]
choices[37]=[2,4]

choices[38]=[2,4]
choices[39]=[2,4]
choices[40]=[2,4]

#page4
choices[41]=[2,4]
choices[42]=[2,4]
choices[43]=[2,4]
choices[44]=[2,4]
choices[45]=[2,4]

for humans in range(80):
    url = ""

    driver = webdriver.Chrome()
    driver.get(url)

    count = 0
    for page in range(4):
        print page
        if page == 0:
            elements = driver.find_elements_by_class_name("freebirdFormviewerViewItemsItemItem")
            for i, option in enumerate(elements):
                if i > 0:
                    selectors = option.find_elements_by_class_name("exportLabelWrapper")
                    ex = randint(choices[count][0], choices[count][1])
                    print "count: %d min: %d max: %d ex: %d" % (count, choices[count][0], choices[count][1], ex)
                    count = count + 1
                    time.sleep( 1 )
                    if i == 1:
                        if humans % 3 == 0:
                            ex = 0
                        else:
                            ex = 1
                    for j, object in enumerate(selectors):
                        if ex == j:
                            object.click()
        else:
            elements = driver.find_elements_by_class_name("freebirdFormviewerViewItemsGridRowGroup")
            for i, option in enumerate(elements):
                selectors = option.find_elements_by_class_name("quantumWizTogglePaperradioOffRadio")
                ex = randint(choices[count][0], choices[count][1])
                print "count: %d min: %d max: %d ex: %d" % (count, choices[count][0], choices[count][1], ex)
                count = count + 1
                time.sleep( 1 )
                for j, object in enumerate(selectors):
                    if ex == j:
                        object.click()

        time.sleep( 1 )
        if page < 3:
            buttons = driver.find_elements_by_class_name("freebirdFormviewerViewNavigationButtons")
            for i, object in enumerate(buttons):
                object.click()
        else:
            buttons = driver.find_elements_by_class_name("freebirdFormviewerViewNavigationSubmitButton")
            for i, object in enumerate(buttons):
                object.click()

    time.sleep( 1 )
    driver.quit()
