import sqlite3
import csv
from models import Project

path = "/home/dkapfumvuti/project-tracker/src/instance/projects.db"

def get_data():
    with open('projects.csv') as projects_csv:
        temp = csv.DictReader(projects_csv)
        project_data = []
        for row in temp:
            project_data.append(row)
    projects = []
    for item in project_data:
        projects.append(Project(name=item["name"], client=item["client"], duration=int(item["duration"])))
    
    return projects
            

def populate(host):
    with sqlite3.connect(host) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO project (name, client, duration) VALUES (?, ?, ?)", ('Website Redesign', 'Tech Solutions Inc.', 15),)
        cur.execute("INSERT INTO project (name, client, duration) VALUES (?, ?, ?)", ('Mobile App Development', 'Innovative Apps LLC', 30))
        cur.execute("INSERT INTO project (name, client, duration) VALUES (?, ?, ?)", ('Cloud Migration', 'Cloud Services Co.', 12))
        cur.execute("INSERT INTO project (name, client, duration) VALUES (?, ?, ?)", ('Data Analysis Project', 'Analytics R Us', 30))
        cur.execute("INSERT INTO project (name, client, duration) VALUES (?, ?, ?)", ('E-commerce Platform', 'Online Retailers Ltd.', 96))
    print("DB populated with 5 records")
    
    





