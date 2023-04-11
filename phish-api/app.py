import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from urllib.parse import urlparse,urlencode
import ipaddress
import re
from bs4 import BeautifulSoup
import urllib
import urllib.request
from datetime import datetime
import requests
import numpy as np
import whois
import tldextract
import string
import datetime
from dateutil.relativedelta import relativedelta
from csv import reader
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = pickle.load(open('SVM_Model.pkl', 'rb'))

# 2.Checks for IP address in URL (Have_IP)
def havingIP(url):
  index = url.find("://")
  split_url = url[index+3:]
  index = split_url.find("/")
  split_url = split_url[:index]
  split_url = split_url.replace(".", "")
  counter_hex = 0
  for i in split_url:
    if i in string.hexdigits:
      counter_hex +=1
  total_len = len(split_url)
  having_IP_Address = 0
  if counter_hex >= total_len:
    having_IP_Address = 1
  return having_IP_Address

# 3.Checks the presence of @ in URL (Have_At)
sc=['@','~','`','!', '$','%','&']
def haveAtSign(url):
  flag=0
  for i in range(len(sc)):
    if sc[i] in url:
      at = 1
      flag=1
      break
  if flag==0:
    at = 0
  return at

# 4.Finding the length of URL and categorizing (URL_Length)
def getLength(url):
  if len(url) < 54:
    length = 0
  else:
    length = 1
  return length

# 5.Gives number of '/' in URL (URL_Depth)
def getDepth(url):
  s = urlparse(url).path.split('/')
  depth = 0
  for j in range(len(s)):
    if len(s[j]) != 0:
      depth = depth+1
  return depth

# 6.Checking for redirection '//' in the url (Redirection)
def redirection(url):
  pos = url.rfind('//')
  if pos > 6:
    if pos > 7:
      return 1
    else:
      return 0
  else:
    return 0

# 7.Existence of “HTTPS” Token in the Domain Part of the URL (https_Domain)
def httpDomain(url):
  domain = urlparse(url).netloc
  if 'https' in domain:
    return 1
  else:
    return 0

#listing shortening services
shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"

# 8. Checking for Shortening Services in URL (Tiny_URL)
def tinyURL(url):
    match=re.search(shortening_services,url)
    if match:
        return 1
    else:
        return 0

# 9.Checking for Prefix or Suffix Separated by (-) in the Domain (Prefix/Suffix)
def prefixSuffix(url):
    if '-' in urlparse(url).netloc:
        return 1            # phishing
    else:
        return 0            # legitimate



# 11.DNS Record availability (DNS_Record)
# obtained in the featureExtraction function itself

# 12.Web traffic (Web_Traffic)
def web_traffic(url):
    try:
      extract_res = tldextract.extract(url)
      url_ref = extract_res.domain + "." + extract_res.suffix
      html_content = requests.get("https://www.alexa.com/siteinfo/" + url_ref).text
      soup = BeautifulSoup(html_content, "lxml")
      value = str(soup.find('div', {'class': "rankmini-rank"}))[42:].split("\n")[0].replace(",", "")
      if not value.isdigit():
        return 1
      value = int(value)
      if value < 100000:
        return 0
      else:
        return 1
    except:
        return 1

# 13.Survival time of domain: The difference between termination time and creation time (Domain_Age)
def domainAge(url):
  extract_res = tldextract.extract(url)
  url_ref = extract_res.domain + "." + extract_res.suffix
  try:
    whois_res = whois.whois(url)
    if datetime.datetime.now() > whois_res["creation_date"][0] + relativedelta(months=+6):
      return 0
    else:
      return 1
  except:
    return 1

# 14.End time of domain: The difference between termination time and current time (Domain_End)
def domainEnd(domain_name):
  expiration_date = domain_name.expiration_date
  if isinstance(expiration_date,str):
      try:
        expiration_date = datetime.strptime(expiration_date,"%Y-%m-%d")
      except:
        end=1
  if (expiration_date is None):
      end=1
  elif (type(expiration_date) is list):
      today = datetime.datetime.now()
      domainDate = abs((expiration_date[0] - today).days)
      if ((domainDate/30) < 6):
        end = 1
      else:
        end=0
  else:
      today = datetime.datetime.now()
      domainDate = abs((expiration_date - today).days)
      if ((domainDate/30) < 6):
        end = 1
      else:
        end=0
  return end

# 15. IFrame Redirection (iFrame)
def iframe(response):
  if response == "":
      return 1
  else:
      if re.findall(r"[<iframe>|<frameBorder>]", response.text):
          return 0
      else:
          return 1

# 16.Checks the effect of mouse over on status bar (Mouse_Over)
def mouseOver(response):
  if response == "" :
    return 1
  else:
    if re.findall("<script>.+onmouseover.+</script>", response.text):
      return 1
    else:
      return 0

# 18.Checks the number of forwardings (Web_Forwards)
def forwarding(response):
  if response == "":
    return 1
  else:
    if len(response.history) <= 2:
      return 0
    else:
      return 1

#16. Extra feature checks url exists in popular websites data
def checkCSV(url):
  flag=0
  try:
    checkURL=urlparse(url).netloc
  except:
    return 1
  with open('Web_Scrapped_websites.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if row[0]==checkURL:
            flag=0
            break
        else:
            flag=1
  if flag==0:
      return 0
  else:
      return 1

def featureExtraction(url):

  features = []
  #Address bar based features (10)
  #features.append(getDomain(url))
  features.append(havingIP(url))
  features.append(haveAtSign(url))
  features.append(getLength(url))
  features.append(getDepth(url))
  features.append(redirection(url))
  features.append(httpDomain(url))
  features.append(tinyURL(url))
  features.append(prefixSuffix(url))

  #Domain based features (4)
  dns = 0
  try:
    domain_name = whois.whois(urlparse(url).netloc)
  except:
    dns = 1

  features.append(dns)
  features.append(web_traffic(url))
  features.append(1 if dns == 1 else domainAge(url))
  features.append(1 if dns == 1 else domainEnd(domain_name))

  # HTML & Javascript based features
  try:
    response = requests.get(url)
  except:
    response = ""

  features.append(iframe(response))
  features.append(mouseOver(response))
  features.append(forwarding(response))

  return features

@app.route('/',methods=["GET","POST"])
def home():
    return "Hello World"

@app.route('/post',methods=['POST'])
def predict():
  url=request.form['URL']
  dataPhish=0
  if checkCSV(url)==0:
    dataPhish=0
  else:
    dataPhish=1
  if dataPhish==0:
    return "0"
  else:
    features=featureExtraction(url)
  if features.count(0)==15 or features.count(0)==14:
    prediction=0
  else:
    prediction = model.predict([features])
  if prediction==1 and dataPhish==1:
    return "-1"
  else:
    return "1"
if __name__ == "__main__":
    app.run(debug=True)
