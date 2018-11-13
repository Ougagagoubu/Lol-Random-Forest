import pymongo
import requests
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
        
        def get_json(self, url):    
            r  = requests.get(url)
            print("aktuelle URL: ", url)
            j = json.loads(r.text)
            j["_id"] = j["gameId"] #set "primary key" on gameID => prevents multiple uploads of same Match
               
            time.sleep(0.1) # if having trouble getting the games, set this higher to get better server response
        
            print("rufe JSON der gameID:", j["_id"], " ab ...")
            return j

        self.mongo_str = 'mongodb://' + mongo_client + ':' + mongo_pw + '@' + mongo_path

        #
        self.client = pymongo.MongoClient(self.mongo_str)
        self.db = self.client.test
        self.games = self.db.get_collection("games")
        self.gameList = get_game_list()  # returns a set

class ProvideData:

    def get_matchlist_from_textfile(self):
        filename = askopenfilename()
        with open(filename, 'r') as f:
            return set(f.read().split(',\n'))
        

    def get_gameid_list(self, match_list):
        return set(map(lambda x: int(x.split('?')[0].split('/')[-1]), match_list))
            
    def open_file(self):
        pass