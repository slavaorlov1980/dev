import json


class CharList:
    file_name = 'rnm_char_data.json'

    def __init__(self) -> object:
        with open(self.file_name) as file:
            self.data = json.load(file)

    def most_popular_char(self) -> str:

        result = {
            "count": 0,
            "mpchar": "",
        }

        for i in self.data:
            length = len(i.get('episode'))

            if length > result["count"]:
                result["count"] = length
                result["mpchar"] = i.get('name')
        
        return result['mpchar']

    def most_popular_dead(self) -> str:
        count = 0
        for i in self.data:
            if i.get('status') == 'Dead':
                length = len(i.get('episode'))
                if length > count:
                    count = length
                    mpdead = i.get('name')
        return mpdead

    def all_chars_in_episode(self, ep):
        # target = ('https://rickandmortyapi.com/api/episode/' + str(ep))
        char_list = []
        for i in self.data:
            for j in i.get('episode'):
                # print(j, self._get_episode_number(j), ep)
                if self._get_episode_number(j) == int(ep):
                    char_list.append(i.get('name'))
        return char_list

    def _get_episode_number(self, episode_name):
        return int(episode_name.split("/")[-1])


if __name__ == '__main__':
    chr = CharList()
    chr.print_most_popular_char()
    print()
    chr.print_most_popular_dead()
    print()
    print('All characters in episode 2')
    for i in chr.all_chars_in_episode(2):
        print(i)
    # for i in chr.data:
    #     print(i.get('location'))
    # print(chr.data[0].keys())
