import pymongo
import pandas as pd

myclient = pymongo.MongoClient("")

mydb = myclient["ProdRamooz"]
productcol = mydb["products"]
usercol = mydb["users"]
artisancol = mydb["artisan"]

#artisan
artisan_speciality = []
artisan_tags = []
artisan_reference = []
artisan_reference_links = []
artisan_audio = []
artisan_image = []
artisan_video = [] 
modified_by = []
items = []
item_doc = []
item_doc_text = []
profileImg = []
artisan_first_name = []
artisan_last_name = []
artisan_email = []
artisan_city = []
artisan_city1 = []
artisan_city2 = []
artisan_province = []
artisan_province1 = []
artisan_province2 = []
artisan_experience = []
artisan_shop_artisan = []
modified_date = []
created_date = []
created_by = []
artisan_comments = []
artisan_primary_phoneno = []
artisan_secondary_phoneno = []
artisan_other_phoneno = []
artisan_discription = []
artisan_bank_name = []
artisan_bank_branchname = []
artisan_bank_title = []
artisan_IBAN = []
artisan_bank_accountno = []
jazz_easypaisa = []
artisan_jazzcash_easypaisa = []
artisan_cnic = []
artisan_ntn = []
artisan_gender = []
artisan_age = []
artisan_primary_address = []
artisan_secondary_address = []
artisan_other_address = []
famous_land_mark = []
famous_land_mark1 = []
famous_land_mark2 = [] 

#product
profileImg = []
item_tags = []
item_reference_text = []
item_reference_url = []
item_audio = []
item_image = []
item_video = []
item_doc = []
sku = []
item_name = []
item_address_line1 = []
item_landmark1 = []
item_province1 = []
item_district1 = []
item_city1 = []
item_village_tehsil1 = []
item_address_line2 = []
item_landmark2 = []
item_province2 = []
item_district2 = []
item_city2 = []
item_village_tehsil2 = []
item_address_line3 = []
item_landmark3 = []
item_province3 = []
item_district3 = []
item_city3 = []
item_village_tehsil3 = []
item_subcategory = []
item_notes = []
item_product_value = []
item_created_date = []
item_modified_date = []
item_category = []
item_description = []
created_by = []


#user
_id = []
firstname = []
lastname = []
email = []
password = []
createdAt = []
updatedAt = []
__v = []

for z in artisancol.find():
  #print(x['profileImg'])
  artisan_speciality.append(z['artisan_speciality'])
  artisan_tags.append(z['artisan_tags'])
  artisan_reference.append(z['artisan_reference'])
  try:
    artisan_reference_links.append(z['artisan_reference_links'])
  except:
    artisan_reference_links.append("")

  artisan_audio.append(z['artisan_audio'])
  artisan_image.append(z['artisan_image'])
  artisan_video.append(z['artisan_video'])
  modified_by.append(z['modified_by'])
  items.append(z['items'])
  item_doc.append(z['item_doc'])
  item_doc_text.append(z['item_doc_text'])
  profileImg.append(z['profileImg'])
  artisan_first_name.append(z['artisan_first_name'])
  artisan_last_name.append(z['artisan_last_name'])
  artisan_email.append(z['artisan_email'])
  artisan_city.append(z['artisan_city'])
  artisan_city1.append(z['artisan_city1'])
  artisan_city2.append(z['artisan_city2'])
  artisan_province.append(z['artisan_province'])
  artisan_province1.append(z['artisan_province1'])
  artisan_province2.append(z['artisan_province2'])
  artisan_experience.append(z['artisan_experience'])
  artisan_shop_artisan.append(z['artisan_shop_artisan'])
  modified_date.append(z['modified_date'])
  created_date.append(z['created_date'])
  created_by.append(z['created_by'])
  artisan_comments.append(z['artisan_comments'])
  artisan_primary_phoneno.append(z['artisan_primary_phoneno'])
  artisan_secondary_phoneno.append(z['artisan_secondary_phoneno'])
  artisan_other_phoneno.append(z['artisan_other_phoneno'])
  artisan_discription.append(z['artisan_discription'])
  artisan_bank_name.append(z['artisan_bank_name'])
  artisan_bank_branchname.append(z['artisan_bank_branchname'])
  artisan_bank_title.append(z['artisan_bank_title'])
  artisan_IBAN.append(z['artisan_IBAN'])
  artisan_bank_accountno.append(z['artisan_bank_accountno'])
  jazz_easypaisa.append(z['jazz_easypaisa'])
  artisan_jazzcash_easypaisa.append(z['artisan_jazzcash_easypaisa'])
  artisan_cnic.append(z['artisan_cnic'])
  artisan_ntn.append(z['artisan_ntn'])
  artisan_gender.append(z['artisan_gender'])
  artisan_age.append(z['artisan_age'])
  artisan_primary_address.append(z['artisan_primary_address'])
  artisan_secondary_address.append(z['artisan_secondary_address'])
  artisan_other_address.append(z['artisan_other_address'])
  famous_land_mark.append(z['famous_land_mark'])
  famous_land_mark1.append(z['famous_land_mark1'])
  famous_land_mark2.append(z['famous_land_mark2'])
  

