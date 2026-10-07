import llm
import json
def analyze_report(source_text,company, report_year):
    prompt=f"""请分析以下上市公司年报中的业务介绍，并严格按照指定 JSON 格式返回。
    【要求】1.business：概括公司主要业务，35字内
    2.revenue_drivers：列出主要收入来源/收入驱动因素，每条35字内
    3.competitive_advantages：列出竞争优势，每条35字内
    4.risks：列出文本中明确提到的风险，每条35字内
    5.management_outlook：提取管理层对未来发展的判断，每条35字内
    6.第一个字符必须是'{',最后一个字符必须是'}'，不要任何解释文字，不要用markdown代码块包裹
    7.只能根据提供的文本回答。文本中没有明确提到的信息不要自行编造。
    【字段】{{ "business": "...","revenue_drivers": [],"competitive_advantages": [],"risks": [],"management_outlook": [] }}
    【年报】{source_text}"""
    text=llm.call_llm(prompt)
    try:
        result=json.loads(text)
    except json.JSONDecodeError:
        raise ValueError("模型返回的不是合法JSON")
    revenue_drivers=json.dumps(result["revenue_drivers"],ensure_ascii=False)
    competitive_advantages=json.dumps(result["competitive_advantages"],ensure_ascii=False)
    risks=json.dumps(result["risks"],ensure_ascii=False)
    management_outlook=json.dumps(result["management_outlook"],ensure_ascii=False)
    report_data = (company, report_year,source_text,result["business"],revenue_drivers,competitive_advantages,risks,management_outlook)
    return report_data