import random

import requests
from lxml import html

def get_random_tivix_member_bio():
    '''
    returns a string of a randomly chosen tivix member bio
    '''
    members = get_list_of_tivix_members()
    member_url = random.choice(members)
    page = requests.get('http://www.tivix.com' + member_url)
    tree = html.fromstring(page.content)
    name = tree.xpath('//h1[@class="member-name"]/text()')[0]
    position = tree.xpath('//h2[@class="member-title"]/text()')[0]
    bio_list = tree.xpath('//div[@class="member-bio"]/div/div//text()')
    bio = ' '.join(bio_list)
    # Creating the full text with correct punctuation
    full_text = '%s. %s. %s.' % (name, position, bio)
    return full_text

def get_list_of_tivix_members():
    '''
    returns an array of tivix member bio url paths
    '''
    page = requests.get('http://www.tivix.com/team-members/')
    tree = html.fromstring(page.content)
    members = tree.xpath('//div[@class="team-member"]/a/attribute::href')
    return members
