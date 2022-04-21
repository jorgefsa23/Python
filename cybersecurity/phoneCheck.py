import phonenumbers

from phonenumbers import geocoder

from phonenumbers import timezone


#phone = "+5571992328105" 
phone = input("Input phone number [Format:+55110000000]:")

phone_numbers = phonenumbers.parse(phone) # Parsing String to Phone number

# Getting region information (geocoder)
region = geocoder.description_for_number(phone_numbers, 'pt')
print("Region:", region)

# to get timezone of the phone number
timeZone = timezone.time_zones_for_number(phone_numbers)
print("Time zone:", timeZone)

# Validating a phone number
valid = phonenumbers.is_valid_number(phone_numbers)
print("This is a valid number:", valid)