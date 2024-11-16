import pywhatkit

# Inputs for the user
phone_no = input("Enter phone number with country code (e.g., +1234567890): ")
message = input("Enter the message: ")
time_hour = int(input("Enter the hour (24-hour format): "))
time_minute = int(input("Enter the minute: "))

# Sending the WhatsApp message
try:
    print(f"Sending message to {phone_no} at {time_hour}:{time_minute}...")
    pywhatkit.sendwhatmsg(phone_no, message, time_hour, time_minute)
    print("Message sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
