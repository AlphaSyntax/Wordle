import unittest
from unittest.mock import patch, call
from wyrdle import get_random_word, show_guess, game_over

class TestYourModule(unittest.TestCase):

    @patch('wyrdle.random.choice', return_value='HELLO')
    def test_get_random_word(self, _):
        self.assertEqual(get_random_word(), 'HELLO')

    @patch('builtins.print')
    def test_show_guess_correct(self, mock_print):
        show_guess('HELLO', 'HELLO')
        calls = [call('Correct letters:', 'E, H, L, O'),
                 call('Misplaced letters:', ''),
                 call('Wrong letters:', '')]
        mock_print.assert_has_calls(calls, any_order=True)

    @patch('builtins.print')
    def test_show_guess_misplaced(self, mock_print):
        show_guess('HELLO', 'LOHEE')
        calls = [call('Correct letters:', ''),
                 call('Misplaced letters:', 'E, H, L, O'),
                 call('Wrong letters:', '')]
        mock_print.assert_has_calls(calls, any_order=True)

    @patch('builtins.print')
    def test_show_guess_wrong(self, mock_print):
        show_guess('HELLO', 'WORLD')
        calls = [call('Correct letters:', 'L'),
                 call('Misplaced letters:', 'O'),
                 call('Wrong letters:', 'E, H')]
        mock_print.assert_has_calls(calls, any_order=True)

    @patch('builtins.print')
    def test_game_over(self, mock_print):
        game_over('HELLO')
        mock_print.assert_called_once_with('The word was HELLO')

if __name__ == '__main__':
    unittest.main()

