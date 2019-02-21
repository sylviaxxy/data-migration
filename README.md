# Data Migration



# Introduction

Imagine a scenario where you were given the task create an ETL (Extract, Transform, Load) so that API data is consumable by 
business analysts. Fortunately, your co-workers have already done the Extract step and has provided you with a .zip file 
containing retail order data in the raw JSON format. Your project manager has put you on the task to support these business 
analysts so that they can query that data using SQL from a PSQL database. While you’re at it, they would also want you to 
create a user table that would contain summary metrics that you think business analysts would find useful.
Note: Keep in mind that the newly created tables have to be sanely structured and those steps should be reproducible with 
the expectation that the ETL would run daily.

# Approach


# Output

## Postgres database with the following tables:
- One table for the orders data 
- One table user data saved 

# Schema

# How to start

