from scraper.tivix import get_list_of_tivix_members
from scraper.tivix import get_random_tivix_member_bio

def test_get_all_tivix_members():
    members = get_list_of_tivix_members()
    assert members
    assert '/team-members/jack-muratore/' in  members
    assert '/team-members/kyle-connors/' in members
    assert '/team-members/tan-nguyen/' in members
    assert '/team-members/will-liu/' in members
    assert '/team-members/george-bush/' not in members

def test_output_random_bio():
    bret_bio = get_random_tivix_member_bio('bret-waters')
    assert 'Bret Waters' in bret_bio
    assert 'ridiculously smart team' in bret_bio
    flavio_bio = get_random_tivix_member_bio('flavio-zhingri')
    assert 'hardest person' in flavio_bio


