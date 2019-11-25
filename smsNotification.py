def sendSmsNotification(category, location):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Hello,\n" + category + " identified at location " + location + " and need your attention to make our workspace clean.\n Thanks\n SmartBin-e-Alert Team&language=english&route=p&numbers=9441440625,8099440764"
    headers = {
    'authorization': "SfQzF3ydwcpGJk2NoUqh1E5xCTvKLaHDsjet8OVPuXribBnZ4Yo8M9wWnBCevZkOt4DypxgK01VQ2fcl",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)