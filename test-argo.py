import logging
import requests
import sys
import urllib3
import json

urllib3.disable_warnings(urllib3.exceprions.InsecureRequestWarning)

sys.path.insert(1, '/app_argo/config')
from config import *

def url_up(url)
    try:
        r = requests.get(url , verify=False)
        if (r.status_code != 200):
            raise Exception
            
    except Exception as err:
        print(err)
        sys.exit(1)
        return False
    return True
  
def clusterjob()
    cookies = {'argocd.token': token}
    try:
        argo = requests.get(argoUrl + appsApi, cookies=cookies, verify=False)
    except Exception as err:
        print(err)
        return
    appsRes = json.loads(argo.content)
    for app in appRes['items']:
        server = app['server']
        splitCluster = server.split(".")
        Cluster_name = splitCluster[1]
        status =  app['connectionState']['status']
        if Cluster_name==cluster_name:
             if status != "Successful":
                 print("cluster no connected", 'err')
                 sys.exit(1)
                 return False
             elif (status =="Successful"):
                 return True
    
    print("cluster not found", 'err')
    sys.exit(1)
    

def repojob()
    cookies = {'argocd.token': token}
    argo = requests.get(argoUrl + repoApi, cookies=cookies, verify=False)
    appsRes = json.loads(argo.content)
    for app in appRes['items']:
        repo = app['repo']
        status =  app['connectionState']['status']
        if status != "Successful":
            print("repo no connected", 'err')
            sys.exit(1)
        break
        
def main(url)

    url_up(url)
    clusterjob()
    repojob()
    print('success')
    sys.exit(0)
    
if __name__ == '__main__':
    (main(url))
            
        
    
  
                            
 
