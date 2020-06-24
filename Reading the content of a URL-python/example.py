
#!/usr/bin/env python3
import requests 
from requests.exceptions import HTTPError
print('The version of requests is: ' + requests.__version__)

 
#print(response)
#<Response [22]> means that our requests was successful!, however 404 NOT FOUND 
#print(response.status_code) the output is: 200 ! this is GOOD

link = input('pleas input the link: ')

#response has some formation known as 'payload'
response = requests.get(link)

if response: # it evalute to True if the status code was between 200 and 400
    print('Success!')
    while True :
        ask = input(str('Do you want to get the HTML text of the page: '))
        if ask.lower()=='yes':
            print(response.text)
            break 
        elif ask.lower()=='no':
            print('Merci beaucoup!')
            break
        else:
            print('Error INPUT! answer again:  ')
        ask = input('Do you want to get the HTML text of the page: ')


else:
    print('An error has occured.!')






























