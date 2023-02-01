import requests
import json

headers = {
    'Authorization': 'Bearer TinkoffOpenApiSandboxSecretToken',
    'Content-Type': 'application/json',
    
}

json_data = {
    "correlationId": 4536394586934857,
    "companyAccountNumber": "40802123456789012345",
    "registryCreateType": "FAIL_ERRORS",
    "payments": [
    {
        "number": 1,
        "accountNumber": "12345678901234567890",
        "paymentPurpose": "Оплата по договору",
        "selfEmployedInfo": {
        "firstName": "Петр",
        "lastName": "Петров",
        "middleName": "Петрович"
        },
        "sum": 750,
        "revenueTypeCode": "2"
    }
    ],
    "taxHolding": True,
    "incomeType": "FROM_LEGAL_ENTITY"
}

response = requests.post('https://business.tinkoff.ru/openapi/sandbox/api/v1/self-employed/payment-registry/create', headers=headers, data = json_data)



print(response.text)