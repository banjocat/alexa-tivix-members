import random

import requests
from lxml import html

def get_random_tivix_member_bio():
    members = get_list_of_tivix_members()
    member_url = random.choice(members)
    page = requests.get('http://www.tivix.com/team-members' + member_url)
    return 'Nothing yet'

def get_list_of_tivix_members():
    page = requests.get('http://www.tivix.com/team-members/')
    tree = html.fromstring(page.content)
    members = tree.xpath('//div[@class="team-member"]/a/attribute::href')
    return members
