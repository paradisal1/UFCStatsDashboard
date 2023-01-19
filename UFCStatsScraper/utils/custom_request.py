from scrapy import Request

url = 'https://www.espn.com/mma/fightcenter/_/id/400255729/league/ufc'

headers = {
    "authority": "www.espn.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "referer": "https://www.espn.com/mma/fightcenter/_/id/400255729/league/ufc",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Microsoft Edge\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55"
}

cookies = {
    "edition-view": "espn-en-us",
    "edition": "espn-en-us",
    "region": "ccpa",
    "SWID": "F2604355-890A-4FB9-CF07-BC9FD3B7234D",
    "usprivacy": "1YNY",
    "cookieMonster": "1",
    "connectionspeed": "full",
    "_cb_ls": "1",
    "_cb": "Bi8iNQBi1S5pDvlA63",
    "_v__chartbeat3": "CtNUE5BoHpeABvghiH",
    "userAB": "D",
    "anonymous_favorites_params": "athlete%3D29cb2c3192b0e6974443f5e6a48171d1%26athlete%3D29cb2c3192b0e6974443f5e6a48171d1",
    "country": "us",
    "_dcf": "1",
    "s_ensCDS": "0",
    "s_ensRegion": "ccpa",
    "s_ensNSL": "0",
    "_nr": "0",
    "AMCVS_EE0201AC512D2BE80A490D4C%40AdobeOrg": "1",
    "_omnicwtest": "works",
    "s_c24": "1674090347163",
    "s_cc": "true",
    "client_type": "html5",
    "client_version": "4.6.0",
    "s_sq": "wdgespcom%252Cwdgespge%3D%2526pid%253Despn%25253Amma%25253Aindex%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.espn.com%25252Fmma%25252Fschedule%2526ot%253DA",
    "s_omni_lid": "subnav%2Bsubnav_mma_schedule%2Fresults",
    "userZip": "46038",
    "hashedIp": "cc91894ae14ea01379f49f5092e81a011903b1c3e27a839752708478d0792804",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Wed+Jan+18+2023+23%3A48%3A07+GMT-0500+(Eastern+Standard+Time)&version=202212.1.0&isIABGlobal=false&hosts=&consentId=5bec4278-1117-4e59-a806-bf417dfef3e7&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1&AwaitingReconsent=false",
    "_chartbeat2": ".1673756820136.1674103687551.11111.BqktGoC4C9PkByyctGDwyrd_BD5LgL.1",
    "_cb_svref": "null",
    "AMCV_EE0201AC512D2BE80A490D4C%40AdobeOrg": "870038026%7CMCMID%7C87420802407948636493756307006182450889%7CMCAID%7CNONE%7CMCOPTOUT-1674110888s%7CNONE%7CvVersion%7C5.0.0%7CMCIDTS%7C19377",
    "_v__SUPERFLY_lockout": "1",
    "_SUPERFLY_lockout": "1"
}

def generate_initial_request(url=url, headers=headers, cookies=cookies):
    return Request(
        url=url,
        method='GET',
        dont_filter=True,
        cookies=cookies,
        headers=headers,
    )
