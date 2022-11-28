import datetime

import pytest

from POM.Buses import Bus_module
from Data.reading_objects import ReadExel
from Library.config import Config

class Test_Buses:
    read_xl = ReadExel()
    details = read_xl.read_test_data(Config.read_test_data)
    @pytest.mark.parametrize('from_,to_,name_,age_,email_,mobile_number',details)
    def test_buses(self,from_,to_,name_,age_,email_,mobile_number,_driver):
        try:
            bus = Bus_module(_driver)
            bus.bus_click()
            bus.departure_place(from_)
            bus.arrival_place(to_)
            bus.primo_pop_up()
            bus.quick_filters()
            bus.select_seats_details()
            bus.enter_name(name_)
            bus.enter_age(age_)
            bus.gender()
            bus.enter_email_id(email_)
            bus.enter_contact_no(mobile_number)
            bus.secure_trip()
            bus.proceed_to_payment()
        except TypeError :
            print('Enter valid phone no.')



