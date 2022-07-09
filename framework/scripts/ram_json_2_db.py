import json
import sys
sys.path.append(r'/home/slava/dev/dev/framework')
from database import DATABASE

file_name = '../rnm_char_data.json'

with open(file_name) as file:
    data = json.load(file)

db_obj = DATABASE()

# print(episode_dict)
# таблица связей


# for i in data:
#     db_list = [i.get('id'), i.get('name'), i.get('status'), i.get('species'), i.get('type'), i.get('gender'), i.get('image'), i.get('url'), i.get('created')]
#     db_obj.do('INSERT INTO chars VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', db_list)

# for i in data:
#     for j in i.get('episode'):
#         id = i.get('id')
#         ep = int(j.split('/')[-1])
#         db_obj.do('INSERT INTO link VALUES (?, ?)', [id, ep])

# for i in episode_dict:
#     ep_list = [i, episode_dict.get(i)]
#     db_obj.do('INSERT INTO episodes VALUES (?, ?)', ep_list)


    # db_list = [i.get('id'), i.get('name'), i.get('status'), i.get('species'), i.get('type'), i.get('gender'), i.get('image'), i.get('url'), i.get('created')]
    # db_obj.do('INSERT INTO chars VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', db_list)

print(db_obj.select('SELECT * FROM link WHERE id_char = ?', [50]))


# docker
