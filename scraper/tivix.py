import requests
from lxml import html

def get_random_tivix_member_bio():
    return 'Nothing yet'

def get_list_of_tivix_members():
    page = requests.get('http://www.tivix.com/team-members/')
    tree = html.fromstring(page.content)
