# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: login.py
# @Author: xiaohanzhang
# @Date: 2021/4/25

import randomMac
import requests
import time

"""
1、/auth/getLoginCode?areaCode={areaCode}&account={account}&salt={salt}&mac={mac}&deviceId={deviceId}&myInviteCode={myInviteCode} 
String salt = genSalt();
String loginPasswordMd5 = LoginPassword.md5(key);
String mac = MAC.encodeBase64(("" + areaCode + account + salt).getBytes(), loginPasswordMd5);

2、/authkeys/uploadLoginKey?publicKey={publicKey}&privateKey={privateKey}&mac={mac}&userId={userId}&salt={salt} 
3、/authkeys/getLoginPrivateKey?userId={userId}&mac={macPrivateKey}&salt={saltPrivateKey}
4、/user/login/v1?companyId=&lang=zh&userAgent=ad&data={data}&salt={salt}&userId={userId}&deviceId=android&language=zh
调用第一个接口获取code,没有则调用第二个接口upload，再调用第一个接口，第三个 第四个
压测顺序 新增接口1，login2，login1，login3，新增接口2，login4
"""
# domain = '192.168.1.37:8093'
domain = 'qdgvcc.co-meeting.cn'
protocol = 'http'
protocol = 'https'

# def pwd_md5(password):
#     pwd = hashlib.md5(password.encode(encoding='utf-8')).hexdigest()
#     print(pwd)
#     return pwd

def get_login_param1(phone, pwd, time):

    # url = 'http://192.168.1.37:8093/api/app/gvcc/login-req-param'
    url = protocol + '://' + domain + '/api/app/gvcc/login-req-param'
    params = {
        'areaCode': '86',
        'account': phone,
        'salt': time,
        'loginPassword': pwd
    }
    # print(f"get_mac = {params}")
    response = requests.get(url, params=params)
    if response.status_code == 200 and response.json()['resultCode'] == 1:
        data = response.json()['data']
        print(f"get_login_param1 response = {data}")
        return data
    else:
        print(f'获取mac失败, {phone}')


def get_login_param2(userId, loginPassword, encryptedCode, encryptedPrivateKey):
    url = protocol + '://' + domain + '/api/app/gvcc/loginv1-req-param'
    params = {
        'userId': userId,
        'loginPassword': loginPassword,
        'encryptedCode': encryptedCode,
        'encryptedPrivateKey': encryptedPrivateKey
    }
    response = requests.get(url, params=params)
    print(f"get_login_param2 response = {response.json()}")
    return response.json()['data']


# def base64_mac():
#     login_time = int(time.time() * 1000)
#     # secret = f"'', '86', '18205322783',{login_time}, {pwd_md5('abc12345')}"
#     secret = f"'86', '18200000002',{login_time}, '7ba1bd982b33ac731c2c3bca90e77be9'"
#     bytesStr = secret.encode(encoding='utf-8')
#     mac = hashlib.md5(bytesStr).hexdigest()
#     # mac = base64.b64encode(bytesStr)
#     print(mac)
#     return (mac, login_time)

def write_txt(str):
    with open("user.txt", "a", encoding='utf-8') as f:
        f.write(str + '\n')


def login1(phone, mac, login_time):
    url = protocol + '://' + domain + '/auth/getLoginCode'
    if mac:
        data = {
            'areaCode': '86',
            'account': phone,
            'salt': login_time,
            'mac': mac,
            'deviceId': 'android'
        }
        print(f'login1_data = {data}')
        response = requests.post(url, data=data)
        print(response.json())
        if response.status_code == 200 and response.json()['resultCode'] == 1:
            data = response.json()['data']
            print(f"login1 response = {data}")
            return data['code']
        else:
            print(f"login1登录失败, {phone}")


def login2(userId, publicKey, privateKey, mac, salt):
    url = protocol + '://' + domain + '/authkeys/uploadLoginKey'
    data = {
        'publicKey': publicKey,
        'privateKey': privateKey,
        'mac': mac,
        'userId': userId,
        'salt': salt
    }
    # print(f"login2 request = {data}")
    response = requests.post(url, data=data)
    if response.status_code == 200 and response.json()['resultCode'] == 1:
        data = response.json()
        print(f"login2 response = {data}")
        return data['resultCode']
    else:
        print(f"login2登录失败")


def login3(userId, mac, salt):
    url = protocol + '://' + domain + '/authkeys/getLoginPrivateKey'
    data = {
        'userId': userId,
        'mac': mac,
        'salt': salt
    }
    response = requests.post(url, data=data)

    print(f'login3_response = {response.json()}')
    return response.json()['data']['privateKey']


def login4(userId, salt, data):
    url = protocol + '://' + domain + '/user/login/v1'
    post_data = {
        'companyId': '',
        'lang': 'zh',
        'userAgent': 'ad',
        'userId': userId,
        'data': data,
        'deviceId': 'android',
        'salt': salt,
        'language': 'zh'
    }
    response = requests.post(url, data=post_data)
    print(f"login4 response = {response.json()}")
    data_str = response.json()['data']['data']
    return data_str


def get_token(data, encryptedCode, privateKey, pwd):
    url = protocol + '://' + domain + '/api/app/gvcc/deal-loginv1-data'
    params = {
        'data': data,
        'encryptedCode': encryptedCode,
        'privateKey': privateKey,
        'loginPassword': pwd
    }
    response = requests.get(url, params=params)
    print(response.json())
    return response.json()['data']['access_token']


def login():
    login_time = int(time.time() * 1000)
    phone = '18205322783'
    pwd = 'abc123456'
    data = get_login_param1(phone, pwd, login_time)
    mac = data['getLoginCode_Mac']

    # userId = login1(phone, mac, login_time)
    uploadLoginKeyParam = data['uploadLoginKeyParam']
    getLoginPrivateKeyParam = data['getLoginPrivateKeyParam']
    userId = uploadLoginKeyParam['userId']
    resultCode = login2(userId, uploadLoginKeyParam['publicKey'], uploadLoginKeyParam['privateKey'],
                        uploadLoginKeyParam['mac'], uploadLoginKeyParam['salt'])
    if resultCode and resultCode == 1:
        code = login1(phone, mac, login_time)
        privateKey = login3(userId, getLoginPrivateKeyParam['mac'], getLoginPrivateKeyParam['salt'])
        data = get_login_param2(userId, pwd, code, privateKey)
        data2 = login4(userId, data['salt'], data['data'])
        token = get_token(data2, code, privateKey, pwd)
        print(f"token = {token}")



def main():
    login()


if __name__ == '__main__':
    main()