import DataHub

match_list = DataHub.ProvideData.get_matchlist_from_textfile()

if 'jsons' not in locals():
    jsons = []
if len(jsons) < len(match_list):
    jsons = [DataHub.DataAggregation.get_json(url) for url in match_list] # alle jsons hintereinandergeklatscht