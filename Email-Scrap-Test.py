import re
import urllib.request

url = "https://www.example.com/abot-us"
response = urllib.request.urlopen(url)
html_content = response.read().decode('utf-8')

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html_content)

print(emails)
