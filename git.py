import os
import random

username = ''
token = ''
repository = ''
email = ''

for i in range(200):
    d = str(i) + 'days ago'
    rand = random.randrange(1, 12)
    with open('test.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add test.txt')
    os.system(f'git commit --date="2023-{rand}-{d}" -m 1 --author="{username} <{email}>"')

# Push to GitHub using the specified username and token
os.system(f'git remote add origin_with_token https://{username}:{token}@github.com/{username}/{repository}.git')
os.system('git push -u origin_with_token main')

# Remove the temporary remote
os.system('git remote remove origin_with_token')

