from constants import *
import datetime
from faker import Faker
import random

def generate_campaign_data(campaign_names, campaign_type, campaign_full = None):
    #Set the generator seeds for consistency
    Faker.seed(1)
    fake = Faker()
    random.seed(1)
    
    campaigns_other = []
    for c in campaign_names:
        if c != 'Less Musk More Tusk':
            START_DATE = fake.date_between(ORG_START, CURRENT_DATE)
            END_DATE = random.choice([fake.date_between(START_DATE, CURRENT_DATE), None])
            campaign = {'campaign_name':c
                        ,'campaign_type': campaign_type
                        ,'campaign_start_date': START_DATE
                        ,'campaign_end_date': END_DATE}

        else:
            campaign = {'campaign_name':c
                        ,'campaign_type': campaign_type
                        ,'campaign_start_date': datetime.date(2025,2,1)
                        ,'campaign_end_date': None}
        campaigns_other.append(campaign)
    
    #Combine the lists if an input was recieved
    if campaign_full:
        campaigns = campaigns_other + campaign_full
    #Otherwise return the generated names
    else:
        campaigns = campaigns_other
        
    return campaigns