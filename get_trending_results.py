from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

load_dotenv()
serp_api_key = os.getenv("SERP_API_KEY")
 
def send_trending_keywords():

 params = {
  "api_key": serp_api_key,
  "engine": "google_trends",
  "q": "cricket",
  "hl": "en",
  "geo": "IN",
  "cat": "20",
  "gprop": "youtube",
  "date": "now 1-H",
  "data_type": "RELATED_QUERIES"
  }

 search = GoogleSearch(params)
 results = search.get_dict()



 keywords = []

 rising_queries = [query['query'] for query in results['related_queries']['rising']]
 
 for query in rising_queries:
    keywords.append(query)

 top_queries = [query['query'] for query in results['related_queries']['top']]
 
 for query in top_queries:
    keywords.append(query)

 
 print("-----------------------------------------")
 return keywords