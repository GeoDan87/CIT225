from constants import *
import datetime
from faker import Faker
import random
import numpy as np

def generate_podcast_info(podcast_names):
    #Set the generator seeds for consistency
    Faker.seed(1)
    fake = Faker()
    random.seed(1)
    podcast_info = []
    for p in podcast_names:
        START_DATE = fake.date_between(ORG_START, CURRENT_DATE)
        podcast = {'podcast_name': p.get('podcast_name')
                    ,'podcast_description':  p.get('podcast_description')
                    ,'language_code': 'eng'
                    ,'podcast_start_date': START_DATE
                    ,'podcast_end_date': None}
        podcast_info.append(podcast)
    return podcast_info

def generate_newsletter_info(newsletter_names):
    #Set the generator seeds for consistency
    Faker.seed(1)
    fake = Faker()
    random.seed(1)
    newsletter_info = []
    for n in newsletter_names:
        START_DATE = fake.date_between(ORG_START, CURRENT_DATE)
        newsletter = {'newsletter_name': n.get('newsletter_name')
                    ,'newsletter_description':  n.get('newsletter_description')
                    ,'newsletter_start_date': START_DATE
                    ,'newsletter_end_date': None}
        newsletter_info.append(newsletter)
    return newsletter_info

def generate_podcast_subs(supporter_ids, podcast_info):
    #Create a probablity threshold to guide the percentage of sustaining donations that are still active
    PROB_THRESHOLD = 0.7
    
    #Set the random seeds
    Faker.seed(1)
    fake = Faker()
    random.seed(1)
    
    #Sample the supporter data to create only a subset of them to tie to sustaining donations
    supporter_idsf = random.sample([i.get('supporter_id') for i in supporter_ids], int(np.ceil(len(supporter_ids) * PROB_THRESHOLD)))
    podcast_len = [r for r in range(1, len(podcast_info) + 1)]
    podcast_subs = []
    
    for e in supporter_idsf:
    
        podcast_ids = random.sample([p.get('podcast_id') for p in podcast_info], random.choice(podcast_len))

        for p in podcast_ids:
            podcast = [i for i in podcast_info if i.get('podcast_id') == p][0]
            START_DATE = fake.date_between(podcast.get('podcast_start_date'), CURRENT_DATE)
            podcast_sub = {'supporter_id': e
                           ,'podcast_id': podcast.get('podcast_id')
                           ,'podcast_subscribed_date': START_DATE}
            podcast_subs.append(podcast_sub)
    return podcast_subs
    
def generate_newsletter_subs(email_ids, newsletter_info):
    #Create a probablity threshold to guide the percentage of sustaining donations that are still active
    PROB_THRESHOLD = 0.7
    
    #Set the random seeds
    Faker.seed(1)
    fake = Faker()
    random.seed(1)
    
    #Sample the supporter data to create only a subset of them to tie to sustaining donations
    email_idsf = random.sample([i.get('email_id') for i in email_ids], int(np.ceil(len(email_ids) * PROB_THRESHOLD)))
    newsletter_len = [r for r in range(1, len(newsletter_info) + 1)]
    newsletter_subs = []
    
    for e in email_idsf:
        LANG = random.choice(['eng', 'spa', 'fra', 'por'])
        
        newsletter_ids = random.sample([n.get('newsletter_id') for n in newsletter_info], random.choice(newsletter_len))
        
        
        for n in newsletter_ids:
            newsletter = [i for i in newsletter_info if i.get('newsletter_id') == n][0]
            START_DATE = fake.date_between(newsletter.get('newsletter_start_date'), CURRENT_DATE)
            newsletter_sub = {'email_id': e
                              ,'newsletter_id': newsletter.get('newsletter_id')
                              ,'newsletter_subscribed': random.choice([0,1])
                              ,'newsletter_subscribed_date': START_DATE
                              ,'language_code': LANG
                              ,'newsletter_url': newsletter.get('newsletter_url') +'?lang=' + LANG}
            newsletter_subs.append(newsletter_sub)
    return newsletter_subs
    
    
