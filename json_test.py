import json
# person = {    "name": "John",
#     "age": 30, "city": "New York",
#     "is_student": False, "courses": ["Math", "Science"],
#     "address": {"street": "123 Main St", "zip": "10001"}
# }

# pJSON = json.dumps(person, indent=4)
# print(pJSON)

# # Saving the JSON object to a file
# # the r means read mode, and w means write mode
# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)

class User:

    def __init__(self, name, age, city, is_student, courses, address):
        self.name = name
        self.age = age
        self.city = city
        self.is_student = is_student
        self.courses = courses
        self.address = address

user = User(
    'John',
    30,
    'New York',
    False,
    ['Math', 'Science'],
    {'street': '123 Main St', 'zip': '10001'}
)

def user_to_json(user):
    if isinstance(user, User):
        return {
            'name': user.name,
            'age': user.age,
            'city': user.city,
            'is_student': user.is_student,
            'courses': user.courses,
            'address': user.address,
            user.__class__.__name__: True
        }
    else:
        raise TypeError(f"Object of type {user.__class__.__name__} is not JSON serializable") 

user_json = user_to_json(user)
print(json.dumps(user_json, indent=4))