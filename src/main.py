from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_blog_for_keywords(url, keywords):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Check if we got a successful response
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []  # Return an empty list on error

    soup = BeautifulSoup(response.content, 'lxml')
    post_elements = soup.find_all('div.', class)
    
    matching_posts = []
    for post in post_elements:
        title = post.h5.text
        link = post['href']
        text = post.a.text.split()
        if any(keyword.lower() in title.lower() for keyword in keywords):
            matching_posts.append({'title': title, 'link': link, 'source': url})
    return matching_posts.text

if __name__ == '__main__':
    urls = [
        'https://www.healthline.com/health/healthy-sex/sexual-fantasies',
        'https://www.cosmopolitan.com/sex-love/advice/g3025/sexual-fantasies/',
        'https://www.womenshealthmag.com/sex-and-love/a29501609/common-sexual-fantasies/',
        'https://www.glamour.com/story/6-totally-normal-sex-fantasies',
        'https://www.menshealth.com/sex-women/a42574531/sexual-fantasies/',
        'https://www.oprahdaily.com/life/relationships-love/a28697121/sexual-fantasies/',
        'https://www.everydayhealth.com/mens-health-pictures/top-sexual-fantasies-for-men.aspx',
        'https://www.prevention.com/sex/a44640327/sexual-fantasies/',
        'https://www.menshealth.com/sex-women/a34963759/sex-bucket-list/',
        'https://fantasyapp.com/en/blog/list-kinks-explore-sexual-fantasies/',
        'https://www.glamour.com/story/a-to-z-kinks-and-fetishes',
        'https://www.cosmopolitan.com/sex-love/a24481923/kinks-fetish-list/',
        'https://www.womenshealthmag.com/sex-and-love/a18371849/9-sexual-fetishes-youve-never-heard-of-before/',
    ]

    keywords = ['Kink', 'Fantasies', 'sex fantasies', 'sex bucket list', 'spice up', 'romance', 'fetishes', 'kinks', 'fantasy']

    all_results = []

    for url in urls:
        all_results.extend(scrape_blog_for_keywords(url, keywords))

    # Convert the results to a DataFrame and save as Excel
    df = pd.DataFrame(all_results)
    df.to_excel('keyword_matching_blog_posts.xlsx', index=False)

    print("Scraping completed and saved to 'keyword_matching_blog_posts.xlsx'")
