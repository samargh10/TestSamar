from behave import *
from selenium import webdriver
from selenium.webdriver import support
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time

finalProduct = ""
@given("I launch the URL")
def I_Launch_the_URL(context):
    context.driver = webdriver.Chrome("C:/Users/Saswath/Documents/chromedriver_win32/chromedriver.exe")
    context.driver.get("https://testscriptdemo.com/")
    context.driver.maximize_window()
    delay = 5
    myElem = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '//img[1]')))

@Then("I should see the home page")
def I_should_see_the_home_page(context):
    title   = context.driver.title
    print("title is: ", title)
    if (title == "TESTSCRIPTDEMO – Automation Practice"):
        pass

@given("I am in the home page")
def I_am_in_the_home_page(context,driver):
    delay = 5
    myElem = context.WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))

@When("I click on Shop menu")
def step_impl(context):
    delay = 10
    shopLink = WebDriverWait(context.driver, delay).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Shop')]")))
    shopLink.click()
    acceptCookies = WebDriverWait(context.driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cc-window']/div[5]/a[1]")))
    acceptCookies.click()

@Then("I should be able to add four different products to wish list")
def step_impl(context):
    delay = 20
    prodList = ["Modern","Bikini","Black trousers","Evening trousers"]
    for  x in prodList:
        itemLink = WebDriverWait(context.driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//h2[text()='"+x+"']/following-sibling::img")))
        print(x)
        itemLink.click()
        time.sleep(10)
        wishList = WebDriverWait(context.driver, delay).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='summary entry-summary']//span[text()='Add to wishlist']")))
        wishList.click()
        time.sleep(10)
        shopLink = WebDriverWait(context.driver, delay).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Shop')]")))
        shopLink.click()



@When("I click on Wish list")
def step_templ(context):
    delay = 30

    wishListLink = WebDriverWait(context.driver, delay).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='header-right col-md-3 hidden-xs']//i[@class='lar la-heart']")))
    wishListLink.click()
    time.sleep(100)


@Then("I should be able to add four different products to wish list page")
def read_table(context):
    table_id = context.driver.find_element(By.XPATH, '//table[1]')
    rows = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
    for row in rows:
        # Get the columns (all the column 2)
        col = row.find_elements(By.TAG_NAME, "td")[1]  # note: index start from 0, 1 is col 2
        print(col.text)  # prints text from the element


@then(u'I should see the Wish list page')
def step_impl(context):
    delay = 10
    wishListLink = WebDriverWait(context.driver, delay).until(EC.visibility_of_element_located((By.XPATH, " //h1[text()='Wishlist']")))



@then(u'all the four products should be displayed')
def step_impl(context):
    pass


@given(u'All the four products are displayed in wish list')
def step_impl(context):
    pass


@Then("I compare the prices of products and select lowest price product")
def step_impl(context):
    table_id = context.driver.find_element(By.XPATH, '//table[1]')


    prodName1  = table_id.find_element(By.XPATH,"//table//tr[1]//td[3]")
    prodPrice1= table_id.find_element(By.XPATH,"//table//tr[1]//td[4]//ins//span[@class='woocommerce-Price-amount amount']")

    prodName2 = table_id.find_element(By.XPATH, "//table//tr[2]//td[3]")
    prodPrice2 = table_id.find_element(By.XPATH, "//table//tr[2]//td[4]//ins//span[@class='woocommerce-Price-amount amount']")

    prodName3 = table_id.find_element(By.XPATH, "//table//tr[3]//td[3]")
    prodPrice3 = table_id.find_element(By.XPATH,"//table//tr[3]//td[4]//ins//span[@class='woocommerce-Price-amount amount']")

    prodName4 = table_id.find_element(By.XPATH, "//table//tr[4]//td[3]")
    prodPrice4 = table_id.find_element(By.XPATH, "//table//tr[4]//td[4]//ins//span[@class='woocommerce-Price-amount amount']")
    strProdPrice1 = int(removeSplChars(prodPrice1.text))
    strProdPrice2 = int(removeSplChars(prodPrice2.text))
    strProdPrice3 = int(removeSplChars(prodPrice3.text))
    strProdPrice4 = int(removeSplChars(prodPrice4.text))
    numList = [strProdPrice1,strProdPrice2,strProdPrice3,strProdPrice4]
    minPrice = min(numList)
    print(minPrice)
    if(minPrice == strProdPrice1):
        addCartBtn = table_id.find_element(By.XPATH, "//table//tr[1]//td[6]")
        finalProduct = prodName1.text
    elif(minPrice == strProdPrice2):
        addCartBtn = table_id.find_element(By.XPATH, "//table//tr[2]//td[6]")
        finalProduct = prodName2.text
    elif(minPrice == strProdPrice3):
        addCartBtn = table_id.find_element(By.XPATH, "//table//tr[3]//td[6]")
        finalProduct = prodName3.text
    else:
        addCartBtn = table_id.find_element(By.XPATH, "//table//tr[4]//td[6]")
        finalProduct = prodName4.text

    time.sleep(30)
    addCartBtn.click()

@then(u'add the selected product to cart')
def step_impl(context):
    time.sleep(100)

@When("I click on Cart")
def step_impl(context):
    delay = 10
    cartLink = WebDriverWait(context.driver, delay).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='header-right col-md-3 hidden-xs']//i[@class='la la-shopping-bag']")))
    cartLink.click()
    time.sleep(20)

@Then("I should be able to see the least priced product displayed in cart")
def step_impl(context):
    cartTable = context.driver.find_element(By.XPATH,"//table[@class='shop_table shop_table_responsive cart woocommerce-cart-form__contents']")
    cartProd = cartTable.find_element(By.XPATH,"//table[1]//tbody//tr[1]//td[3]")
    cartProdText = cartProd.text
    if(finalProduct == cartProdText):
        print("Success")
    else:
        print("fail")


def removeSplChars(val):
    a_string = val
    alphanumeric = ""
    for character in a_string:
      if character.isalnum():
         alphanumeric += character



    print(alphanumeric)
    return(alphanumeric)