import random
import difflib

import requests
from lxml import html

def get_random_tivix_member_bio(member=None):
    '''
    returns a string of a randomly chosen tivix member bio
    or get specific team member (for testing)
    '''
    if member:
        member_url = '/team-members/%s/' % member
    else:
        members = _get_list_of_tivix_members()
        member_url = random.choice(members)
    full_text = _create_bio_from_member_url(member_url)
    return full_text

def get_closest_tivix_matched_bio(name):
    '''
    returns the closet matched bio from name
    '''
    members = _get_list_of_tivix_members()
    # the url is lowercase and hyphens instead of spaces
    name_formatted = name.replace(' ', '-').lower()
    name_url = '/team-members/%s/' % name_formatted
    member_matches = difflib.get_close_matches(name_url, members, n=1, cutoff=.9)
    if len(member_matches) != 1:
        return "Unable to find tivix member."
    member_url = member_matches[0]
    full_text = _create_bio_from_member_url(member_url)
    return full_text

def _create_bio_from_member_url(member_url):
    page = requests.get('http://www.tivix.com' + member_url)
    tree = html.fromstring(page.content)
    name = tree.xpath('//h1[@class="member-name"]/text()')[0]
    position = tree.xpath('//h2[@class="member-title"]/text()')[0]
    bio_list = tree.xpath('//div[@class="member-bio"]/div/div//text()')
    bio = ' '.join(bio_list)
    # Creating the full text with correct punctuation
    full_text = '%s. %s. %s.' % (name, position, bio)
    return full_text

def _get_list_of_tivix_members():
    '''
    returns an array of tivix member bio url paths
    '''
    page = requests.get('http://www.tivix.com/team-members/')
    tree = html.fromstring(page.content)
    members = tree.xpath('//div[@class="team-member"]/a/attribute::href')
    return members


