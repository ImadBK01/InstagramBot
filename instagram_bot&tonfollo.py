#                            @author = IMAD BOUZKRAOUI
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Add this import
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import random
import pymysql
import urllib.parse






def comment(n):
    positive_comments = [
    "Amazing!",
    "Beautiful!",
    "Incredible!",
    "Fantastic!",
    "Lovely!",
    "Awesome!",
    "Inspiring!",
    "Marvelous!",
    "Brilliant!",
    "Stunning!",
    "Impressive!",
    "Gorgeous!",
    "Adorable!",
    "Fabulous!",
    "Outstanding!",
    "Charming!",
    "Elegant!",
    "Uplifting!",
    "Magical!",
    "Joyful!",
    "Radiant!",
    "Exquisite!",
    "Spectacular!",
    "Delightful!",
    "Superb!",
    "Captivating!",
    "Heartwarming!",
    "Cheerful!",
    "Impressive!",
    "Harmonious!",
    "Sunny!",
    "Wonderful!",
    "Refreshing!",
    "Cute!",
    "Fantastic!",
    "Epic!",
    "Breathtaking!",
    "Glowing!",
    "Astonishing!",
    "Sweet!",
    "Jubilant!",
    "Splendid!",
    "Clever!",
    "Positive vibes!",
    "Harmony!",
    "Remarkable!",
    "Crisp!",
    "Vibrant!",
    "Enchanting!",
    ]
    for i in range(n):
        cmt = random.choice(positive_comments)
        try:
            filter_button = driver.find_element(By.CSS_SELECTOR, "button.btn-filter.btn.btn-small.bg-dark.white-text.waves-effect.modal-trigger")
            if filter_button:
                filter_button.click()
                print("Button Filter clicked")
        except Exception as e:
            print(f"Error while clicking Filter button: {e}")
        
        time.sleep(2.3)
        
        try:
            WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='account_action_id_3']//span"))).click()
        except TimeoutException as e:
            print(f"Timeout while waiting for element: {e}")
        
        time.sleep(2.3)
        
        try:
            filter_link = driver.find_element(By.CSS_SELECTOR, "a.waves-effect.waves-light.btn.btn-submit.btn-send-filter.modal-close")
            time.sleep(3)
            filter_link.click()
        except Exception as e:
            print(f"Error while clicking Filter link: {e}")
        
        time.sleep(3)
        
        css_selector = "/html/body/main/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/a"
        
        try:
            earn_coins_link = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, css_selector)))
            actions = ActionChains(driver)
            actions.move_to_element(earn_coins_link).click().perform()
        except TimeoutException as e:
            print(f"Timeout while waiting for element: {e}")
        
        time.sleep(5)
        new_tab = driver.window_handles[-1]
        driver.switch_to.window(new_tab)
        
        try:
            comment_btn = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//textarea[@aria-label="Add a comment…"]')))
            comment_btn.click()
            try:
                comment_btn.send_keys(cmt)
            except StaleElementReferenceException:
                comment_btn = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//textarea[@aria-label="Add a comment…"]'))
                )
                comment_btn.click()
                comment_btn.send_keys(cmt)
                time.sleep(1)
        except TimeoutException as e:
            print(f"Timeout while waiting for element: {e}")

        
        post_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="button" and contains(text(), "Post")]'))
        )
        if post_button:
            post_button.click()
            time.sleep(5)
            driver.close()
        else:
            driver.close()
            time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@onclick='Action.confirmAction();' and contains(@class, 'btn-confirm-action')]"))
        ).click()
        time.sleep(10)

    
