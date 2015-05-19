import unittest
from main.domain.ladron import Ladron
from main.domain.banco import Banco
from mock import Mock
import time
from test.common.condition_wrapper import ConditionWrapper

class LadronTest(unittest.TestCase):
    
    def test_objetive_is_setted_correctly(self):
        ladron = Ladron()
        banco = Banco
        ladron.objetivo = banco
        self.assertEqual(ladron.objetivo , banco)
        
    def test_ladron_invoke_wait_when_start_without_objetive(self):
        condition_mock = Mock()
        condition_mock.append = Mock()
        ladron = Ladron(ConditionWrapper(condition_mock))
        ladron.start()
        time.sleep(1)
        condition_mock.append.assert_any_call()
        