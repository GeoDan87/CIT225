from faker import Faker
from constants import *
import random
import uuid
import numpy as np
from dateutil.relativedelta import relativedelta

def generate_fake_sustaining(supporter_data, sustaining_pct):
    
    #Create a probablity threshold to guide the percentage of sustaining donations that are still active
    PROB_THRESHOLD = 0.9
    
    #Set the random seeds
    Faker.seed(1)
    fake = Faker()
    random.seed(1)
    
    #Sample the supporter data to create only a subset of them to tie to sustaining donations
    supporter_dataf = random.sample(supporter_data, int(np.ceil(len(supporter_data) * sustaining_pct)))
    
    data_list = []
    
    #Reset the random seed to ensure consistency
    random.seed(1)
    
    #Generate records as per the nrecs argument
    for i, s in enumerate(supporter_dataf):
        #Generate a probablity to compare to the threshold
        prob = random.uniform(0, 1)
        
        #If the probability is greater than or equal to the threshold, give the donation a canceled status
        if prob >= PROB_THRESHOLD:
            #Choose a random status that's not completed
            STATUS = random.choice([2,3,4])
            START_DATE = fake.date_between(ORG_START, CURRENT_DATE)
            END_DATE = fake.date_between(START_DATE, CURRENT_DATE)
        else:
            STATUS = 1
            START_DATE = fake.date_between(ORG_START, CURRENT_DATE)
            END_DATE = None
            
        #Create the dictionary of data
        data_dict = {
                      'supporter_id': s
                     ,'sustaining_start_date': START_DATE
                     ,'sustaining_end_date': END_DATE
                     ,'sustaining_status': STATUS
                     }
        
        #Add the dictionary of data to the output list
        data_list.append(data_dict)

    return data_list


def generate_fake_donation_sust(sustaining_data, campaigns_data, statuses):
    
    #Set the random seed to ensure consistency
    random.seed(1)
    Faker.seed(1)
    fake = Faker()
    
    data_list = []

    for d in sustaining_data:
        START_DATE = d.get('sustaining_start_date')
        END_DATE = d.get('sustaining_end_date')
        SUPPORTER_ID = d.get('supporter_id')
        SUSTAINING_ID = d.get('sustaining_id')
        CAMPAIGNS = [c.get('campaign_id') for c in campaigns_data 
                     if (START_DATE >= c.get('campaign_start_date') and c.get('campaign_end_date') == None)
                     or (START_DATE >= c.get('campaign_start_date') and START_DATE <= c.get('campaign_end_date'))]
        
        #Set none dates to the current date
        if not END_DATE:
            END_DATE = CURRENT_DATE
        
        #Generate the values that will be consistent for sustaining donations
        N_DONATIONS = int(np.floor((abs(START_DATE - END_DATE).days/365) * 12))
        CURRENCY_DICT = random.choice(CURRENCIES)
        CURRENCY_CODE = CURRENCY_DICT.get('currency')
        EXCHANGE_RATE = CURRENCY_DICT.get('exchange_rate')
        USD_AMOUNT = round(random.uniform(10, 500), 2)
        LOCAL_AMOUNT = round(USD_AMOUNT * EXCHANGE_RATE, 2)
        
        if CAMPAIGNS:
            CAMPAIGN_ID = random.choice(CAMPAIGNS)
            URL = [c.get('campaign_url') for c in campaigns_data if c.get('campaign_id') == CAMPAIGN_ID][0]
        else:
            CAMPAIGN_ID = None
            URL = None

        for m in range(0, N_DONATIONS):
            DONATION_DATE= relativedelta(months=m) + START_DATE

            #Create the dictionary of data
            data_dict = {
                          'supporter_id': SUPPORTER_ID
                         ,'sustaining_id': SUSTAINING_ID
                         ,'donation_url': URL
                         ,'donation_status': random.choices(statuses, weights = [0.01, 0.9, 0.03, 0.01, 0.05], k = 1)[0]
                         ,'currency_code': CURRENCY_CODE
                         ,'donation_local_amount': LOCAL_AMOUNT
                         ,'donation_usd_amount': USD_AMOUNT
                         ,'campaign_id': CAMPAIGN_ID
                         ,'donation_date': DONATION_DATE
                         }

            #Add the dictionary of data to the output list
            data_list.append(data_dict)

    return data_list

def generate_fake_donation(supporter_data, campaigns_data, statuses, donor_pct):
    
    #Set the random seed to ensure consistency
    random.seed(1)
    Faker.seed(1)
    fake = Faker()
    
    random.seed(1)
    #Sample the supporter data to create only a subset of them to tie to sustaining donations
    supporter_dataf = random.sample(supporter_data, int(np.ceil(len(supporter_data) * donor_pct)))
    
    data_list = []
    
    for d in supporter_dataf:
        DONATION_DATE = fake.date_between(ORG_START, CURRENT_DATE)
        SUPPORTER_ID = d
        CAMPAIGNS = [c.get('campaign_id') for c in campaigns_data 
                     if (DONATION_DATE >= c.get('campaign_start_date') and c.get('campaign_end_date') == None)
                     or (DONATION_DATE >= c.get('campaign_start_date') and DONATION_DATE <= c.get('campaign_end_date'))]
        
        #Generate the values that will be consistent for sustaining donations
        CURRENCY_DICT = random.choice(CURRENCIES)
        CURRENCY_CODE = CURRENCY_DICT.get('currency')
        EXCHANGE_RATE = CURRENCY_DICT.get('exchange_rate')
        USD_AMOUNT = round(random.uniform(10, 500), 2)
        LOCAL_AMOUNT = round(USD_AMOUNT * EXCHANGE_RATE, 2)
        if CAMPAIGNS:
            CAMPAIGN_ID = random.choice(CAMPAIGNS)
            URL = [c.get('campaign_url') for c in campaigns_data if c.get('campaign_id') == CAMPAIGN_ID][0]
        else:
            CAMPAIGN_ID = None
            URL = None

        #Create the dictionary of data
        data_dict = {
                      'supporter_id': SUPPORTER_ID
                     ,'donation_url': URL
                     ,'donation_status': random.choices(statuses, weights = [0.01, 0.9, 0.03, 0.01, 0.05], k = 1)[0]
                     ,'currency_code': CURRENCY_CODE
                     ,'donation_local_amount': LOCAL_AMOUNT
                     ,'donation_usd_amount': USD_AMOUNT
                     ,'campaign_id': CAMPAIGN_ID
                     ,'donation_date': DONATION_DATE
                     }

        #Add the dictionary of data to the output list
        data_list.append(data_dict)

    return data_list
