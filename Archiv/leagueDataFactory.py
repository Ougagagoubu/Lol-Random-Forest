import pymongo


class LeagueDataFactory:

    def __init__(self,
                 current_week=1,
                 mongo_client='bth84',
                 mongo_pw='ch!M3R42',
                 mongo_path='cluster0-shard-00-00-rafzz.mongodb.net:27017, \
                            cluster0-shard-00-01-rafzz.mongodb.net:27017,  \
                            cluster0-shard-00-02-rafzz.mongodb.net:27017/  \
                            test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
                 ):
        def get_game_list():
            cursor = self.games.aggregate([
                {"$group": {"_id": "$gameId"}}
            ])
            return set(map(lambda x: x['_id'], list(cursor)))

        def get_match_list():
            with open('./SummerSplit.txt', 'r') as f:
                match_list = set(f.read().split(',\n'))

            match_list = set(map(lambda x: int(x.split('?')[0].split('/')[-1]), match_list))
            return match_list

        self.current_week = current_week
        self.mongo_str = 'mongodb://' + mongo_client + ':' + mongo_pw + '@' + mongo_path

        #
        self.client = pymongo.MongoClient(self.mongo_str)
        self.db = self.client.test
        self.games = self.db.get_collection("games")
        self.gameList = get_game_list()  # returns a set
        self.matchList = get_match_list()  # returns a set
        self.listToImport = list(self.matchList - self.gameList)