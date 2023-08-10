-- Creates the user table with id, email,
-- name and country attributes.
-- country is an enumeration with 'US' set as default
CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country enum('US', 'CO', 'TN') NOT NULL DEFAULT 'US' 
);
