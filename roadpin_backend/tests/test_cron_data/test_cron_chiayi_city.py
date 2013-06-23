# -*- coding: utf-8 -*-

import logging
import unittest
from app.cron_data import cron_chiayi_city

class TestCronChiayiCity(unittest.TestCase):
    '''unit tests for cron_chiayi_city'''

    def setUp(self):
        '''setup for all the tests'''
        logging.info('setup')
        self.____never_used_variable = 1

    def tearDown(self):
        '''teardown for all the tests'''
        logging.info("teardown")

    def test_cron_chiayi_city_true(self):
        '''True should not assert.'''
        assert True

    def test_bottle_tmp_never_used_variable_as_1(self):
        '''a == 1 should not assert.'''
        logging.info("test_bottle_tmp: test_bottle_tmp_true")
        assert self.____never_used_variable == 1
