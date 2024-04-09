# import requests
import requests

url = "https://shopee-e-commerce-data.p.rapidapi.com/shopee/search/items/v2"

querystring = {"site":"vn","keyword":"quanao","by":"relevancy","page":"1","pageSize":"30"}

headers = {
	"X-RapidAPI-Key": "905a446b21mshe93a712a3d8b4d8p114394jsnc332ec2c883f",
	"X-RapidAPI-Host": "shopee-e-commerce-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

# import requests

# url = "https://lazada-api.p.rapidapi.com/lazada/search/items"

# querystring = {"keywords":"quao ao","site":"vn","page":"1"}

# headers = {
# 	"X-RapidAPI-Key": "bfb8688e81msh06d08c21ef6c99bp1903ccjsn0847540c0f1f",
# 	"X-RapidAPI-Host": "lazada-api.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

# import requests

# url = "https://get-tiki-sale.p.rapidapi.com/tiki-api/tivi"

# headers = {
# 	"X-RapidAPI-Key": "bfb8688e81msh06d08c21ef6c99bp1903ccjsn0847540c0f1f",
# 	"X-RapidAPI-Host": "get-tiki-sale.p.rapidapi.com"
# }

# try:
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()  # Kiểm tra nếu có lỗi khi gửi yêu cầu
#     print(response.json())  # In ra nội dung JSON nếu không có lỗi
# except requests.exceptions.HTTPError as err:
#     print(f"HTTP error occurred: {err}")
# except requests.exceptions.RequestException as err:
#     print(f"An error occurred: {err}")
