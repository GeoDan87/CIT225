from db_connect import *
from generate_donation_data import *
from generate_campaign_data import *
from constants import *
import datetime

SUSTAINING_PCT = 0.1
DONOR_PCT = 0.25

con = connect_db_engine()

#Query the campaign types
campaign_types = select_data(con, 'campaign_type', 'hfh')

#Query the supporters table
supporters = select_data(con, 'supporter', 'hfh')
supporter_ids = [s.get('supporter_id') for s in supporters]

#Select the supporter data to use the ids to generate email address data
CAMPAIGN_TYPE = [c.get('campaign_type') for c in campaign_types if c.get('campaign_type_desc') == 'Fundraising Campaign'][0]

#Create the full campaign for end of year fundraising
campaigns_eoy = [{'campaign_name':'End of Year 2018'
                  ,'campaign_type': CAMPAIGN_TYPE
                  ,'campaign_start_date': datetime.date(2018, 11, 1)
                  ,'campaign_end_date': datetime.date(2018, 12, 31)}
                 ,{'campaign_name': 'End of Year 2019'
                   ,'campaign_type': CAMPAIGN_TYPE
                   ,'campaign_start_date':datetime.date(2019, 11, 1)
                   ,'campaign_end_date': datetime.date(2019, 12, 31)}
                 ,{'campaign_name':'End of Year 2020'
                   ,'campaign_type': CAMPAIGN_TYPE
                   ,'campaign_start_date':datetime.date(2020, 11, 1)
                   ,'campaign_end_date': datetime.date(2020, 12, 31)}
                 ,{'campaign_name':'End of Year 2021'
                   ,'campaign_type': CAMPAIGN_TYPE
                   ,'campaign_start_date': datetime.date(2021, 11, 1)
                   ,'campaign_end_date': datetime.date(2021, 12, 31)}
                 ,{'campaign_name':'End of Year 2022'
                   ,'campaign_type': CAMPAIGN_TYPE
                   ,'campaign_start_date': datetime.date(2022, 11, 1)
                   ,'campaign_end_date': datetime.date(2022, 12, 31)}
                 ,{'campaign_name':'End of Year 2023'
                   ,'campaign_type': CAMPAIGN_TYPE
                   ,'campaign_start_date': datetime.date(2023, 11, 1)
                   ,'campaign_end_date': datetime.date(2023, 12, 31)}
                 ,{'campaign_name':'End of Year 2024'
                   ,'campaign_type': CAMPAIGN_TYPE
                   ,'campaign_start_date': datetime.date(2024, 11, 1)
                   ,'campaign_end_date': datetime.date(2024, 12, 31)}]

#Feed in campaign names for fundraising
campaign_names = ['Sea What We Can Do'
                 ,'Tidal Wave of Generosity'
                 ,'Mammoth Manatee Mission'
                 ,'Flippers for the Future'
                 ,'Save the Sea Potatoes'
                 ,'Gentle Giants, Huge Hearts'
                 ,'Drift with the Tide of Kindness'
                 ,'Manatee Mania Fundraiser'
                 ,'Blubbering for a Cause'
                 ,'Seagrass Saviors'
                 ,'Aquatic Angels'
                 ,'Swim Against the Current'
                 ,'Mangrove Moolah'
                 ,'Barnacle Buddies Unite'
                 ,'Ripple Effect for Manatees'
                 ,'Coastal Conservation Crusade'
                 ,'Marineland Miracles'
                 ,'Paddle for Preservation'
                 ,'Tusks and Trust'
                 ,'Buoyant Beings Benefit'
                 ,'Maritime Mammal Makers'
                 ,'Currents of Compassion'
                 ,'Waterway Watchers'
                 ,'Fins and Funds'
                 ,'Sea Cow Salvation'
                 ,'Less Musk More Tusk']

campaigns = generate_campaign_data(campaign_names, CAMPAIGN_TYPE, campaign_full = campaigns_eoy)

#Insert the reference data
insert_data(con, 'campaign', 'hfh', campaigns)

campaigns = select_data(con, 'campaign', 'hfh')

#Add a URL to the campaigns for logic
for c in campaigns:
    c.update({'campaign_url': FUNDRAISING_BASE_URL + c.get('campaign_name').lower().replace(' ','-')})
    
#Generate the fake sustaining donors
sustaining_donors = generate_fake_sustaining(supporter_ids, SUSTAINING_PCT)

#Insert the sustaining donor data
insert_data(con, 'sustaining_donation', 'hfh', sustaining_donors)

statuses = [s.get('donation_status') for s in select_data(con, 'donation_status', 'hfh')]

#Generate the donation records for sustaining donors
sustaining = select_data(con, 'sustaining_donation', 'hfh')

sustaining_donations = generate_fake_donation_sust(sustaining, campaigns, statuses)
#Insert the sustaining donor data
insert_data(con, 'donation', 'hfh', sustaining_donations)

#Generate the donation records for non-sustaining donors
donations = generate_fake_donation(supporter_ids, campaigns, statuses, DONOR_PCT)
#Insert the sustaining donor data
insert_data(con, 'donation', 'hfh', donations)