auth_response = {
    "data": {
        "token": "token",
        "onBoardApplied": True,
        "customer": {
            "id": 123456,
            "regVersion": None,
            "name": "Bob Alice",
            "birthDate": "1990-01-03T00:00:00",
            "cellPhoneNumber": "912345678",
            "indicativeCellPhoneNumber": "+351",
            "workPostalCode": 1998000,
            "residencePostalCode": 1998000,
            "gender": "MALE",
            "emailStatus": "VALIDATED",
            "workPlace": "Lisboa",
            "residencePlace": "Lisboa",
            "nif": None,
            "registerStatus": "REGISTERED",
            "initialActions": [],
            "latCoordinateWork": 38.71496790538967,
            "lngCoordinateWork": -9.124689422764673,
            "latCoordinateResidence": 38.71496790538967,
            "lngCoordinateResidence": -9.124689422764673,
            "passwordStatus": "DEFINED",
            "email": "test@email.com"
        }
    },
    "message": [
        None
    ]
}

card_list = {
        "data": [
            {
                "id": 123456,
                "regVersion": None,
                "number": "1992847394384756",
                "ownerName": "BOB ALICE",
                "status": "ACTIVE",
                "product": {
                    "id": 12345678,
                    "bin": 12345678,
                    "name": "Edenred Refeição PVL",
                    "productType": "RESTAURANT",
                    "digital": False
                },
                "associatedUsers": [],
                "holder": {
                    "id": 987654,
                    "regVersion": None,
                    "customer": {
                        "id": 123456,
                        "regVersion": None,
                        "name": "Bob Alice",
                        "registerDate": "2000-03-02T10:00:00.000+0000",
                        "lastLoginDateHour": "2024-03-02T10:00:00.000+0000",
                        "status": "ACTIVE"
                    },
                    "pointsEarned": None
                },
                "favorite": "TRUE",
                "productDetails": None,
                "subProductModel": {
                    "id": 4,
                    "created": None,
                    "updated": None,
                    "product": {
                        "id": 98765432,
                        "bin": 98765432,
                        "name": "Edenred Refeição PVL",
                        "productType": "RESTAURANT",
                        "digital": False
                    },
                    "productDetails": None,
                    "name": "Edenred Refeição PVL"
                }
            }
        ],
        "message": [
            "Operação realizada com sucesso!"
        ]
    }


movements_list = {
    "data": {
        "account": {
            "iban": None,
            "cardNumber": "1992847394384756",
            "availableBalance": 69.00,
            "cardHolderFirstName": "Bob Alice",
            "cardHolderLastName": "MY COMPANY",
            "cardActivated": True
        },
        "movementList": [{
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
    },
    "message": [
        "Operação realizada com sucesso!"
    ]
}