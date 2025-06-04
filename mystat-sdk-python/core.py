import requests

def get_auth(login, password):

        url = 'https://mapi.itstep.org/v1/mystat/auth/login'

        headers = {
                'accept':'application/json, text/plain, */*',
                'authorization':'Bearer',
                'content-type':'application/json',
                'referer':'https://mystat.itstep.org/',
                'sec-ch-ua':'"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
                'sec-ch-ua-mobile':'?0',
                'sec-ch-ua-platform':"Windows",
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
                'x-language':'ru'
        }

        data = {"login": login, "password": password}
        response = requests.post(url, json=data, headers = headers)

        if response.status_code == 200:

                return True, response.text
        else:
                return False


def get_marks(login, password):
        result = get_auth(login, password)
        if(result[0] == False):
                return False
        else:
                url = 'https://mapi.itstep.org/v1/mystat/aqtobe/statistic/marks'

        headers = {
                'accept':'application/json, text/plain, */*',
                'authorization':f'Bearer {result[1]}',
                'content-type':'application/json',
                'referer':'https://mystat.itstep.org/',
                'sec-ch-ua':'"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
                'sec-ch-ua-mobile':'?0',
                'sec-ch-ua-platform':"Windows",
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
                'x-language':'ru'
        }

        response = requests.get(url, headers = headers)
        if(response.status_code == 200):
                return response.text
        else:
                return False
