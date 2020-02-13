import requests
import re
import os

url="https://tools.ietf.org/html/rfc"
os.remove("rfc_list.csv")
f = open("rfc_list_v_1_0.csv", "a")

for i in range(1,8694):
    url_new = url+str(i)
    PARAMS = {}
    response = requests.get(url = url_new, params = PARAMS)
    result_title = re.findall('DC.Title\" content=\"(.+?)\"', str(response.content))
    if result_title:
        final_string = "RFC"+str(i)+", "+result_title[0]+", "+url_new+"\n"
        print(final_string)
        f.write(final_string)
    else:
        final_string = "RFC" + str(i) + ", " + "NO TITLE" + ", " + url_new+"\n"
        print(final_string)
        f.write(final_string)
f.close()