#Liking posts
def like(n):
    for i in range(n):
        try:
            filter_button = driver.find_element(By.CSS_SELECTOR, "button.btn-filter.btn.btn-small.bg-dark.white-text.waves-effect.modal-trigger")
            if filter_button:
                filter_button.click()
            print("Button Filter clicked")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(2.3)
        WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='account_action_id_2']//span"))).click()
        time.sleep(2.3)
        filter_link = driver.find_element(By.CSS_SELECTOR, "a.waves-effect.waves-light.btn.btn-submit.btn-send-filter.modal-close")
        time.sleep(3)
        filter_link.click()
        time.sleep(3)
        # Use CSS selector for the element
        css_selector = "/html/body/main/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/a"
        
        # Define the XPath
        
        # Wait for the presence of the element
        earn_coins_link = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, css_selector)))
        
        # Use ActionChains to move to the element and click
        actions = ActionChains(driver)
        actions.move_to_element(earn_coins_link).click().perform()
        time.sleep(6)
        # Switch to the new tab
        new_tab = driver.window_handles[-1]  # Get the handle of the last opened tab
        driver.switch_to.window(new_tab)
        like_button = WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.XPATH, "//span[@class='xp7jhwk']//div[@role='button']")))
        # Use ActionChains to move to the element and click
        if like_button:
            actions = ActionChains(driver)
            actions.move_to_element(like_button).click().perform()
            time.sleep(7)
            driver.close()
            time.sleep(3)
        else:
            driver.close()
        # Switch back to the last remaining window (second window)
        driver.switch_to.window(driver.window_handles[-1])
        
        # Wait for the button to be clickable (maximum wait time: 10 seconds)
        conf_btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@onclick='Action.confirmAction();' and contains(@class, 'btn-confirm-action')]"))
        )
        
        # Do something with the element, for example, click it
        conf_btn.click()
        time.sleep(3)
    
#FOLLOWING
def follow(n):
    for i in range(n):
        try:
            filter_button = driver.find_element(By.CSS_SELECTOR, "button.btn-filter.btn.btn-small.bg-dark.white-text.waves-effect.modal-trigger")
            if filter_button:
                filter_button.click()
            print("Button Filter clicked")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(2.3)
        WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='account_action_id_1']//span"))).click()
        time.sleep(2.3)
        filter_link = driver.find_element(By.CSS_SELECTOR, "a.waves-effect.waves-light.btn.btn-submit.btn-send-filter.modal-close")
        time.sleep(3)
        filter_link.click()
        time.sleep(3)
        # Use CSS selector for the element
        css_selector = "/html/body/main/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/a"
        
        # Define the XPath
        
        # Wait for the presence of the element
        earn_coins_link = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, css_selector)))
        
        # Use ActionChains to move to the element and click
        actions = ActionChains(driver)
        actions.move_to_element(earn_coins_link).click().perform()
        time.sleep(3)
        # Switch to the new tab
        new_tab = driver.window_handles[-1]  # Get the handle of the last opened tab
        driver.switch_to.window(new_tab)
        time.sleep(3)
        follow_button = WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.XPATH, "//button[@type='button']")))
        # Use ActionChains to move to the element and click
        if follow_button:
            actions = ActionChains(driver)
            actions.move_to_element(follow_button).click().perform()
            time.sleep(7)
            driver.close()
            time.sleep(3)
        else:
            driver.close()
        # Switch back to the last remaining window (second window)
        driver.switch_to.window(driver.window_handles[-1])
        
        # Wait for the button to be clickable (maximum wait time: 10 seconds)
        conf_btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@onclick='Action.confirmAction();' and contains(@class, 'btn-confirm-action')]"))
        )
        
        # Do something with the element, for example, click it
        conf_btn.click()
        time.sleep(3)

