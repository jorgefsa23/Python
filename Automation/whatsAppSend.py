
import pywhatkit 

#Send message to a contact at 15:30hs :
pywhatkit.sendwhatmsg('+1xxxxxxxx', 'Hello!!!', 15, 30) #phone number with country code, message, hour and minutes

#Send message to a contact and close tab after seconds
pywhatkit.sendwhatmsg('+1xxxxxxx', 'Message 2', 15, 30, 15, True, 2) #add: wait_time, tab_close (True) and close_time (seconds)

#Send message to a group:
pywhatkit.sendwhatmsg_to_group('group-id', 'Message 3', 19, 2) #syntax: group id, message, hour and minutes