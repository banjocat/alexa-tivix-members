import random
import difflib
import re
import logging

import requests
from fuzzywuzzy import process
from lxml import html

LEVESHTEIN_LIMIT = 60

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
    logging.debug('Spoken name: %s' % name)
    members = _get_list_of_tivix_members(full_url=False)
    # members are lowercase
    name_formatted = name.lower()
    member_match = process.extractOne(name_formatted, members)
    logging.debug('member_match: %s' % str(member_match))
    if member_match[1] < LEVESHTEIN_LIMIT:
        return "Cannot find %s" % name
    member = member_match[0]
    member_url = '/team-members/%s/' % member.replace(' ', '-')
    full_text = _create_bio_from_member_url(member_url)
    return full_text

def _create_bio_from_member_url(member_url):
    '''
    creates an alexa statement from the tivix member's bio page
    '''
    page = requests.get('http://www.tivix.com' + member_url)
    tree = html.fromstring(page.content)
    name = tree.xpath('//h1[@class="member-name"]/text()')[0]
    position = tree.xpath('//h2[@class="member-title"]/text()')[0]
    bio_list = tree.xpath('//div[@class="member-bio"]/div/div//text()')
    bio = ' '.join(bio_list)
    # Creating the full text with correct punctuation
    full_text = '%s. %s. %s.' % (name, position, bio)
    return full_text

def _get_list_of_tivix_members(full_url=True, lastname=True):
    '''
    returns an array of tivix member bio url paths
    if full_url is set to false it will just return the names
    if lastname is set and full_url is false.. it will
    only include the first name
    '''
    page = requests.get('http://www.tivix.com/team-members/')
    tree = html.fromstring(page.content)
    members = tree.xpath('//div[@class="team-member"]/a/attribute::href')
    if full_url:
        return members
    # stripping out the url part
    names_only = []
    get_name = re.compile('/team-members/(.*)-(.*)/')
    for member in members:
        match = get_name.match(member)
        if not match:
            logging.error('invalid url found (%s)', member)
            continue
        firstname = match.groups(0)[0]
        lastname = match.groups(0)[1]
        names_only.append('%s %s' % (firstname, lastname))
    return names_only


