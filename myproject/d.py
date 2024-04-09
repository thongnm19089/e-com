from apify_client import ApifyClient

# Initialize the ApifyClient with your Apify API token
client = ApifyClient("apify_api_osA6Bts5hCLrPQ2NoAkbGOl5tLfyFe3ZMAD6")

# Prepare the Actor input
run_input = {
    "keyword": "jeans",
    "maxItems": 3,
    "startUrl": [],
    "proxy": { "useApifyProxy": True },
}

# Run the Actor and wait for it to finish
run = client.actor("lukass/shopee-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)