import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse

def duckduckgo_search(query, num_results):
    url = f"https://duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    except requests.RequestException as e:
        print(f"Error fetching search results: {e}")
        return None

def extract_links(soup):
    links = []
    for item in soup.find_all('a', class_='result__a'):
        link = item['href']
        links.append(link)
    return links

def main():
    query = "website clothes "
    num_results = 50  # DuckDuckGo shows 30 results by default
    soup = duckduckgo_search(query, num_results)
    if soup:
        links = extract_links(soup)
        df = pd.DataFrame(links, columns=["Website"])
        df.to_csv("design_deco_mode_sites_occitanie.csv", index=False)
        print(f"Found {len(links)} sites")
    else:
        print("Failed to fetch search results.")

if __name__ == "__main__":
    main()
