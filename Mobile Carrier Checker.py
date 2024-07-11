import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import random

while True:

 with open('NumberList.txt','r', encoding='utf-8') as F:
    Lines = F.readlines()
    number = random.choice(Lines)

 phone_number = phonenumbers.parse(number)
 country_code = phone_number.country_code
 national_number = phone_number.national_number
 print("Country Code:", country_code)
 print("National Number:", national_number)

 time_zone = timezone.time_zones_for_number(phone_number)
 print("Timezone:", time_zone)

 location = geocoder.description_for_number(phone_number, "en")
 print("Location:", location)

 service_provider = carrier.name_for_number(phone_number, "en")
 print("Service Provider:", service_provider)

# Save the results to a text file without deleting the old results
 with open("phone_number_info.txt", "a", encoding='utf-8') as f:
    f.write("Phone Number: " + number)
    f.write("Country Code: " + str(country_code))
    f.write("\nNational Number: " + str(national_number))
    f.write("\nTimezone: " + str(time_zone))
    f.write("\nLocation: " + location)
    f.write("\nService Provider: " + service_provider)
    f.write("\n\n")