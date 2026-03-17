# trending-riddle-video-automation



##  Project Description

As a YouTuber, timing plays a major role in getting views, likes, and subscribers. Posting content when a topic is trending can make a huge difference. But in reality, it’s not always possible to monitor trends continuously. Because of this, we often miss the right moment to create content.

To solve this problem, I built this automation project. The main idea is to track trending keywords related to my niche and act on them immediately without manual effort. This helps me make sure I don’t miss trending opportunities.

---

##  Project Workflow

1. The project runs in an infinite loop and fetches trending keywords every hour using SerpApi (Google Trends - YouTube).

2. The fetched keywords are compared with my predefined keywords stored in a MySQL database using an `IN` operator.

3. If a match is found, the system takes the corresponding riddle and generates a video using MoviePy.

---
