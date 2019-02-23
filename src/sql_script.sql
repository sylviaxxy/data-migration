CREATE ROLE insight WITH LOGIN PASSWORD 'qwertyui123';
ALTER ROLE insight CREATEDB;

psql postgres -U insight

CREATE DATABASE business;

CREATE TABLE Orders(
   "source_identifier",
   "subtotal_price",
   "buyer_accepts_marketing",
   "reference",
   "cart_token",
   "updated_at",
   "taxes_included",
   "currency",
   "total_weight",
   "source_name",
   "processed_at",
   "closed_at",
   "location_id",
   "gateway",
   "confirmed",
   "user_id",
   "tags",
   "total_price_usd",
   "financial_status",
   "id",
   "note",
   "landing_site",
   "processing_method",
   "total_line_items_price",
   "cancelled_at",
   "test",
   "app_id",
   "total_tax",
   "cancel_reason",
   "total_discount",
   "landing_site_ref",
   "number",
   "total_discounts",
   "checkout_id",
   "source_url",
   "browser_ip",
   "device_id",
   "referring_site",
   "total_price",
   "checkout_token",
   "created_at",
   "fulfillment_status",
   "token",
   "contact_email",
   "order_status_url",
   "order_number",
   PRIMARY KEY( one or more columns )
);

CREATE TABLE Users(
   "user_id",
   "customer_locale",
   "email",
   "phone",
   "name",
   PRIMARY KEY( one or more columns )
);


CREATE TABLE Line_items(
   "quantity",
   "product_id",
   "id",
   "variant_id",
   "order_id",
   PRIMARY KEY( one or more columns )
);
