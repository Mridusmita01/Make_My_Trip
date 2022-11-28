from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@given('launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(20)


@when('open make_my_trip page')
def step_impl(context):
    context.driver.get(r'https://www.makemytrip.com/')
    context.driver.maximize_window()
    time.sleep(2)


@then(u'click bus module')
def step_impl(context):
    context.driver.find_element_by_xpath('//a[@href="https://www.makemytrip.com/bus-tickets/"]').click()


@then('enter the arrival places "Pune"')
def step_impl(context):
    context.driver.find_element_by_xpath('//label[@for="fromCity"]').click()
    context.driver.find_element_by_xpath('//input[@placeholder="From"]').send_keys("Pun")
    context.driver.find_element_by_xpath('//span[text()="Pune, Maharashtra"]').click()


@then('enter the destination places "banglo"')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@placeholder="To"]').send_keys("bengaluru")
    context.driver.find_element_by_xpath('//span[text()="Bangalore (Bengaluru), Karnataka"]').click()


@then(u'enter the date')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//div[@class="bussw_inputBox dayPickerRailWrap dates inactiveWidget  activeWidget"]').click()
    all_dates = context.driver.find_elements_by_xpath('//div[@class="DayPicker-Week"]//div[@class="DayPicker-Day"]')
    for date in all_dates:
        if date.get_attribute('aria-label') == "Wed Nov 30 2022":
            date.click()
            break


@then('click on serach')
def step_impl(context):
    context.driver.find_element_by_id('search_button').click()

@then(u'dismiss')
def step_impl(context):
    context.driver.find_element_by_xpath('//img[@class="primoCloseIcon"]').click()


@then(u'click on select seat button')
def step_impl(context):
    context.driver.find_element_by_xpath('//a[@data-test-id="select-seats"]').click()


@then(u'select the seat')
def step_impl(context):
    upper_seats = context.driver.find_elements_by_xpath(
        '//div[@class="bus-card"]//div[@data-testid="seat_horizontal_sleeper_available"]//img[@class="seat-icon"]')
    for seat in upper_seats:
        if seat.get_attribute('class') == "seat-icon":
            seat.click()
            break


@then(u'click on book seat button')
def step_impl(context):
    context.driver.find_element_by_xpath('//div[@class="cta-book-seats font16 capText makeFlex hrtlCenter vrtlCenter active"]').click()

@then(u'travel details')
def step_impl(context):
    context.driver.find_element_by_id("fname").send_keys('Mridusmita')
    context.driver.find_element_by_id('age').send_keys(22)
    gender = context.driver.find_element_by_xpath('//span[@class="font14 defaultGreyText truncate"]')
    action_obj = ActionChains(context.driver)
    action_obj.move_to_element(gender).perform()
    time.sleep(5)
    context.driver.find_element_by_xpath('(//li[@class=" removeOutline"])[1]').click()


@then(u'contact details')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@type="email"]').send_keys('mk4995861@gmail.com')
    context.driver.find_element_by_id('mobileNumber').send_keys(7218324083)
    context.driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')


@then(u'select options')
def step_impl(context):
    context.driver.find_element_by_xpath('//div[@class="makeFlex column travelInsuranceMsg font14 latoRegular"]//div[2]//span[1]').click()


@then(u'proceed to payment')
def step_impl(context):
    context.driver.find_element_by_xpath('//a[@class="paymentBtn whiteText latoBold font16 capText"]').click()
    time.sleep(20)
    context.driver.close()

