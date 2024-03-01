import os
import random

username = 'sintiadea10'
token = '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'
repository = 'https://gist.github.com/lionff/455529f40ceadf4a7f89dcee6b502bd9'
email = 'akunbarujadi379@gmail.com'

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
