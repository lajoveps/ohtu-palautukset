import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_existing_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")

    def test_search_returns_none_for_unknown_player(self):
        player = self.stats.search("Selanne")

        self.assertIsNone(player)

    def test_team_returns_players_of_team(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]

        self.assertEqual(len(players), 3)
        self.assertIn("Semenko", names)
        self.assertIn("Kurri", names)
        self.assertIn("Gretzky", names)

    def test_team_returns_empty_list_for_unknown_team(self):
        players = self.stats.team("XYZ")

        self.assertEqual(players, [])

    def test_top_returns_best_players_first(self):
        players = self.stats.top(2)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")