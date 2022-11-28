# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from  selenium.webdriver.support.select import Select
from  Library.config import Config
from selenium.webdriver.common.action_chains import ActionChains
import time
from Data.reading_objects import ReadExel
read_xl = ReadExel()
bus_object = read_xl.read_locators(Config.read_locators)
print(bus_object)


# path = r"C:\Users\HP\Desktop\driver_\chromedriver.exe"
# driver = webdriver.Chrome(path)


# driver.get(r'https://www.makemytrip.com/')
# driver.maximize_window()
# driver.implicitly_wait(60)
class Bus_module:
    def __init__(self, driver):
        self.driver = driver

    def bus_click(self):
        #Buses
        self.driver.find_element(*bus_object['bus_click']).click()
        time.sleep(1)

        #From
    def departure_place(self,from_):
        self.driver.find_element(*bus_object['from_click']).click()
        time.sleep(1)
        self.driver.find_element(*bus_object['from_input']).send_keys(from_)
        time.sleep(1)
        self.driver.find_element(*bus_object['from_select']).click()
        time.sleep(1)

        #To
    def arrival_place(self,to_):
        self.driver.find_element(*bus_object['to_input']).send_keys(to_)
        time.sleep(1)
        self.driver.find_element(*bus_object['to_click']).click()
        time.sleep(1)

        #Date
        self.driver.find_element(*bus_object['date_click']).click()
        time.sleep(2)
        all_dates = self.driver.find_elements(*bus_object['date_select'])
        for date in all_dates:
            if date.get_attribute('aria-label') == "Wed Dec 14 2022":
                date.click()
                time.sleep(2)
                break

        #Search
        self.driver.find_element(*bus_object['search_click']).click()
        time.sleep(1)

# class Seat_Selection:
#     def __init__(self, driver):
#         self.driver = driver

    def primo_pop_up(self):
        self.driver.find_element(*bus_object['prime_pop_up_click']).click()
        time.sleep(1)

    def quick_filters(self):
        self.driver.find_element(*bus_object['sleeper']).click()
        time.sleep(2)

    def select_seats_details(self):
        self.driver.find_element(*bus_object['seat_drop_down']).click()
        time.sleep(1)

        # Seat icon
        seats = self.driver.find_elements(*bus_object['seat_icon'])
        for seat in seats :
            if seat.get_attribute('class') == "seat-icon" :
                seat.click()
                time.sleep(2)
                break

        # Book_seat_button
        self.driver.find_element(*bus_object['book_seat_button']).click()
        time.sleep(2)

    def enter_name(self,name_):
        self.driver.find_element(*bus_object['name']).send_keys(name_)
        time.sleep(2)

    def enter_age(self,age_):
        self.driver.find_element(*bus_object['age']).send_keys(age_)
        time.sleep(2)

    def gender(self):
        gender = self.driver.find_element(*bus_object['gender_drop_down'])
        time.sleep(2)
        action_obj = ActionChains(self.driver)
        time.sleep(2)
        action_obj.move_to_element(gender).perform()
        time.sleep(2)
        self.driver.find_element(*bus_object['gender_click']).click()
        time.sleep(2)

    def enter_email_id(self,email_):
        # Enter_Contact_details
        self.driver.find_element(*bus_object['email_id']).send_keys(email_)
        time.sleep(2)

    def enter_contact_no(self, mobile_number):
        self.driver.find_element(*bus_object['mobile_no']).send_keys(mobile_number)
        time.sleep(2)
        # action_obj.send_keys(Keys.PAGE_DOWN).perform()
        self.driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
        time.sleep(2)

    def secure_trip(self):
        # Secure trip
        self.driver.find_element(*bus_object['secure_trip_click']).click()

    def proceed_to_payment(self):
        # Proceed to payment
        self.driver.find_element(*bus_object['proceed_payment']).click()




# bus =Bus_module(driver)
# bus.bus_click()
# bus.departure_place()
# bus.arrival_place()
# bus.primo_pop_up()
# bus.quick_filters()
# bus.select_seats_details()
# bus.enter_name()
# bus.enter_age()
# bus.gender()
# bus.enter_email_id()
# bus.enter_contact_no()
# bus.secure_trip()
# bus.proceed_to_payment()



