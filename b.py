import requests 
import re
import json
import time
import xlwt

#
#
#���ñ��
#����Ҫ�����Ǹ�ɶ��
#������4�д���Ϳ��������д������
#
style=xlwt.XFStyle()
font=xlwt.Font()
font.name='SimSun'
style.font=font

#����һ�����
w=xlwt.Workbook(encoding='utf-8')
#��Ӹ�sheet
ws=w.add_sheet('sheet 1',cell_overwrite_ok=True)
#��ǰд���񵽵� row��
row=1
#
#д����ͷ
#
ws.write(0,0,'content')
ws.write(0,1,'userClientShow')
ws.write(0,2,'creationTime')
ws.write(0,3,'userLevelName')
ws.write(0,4,'productColor')
ws.write(0,5,'userLevelId')
ws.write(0,6,'score')
ws.write(0,7,'referenceName')
ws.write(0,8,'referenceTime')
ws.write(0,9,'isMobile')
ws.write(0,10,'nickname')

#
#����һ��json����
#������д�����
#һ��һҳ����
#
def write_json_to_xls(dat):
    global row
    for comment in dat['comments']:
        ws.write(row,0,comment['content'])
        ws.write(row,1,comment['userClientShow'])
        ws.write(row,2,comment['creationTime'])
        ws.write(row,3,comment['userLevelName'])
        ws.write(row,4,comment['productColor'])
        ws.write(row,5,comment['userLevelId'])
        ws.write(row,6,comment['score'])
        ws.write(row,7,comment['referenceName'])
        ws.write(row,8,comment['referenceTime'])
        ws.write(row,9,comment['isMobile'])
        ws.write(row,10,comment['nickname'])
        row+=1

#
#
# ѭ����ȡ����
#
#
for i in range(1,10+1):
    url='https://club.jd.com/comment/productPageComments.action?productId=1475512465&score=0&sortType=5&page=%d&pageSize=100&isShadowSku=0&fold=' % i
    try:
        json_req = requests.get(url)
        dat = json_req.json()
        write_json_to_xls(dat)
        print(u'д��һҳ����')
    except Exception as e:
       print(u'��ȡ����ʧ������',e)
    time.sleep(0.5)


#�����ݴ�����
w.save('result.xls')