for y in usercol.find():
  #print(x['profileImg'])
  _id.append(y['_id'])
  firstname.append(y['firstname'])
  lastname.append(y['lastname'])
  email.append(y['email'])
  password.append(y['password'])
  createdAt.append(y['createdAt'])
  updatedAt.append(y['updatedAt'])
  __v.append(y['__v'])


i = 0


for x in productcol.find():
  #print(x['profileImg'])
  profileImg.append(x['profileImg'])
  item_tags.append(x['item_tags'])
  try:
    item_reference_text.append(x['item_reference_text'])
  except:
     item_reference_text.append("")
  try:
    item_reference_url.append(x['item_reference_url'])
  except:
     item_reference_url.append("")
  item_audio.append(x['item_audio'])
  item_image.append(x['item_image'])
  item_video.append(x['item_video'])
  item_doc.append(x['item_doc'])
  #print(x['item_doc'])
  try:
    sku.append(x['sku'])
  except:
     sku.append("")
 



  item_name.append(x['item_name'])
  try:
    item_address_line1.append(x['item_address_line1'])
  except:
     item_address_line1.append("")
  try:
    item_landmark1.append(x['item_landmark1'])
  except:
     item_landmark1.append("")
  try:
    item_province1.append(x['item_province1'])
  except:
     item_province1.append("")
  try:
    item_district1.append(x['item_district1'])
  except:
    item_district1.append("")
  try:
    item_village_tehsil1.append(x['item_village_tehsil1'])
  except:
    item_village_tehsil1.append("")
  try:
    item_address_line2.append(x['item_address_line2'])
  except:
    item_address_line2.append("")
  try:
    item_landmark2.append(x['item_landmark2'])
  except:
    item_landmark2.append("")
  try:
    item_province2.append(x['item_province2'])
  except:
    item_province2.append("")
  try:
    item_district2.append(x['item_district2'])
  except:
    item_district2.append("")
  try:
    item_city2.append(x['item_city2'])
  except:
    item_city2.append("")
  try:
    item_village_tehsil2.append(x['item_village_tehsil2'])
  except:
    item_village_tehsil2.append("")
  try:
    item_address_line3.append(x['item_address_line3'])
  except:
    item_address_line3.append("")
  try:
    item_landmark3.append(x['item_landmark3'])
  except:
    item_landmark3.append("")
  try:
    item_city3.append(x['item_city3'])
  except:
    item_city3.append("")
  try:
    item_district3.append(x['item_district3'])
  except:
    item_district3.append("")
  try:
    item_village_tehsil3.append(x['item_village_tehsil3'])
  except:
    item_village_tehsil3.append("")


  item_subcategory.append(x['item_subcategory'])
  try:
    item_notes.append(x['item_notes'])
  except:
    item_notes.append("")
  item_product_value.append(x['item_product_value'])
  item_created_date.append(x['item_created_date'])
  item_modified_date.append(x['item_modified_date'])
  item_category.append(x['item_category'])
  item_description.append(x['item_description'])
  created_by.append(x['created_by'])
  i += 1
  #print(x)
print(item_doc)
print(len(item_doc))
#print(i)

