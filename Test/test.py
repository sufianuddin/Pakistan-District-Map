import pymongo
import certifi
import pandas as pd
import json

uri = ""
myclient = pymongo.MongoClient(uri, tlsCAFile=certifi.where())

mydb = myclient["ProdRamooz"]

artisancol = mydb["artisan"]

artisans_ls = []

path = "C:/Users/Sufian.Uddin\Desktop/RamoozETL/RamoozData/"

for y in artisancol.find():
    ls = y["items"]
    if not ls:
        try:
            res = json.loads(ls)
        except:
            # print("List is empty")
            data = {"ArtisanID": y["_id"], "ItemID": "N/A"}
            artisans_ls.append(data)
    else:
        res = json.loads(ls[0:1][0])
        # print("List is not empty")
        data = {"ArtisanID": y["_id"], "ItemID": res["_id"]}
        artisans_ls.append(data)

df = pd.DataFrame(artisans_ls)
print(df)
df.to_excel(path + "ArtisanItems.xlsx", sheet_name="ArtisanItems")
