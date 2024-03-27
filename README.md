# edenredpt

**edenredpt** is an unofficial API library for myEdenred (Portugal)

## Installing

**edenredpt** is available on PyPI:

```console
$ python -m pip install edenredpt
```

## Supported Features

- Get card current balance
- Get card movements
- Export card movements as csv

## Usage

### get_balance()
```python
from edenredpt import Edenred

edenred = Edenred(username='user@email.com', password='mypassword')
print(edenred.get_balance())
```
Output:
```sh
69.0
```


### get_transactions()
```python
from edenredpt import 
import pprint

edenred = Edenred(username='user@email.com', password='mypassword')
pprint.pprint(edenred.get_transactions())
```
Output:
```javascript
[{'amount': 182.4,
  'balance': 204.44,
  'category': {'description': 'Crédito', 'id': 5},
  'categoryId': None,
  'mcc': '0',
  'transactionDate': '2024-03-23T21:11:03.228+0000',
  'transactionName': 'Transferência Bancária',
  'transactionType': 4050},
 {'amount': -13.89,
  'balance': 22.04,
  'category': {'description': 'Supermercado', 'id': 2},
  'categoryId': None,
  'mcc': '5411',
  'transactionDate': '2024-03-21T14:11:52.312+0000',
  'transactionName': 'Compra: LIDL',
  'transactionType': 4010}]
```

### get_transactions_csv()
```python
from edenredpt import Edenred

edenred = Edenred(username='user@email.com', password='mypassword')
csv = edenred.get_transactions_csv()
print(csv)

file='./transactions.csv' 
with open(file, 'w') as writer:
    writer.write(csv)
```
Output:
```sh
transactionDate,transactionName,amount,balance
2024-03-23T21:11:03.228+0000,Transferência Bancária,182.4,204.44
2024-03-21T14:11:52.312+0000,Compra: LIDL,-13.89,22.04
```