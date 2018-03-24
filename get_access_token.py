import requests,json
import random,string

login_id=''#メールアドレス
login_pass=''#パスワード

uuid=''.join([random.choice(string.ascii_letters + string.digits) for i in range(32)])
print("uuid="+uuid)

headers = {"Content-Type":"application/json"}
payload={"_app_version":"4724","_platform":"ios","uuid":uuid,"User-Agent":"Mercari_r/600 (Android 23; ja; arm64-v8a,; samsung SC-02H Build/6.0.1)"}
access_token=requests.post("https://api.mercari.jp/auth/create_token", params=payload,headers=headers).json()
access_token=access_token['data']['access_token']
print("access_token:\n"+access_token)

payload={"_app_version":"4724","_platform":"ios","_access_token":access_token,"User-Agent":"Mercari_r/600 (Android 23; ja; arm64-v8a,; samsung SC-02H Build/6.0.1)"}
r=requests.post("https://api.mercari.jp/global_token/get", params=payload,headers=headers).json()
global_access_token=r['data']['global_access_token']
print("global_access_token:\n"+global_access_token)

payload={"_app_version":"4724","_platform":"ios","_access_token":access_token,"_global_access_token":global_access_token,"User-Agent":"Mercari_r/600 (Android 23; ja; arm64-v8a,; samsung SC-02H Build/6.0.1)","iv_cert":uuid,"email":login_id,"revert":"check","password":login_pass}
r=requests.post("https://api.mercari.jp/users/login", params=payload,headers=headers).json()
uid=r["data"]["id"]
print("id:\n"+str(r["data"]["id"]))

input()
