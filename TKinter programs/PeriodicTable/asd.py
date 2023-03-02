from selenium import webdriver
import time

# Replace with the path to your chromedriver executable
driver = webdriver.Chrome('chromedriver.exe')

# Replace with your message and the phone numbers of your recipients
message = 'Hello'
recipients = ['8149295021', '7798195165']

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code and for the page to load
input('Press Enter after scanning QR code and loading page')

# Loop through the recipients and send the message
for recipient in recipients:
    # Construct the URL for the recipient's chat
    url = f'https://web.whatsapp.com/send?phone={recipient}&text={message}'
    driver.get(url)

    # Wait for the chat window to load
    time.sleep(5)

    # Find and click the send button
    send_button = driver.find_element_by_xpath('//span[@data-testid="send"]')
    send_button.click()

# Close the browser
driver.quit()
