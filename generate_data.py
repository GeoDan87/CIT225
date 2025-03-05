from faker import Faker
import random
import uuid
import numpy as np

def generate_fake_supporters(nrecs = 10):
    Faker.seed(1)
    fake = Faker()
    i = 1
    #Set a arbitrary percentage 
    PCT = 0.2
    LOGIN_IDS = [fake.uuid4() for i in range(0, int(np.ceil(nrecs * PCT)))]
    
    data_list = []
    #Set the random seed to ensure consistency    
    random.seed(1)
    
    #Generate records as per the nrecs argument
    while i <= nrecs:
       
        #Create the dictionary of data
        data_dict = {
                     'first_name': fake.first_name()
                     ,'last_name': fake.last_name()
                     ,'login_id': uuid.UUID(random.choices([fake.uuid4()] + [random.choice(LOGIN_IDS)]
                                                           , weights = [1 - PCT, PCT], k = 1)[0])
                     ,'date_of_birth': fake.date_of_birth()
                     ,'country_code': fake.country_code()
                     }
        
        #Add the dictionary of data to the output list
        data_list.append(data_dict)
        
        #Add one to i to avoid an infinte loop
        i += 1
    
    return data_list

def generate_fake_emails(supporter_data, pct_dups = 0.1):
    DOI_PCT = 0.8 
    OO_PCT = 0.05
    
    Faker.seed(1)
    fake = Faker()
    
    data_list = []
    
    #Set the random seed to ensure consistency
    random.seed(1)
    #Generate records as per the nrecs argument
    for i, s in enumerate(supporter_data):
        
        #Create the dictionary of data
        data_dict = {
                      'supporter_id': s
                     ,'email_address': fake.safe_email()
                     ,'email_double_opt_in': random.choices([0,1] , weights = [1 - DOI_PCT, DOI_PCT])[0]
                     ,'email_opt_out': random.choices([0,1] , weights = [1 - OO_PCT, OO_PCT])[0]
                     }
        
        #Add the dictionary of data to the output list
        data_list.append(data_dict)
        
    for i in range(0, int(np.ceil(len(supporter_data) * pct_dups))):
                #Set the random seed to 1 after each iteration to ensure consistency
                
        #Create the dictionary of data
        data_dict = {
                      'supporter_id': random.choice(supporter_data)
                     ,'email_address': fake.safe_email()
                     ,'email_double_opt_in': random.choices([0,1] , weights = [1 - DOI_PCT, DOI_PCT])[0]
                     ,'email_opt_out': random.choices([0,1] , weights = [1 - OO_PCT, OO_PCT])[0]
                     }
    
        #Add the dictionary of data to the output list
        data_list.append(data_dict)

    return data_list