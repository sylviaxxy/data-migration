import os
import psycopg2
import json
import csv
import datetime
import pandas as pd


def get_column_names(path='../data/2017-10-30.json'):
    with open(path, 'rb') as f:
        record_list = json.load(f)
        col_name_list = []
        for col_name in record_list['orders'][0].keys():
            col_name_list.append(col_name)
    return col_name_list

col_name_list = get_column_names('../data/2017-10-30.json')

def define_col_list():
    order_col_list = ["source_identifier",
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
                      "id", # is this order id ?
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
                      "order_number"]

    user_col_list = ["user_id",
                     "customer_locale",
                     "email",
                     "phone",
                     "name"]

    line_item_list = ["quantity",
                      "product_id",
                      "id",
                      "variant_id",
                      "order_id"]
    return order_col_list, user_col_list, line_item_list

order_col_list, user_col_list, line_item_list = define_col_list()


json_file_path_1 = '../data/2017-10-30.json'

def transform_file(json_file_path):
    order_df = pd.DataFrame(columns=order_col_list)
    user_df = pd.DataFrame(columns=user_col_list)
    line_item_df = pd.DataFrame(columns=line_item_list)
    with open(json_file_path, 'rb') as f:
        order_dict = json.load(f)
        for line in order_dict['orders']:
            order_new_row = {}
            for order_col in order_col_list:
                order_new_row[order_col] = line[order_col]
            order_df = order_df.append(order_new_row, ignore_index=True)

            user_new_row = {}
            for user_col in user_col_list:
                user_new_row[user_col] = line[user_col]
            user_df = user_df.append(user_new_row, ignore_index=True)

            for line_item_line in line['line_items']:
                line_item_new_row = {}
                for line_item_col in line_item_list[:-1]:
                    line_item_new_row[line_item_col] = line_item_line[line_item_col]
                line_item_new_row['order_id'] = line['id']
                line_item_df = line_item_df.append(line_item_new_row, ignore_index=True)
    return order_df, user_df, line_item_df

order_df, user_df, line_item_df = transform_file(json_file_path_1)

col_num = len(order_df.iloc[0,:])
s = "%s,"*(col_num-1) + "%s"
sql_query_templates = "INSERT INTO Orders ({0}) VALUES ({1})".format(','.join(order_col_list), s)
sql_query = sql_query_templates, tuple(order_df.values.tolist()[0])

conn = psycopg2.connect(host="localhost", database="business", user="insight", password="qwertyui123")
print("Database Connected")
cur = conn.cursor()
cur.execute(sql_query)
conn.commit()
conn.close()

#def write_file(order_df,user_df,line_item_df):
    #conn = psycopg2.connect(host="localhost", database="Business", user="insight", password="qwertyui123")
    #print("Database Connected")
    #cur = conn.cursor()
    #for i in len(order_df):
        #cur.execute("INSERT INTO Orders {col} VALUES {val}".format(col = ','.join(order_col_list, val = (order_df.iloc[i,:]))

    #conn.commit()
    #cur.close()
    #conn.close()
    #print ("Successfully write the df into Postgresql database.")

path = '../data'

def dump_directory(path):
    for file in os.listdir(path):
        if not file.startswith('.'):
            json_file_path = os.path.join(path, file)
            print("Now start to process all json files under data folder .", str(file))
            order_df, user_df, line_item_df = transform_file(json_file_path)
            write_file(order_df, user_df, line_item_df)
    print("All json files under the data folder has been migrated into Postgresql database.")

#dump_directory(path)