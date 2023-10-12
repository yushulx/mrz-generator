import random
import datetime

VALID_COUNTRY_CODES = ['USA', 'CAN', 'GBR', 'AUS', 'FRA', 'CHN', 'IND',
                       'BRA', 'JPN', 'ZAF', 'RUS', 'MEX', 'ITA', 'ESP', 'NLD', 'SWE', 'ARG', 'BEL', 'CHE']


def random_date(start_year=1900, end_year=datetime.datetime.now().year):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)

    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:  # February
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # leap year
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)

    return datetime.date(year, month, day)


def random_string(length=10, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    return ''.join(random.choice(allowed_chars) for i in range(length))


def random_mrz_data():
    surname = random_string(random.randint(3, 7))
    given_name = random_string(random.randint(3, 7))
    nationality = random.choice(VALID_COUNTRY_CODES)
    sex = random.choice(['M', 'F'])
    document_number = random_string(9, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    birth_date = random_date()
    expiry_date = random_date(start_year=datetime.datetime.now(
    ).year, end_year=datetime.datetime.now().year + 10)

    return {
        'Surname': surname,
        'Given Name': given_name,
        'Nationality': nationality,
        'Sex': sex,
        'Document Number': document_number,
        'Birth Date': birth_date.strftime('%y%m%d'),
        'Expiry Date': expiry_date.strftime('%y%m%d')
    }


if __name__ == "__main__":
    print(random_mrz_data())
