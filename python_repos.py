import requests

#make an api rquest and store results

url = 'https://api.github.com/search/repositories?q=language:Python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

#store api response in a variable
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f'\nSelected information about first repository:')
print(f"Name:{repo_dict['name']}")
print(f"Owner:{repo_dict['owner']['login']}")
print(f"Stars:{repo_dict['stargazers_count']}")
print(f"Repository:{repo_dict['html_url']}")
print(f"Created:{repo_dict['created_at']}")
print(f"Updated:{repo_dict['updated_at']}")
print(f"Descripton:{repo_dict['description']}")
