import unittest
from unittest import mock
from edenredpt import Edenred, AuthenticationException
from requests import cookies
from tests.response_payloads import auth_response, card_list, movements_list


class MockResponse:
        def __init__(self, json_data, status_code, content = None, cookies = None):
            self.json_data = json_data
            self.status_code = status_code
            self.content = content
            self.cookies = cookies
        
        def json(self):
            return self.json_data

def mocked_edenred_post_api(*args, **kwargs):

    if args[0] == 'https://www.myedenred.pt/edenred-customer/v2/authenticate/default?appVersion=1.0&appType=PORTAL&channel=WEB':
        if kwargs['json']['userId'] != 'username@email.com' or kwargs['json']['password'] != 'password':
            return MockResponse({"message": ["Credenciais inválidas. Por favor, tente novamente."], "internalCode": "10403"}, 409)

        cookie_jar = cookies.RequestsCookieJar()
        cookie_jar.set('cookie_key_1', 'cookie_value_1', domain = '.www.myedenred.pt')
        cookie_jar.set('cookie_key_2', 'cookie_value_2', domain = '.www.myedenred.pt')
        return MockResponse(auth_response, 200, "", cookie_jar)
    
    return MockResponse(None, 404)

def mocked_edenred_get_api(*args, **kwargs):

    if kwargs['headers']['Cookie'] != 'cookie_key_1=cookie_value_1; cookie_key_2=cookie_value_2; ' or kwargs['headers']['Authorization'] != 'token':
            return MockResponse({"message":["A sua sessão expirou."],"internalCode":10405}, 401)
    
    if args[0] == 'https://www.myedenred.pt/edenred-customer/v2/protected/card/list?appVersion=1.0&appType=PORTAL&channel=WEB':
        return MockResponse(card_list, 200)
    elif args[0] == 'https://www.myedenred.pt/edenred-customer/v2/protected/card/123456/accountmovement?appVersion=1.0&appType=PORTAL&channel=WEB':
        return MockResponse(movements_list, 200)
    
    return MockResponse(None, 404)

class TestEdenred(unittest.TestCase):

    maxDiff = None

    @mock.patch('edenredpt.edenredpt.requests.post', side_effect=mocked_edenred_post_api)
    @mock.patch('edenredpt.edenredpt.requests.get', side_effect=mocked_edenred_get_api)
    def test_init_class_success(self, mock_get, mock_post):
        edenred = Edenred('username@email.com', 'password')

        # Assert POST Authentication results
        self.assertEqual(edenred.token, 'token')
        self.assertEqual(edenred.cookie, 'cookie_key_1=cookie_value_1; cookie_key_2=cookie_value_2; ')
        
        # Assert GET Card Id results
        self.assertEqual(edenred.card_id, 123456)


    @mock.patch('edenredpt.edenredpt.requests.post', side_effect=mocked_edenred_post_api)
    @mock.patch('edenredpt.edenredpt.requests.get', side_effect=mocked_edenred_get_api)
    def test_init_class_auth_error(self, mock_get, mock_post):

        # Assert that exception is raised in case of incorrect credentails
        with self.assertRaises(AuthenticationException):
            edenred = Edenred('invalid_user@email.com', 'blablabla')


    @mock.patch('edenredpt.edenredpt.requests.post', side_effect=mocked_edenred_post_api)
    @mock.patch('edenredpt.edenredpt.requests.get', side_effect=mocked_edenred_get_api)
    def test_get_balance_success(self, mock_get, mock_post):

        edenred = Edenred('username@email.com', 'password')

        # Assert balance
        self.assertEqual(edenred.get_balance(), 69.00)

    @mock.patch('edenredpt.edenredpt.requests.post', side_effect=mocked_edenred_post_api)
    @mock.patch('edenredpt.edenredpt.requests.get', side_effect=mocked_edenred_get_api)
    def test_get_transactions_success(self, mock_get, mock_post):

        edenred = Edenred('username@email.com', 'password')

        movements = [{
                "transactionDate": "2024-03-25T08:52:41.912+0000",
                "transactionType": 4010,
                "transactionName": "Compra: CONTINENTE",
                "amount": -30.02,
                "mcc": "5411",
                "category": {
                    "id": 2,
                    "description": "Supermercado"
                },
                "categoryId": None,
                "balance": 69.00
            },
            {
                "transactionDate": "2024-02-29T18:06:42.723+0000",
                "transactionType": 4050,
                "transactionName": "Transferência Bancária",
                "amount": 70.00,
                "mcc": "0",
                "category": {
                    "id": 5,
                    "description": "Crédito"
                },
                "categoryId": None,
                "balance": 99.02
            }]
        
        # Assert transactions list
        self.assertCountEqual(edenred.get_transactions(), movements)

    @mock.patch('edenredpt.edenredpt.requests.post', side_effect=mocked_edenred_post_api)
    @mock.patch('edenredpt.edenredpt.requests.get', side_effect=mocked_edenred_get_api)
    def test_get_transactions_csv_success(self, mock_get, mock_post):

        edenred = Edenred('username@email.com', 'password')
        result = edenred.get_transactions_csv()

        movements = "transactionDate,transactionName,amount,balance\r\n2024-03-25T08:52:41.912+0000,Compra: CONTINENTE,-30.02,69.0\r\n2024-02-29T18:06:42.723+0000,Transferência Bancária,70.0,99.02\r\n"
        # Assert transactions csv string
        self.assertEqual(result, movements)