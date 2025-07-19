# Reddit Scraping & Analysis Assessment

This project demonstrates data collection, cleaning, and analysis skills using Reddit as a real-world data source. The assessment consists of three interconnected tasks that progressively build upon each other.

## 📋 Project Overview

### Task A: Reddit API Basics — Data Collection & Storage
**Goal**: Collect Reddit post and comment data using the PRAW library and store it in structured format.

### Task B: Reddit Data Cleaning & Transformation  
**Goal**: Clean and transform the raw Reddit data to prepare it for analysis.

### Task C: Reddit Data Analysis & Visualization
**Goal**: Perform analysis and create visualizations to extract insights from the cleaned data.

## 🚀 Setup Instructions

### Prerequisites
- Python 3.7+
- Reddit API credentials (client_id, client_secret)

### Required Packages
```bash
pip install praw pandas matplotlib seaborn
```

### Reddit API Setup
1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Create a new "script" application
3. Note your `client_id` and `client_secret`
4. Update `config.py` with your credentials

## 📂 File Structure

```
Assessment/
├── main.py                 # Task A: Data collection script
├── Task_2.ipynb           # Task B: Data cleaning notebook
├── Task_3.ipynb           # Task C: Analysis & visualization notebook
├── config.py              # Reddit API credentials
├── posts.csv              # Raw posts data
├── comments.csv           # Raw comments data
├── posts_cleaned.csv      # Cleaned posts data
├── comments_cleaned.csv   # Cleaned comments data
├── reddit_data_cleaned.db # SQLite database with cleaned data
└── README.md              # This file
```

## 🔧 Usage Instructions

### Step 1: Data Collection (Task A)
```bash
python main.py
```
This will:
- Connect to Reddit API using PRAW
- Scrape 50 most recent posts from r/dataisbeautiful
- Collect up to 100 top-level comments per post
- Save data to `posts.csv` and `comments.csv`

### Step 2: Data Cleaning (Task B)
Open and run `Task_2.ipynb` in Jupyter Notebook or VS Code. This will:
- Remove deleted/removed posts and comments
- Convert UTC timestamps to readable dates
- Remove null/empty comment bodies
- Add comment and title length fields
- Export cleaned data to CSV and SQLite formats

### Step 3: Data Analysis (Task C)
Open and run `Task_3.ipynb` to perform:
- Basic analysis (top posts, active users)
- Text analysis (keyword extraction, comment lengths)
- Visualizations (bar charts, line charts)

## 📊 Data Schema

### Posts Table/CSV
| Field | Type | Description |
|-------|------|-------------|
| PostID | String | Unique Reddit post identifier |
| Title | String | Post title |
| Author | String | Username of post author |
| Score | Integer | Post upvotes minus downvotes |
| NumComments | Integer | Total number of comments |
| CreatedUTC | Float | Unix timestamp of post creation |

### Comments Table/CSV
| Field | Type | Description |
|-------|------|-------------|
| CommentID | String | Unique Reddit comment identifier |
| PostID | String | ID of parent post |
| Author | String | Username of comment author |
| Score | Integer | Comment upvotes minus downvotes |
| Body | String | Comment text content |
| CreatedUTC | Float | Unix timestamp of comment creation |

## 🎯 Subreddit Used

**r/dataisbeautiful** - A community focused on data visualization and statistical graphics. This subreddit was chosen because:
- High engagement and quality content
- Diverse range of topics and discussion
- Good mix of posts and comments for analysis
- Relevant to data science and visualization themes

## 📈 Analysis Results

The analysis reveals several interesting insights about r/dataisbeautiful:
- **Engagement Patterns**: Posts with visual content tend to receive higher scores
- **User Activity**: A small number of highly active users contribute significantly to discussions
- **Content Themes**: Common keywords reflect data visualization, statistics, and current events
- **Temporal Patterns**: Post frequency varies by day, showing community activity patterns

## 🛠️ Technical Implementation

### Data Collection Features
- Secure credential management via config file
- Error handling for API rate limits
- Efficient comment extraction with PRAW
- Structured data export to CSV format

### Data Cleaning Features
- Comprehensive filtering of deleted/removed content
- Timestamp conversion with timezone awareness
- Text length calculations for analysis
- Multiple export formats (CSV + SQLite)

### Analysis Features
- Statistical analysis of post and comment metrics
- Natural language processing for keyword extraction
- Interactive visualizations with matplotlib/seaborn
- Comprehensive reporting of findings

## 📝 Notes

- The script respects Reddit's API rate limits
- All personal credentials are stored securely in `config.py`
- Data collection may take several minutes depending on comment volume
- Visualizations are optimized for clarity and insight presentation

## 🔒 Security

- Reddit API credentials are stored in a separate config file
- The config file should not be committed to version control
- All API calls use secure HTTPS connections
- No sensitive user data is stored beyond what's publicly available

---

*This project was completed as part of a data engineering assessment focusing on API usage, data wrangling, and analysis skills.*
