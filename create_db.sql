CREATE DATABASE hfh;

CREATE TABLE hfh.supporter(supporter_id INT PRIMARY KEY AUTO_INCREMENT
						   ,login_id UUID NOT NULL
						   ,first_name VARCHAR(255) NOT NULL
						   ,last_name VARCHAR(255)
						   ,date_of_birth DATE
						   ,country VARCHAR(3)
						   ,create_timestamp TIMESTAMP DEFAULT
						   ,update_timestamp TIMESTAMP NULL ON UPDATE CURRENT_TIMESTAMP);

CREATE TABLE hfh.campaign(campaign_id INT PRIMARY KEY AUTO_INCREMENT
						  ,campaign_type INT
						  ,campaign_name VARCHAR(255)
						  ,campaign_start DATE
						  ,campaign_end DATE
						  ,create_timestamp TIMESTAMP DEFAULT
						  ,update_timestamp TIMESTAMP NULL ON UPDATE NOW());

CREATE TABLE hfh.petition(petition_id INT PRIMARY KEY AUTO_INCREMENT
						  ,supporter_id INT
						  ,campaign_id INT
						  ,signed BOOLEAN
						  ,signed_date DATE
						  ,create_timestamp TIMESTAMP DEFAULT
						  ,update_timestamp TIMESTAMP NULL ON UPDATE NOW()
						  ,CONSTRAINT `fk_campaign_petition` FOREIGN KEY (campaign_id) REFERENCES campaign(campaign_id)
    					   ON DELETE CASCADE
    					   ON UPDATE RESTRICT
						  ,CONSTRAINT `fk_supporter_petition` FOREIGN KEY (supporter_id) REFERENCES supporter(supporter_id)
    					   ON DELETE CASCADE
    					   ON UPDATE RESTRICT);


CREATE TABLE hfh.donation(donation_id INT PRIMARY KEY AUTO_INCREMENT
						  ,supporter_id INT NOT NULL FOREIGN KEY REFERNCES hfh.supporter(supporter_id)
						  ,donation_local_currency VARCHAR(3)
						  ,donation_local_amount DECIMAL
						  ,donation_usd_amount DECIMAL
						  ,donation_source VARCHAR(4000)
						  ,donation_date DATE
						  ,donation_status INT
						  ,campaign_id INT
						  ,create_timestamp TIMESTAMP DEFAULT
						  ,update_timestamp TIMESTAMP NULL ON UPDATE NOW()
						  ,CONSTRAINT `fk_campaign_donation` FOREIGN KEY (campaign_id) REFERENCES campaign(campaign_id)
    					   ON DELETE CASCADE
    					   ON UPDATE RESTRICT
						  ,CONSTRAINT `fk_supporter_donation` FOREIGN KEY (supporter_id) REFERENCES supporter(supporter_id)
    					   ON DELETE CASCADE
    					   ON UPDATE RESTRICT);

CREATE TABLE hfh.podcast_info(podcast_id INT PRIMARY KEY AUTO_INCREMENT
							  ,podcast_name VARCHAR(255)
							  ,podcast_description VARCHAR(2000)
							  ,podcast_start DATE
							  ,podcast_end DATE
							  ,create_timestamp TIMESTAMP DEFAULT
							  ,update_timestamp TIMESTAMP NULL ON UPDATE NOW());
									  
CREATE TABLE hfh.podcast_subscription(podcast_subscription_id INT PRIMARY KEY
									  ,podcast_id INT
									  ,supporter_id INT NOT NULL FOREIGN KEY REFERNCES hfh.supporter(supporter_id)
									  ,create_timestamp TIMESTAMP DEFAULT
									  ,update_timestamp TIMESTAMP NULL ON UPDATE NOW()
									  ,CONSTRAINT `fk_podcast_podcastsub` FOREIGN KEY (podcast_id) REFERENCES podcast(podcast_id)
    					   		   	   ON DELETE CASCADE
    					   		   	   ON UPDATE RESTRICT
						  		  	  ,CONSTRAINT `fk_supporter_podcast` FOREIGN KEY (supporter_id) REFERENCES supporter(supporter_id)
    					   		   	   ON DELETE CASCADE
    					   		       ON UPDATE RESTRICT);
										