#View story
def story(n):
    for i in range(n):
        try:
            filter_button = driver.find_element(By.CSS_SELECTOR, "button.btn-filter.btn.btn-small.bg-dark.white-text.waves-effect.modal-trigger")
            if filter_button:
                filter_button.click()
            print("Button Filter clicked")
        except Exception as e:
            print(f"Error: {e}")
            continue
        time.sleep(2.3)
        WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='account_action_id_6']//span"))).click()
        time.sleep(2.3)
        filter_link = driver.find_element(By.CSS_SELECTOR, "a.waves-effect.waves-light.btn.btn-submit.btn-send-filter.modal-close")
        time.sleep(3)
        filter_link.click()
        time.sleep(3)
        # Use CSS selector for the element
        css_selector = "/html/body/main/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/a"
        # Wait for the presence of the element
        earn_coins_link = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, css_selector)))
        
        # Use ActionChains to move to the element and click
        actions = ActionChains(driver)
        actions.move_to_element(earn_coins_link).click().perform()
        time.sleep(3)
        # Switch to the new tab
        new_tab = driver.window_handles[-1]  # Get the handle of the last opened tab
        driver.switch_to.window(new_tab)
        time.sleep(3)
        # Use ActionChains to move to the element and click
        try:
            story_button = WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.XPATH, '//div[@class="x1i10hfl xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1k74hu9 x1lq5wgf xgqcy7u x30kzoy x9jhf4c x9f619 x1ypdohk x78zum5 x1f6kntn xwhw2v2 xl56j7k x17ydfre x1n2onr6 x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xn3w4p2 x5ib6vp xc73u3c xc58f59 xm71usk x19hv4p6 xfn85t x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x178xt8z xm81vs4 xso031l xy80clv x9bdzbf" and @role="button" and @tabindex="0"]')))
            actions = ActionChains(driver)
            actions.move_to_element(story_button).click().perform()
            time.sleep(7)
            driver.close()
            time.sleep(3)
        # Continue with the rest of your code using story_button
        except TimeoutException:
            print("Button not found within the specified time. Skipping...")
            driver.close()
            


        # Switch back to the last remaining window (second window)
        driver.switch_to.window(driver.window_handles[-1])
        
        # Wait for the button to be clickable (maximum wait time: 10 seconds)
        conf_btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@onclick='Action.confirmAction();' and contains(@class, 'btn-confirm-action')]"))
        )
        
        # Do something with the element, for example, click it
        conf_btn.click()
        time.sleep(3)


def OpenInsta(username,password):
    #Open instagram account
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    
    #Locate the username and password fields
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    
    # Enter the username and password
    username_field.send_keys(username)
    time.sleep(x)
    password_field.send_keys(password)
    
    # Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    time.sleep(x)
    login_button.click()
    time.sleep(2)
    # Open a new tab using JavaScript
    driver.execute_script("window.open()")
    
    # Switch to the new tab
    new_tab = driver.window_handles[-1]  # Get the handle of the last opened tab
    driver.switch_to.window(new_tab)
    
    #SIGN IN PAGE
    
    driver.get("https://tonfollowers.com/signin")
    
    #ENTRING EMAIL AND PASSWORD & sumbit
    # Find an element by its ID attribute
    email_input = driver.find_element("id", "email")
    email_input.send_keys("wafaeali2001@gmail.com")
    password_input=driver.find_element("id", "password")
    password_input.send_keys("imad@2001")
    
    # Find the button by its XPath
    submit_button = driver.find_element('xpath', '//button[@type="submit" and contains(@class, "bg-primary")]')
    
    # Click the button
    submit_button.click()
    time.sleep(3)
    account = driver.find_element(By.CSS_SELECTOR, "#img-account-head.image-account-active.circle.modal-trigger.hide-on-small-only")
    time.sleep(2)
    account.click()
    time.sleep(3)
    try:
        # Wait for the presence of the <a> element with the specified <div> content
        a_element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(@class, 'collection-accounts') and .//div[text()='{username}']]"))
        )
    
        # Wait for the element to be clickable before clicking
        a_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(@class, 'collection-accounts') and .//div[text()='{username}']]"))
        )
        time.sleep(2)
        # Click the <a> element if it exists
        if a_element:
            a_element.click()
            print('done')
        else:
            time.sleep(2)
            print('Element not found or not clickable')
    except TimeoutException:
        print('Element not found or not clickable')
        # Handle the timeout exception as needed
    time.sleep(2)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
    time.sleep(5)


for i in range(0,3):
    x = random.randint(2,3)
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(2)
    try:
        con=pymysql.connect(host='localhost',user='root',password='samt2001',database='M23')
        mycursor=con.cursor()
    except:
        print("ErrorDatabase Connectivity Issue, Please Try Again")
    sql = "SELECT  username, password FROM iacca where email='imad' ORDER BY RAND() LIMIT 1;"
    mycursor.execute(sql)
    rows = mycursor.fetchone()
    username = rows[0]
    password = rows[1] 
    print(username)
    print(password)
    OpenInsta(username,password)
    comment(5)
    story(5)
    follow(5)
    like(5)
    time.sleep(5)
    sql = "UPDATE iacca SET score = score + 1 WHERE username=%s;"
    mycursor.execute(sql,(username))
    driver.quit()





    
    
    