artisan = {
'artisan_speciality': artisan_speciality, 'artisan_tags': artisan_tags, 'artisan_reference': artisan_reference, 'artisan_reference_links': artisan_reference_links, 'artisan_audio': artisan_audio, 
'artisan_image': artisan_image, 'artisan_video': artisan_video, 'modified_by': modified_by, 'items': items, 
#'item_doc': item_doc, 
'item_doc_text': item_doc_text,
#'profileImg': profileImg, 
'artisan_first_name': artisan_first_name, 'artisan_last_name': artisan_last_name, 'artisan_email': artisan_email, 'artisan_city': artisan_city, 'artisan_city1': artisan_city1, 'artisan_city2': artisan_city2, 
'artisan_province': artisan_province, 'artisan_province1': artisan_province1, 'artisan_province2': artisan_province2, 'artisan_experience': artisan_experience, 'artisan_shop_artisan': artisan_shop_artisan, 
'modified_date': modified_date, 
'created_date': created_date, 
#'created_by': created_by, 
'artisan_comments': artisan_comments, 
'artisan_primary_phoneno': artisan_primary_phoneno, 
'artisan_secondary_phoneno': artisan_secondary_phoneno, 'artisan_other_phoneno': artisan_other_phoneno, 'artisan_discription': artisan_discription, 'artisan_bank_name': artisan_bank_name, 
'artisan_bank_branchname': artisan_bank_branchname, 'artisan_bank_title': artisan_bank_title, 'artisan_IBAN': artisan_IBAN, 'artisan_bank_accountno': artisan_bank_accountno, 'jazz_easypaisa': jazz_easypaisa,
'artisan_jazzcash_easypaisa': artisan_jazzcash_easypaisa, 'artisan_cnic': artisan_cnic, 'artisan_ntn': artisan_ntn, 'artisan_gender': artisan_gender, 'artisan_age': artisan_age, 
'artisan_primary_address': artisan_primary_address, 'artisan_secondary_address': artisan_secondary_address, 'artisan_other_address': artisan_other_address, 'famous_land_mark': famous_land_mark,
'famous_land_mark1': famous_land_mark1, 'famous_land_mark2':famous_land_mark2               

} 

artisan_df = pd.DataFrame(data=artisan)
print(artisan_df)

artisan_df.to_csv('artisan_prod.csv')

user = {'_id': _id, 'firstname': firstname, 'lastname': lastname, 'email': email, 'password': password, 
'createdAt': createdAt, 'updatedAt': updatedAt, '__v': __v


} 

user_df = pd.DataFrame(data=user)
#print(user_df)

user_df.to_csv('user_prod.csv')






product = {
  #'profileImg': profileImg, 
  'item_tags': item_tags, 
   'item_reference_text': item_reference_text, 
   'item_reference_url': item_reference_url,
   'item_audio': item_audio, 
   'item_image': item_image, 
   'item_video': item_video, 
   #'item_doc': item_doc,
   'sku': sku, 
   'item_name' : item_name, 
   'item_address_line1': item_address_line1, 
   'item_landmark1': item_landmark1,
   'item_province1': item_province1, 
   'item_district1': item_district1,  
   'item_village_tehsil1': item_village_tehsil1, 
   'item_address_line2': item_address_line2, 
   'item_landmark2': item_landmark2, 
   'item_province2': item_province2, 
   'item_district2': item_district2,
   'item_city2': item_city2, 
   'item_village_tehsil2': item_village_tehsil2, 
   'item_address_line3': item_address_line3, 
   'item_landmark3': item_landmark3,
#   'item_province3': item_province3, 
   'item_district3': item_district3, 
   'item_city3': item_city3, 
   'item_village_tehsil3': item_village_tehsil3,
   'item_subcategory': item_subcategory,
   'item_notes': item_notes, 
   'item_product_value': item_product_value, 
#   #'item_created_date': item_created_date,
   'item_modified_date': item_modified_date, 
   'item_category': item_category,
   'item_description': item_description,
# # 'created_by': created_by
  }

product_df = pd.DataFrame(data=product)
print(product_df)
product_df.to_csv('product_prod.csv')
