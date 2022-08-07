import pywhatkit

phone_number = input('Enter phone number: ')
# pywhatkit.sendwhatmsg(phone_number, 'Hi, How are you?', 13, 37)

pywhatkit.sendwhatmsg(phone_number, 'Hi, How are you', 13, 45, wait_time=15, tab_close=True, close_time=10)
print("Message Sent!")  # Prints success message in console

# Send message to a group
group_id = input("Enter group id: ")

pywhatkit.sendwhatmsg_to_group(group_id, "Test Group", 13, 55)
