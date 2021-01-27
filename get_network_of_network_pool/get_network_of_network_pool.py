#Get Network of Network Pool
#Get details of a network in a givel network pool
import requests
import json
import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils
import pprint

class GetNetworkofNetworkPools:
    def __init__(self):
        print('Get Network of Network Pools')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]
        self.network_pool_id = sys.argv[4]
        self.network_id = sys.argv[5]

    def get_network_of_network_pool(self):
        get_network_of_pool_url = 'https://'+self.hostname+'/v1/network-pools/'+self.network_pool_id+'/networks/'+self.network_id
        pprint.pprint(self.utils.get_request(get_network_of_pool_url))

if __name__== "__main__":
    GetNetworkofNetworkPools().get_network_of_network_pool()
