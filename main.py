import json
import database
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
    rows=database.query_info()
    print_result(rows)

if __name__ == "__main__":
    main()

