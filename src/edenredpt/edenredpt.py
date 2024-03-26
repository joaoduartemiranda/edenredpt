import io, logging, csv
import requests
from .exceptions import EdenredAPIException, AuthenticationException

class Edenred:
    def __init__(self, username, password, url = 'https://www.myedenred.pt'):
        self.username = username
        self.password = password
        self.url = url
        self.token, self.cookie = self.__edenred_auth()
        self.card_id = self.__get_card_id()

    def __edenred_auth(self):
        res = requests.post(f'{self.url}/edenred-customer/v2/authenticate/default?appVersion=1.0&appType=PORTAL&channel=WEB',
            json = {'userId': self.username, 'password': self.password})

        if res.status_code == 409:
            logging.error(f'Error message: {res.json()["message"][0]}')
            raise AuthenticationException("Invalid credentials")
        if res.status_code != 200:
            logging.error(f'Status code: {res.status_code}, Content: {res.content}')
            raise EdenredAPIException(f"Error while calling Edenred authenticate API.")

        token = res.json()['data']['token']
        cookie = ''
        for c in res.cookies:
            cookie += f'{c.name}={c.value}; '
        return token, cookie

    def __edenred_get(self, path):
        res = requests.get(f'{self.url}{path}',
            headers = {'Cookie': self.cookie, 'Authorization': self.token, 'Content-Type': 'application/json'})

        if res.status_code == 401:
            logging.error(f'Error message: {res.json()["message"][0]}')
            raise AuthenticationException("Session Expired")
        if res.status_code != 200:
            logging.error(f'Status code: {res.status_code}, Content: {res.content}')
            raise EdenredAPIException(f"Error while calling Edenred API.")
        
        return res.json()

    def __get_card_id(self):
        return self.__edenred_get('/edenred-customer/v2/protected/card/list?appVersion=1.0&appType=PORTAL&channel=WEB')['data'][0]['id']
    
    def get_balance(self):
        return self.__edenred_get(f'/edenred-customer/v2/protected/card/{self.card_id}/accountmovement?appVersion=1.0&appType=PORTAL&channel=WEB')['data']['account']['availableBalance']

    def get_transactions(self):
        return self.__edenred_get(f'/edenred-customer/v2/protected/card/{self.card_id}/accountmovement?appVersion=1.0&appType=PORTAL&channel=WEB')['data']['movementList']
    
    def get_transactions_csv(self):
        transactions = self.get_transactions()
        keys = ['transactionDate', 'transactionName', 'amount', 'balance']
        movements = []
        for idx, row in enumerate(transactions):
            movements.append({k: row[k] for k in set(keys) & set(row.keys())})

        output = io.StringIO()
        writer = csv.DictWriter(output, keys)
        writer.writeheader()
        writer.writerows(movements)

        return output.getvalue()