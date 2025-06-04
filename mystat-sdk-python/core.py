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
                return False, None


def get_marks(token):
        url = 'https://mapi.itstep.org/v1/mystat/aqtobe/statistic/marks'

        headers = {
                'accept':'application/json, text/plain, */*',
                'authorization':f'Bearer {token}',
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
                return response.json()
        else:
                return False


def get_schedule(week = True, date = None):
        if week:
                url = f"https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?type=week&date_filter={date}"
        else:
                url = f"https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?type=month&date_filter={date}"
        headers = {
                'accept':'application/json, text/plain, */*',
                'authorization':f'Bearer {token}',
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
                return response.json()['data', []]
        else:
                return None

def calc_avr_mark(token):
        marks_data = get_marks(token)
        if not marks_data:
                print("не удалось получить оценки")
                return None
        marks = []
        for i in marks_data:
                if "mark" in i:
                        marks.append(int(i["mark"]))
        average = sum(marks)/ len(marks)
        return average
