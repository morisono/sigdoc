from faker import Faker
import random

fake = Faker('ja_JP')

presets = {
    "education": ['小学校卒', '中学校卒', '高校卒', '専門学校卒', '短大卒', '大学卒', '大学院卒'],
    "political_party": ['自由民主党', '立憲民主党', '公明党', '共産党', '社民党', '無所属'],
    "marital_status": ['未婚', '既婚', '離婚済み', '未亡人'],
    "spouse": ['なし', 'あり'],
    "consideration_required_information": {
        "race_belief_social_status": ['なし', 'アジア人', '白人', '黒人', 'ヒスパニック', '先住民族', '混血'],
        "disability_information": ['なし', '視覚障害', '聴覚障害', '肢体不自由', '知的障害', '精神障害'],
        "medical_history": ['なし', '心臓病', '糖尿病', '高血圧', 'アレルギー', '喘息'],
        "medical_checkup_results": ['なし', '異常なし', '要観察', '要治療'],
        "crime_history": ['なし', '詐欺', '窃盗', '暴行', '薬物'],
        "victim_of_crime": ['なし', '詐欺被害', '盗難被害', '暴行被害', '性犯罪被害']
    },
    "sensitive_information": {
        "thoughts_beliefs_religion": ['なし', 'キリスト教', 'イスラム教', '仏教', 'ヒンドゥー教', '無宗教', 'その他'],
        "race_ethnicity_origin": ['なし', 'アジア人', '白人', '黒人', 'ヒスパニック', '先住民族', '混血'],
        "physical_mental_disability": ['なし', '視覚障害', '聴覚障害', '肢体不自由', '知的障害', '精神障害'],
        "worker_union_activities": ['なし', '労働組合員', '労働組合非加入', 'ストライキ参加経験あり', 'ストライキ参加経験なし'],
        "political_rights_exercise": ['なし', 'デモ参加経験あり', 'デモ参加経験なし', '署名活動参加経験あり', '署名活動参加経験なし'],
        "healthcare_sexual_life": ['なし', '性病治療経験あり', '性病治療経験なし', '避妊手術経験あり', '避妊手術経験なし']
    }
}

def gen_fakedata():
    fakedata = {
        "id": fake.random_int(min=1000, max=9999, step=1),
        "name": fake.name(),
        "age": fake.random_int(min=20, max=90, step=1),
        "gender": fake.random_element(elements=('男性', '女性')),
        "address": fake.address().replace('\n', ''),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "job": fake.job(),
        "company": fake.company(),
        "credit_card": fake.credit_card_number(card_type=None),
        "bank": fake.bank_country(),
        "family_structure": fake.random_element(elements=('単身', '夫婦', '子供あり', '3世代')),
        "hair_color": fake.random_element(elements=('黒', '茶', '金', '銀')),
        "skin_color": fake.random_element(elements=('白', '黄', '茶', '黒')),
        "height": fake.random_int(min=150, max=200, step=1),
        "weight": fake.random_int(min=50, max=100, step=1),
        "education": fake.random_element(elements=presets["education"]),
        "political_party": fake.random_element(elements=presets["political_party"]),
        "marital_status": fake.random_element(elements=presets["marital_status"]),
        "spouse": fake.random_element(elements=presets["spouse"]),
        "website": fake.url(),
        "consideration_required_information": {
            "race_belief_social_status": fake.random_element(elements=presets["consideration_required_information"]["race_belief_social_status"]),
            "disability_information": fake.random_element(elements=presets["consideration_required_information"]["disability_information"]),
            "medical_history": fake.random_element(elements=presets["consideration_required_information"]["medical_history"]),
            "medical_checkup_results": fake.random_element(elements=presets["consideration_required_information"]["medical_checkup_results"]),
            "crime_history": fake.random_element(elements=presets["consideration_required_information"]["crime_history"]),
            "victim_of_crime": fake.random_element(elements=presets["consideration_required_information"]["victim_of_crime"])
        },
        "sensitive_information": {
            "thoughts_beliefs_religion": fake.random_element(elements=presets["sensitive_information"]["thoughts_beliefs_religion"]),
            "race_ethnicity_origin": fake.random_element(elements=presets["sensitive_information"]["race_ethnicity_origin"]),
            "physical_mental_disability": fake.random_element(elements=presets["sensitive_information"]["physical_mental_disability"]),
            "worker_union_activities": fake.random_element(elements=presets["sensitive_information"]["worker_union_activities"]),
            "political_rights_exercise": fake.random_element(elements=presets["sensitive_information"]["political_rights_exercise"]),
            "healthcare_sexual_life": fake.random_element(elements=presets["sensitive_information"]["healthcare_sexual_life"])
        }
    }
    return fakedata
