from datetime import datetime, date

ORG_START = date(2018, 1, 1)
CURRENT_DATE = datetime.now().date()

FUNDRAISING_BASE_URL = 'https://www.habitatforhugemanatees.org/fundraising/'


#Provide a list of hypothetical currencies in which donations are recieved
CURRENCIES = [{'currency':'USD'
               ,'exchange_rate': 1.0}
               ,{'currency':'CAD'
               ,'exchange_rate': 1.370}
               ,{'currency':'EUR'
               ,'exchange_rate': 0.924}
               ,{'currency':'AUD'
               ,'exchange_rate': 1.516}
               ,{'currency':'MXN'
               ,'exchange_rate': 18.33}
               ,{'currency':'BRL'
               ,'exchange_rate': 5.392}
              ,{'currency':'GBP'
               ,'exchange_rate': 0.783}]