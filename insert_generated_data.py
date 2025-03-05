from db_connect import *
from generate_data import *
from pycountry import countries, languages, currencies

#Connect to the database
con = connect_db_engine()

#Create all the reference data
country_codes = [{'country_code': c.alpha_2
                  ,'country_name': c.name} for c in list(countries)]

language_codes = [{'language_code': c.alpha_3
                  ,'language_name': c.name} for c in list(languages)]

currency_codes = [{'currency_code': c.alpha_3
                  ,'currency_name': c.name} for c in list(currencies)]

campaign_types = [{'campaign_type_desc': 'Petition Signature Campaign'}
                  ,{'campaign_type_desc': 'Advocacy Campaign'}
                  ,{'campaign_type_desc': 'Fundraising Campaign'}
                  ,{'campaign_type_desc': 'Outreach Campaign'}
                  ,{'campaign_type_desc': 'Supporter Retention Campaign'}]

donation_status = [{'donation_status_desc': 'Donation pending'}
                   ,{'donation_status_desc': 'Donation completed and settled'}
                   ,{'donation_status_desc': 'Donation failed'}
                   ,{'donation_status_desc': 'Canceled refund pending'}
                   ,{'donation_status_desc': 'Canceled refund completed'}]

sustaining_status = [{'sustaining_status_desc': 'Active'}
                   ,{'sustaining_status_desc': 'Canceled by donor'}
                   ,{'sustaining_status_desc': 'Canceled due to payment expiration'}
                   ,{'sustaining_status_desc': 'Canceled due to duration'}]

#Insert the reference data
insert_data(con, 'country', 'hfh', country_codes)

insert_data(con, 'language', 'hfh', language_codes)

insert_data(con, 'local_currency', 'hfh', currency_codes)

insert_data(con, 'campaign_type', 'hfh', campaign_types)

insert_data(con, 'donation_status', 'hfh', donation_status)

insert_data(con, 'sustaining_status', 'hfh', sustaining_status)

#Generate the supporter data
supporters = generate_fake_supporters(nrecs = 10000)

#Insert the supporter data
insert_data(con, 'supporter', 'hfh', supporters)

#Select the supporter data to use the ids to generate email address data
supporters = select_data(con, 'supporter', 'hfh')

#Extract the first element (supporter_id) from the supporters database
supporter_ids = [s[0] for s in supporters]

#Generate the fake email_address data
emails = generate_fake_emails(supporter_ids)

#Insert the data into the email_address table
insert_data(con, 'email_address', 'hfh', emails)