from scraper.tivix import get_list_of_tivix_members

def test_get_all_tivix_members():
    members = get_list_of_tivix_members()
    assert members
    assert 'jack-muratore' in  members
    assert 'kyle-conners' in members
    assert 'tan-nguyen' in members
    assert 'will-liu' in members
    assert 'george-bush' not in members

