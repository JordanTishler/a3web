import requests

website_url = "http://www.generaleducation.ca/conspiracy/q/"
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Define the character set to use for brute-forcing
code_length = 32  # Define the length of the code to break

def brute_force_website():
    generate_inputs("")

def generate_inputs(prefix):
    if len(prefix) == code_length:
        code = prefix
        url = website_url + code + ".htm"
        response = requests.get(url)
        if response.status_code == 503:
            print("Incorrect code: " + code)
        else:
            print("Match found! Code: " + code)
            # You can further process the successful response here if needed
            # For example, extract information from the webpage
            return True  # Match found, stop execution
    else:
        for char in charset:
            if generate_inputs(prefix + char):
                return True  # Match found, stop execution

brute_force_website()
