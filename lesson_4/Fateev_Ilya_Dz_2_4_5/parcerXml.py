from lxml import etree
from requests import get


def xmlParce(code: str):
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.content

    root = etree.fromstring(content)
    valCurr = {}
    currencies = []

    for val in root.getchildren():
        for elem in val.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            # print(elem.tag + " => " + text)
            valCurr[elem.tag] = text

        if val.tag == "Valute":
            currencies.append(valCurr)
            valCurr = {}

    for i in currencies:
        if(i.get('CharCode')==code.upper()):
            return (i.get('Value'))
