from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opt = Options()
chrome_driver_path = "P:\\chrome\\chromedriver.exe"
chrome_service = Service(chrome_driver_path)
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(service=chrome_service, options=opt)

i = 0
add_translations_clicked = False


while i < 5:
    try:
        if not add_translations_clicked:
            print("Clicked")
            # wait for the "add-translations-button" element to become clickable
            add_translations_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "add-translations-button"))
            )

            # click on the "add-translations-button" element
            add_translations_button.click()

            add_translations_clicked = False

        # wait for the "text-item" element to become clickable
        text_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "text-item-{}".format(i)))
        )

    
        # click on the "text-item" element if it is not disabled
        print(str(i))
        text_item.click()

        # increment i only after a successful click
        i += 1
        add_translations_clicked = False

    except ElementClickInterceptedException:
        add_translations_clicked = True
        i += 1
        continue

# if add_translations_clicked:
#     text_item = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.ID, "text-item-5"))
#             )

    
#         # click on the "text-item" element if it is not disabled
#     print(str(i))

#     #necessary to exit out of loop
#     text_item.click()


#keep even numbers only

elements = driver.find_elements("xpath", "//ytcp-button[@label='Add']")
print(elements)


for i in range(0, len(elements), 2):  # iterate through every even index
    element = elements[i]
    element.click()
    dialog_xpath = f"/html/body/ytgn-metadata-editor[{i+1}]/tp-yt-paper-dialog/div/div[3]/ytcp-button[2]/div"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dialog_xpath))).click()
    # search.send_keys(Keys.RETURN) 
    # try:
    # #     # dialog = driver.find_element("xpath", "//div[@id='metadata-editor-wrapper']")
    # #     # driver.switch_to.frame(dialog)
        
    #     # cancel_button = driver.find_element("xpath", "/html/body/ytgn-metadata-editor/tp-yt-paper-dialog/div/div[3]/ytcp-button[2]/div")
    #     # cancel_button.click()
    #     driver.implicitly_wait(5)

    

    # except NoSuchElementException:
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytve-captions-editor-modal/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-captions-editor-options-panel/div[2]/div/ul/li[4]/ytcp-ve/a"))).click()
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytve-captions-editor-modal/ytcp-dialog/tp-yt-paper-dialog/div[1]/div/div[2]/div[2]/ytcp-button/div"))).click()









