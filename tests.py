from scraper.tivix import get_list_of_tivix_members

def test_get_all_tivix_members():
    members = get_list_of_tivix_members()
    assert members
    assert '/team-members/jack-muratore/' in  members
    assert '/team-members/kyle-connors/' in members
    assert '/team-members/tan-nguyen/' in members
    assert '/team-members/will-liu/' in members
    assert '/team-members/george-bush/' not in members

