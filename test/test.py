from core import get_auth, get_marks, calc_avr_mark, get_schedule

TEST_LOGIN = "zulmu_aa95"
TEST_PASSWORD = "Mjm74#ng"

def TestCase_1():
        client = get_auth(TEST_LOGIN, TEST_PASSWORD)
        return client[0]

def TestCase_2():
        success, token = get_auth(TEST_LOGIN, TEST_PASSWORD)
        if not success:
                return False
        marks = get_marks(token)
        return marks

def TestCase_3():
        success, token = get_auth(TEST_LOGIN, TEST_PASSWORD)
        if not success:
                return False
        schedule = get_schedule(token, week = True, date = "2025-05-31")
        return schedule

def TestCase_4(): 
        success, token = get_auth(TEST_LOGIN, TEST_PASSWORD)
        if not success:
                return False
        average = calc_avr_mark(token)
        return average
        

print(TestCase_1())
print(TestCase_2())
print(TestCase_3())
print(TestCase_4())
