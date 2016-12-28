from scraper.tivix import get_random_tivix_member_bio
from scraper.tivix import get_closest_tivix_matched_bio
from scraper.tivix import _get_list_of_tivix_members

def test_get_all_tivix_members():
    members = _get_list_of_tivix_members()
    assert members
    assert '/team-members/jack-muratore/' in  members
    assert '/team-members/kyle-connors/' in members
    assert '/team-members/tan-nguyen/' in members
    assert '/team-members/will-liu/' in members
    assert '/team-members/george-bush/' not in members

def test_bio_to_alexa_string():
    bret_bio = get_random_tivix_member_bio('bret-waters')
    assert 'Bret Waters' in bret_bio
    assert 'ridiculously smart team' in bret_bio
    flavio_bio = get_random_tivix_member_bio('flavio-zhingri')
    assert 'hardest person' in flavio_bio

def test_closest_match():
    sumit_bio = get_closest_tivix_matched_bio('Sumit')
    assert 'Sumit' in sumit_bio
    bret_bio = get_closest_tivix_matched_bio('Bret aters')
    assert 'Bret Waters' in bret_bio
    silin_bio = get_closest_tivix_matched_bio('Silin Ya')
    assert 'Silin Na' in silin_bio



