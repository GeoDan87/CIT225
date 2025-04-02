CREATE TABLE hfh.donation_audit (donation_audit_id INT(10) UNSIGNED PRIMARY KEY AUTO_INCREMENT
											,donation_id INT(10) UNSIGNED
											,donation_status INT(10) UNSIGNED NOT NULL
											,create_timestamp TIMESTAMP NULL DEFAULT current_timestamp()
											,update_timestamp TIMESTAMP NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
											,CONSTRAINT `fk_donation_audit_status` FOREIGN KEY (`donation_status`) REFERENCES hfh.donation_status(`donation_status`) ON UPDATE RESTRICT ON DELETE CASCADE
											,CONSTRAINT `fk_donation_id` FOREIGN KEY (donation_id) REFERENCES hfh.donation(donation_id) ON UPDATE RESTRICT ON DELETE CASCADE);

DELIMITER $$
CREATE OR REPLACE TRIGGER hfh.trg_au_donation
	AFTER UPDATE ON hfh.donation
	FOR EACH ROW
	BEGIN
		IF (OLD.donation_status != NEW.donation_status) THEN
			INSERT INTO hfh.donation_audit(donation_id, donation_status)
				VALUES(OLD.donation_id, OLD.donation_status);
		END IF;
	END;$$
	
DELIMITER ;