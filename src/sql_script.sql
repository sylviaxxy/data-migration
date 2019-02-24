CREATE ROLE insight WITH LOGIN PASSWORD 'qwertyui123';
ALTER ROLE insight CREATEDB;

psql postgres -U insight

CREATE DATABASE business;

CREATE TABLE orders(
   source_identifier TEXT,
   subtotal_price NUMERIC,
   buyer_accepts_marketing BOOLEAN,
   reference TEXT,
   cart_token TEXT,
   updated_at TIMESTAMP,
   taxes_included BOOLEAN,
   currency TEXT,
   total_weight NUMERIC,
   source_name TEXT,
   processed_at TIMESTAMP,
   closed_at TIMESTAMP,
   location_id TEXT,
   gateway TEXT,
   confirmed BOOLEAN,
   user_id TEXT,
   tags TEXT,
   total_price_usd NUMERIC,
   financial_status TEXT,
   id TEXT,
   note TEXT,
   landing_site TEXT,
   processing_method TEXT,
   total_line_items_price NUMERIC,
   cancelled_at TIMESTAMP,
   test BOOLEAN,
   app_id TEXT,
   total_tax NUMERIC,
   cancel_reason TEXT,
   total_discount NUMERIC,
   landing_site_ref TEXT,
   number TEXT,
   total_discounts NUMERIC,
   checkout_id TEXT,
   source_url TEXT,
   browser_ip TEXT,
   device_id TEXT,
   referring_site TEXT,
   total_price NUMERIC,
   checkout_token TEXT,
   created_at TIMESTAMP ,
   fulfillment_status TEXT,
   token TEXT,
   contact_email TEXT,
   order_status_url TEXT,
   order_number TEXT
);

CREATE TABLE users(
   user_id TEXT,
   customer_locale TEXT,
   email TEXT,
   phone TEXT,
   name TEXT
);


CREATE TABLE line_items(
   quantity INTEGER,
   product_id TEXT,
   id TEXT,
   variant_id TEXT,
   order_id TEXT
);

