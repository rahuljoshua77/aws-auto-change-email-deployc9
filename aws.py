from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time,os,base64,json,csv,re
from requests_html import HTMLSession
session = HTMLSession()
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from time import sleep
cwd = os.getcwd()
opts = Options()


# opts.add_argument('--headless=chrome')
# #pts.headless = False
import random
import string

# printing lowercase
 

opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
 
opts.add_argument('--disable-setuid-sandbox')
opts.add_argument('--disable-infobars')
opts.add_argument('--ignore-certifcate-errors')
opts.add_argument('--ignore-certifcate-errors-spki-list')
opts.add_argument("--incognito")
opts.add_argument('--no-first-run')
opts.add_argument('--disable-dev-shm-usage')
opts.add_argument("--disable-infobars")
opts.add_argument("--disable-extensions")
opts.add_argument("--disable-popup-blocking")
opts.add_argument('--log-level=3') 
opts.add_argument("--start-maximized")
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option("useAutomationExtension", False)
opts.add_experimental_option("excludeSwitches",["enable-automation"])
 
# mobile_emulation = {
#     "deviceMetrics": { "width": 660, "height": 1080, "pixelRatio": 3.4 },
#     }

def pr(data):
    
    return print(f"{date_show()} [{email}] {data}")
    
def date_show():
    date = f"[{time.strftime('%d-%m-%y %X')}]"
    return date
 
def xpath_type(el,mount):
    return wait(browser,15).until(EC.element_to_be_clickable((By.XPATH, el))).send_keys(mount)

def xpath_fast(el):
    element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return element_all.click()

def xpath_faster(el):
    element_all = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)  
    return element_all.click()

def xpath_execute(el):
    element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all)

def xpath_long(el):
    element_all = wait(browser,30).until(EC.element_to_be_clickable((By.XPATH, el)))
    
    return element_all.click()

def get_country():
    element_all = wait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@class,"awsc-region-menu-item--")]')))
    return element_all

def login_account(email,password):
    sleep(2)
    pr(f'Input data login')
    pr(f"Trying to Login {email}")
 
    xpath_type('//input[@type="email"]',email)
    sleep(2)
    xpath_fast('//button[@id="next_button"]')
    sleep(2)
    xpath_type('//input[@type="password"]',password)
    sleep(2)
    xpath_fast('//button[@id="signin_button"]')

def get_email():
    browser.execute_script("window.open('','');") 
 
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://email-fake.com/')
    sleep(2)
    try:
        xpath_long('//button[@class="fem btn btn-su2 waves-effect waves-light waves-raised"]')
    except:
        pass

    email_new = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//span[@id="email_ch_text"]'))).text
    return email_new


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters + string.digits) for i in range(length))
    return result_str

def getOtp():
    browser.switch_to.window(browser.window_handles[1])
    browser.refresh()
    sleep(2)
    sleep(8)
    browser.refresh()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    otp =  wait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="code"]'))).text
    return otp

def deploy():
    pr(f"Trying to deploy")
    regions = ["https://us-west-1.console.aws.amazon.com/cloud9control/home?region=us-west-1#/create/","https://us-east-2.console.aws.amazon.com/cloud9control/home?region=us-east-2#/create/"]
    for reg in regions:
        browser.get(reg)
        xpath_type('//input[contains(@aria-labelledby,"formField2")]',get_random_string(10))
        try:
            xpath_fast('//button[@data-id="awsccc-cb-btn-accept"]')
        except:
            pass
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        xpath_long('//button[@id="create-button"]')
        notif = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"awsui_flash-content")]'))).text
        
        pr(notif)
        sleep(3)
    os.system('taskkill /F /IM ProtonVPNService.exe')
    os.system('taskkill /F /IM ProtonVPN.exe')
  
    time.sleep(5)
    os.startfile('"C:\\Program Files (x86)\\Proton Technologies\\ProtonVPN\\ProtonVPN.exe"')
    time.sleep(15)
    browser.quit()
    
def change_email():
    global email_new
    browser.get('https://signin.aws.amazon.com/updateaccount?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fbilling%2Fhome%23%2Faccount')
    xpath_long('//button[@id="edit_account_email_button"]')
    pr(f"Getting new mail")
    email_new = get_email()
    pr(f"New Mail: {email_new}")
    browser.switch_to.window(browser.window_handles[0])
    xpath_type('//input[@id="update_account_email_new_email"]',email_new)
    xpath_type('//input[@id="update_account_email_confirm_email"]',email_new)
    xpath_type('//input[@id="update_account_email_password"]',password)
    xpath_long('//button[@id="save_new_account_email_button"]')
    pr(f"Getting OTP")
    otp = getOtp()
    pr(f"OTP Found: {otp}")
    browser.switch_to.window(browser.window_handles[0])
    xpath_type('//input[@id="email_otp"]',otp)
    xpath_long('//button[@id="email_otp_save_changes_button"]')
    notif = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//span[@id="success_title"]'))).text
    sleep(3)
    pr(f"{notif}")
    sleep(5)
    
def main(email,passwords):
    global browser,password
    password=passwords
    # opts.add_experimental_option("mobileEmulation", mobile_emulation)
    opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
    # browser = webdriver.Chrome(use_subprocess=True,driver_executable_path=f"{cwd}//chromedriver.exe")
    browser = webdriver.Chrome(options=opts,desired_capabilities=dc,service=Service(ChromeDriverManager().install()))
    browser.get("https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgsFromTB_ap-southeast-2_00b54cf8a219917d&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=l7OEP9SY07oCH2gRn_OvHk8Jn20mNfIgLX_zsiMvDjU&code_challenge_method=SHA-256")
    login_account(email,password)
    sleep(10)
    try:
        xpath_fast('//a[@href="/"]')
    except:
        pass
    browser.refresh()
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//button[@aria-controls="menu--account"]')))
    print(f'{date_show()} Login success')
    pr(f"Trying to change email")
    change_email()
    deploy()
    with open('success.txt','a') as f:
        f.write(f'{email_new}|{password}\n')

if __name__ == '__main__':
    global email
    response = session.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vR9BiVIK5wPOX6zy5BFBJE8lLcYXy_U8hEYnDBz4if_XCp4CFi9ihxRAQeGtG_HgLFl3T0k9QC2JgmN/pubhtml')
    resp = response.html.xpath('//tbody//tr//td')
    data = []
    for i in resp:
        data.append(i.text)
    formatted_data = []
    for i in range(0, len(data), 2):
        formatted_data.append(f"{data[i]}|{data[i+1]}")

    print(f'{date_show()} Automation Task AWS')
    get_data = open(f"{cwd}\\data.txt","r")
    get_data = get_data.read()
    get_data = get_data.split("\n")
    for i in formatted_data:
        email = i.split("|")[0]
        password = i.split("|")[1]
        try:
            main(email,password)
        except Exception as e:
            try:
                browser.quit()
            except:
                pass
            with open('failed.txt','a') as f:
                f.write(f'{email}|{password}\n')
        