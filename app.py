import time
from get_trending_results import send_trending_keywords
from results_from_db import return_matched_keywords



while True:
 trending_keywords = send_trending_keywords()
 print(trending_keywords)
 
 return_matched_keywords(trending_keywords)
 time.sleep(3600)