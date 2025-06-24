from airflow.www.utils import priority
from notion_client import Client
from pprint import pprint
NOTION_TOKEN = "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"  # Your integration token
DATABASE_ID = "21c8301d-27fc-805a-836b-dacdac678258"  # Tasks Tracker DB ID

notion = Client(auth=NOTION_TOKEN)

tasks = [
    "Define project goals and scope",
    "Create a Notion page to document tech stack and data sources",
    "Set up PostgreSQL database with PostGIS extension locally",
    "Identify public data sources (e.g. skiresort.info, Wikipedia, OSM)",
    "Write Python script to scrape or retrieve resort data (top 50 for start)",
    "Normalize data fields (elevation, vertical drop, skiable area, etc.)",
    "Save raw data as CSV for versioning",
    "Design and create PostgreSQL schema for ski_mountains",
    "Add spatial support using GEOGRAPHY(Point, 4326)",
    "Import cleaned CSV into PostgreSQL",
    "Test spatial queries with PostGIS (ST_Distance, ST_Within)",
    "Install and configure Apache Superset",
    "Connect Superset to PostgreSQL DB",
    "Build deck.gl map view of resorts by elevation",
    "Create bar chart: top countries by number of resorts",
    "Create scatter plot: vertical drop vs. skiable area",
    "Add clustering of resorts (beginner vs. expert)",
    "Integrate weather/snow data (OpenSnow or similar)",
    "Add user rating & popularity fields",
    "Deploy dashboards online"
]

for task in tasks:
    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Task name": {
                "title": [
                    {
                        "text": {
                            "content": task
                        }
                    }
                ]
            },
            "Status": {
                "status": {
                    "name": "Not started"
                }
            },
            "Priority": {
                "select": {
                    "name": "Medium"
                }
            },
            "Assignee": {
                "people": [
                    {
                        "object": "user",
                        "id": "127db580-fda9-4014-8b4f-0f847a991ed0"
                    }
                ]
            },
            "Description": {
                "rich_text": [
                    {
                        "text": {
                            "content": f"This task is part of the Chairlift Charmer ski data project: {task}"
                        }
                    }
                ]
            }
        }
    )