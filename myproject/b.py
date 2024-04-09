# import requests

# url = "http://api.tmapi.top/price_comparison/v2/historical_price/cn"

# querystring = {"apiToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VybmFtZSI6InRob25nIiwiQ29taWQiOm51bGwsIlJvbGVpZCI6bnVsbCwiaXNzIjoidG1hcGkiLCJzdWIiOiJ0aG9uZyIsImF1ZCI6WyIiXSwiaWF0IjoxNzEyNDIzOTU4fQ.JjI7zpqqkozi-fbi2NwIedfG9jFkPMmJcuX_Y2w8TvI","item_id":"","plat":"taobao","period":"360"}

# response = requests.get(url, params=querystring)

# print(response.json())  

############################################
import requests

url = "http://api.tmapi.top/shopee/search/items/v2"

querystring = {"apiToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VybmFtZSI6InRob25nYWEiLCJDb21pZCI6bnVsbCwiUm9sZWlkIjpudWxsLCJpc3MiOiJ0bWFwaSIsInN1YiI6InRob25nYWEiLCJhdWQiOlsiIl0sImlhdCI6MTcxMjQyNTY2M30.0OuTJP8no0aDGYulhxJxMDTDTRoB29UT4ECdotRcMyk","site":"my","keyword":"Baseus Metal Gleam","by":"relevancy","order":"desc","page":1,"pageSize":20}

response = requests.get(url, params=querystring)

print(response.json())

