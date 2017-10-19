from unittest.mock import Mock, patch
from external.gw2 import GW2


@patch('external.gw2.requests.get')
def test_get_raid_kills(mock_get):
    gw2 = GW2(auth='llong-auth')
    mock_get.return_value = Mock(ok=True)
    kills = [
            "gorseval",
            "vale_guardian",
            "bandit_trio",
            "spirit_woods",
            "slothasor",
            "sabetha",
            "samarog",
            "mursaat_overseer",
            "cairn"
            ]
    mock_get.return_value.json.return_value = kills
    assert gw2.get_raid_kills() == kills
