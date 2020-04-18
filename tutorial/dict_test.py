param = {"user_id": 200, 
        "message": "hello",
        "language": "English",
        "location": "Oulu"}

print(type(param))
print(param)


post = dict(message="hello", language="English")
post["user_id"] = 300
post["location"] = "Tampere"

print(post)

print(post['message'])

if 'message' in post:
    print(post['message'])

try:
    print(post['country'])
except KeyError:
    print('The post does not have country')

dir(post)

help(post.get)

cnt = post.get('country', None)
print(cnt)

for key in post.keys():
    value = post[key]
    print(key, "=", value )

for key, value in post.items():
    print(key, "=", value )

for value in post.values():
    print("value =", value)

# merging_dicts.py
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)
