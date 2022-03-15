from this import d
import requests
import json 
from datetime import date

projects = ["projectnanopass", "worldwidewebbland", "pixels-farm", "metroverse", "kaijumutant", "genesis-creepz", "cyberbrokers", "gnssbymgxs", "raidparty", "official-clementines-nightmare"]
today = date.today()
date = today.strftime("%m/%d/%y")
f = open('nft_stats.txt', 'w+')

f.write("project_name," + "date," + "floor_price," + "\n")
for proj_name in projects:
    url = f"https://api.opensea.io/api/v1/collection/{proj_name}/stats"
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)

    json_data = json.loads(response.text)
    
    f.write(proj_name + "," + date + ",")

    f.write(str(json_data["stats"]["floor_price"]))
    f.write("\n")
        
 