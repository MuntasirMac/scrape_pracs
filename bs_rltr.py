from bs4 import BeautifulSoup
import requests
import json

def scrape_agents_by_zip(zip_code):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }

    base_url = f'https://www.realtor.com/realestateagents/{zip_code}'
    page_number = 1
    all_agents_data = []

    while True:
        url = f"{base_url}/pg-{page_number}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to retrieve page {page_number}: {response.status_code}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        d = soup.find('script', {'type': 'application/json'})

        if d is None:
            print(f"No json data found on page {page_number}. Ending pagination.")

        json_data = json.loads(d.string)
        agents = json_data['props']['pageProps']['pageData']['agents']
        if not agents:
            print(f"No agents found on page {page_number}. Ending pagination.")
            break
        all_agents_data.extend(agents)
        page_number += 1
        # print(agents[0])
    output_file = f"{zip_code}_real_estate_agent.json"

    with open(output_file, 'w') as json_file:
        json.dump(all_agents_data, json_file, indent=4)

    print(f"All agents data successfully saved to '{output_file}.")

        # print(json_data.keys())


scrape_agents_by_zip(43222)