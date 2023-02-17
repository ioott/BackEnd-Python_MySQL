CREATE DATABASE dbcw;

CREATE TABLE transactionals_data (
  transaction_id VARCHAR(255) NOT NULL,
  merchant_id VARCHAR(255) NOT NULL,
  user_id VARCHAR(255) NOT NULL,
  card_number VARCHAR(255) NOT NULL,
  transaction_date DATE NOT NULL,
  transaction_amount FLOAT NOT NULL,
  device_id VARCHAR(255) NOT NULL,
  has_cbk BOOL NOT NULL,
  PRIMARY KEY (transaction_id)
);
