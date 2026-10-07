import sqlite3
from config import DB_PATH
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_table():
    conn=get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS annual_report_analysis(
    id INTEGER PRIMARY KEY ,
    company TEXT,
    report_year INTEGER,
    source_text TEXT,
    business TEXT,
    revenue_drivers TEXT,
    competitive_advantages TEXT,
    risks TEXT,
    management_outlook TEXT,
    UNIQUE(company, report_year))''')
    conn.commit()
    conn.close()

def insert_analysis(report_data):
    conn=get_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT OR IGNORE INTO annual_report_analysis 
                   (company,report_year,source_text,business,revenue_drivers,
                   competitive_advantages,risks,management_outlook) 
                   VALUES (?,?,?,?,?,?,?,?)''',report_data)
    conn.commit()
    conn.close()

def query_info():
    conn=get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM annual_report_analysis')
    rows = cursor.fetchall()
    conn.close()
    return rows 