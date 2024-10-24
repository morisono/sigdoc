from faker import Faker
import random

def gen_fakedata():
    fake = Faker('ja_JP')  # Japanese locale

    data = {
        "id": fake.random_number(digits=10, fix_len=True),
        "name": fake.name(),
        "age": str(fake.random_int(min=20, max=70)),
        "gender": random.choice(["男性", "女性"]),
        "dateOfBirth": str(fake.date_of_birth(minimum_age=20, maximum_age=70)),
        "placeOfBirth": fake.prefecture(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": {
            "current": {
                "street": fake.street_address(),
                "city": fake.city(),
                "state": "",
                "zip": fake.zipcode()
            },
            "previous": [
                {
                    "street": fake.street_address(),
                    "city": fake.city(),
                    "state": "",
                    "zip": fake.zipcode(),
                    "moveInDate": str(fake.past_date(start_date="-5y")),
                    "moveOutDate": str(fake.past_date(start_date="-1y"))
                }
            ]
        },
        "nationality": "日本",
        "occupation": "ソフトウェアエンジニア",
        "company": fake.company(),
        "education": [
            {
                "degree": "学士",
                "school": fake.university(),
                "year": str(fake.year()),
                "major": "情報科学"
            }
        ],
        "maritalStatus": random.choice(["既婚", "未婚"]),
        "familyStructure": [
            {
                "relation": "妻",
                "name": fake.name_female(),
                "age": str(fake.random_int(min=20, max=70)),
                "gender": "女性"
            }
        ],
        "hobbies": "読書、映画鑑賞",
        "skills": "Python, JavaScript, C++",
        "languages": "日本語、英語",
        "hairColor": "黒",
        "skinColor": "黄色",
        "characterTraits": "誠実、努力家",
        "personalityProfile": "INTJ",
        "literacyLevels": {
            "digitalLiteracy": "高",
            "financialLiteracy": "中",
            "healthLiteracy": "低"
        },
        "servicesUsed": [
            {
                "serviceName": "GitHub",
                "serviceType": "開発ツール",
                "startDate": str(fake.past_date(start_date="-5y")),
                "endDate": ""
            }
        ],
        "investmentTrusts": [
            {
                "trustName": "ABC投資信託",
                "investmentAmount": "1000000",
                "investmentDate": str(fake.past_date(start_date="-5y"))
            }
        ],
        "utilities": {
            "water": "東京都水道局",
            "electricity": "東京電力",
            "gas": "東京ガス"
        },
        "bankAccounts": [
            {
                "bankName": "三菱UFJ銀行",
                "accountNumber": str(fake.random_number(digits=7, fix_len=True)),
                "accountType": "普通預金"
            }
        ],
        "creditCards": [
            {
                "cardType": "VISA",
                "cardNumber": fake.credit_card_number(card_type='visa'),
                "expiryDate": fake.credit_card_expire(start="now", end="+3y", date_format="%Y-%m")
            }
        ],
        "nearestStation": "銀座駅",
        "commuteRoute": "東京メトロ銀座線",
        "purchaseHistory": [
            {
                "item": "MacBook Pro",
                "purchaseDate": str(fake.past_date(start_date="-1y")),
                "amount": "200000"
            }
        ],
        "affairs": [],
        "criminalRecord": {
            "sexOffenses": "",
            "fraudOffenses": "",
            "drugOffenses": ""
        }
    }

    return data
