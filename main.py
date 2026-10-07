import json
import database
import analysis
def print_result(rows):
    for row in rows: 
        print("公司：", row[1])
        print("年份：", row[2])
        print("业务：", row[4])
        print("收入驱动因素：")
        for item in json.loads(row[5]):
            print("-", item)
        print("竞争优势：")
        for item in json.loads(row[6]):
            print("-", item)
        print("风险：")
        for item in json.loads(row[7]):
            print("-", item)
        print("管理层展望：")
        for item in json.loads(row[8]):
            print("-", item)

def main():
    company=input("请输入公司名称：")
    report_year=int(input("请输入年报年份："))
    with open("data/example_annual_report.txt", "r", encoding="utf-8") as f:
        source_text = f.read()
    database.create_table()
    report_data=analysis.analyze_report(source_text,company,report_year)
    database.insert_analysis(report_data)
    rows=database.query_info()
    print_result(rows)

if __name__ == "__main__":
    main()

