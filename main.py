from typing import Optional
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from github import Github
import json

config_file = open("config.json")
config = json.load(config_file)
config_file.close()

app = FastAPI()
g = Github(config['access_token'])
repo_owner = config['repo_owner']
repo_name = config['repo_name']



@app.get("/")
def read_root():
    response = []
    repo = g.get_user(repo_owner).get_repo(repo_name)
    branches = [match for match in repo.get_branches() if match.name.find(config['branch_name_template']) != -1]
    
    new_branch_name = config['branch_name_template']+'-'+ str(len(branches))

    print(new_branch_name)
    return {}