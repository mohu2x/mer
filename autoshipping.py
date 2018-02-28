import requests,json
####################
access_token=''
global_access_token=''
seller_id=''
####################
wait_list=[]
evidence_list=[]
title_list=[]
params={'_access_token':access_token,
        '_global_access_token':global_access_token,
        'seller_id':seller_id,
        'status':'trading',
        'limit':'100'}
headers = {"Content-Type":"application/json","User-Agent": "Mercari_r/4724 (iOS 10.3.1; ja-JP; iPhone9,2)","X-PLATFORM":"ios","X-APP-VERSION": "4724"}

r=requests.get("https://api.mercari.jp/items/get_items", params=params,headers=headers).json()

for i in range(len(r["data"])):
    if r["data"][i]['transaction_evidence']['status']=="wait_shipping":
        

        params={'id':r["data"][i]['id'],'_use_ssl':'1','_app_version':'4826','_platform':'ios','_access_token':access_token}
        item_detail=requests.get("https://api.mercari.jp/items/get", params=params,headers=headers).json()
        wait_list.append(item_detail["data"]['id'])
        evidence_list.append(item_detail["data"]["transaction_evidence"]["id"])
        title_list.append(item_detail["data"]["name"])




print(wait_list)
print(evidence_list)
print(title_list)

#for item_ID,ev_ID,title in zip(wait_list,evidence_list,title_list):
    #if title=="すいむ 様":
    #    params={'item_id':item_ID,
    #    'body':"ご購入ありがとうございます。\nお取り引き完了までよろしくお願いします。",
    #    '_app_version':'4826','_platform':'ios','_access_token':access_token}
    #    r=requests.post("https://api.mercari.jp/transaction_messages/post", params=params,headers=headers).json()
