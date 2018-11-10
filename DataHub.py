import pymongo
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class DataAggregation:
    ### creates a mongo database to store data
    ### few functions to work and aggregate data
    ### TODO: seperate DB from functions to work with data?
    def __init__(self,
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

        self.mongo_str = 'mongodb://' + mongo_client + ':' + mongo_pw + '@' + mongo_path

        #
        self.client = pymongo.MongoClient(self.mongo_str)
        self.db = self.client.test
        self.games = self.db.get_collection("games")
        self.gameList = get_game_list()  # returns a set

        #eine kleine Änderung hallo

class ProvideData:
    ### Input of Data 
    def __init__(self,
                 filename=askopenfilename(),
                ):

        with open(filename, 'r') as f:
            match_list = set(f.read().split(',\n'))        

        def get_gameid_list(self, match_list):
            return set(map(lambda x: int(x.split('?')[0].split('/')[-1]), match_list))
            
        def open_file(self):
            pass