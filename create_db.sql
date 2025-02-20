DROP DATABASE IF EXISTS hfh;

CREATE DATABASE IF NOT EXISTS hfh;

CREATE TABLE IF NOT EXISTS
	hfh.supporter(supporter_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT
				 ,login_id UUID NOT NULL
				 ,first_name VARCHAR(255) NOT NULL
				 ,last_name VARCHAR(255)
				 ,date_of_birth DATE
				 ,country_code VARCHAR(2) #ISO3601 codes
				 ,create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
				 ,update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

CREATE TABLE IF NOT EXISTS
	hfh.email_address(email_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT
					  ,supporter_id INT UNSIGNED NOT NULL
					  ,email_address VARCHAR(320) #https://www.rfc-editor.org/rfc/rfc3696
					  ,email_double_opt_in TINYINT NOT NULL DEFAULT 0
					  ,email_opt_out TINYINT NOT NULL DEFAULT 0
					  ,create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
					  ,update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
					  ,CONSTRAINT `fk_supporter_email` FOREIGN KEY (supporter_id) REFERENCES hfh.supporter(supporter_id)
					   ON DELETE CASCADE
					   ON UPDATE RESTRICT);	

CREATE TABLE IF NOT EXISTS
	hfh.campaign(campaign_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT
				 ,campaign_type INT UNSIGNED
				 ,campaign_name VARCHAR(255)
				 ,campaign_start DATE
				 ,campaign_end DATE
				 ,create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
				 ,update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

CREATE TABLE IF NOT EXISTS
	hfh.petition(petition_id  INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT
				 ,supporter_id INT UNSIGNED NOT NULL
				 ,campaign_id INT UNSIGNED NOT NULL
				 ,petition_signed_date DATE
				 ,petition_url VARCHAR(2048) #Practical limit
				 ,create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
				 ,update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
				 ,CONSTRAINT `fk_campaign_petition` FOREIGN KEY (campaign_id) REFERENCES hfh.campaign(campaign_id)
				 ON DELETE CASCADE
				 ON UPDATE RESTRICT
				 ,CONSTRAINT `fk_supporter_petition` FOREIGN KEY (supporter_id) REFERENCES hfh.supporter(supporter_id)
				 ON DELETE CASCADE
				 ON UPDATE RESTRICT
				 #Prevent duplicative petition signatures
				 ,CONSTRAINT `unq_supporter_campaign` UNIQUE(supporter_id, campaign_id));

CREATE TABLE IF NOT EXISTS
	hfh.sustaining_donation(sustaining_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT
				 			,supporter_id INT UNSIGNED NOT NULL
							,sustaining_local_currency VARCHAR(3) NOT NULL# ISO4217
							,sustaining_local_amount DECIMAL
							,sustaining_start DATE
							,sustaining_end DATE
							,sustaining_status INT UNSIGNED NOT NULL DEFAULT 1
							,campaign_id INT UNSIGNED 
							,create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
							,update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
							,CONSTRAINT `fk_campaign_sustaining` FOREIGN KEY (campaign_id) REFERENCES hfh.campaign(campaign_id)
							ON DELETE CASCADE
							ON UPDATE RESTRICT
							,CONSTRAINT `fk_supporter_sustaining` FOREIGN KEY (supporter_id) REFERENCES hfh.supporter(supporter_id)
							ON DELETE CASCADE
							ON UPDATE RESTRICT);

CREATE TABLE IF NOT EXISTS
	hfh.donation(donation_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT
				 ,supporter_id INT UNSIGNED NOT NULL
				 ,donation_local_currency VARCHAR(3) NOT NULL# ISO4217
				 ,donation_local_amount DECIMAL
				 ,donation_usd_amount DECIMAL
				 ,donation_url VARCHAR(2048) #Practical limit
				 ,donation_date DATE
				 ,donation_status INT NOT NULL DEFAULT 1
				 ,campaign_id INT UNSIGNED
				 ,sustaining_id INT UNSIGNED
				 ,create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
				 ,update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
				 ,CONSTRAINT `fk_campaign_donation` FOREIGN KEY (campaign_id) REFERENCES hfh.campaign(campaign_id)
				 ON DELETE CASCADE
				 ON UPDATE RESTRICT
				 ,CONSTRAINT `fk_supporter_donation` FOREIGN KEY (supporter_id) REFERENCES hfh.supporter(supporter_id)
				 ON DELETE CASCADE
				 ON UPDATE RESTRICT
				,CONSTRAINT `fk_sustaining_donation` FOREIGN KEY (sustaining_id) REFERENCES hfh.sustaining_donation(sustaining_id)
				 ON DELETE CASCADE
				 ON UPDATE RESTRICT);

CREATE TABLE IF NOT EXISTS
	hfh.podcast_info(podcast_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT
					 ,podcast_name VARCHAR(255)
					 ,podcast_description VARCHAR(2000)
					 ,language_code  VARCHAR(3) #ISO 639-2 https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
					 ,podcast_start DATE
					 ,podcast_end DATE
					 ,create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
					 ,update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
									  
CREATE TABLE IF NOT EXISTS
	hfh.podcast_subscription(podcast_subscription_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT
							 ,podcast_id INT UNSIGNED NOT NULL
							 ,supporter_id INT UNSIGNED NOT NULL
							 ,podcast_subscribed_date DATE NOT NULL
							 ,language_code VARCHAR(3) #ISO 639-2 https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
							 ,create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
							 ,update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
							 ,CONSTRAINT `fk_podcast_podcastsub` FOREIGN KEY (podcast_id) REFERENCES hfh.podcast_info(podcast_id)
							  ON DELETE CASCADE
							  ON UPDATE RESTRICT
							 ,CONSTRAINT `fk_supporter_podcast` FOREIGN KEY (supporter_id) REFERENCES hfh.supporter(supporter_id)
							  ON DELETE CASCADE
							  ON UPDATE RESTRICT
							 /*Put a unique constraint on the combination of supporter
							   and newsletters to prevent duplicates by supporter.*/
							 ,CONSTRAINT `unq_supporter_podcast` UNIQUE (supporter_id, podcast_id));

CREATE TABLE IF NOT EXISTS
	hfh.newsletter_info(newsletter_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT
						,newsletter_name VARCHAR(100)
						,newsletter_description VARCHAR(2000)
						,newsletter_start DATE
						,newsletter_end DATE
						,create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
						,update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
									  
CREATE TABLE IF NOT EXISTS
	hfh.newsletter_subscription(newsletter_subscription_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT
							    ,email_id INT UNSIGNED NOT NULL
							    ,newsletter_id INT UNSIGNED NOT NULL
							    ,newsletter_url VARCHAR(2048) #Practical Limit
							    ,newsletter_subscribed TINYINT DEFAULT 1
							    ,newsletter_subscribed_date DATE NOT NULL
								,language_code VARCHAR(3) #ISO 639-2 https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
							    ,supporter_id INT UNSIGNED NOT NULL
							    ,create_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
							    ,update_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
							    ,CONSTRAINT `fk_newsletter_newslettersub` FOREIGN KEY (newsletter_id) REFERENCES hfh.newsletter_info(newsletter_id)
							     ON DELETE CASCADE
							     ON UPDATE RESTRICT
							    ,CONSTRAINT `fk_email_newsletter` FOREIGN KEY (email_id) REFERENCES hfh.email_address(email_id)
							     ON DELETE CASCADE
							     ON UPDATE RESTRICT
								 /*Put a unique constraint on the combination of emails
								 and newsletters to prevent duplicates by email.*/
								,CONSTRAINT `unq_email_newsletter` UNIQUE (email_id, newsletter_id));
										
