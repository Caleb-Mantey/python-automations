import unittest
from unittest.mock import patch
from gh_actions_lessons.main import send_discord_message

class TestSendDiscordMessage(unittest.TestCase):

    @patch('requests.post')
    def test_send_discord_message_success(self, mock_post):
        mock_post.return_value.status_code = 204
        send_discord_message('https://discord.com/api/webhooks/1332483720296534087/jPo2eLAFw4uASEvlyEMPDlbwYOjys_Ffvq-5ueWDoM2AOOVjOsxqRCqtzNxqw_xmkFUa', 'This is from github actions!🤣🤣🤣🤣')
        self.assertIn('Message sent successfully', 'Message sent successfully')


if __name__ == '__main__':
    unittest.main()