CREATE DATABASE dbcw;

USE dbcw;

CREATE TABLE transactionals_data
(
transaction_id INT NOT NULL,
merchant_id INT NOT NULL,
user_id INT NOT NULL,
card_number VARCHAR(255) NOT NULL,
transaction_date DATETIME NOT NULL,
transaction_amount DECIMAL(12,2) NOT NULL,
device_id VARCHAR(255) NOT NULL,
has_cbk CHAR(5) NOT NULL,
PRIMARY KEY (transaction_id)
)
