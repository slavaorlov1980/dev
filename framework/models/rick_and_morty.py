import json
import sys
sys.path.append(r'/home/slava/dev/dev/framework')
from database import DATABASE


class CharList:
    # file_name = 'rnm_char_data.json'

    def __init__(self) -> object:
        # with open(self.file_name) as file:
        #     self.data = json.load(file)
        pass

    def most_popular_char(self) -> str:

        result = self._popular_char_filter()

        return result

    def _popular_char_filter(self, fields: dict = {}):
        """
        Общий фильтр для методов поиска самых популярных персонажей
        fields = {
            "status": "Dead",
            "gender": "Male"
        }
        """

        db_obj = DATABASE()

        where_qeuery = ""

        if fields:
            where_qeuery = "WHERE "
            count = 1
            dict_len = len(fields)
            for i in fields:
                where_qeuery += f"c.{i} = '{fields[i]}' "
                if dict_len != count:
                    where_qeuery += " AND "
                count += 1

        query = f'''
            SELECT c.name, l.id_char, COUNT(l.id_episode) as count
            FROM link as l
            JOIN  chars as c ON( l.id_char = c.id )
            {where_qeuery}
            GROUP BY l.id_char
            ORDER BY count DESC
            LIMIT 1
        '''

        data = db_obj.select(query)
        result = {
            'name': data[0][0],
            'id': data[0][1],
            'ep_count': data[0][2]
        }

        return result

    def most_popular_dead(self) -> str:

        fields = {'status': 'Dead'}
        result = self._popular_char_filter(fields)
        return result

    def most_popular_female(self):
        fields = {'gender': 'Female'}
        result = self._popular_char_filter(fields)
        return result

    def all_chars_in_episode(self, ep):

        db_obj = DATABASE()
        data = db_obj.select('''
            SELECT l.id_char, c.name
            FROM link as l
            JOIN chars as c ON (c.id = l.id_char)
            WHERE id_episode = ?''', [ep]
        )

        char_list = []
        for i in data:
            char_list.append(i[1])
        print(char_list)

        result = {
            'episode': ep,
            'char_list': char_list
        }

        return result

    def _get_episode_number(self, episode_name):
        return int(episode_name.split("/")[-1])


if __name__ == '__main__':
    chr = CharList()
    print(chr.most_popular_female())
