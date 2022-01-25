users = {'han': 'activeone', 'elona': 'inactive', 'ching': 'active'}

for user, status in users.copy().items():
    if status=='inactive':
        del users[user]

print(users)

act_user = {}
for user, status in users.items():
    if status=='active':
        act_user[user] = status

print(act_user)

