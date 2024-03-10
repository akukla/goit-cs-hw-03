from pymongo import MongoClient

client = MongoClient('mongodb://sa:test1234@localhost:27017/')
db = client['cat_database']
collection = db['cats']

# Виводить всіх котів з колекції
def get_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)

# Виводить інформацію про кота, ідентифікованого за його ім'ям
def get_cat_by_name(name):
    cat = collection.find_one({'name': name})
    print(cat)

# Оновлює вік кота, ідентифікованого за його ім'ям
def update_cat_age(name, age):
    collection.update_one({'name': name}, {'$set': {'age': age}})

# Додає характеристику до кота, ідентифікованого за його ім'ям
def add_feature_to_cat(name, feature):
    collection.update_one({'name': name}, {'$push': {'features': feature}})

# Видаляє кота, ідентифікованого за його ім'ям, з колекції
def delete_cat_by_name(name):
    collection.delete_one({'name': name})

# Видаляє всіх котів з колекції
def delete_all_cats():
    collection.delete_many({})

# Вставляє нового кота в колекцію
def insert_cat(name, age, features):
    cat = {"name": name, "age": age, "features": features}
    collection.insert_one(cat)

# Заповнює колекцію тестовими даними, видаляє попередні данні якщо вони існують
def fill_with_test_data():
    if collection.count_documents({}) > 0:
        delete_all_cats()
    test_cats = [
        {"name": "Barsik", "age": 3, "features": ["ходить в капці", "дає себе гладити", "рудий"]},
        {"name": "Murzik", "age": 5, "features": ["любить гратися", "сірий"]},
        {"name": "Ryzhik", "age": 2, "features": ["рудий", "любить їсти"]},
    ]
    collection.insert_many(test_cats)

fill_with_test_data()

print('\n\nРеалізуйте функцію для виведення всіх записів із колекції.')
get_all_cats()

print('\n\nРеалізуйте функцію, яка дозволяє користувачеві ввести ім\'я кота та виводить інформацію про цього кота.')
get_cat_by_name('Murzik')

print('\n\nСтворіть функцію, яка дозволяє користувачеві оновити вік кота за ім\'ям.')
update_cat_age('Murzik', 4)
get_cat_by_name('Murzik')

print('\n\nСтворіть функцію, яка дозволяє додати нову характеристику до списку features кота за ім\'ям.')
add_feature_to_cat('Murzik', 'любить спати')
get_cat_by_name('Murzik')

print('\n\nРеалізуйте функцію для видалення запису з колекції за ім\'ям тварини.')
delete_cat_by_name('Murzik')
get_all_cats()

print('\n\nРеалізуйте функцію для видалення всіх записів із колекції.')
delete_all_cats()
get_all_cats()