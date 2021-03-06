# -*- coding: utf-8 -*-
from unittest import TestCase
from mock import patch
import py_jenkins.auth as auth

class StandAloneTests(TestCase):

    @patch('__builtin__.open')
    def test_login(self,mock_open):
        mock_open.return_value.read.return_value="netease|password\n"
        self.assertTrue(auth.login('netease','password'))

    @patch('__builtin__.open')
    def test_login_bad_creds(self,mock_open):
        mock_open.return_value.read.return_value = "netease|password"
        self.assertFalse(auth.login('netease1', 'password'))

    @patch('__builtin__.open')
    def test_login_error(self, mock_open):
        mock_open.side_effect=IOError()
        self.assertFalse(auth.login('netease', 'password'))