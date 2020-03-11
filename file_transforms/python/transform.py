import sys
import csv
from datetime import datetime

firstRow = True

def make_str(val):
    return '"' + val + '"'

with open(sys.argv[2], 'wb') as out_file:
    # firstname,lastname,email,DCO_ID,opt in date,OPTOUT
    # emailaddress,firstname,lastname,url,dco,fromEmail,fromName,fromReply,optout
    # DCO_ID,Email
    # email,partner,OPTOUT,opt in date,DCO_ID
    for row in csv.DictReader(open(sys.argv[1],'rb')):
        try:
            if firstRow:
                firstRow = False
                # Email, Birthday, firstname, last modified date, lastname, last order date, my account, opt in date, opt in details, promo date, sp_click, sp_open, sp_sent, zipcode
                out_file.write(','.join(['email', 'birthday', 'first_name','last_modified_date', 'last_name', 'last_order_date', 'my_account', 'opt_in_date', 'opt_in_details', 'promo_date', 'sp_click', 'sp_open', 'sp_sent', 'zipcode']))
                out_file.write('\n')
            try:
                opted_out = row.get('Opted Out', '')
                if opted_out == 'F':
                    email = row.get('Email', '')
                    birthday = row.get('Birthday', '')
                    birthday = datetime.strptime(birthday, '%m/%d/%Y').isoformat() if birthday != '' else birthday
                    first_name = make_str(row.get('firstname', ''))
                    last_modified_date = row.get('Last Modified Date', '')
                    last_modified_date = datetime.strptime(last_modified_date, '%m/%d/%Y %I:%M %p').isoformat() if last_modified_date != '' else last_modified_date
                    last_name = make_str(row.get('LASTNAME', ''))
                    last_order_date = row.get('LastOrderDate', '')
                    last_order_date = datetime.strptime(last_order_date, '%m/%d/%Y').isoformat() if last_order_date != '' else last_order_date
                    my_account = row.get('MYACCOUNT', '')
                    opt_in_date = row.get('Opt In Date', '')
                    opt_in_date = datetime.strptime(opt_in_date,  '%m/%d/%Y %I:%M %p').isoformat() if opt_in_date != '' else opt_in_date
                    opt_in_details = make_str(row.get('Opt In Details', ''))
                    promo_date = row.get('promodate', '')
                    promo_date = datetime.strptime(promo_date, '%m/%d/%Y').isoformat() if promo_date != '' else promo_date
                    sp_click = row.get('SP_Click', '')
                    sp_click = datetime.strptime(sp_click, '%m/%d/%Y').isoformat() if sp_click != '' else sp_click
                    sp_open = row.get('SP_Open', '')
                    sp_open = datetime.strptime(sp_open, '%m/%d/%Y').isoformat() if sp_open != '' else sp_open
                    sp_sent = row.get('SP_Sent', '')
                    sp_sent = datetime.strptime(sp_sent, '%m/%d/%Y').isoformat() if sp_sent != '' else sp_sent
                    zipcode = make_str(row.get('zipcode', ''))

                    out_file.write(','.join([email,birthday,first_name,last_modified_date,last_name,last_order_date,my_account,opt_in_date,opt_in_details,promo_date,sp_click,sp_open,sp_sent,zipcode]))
                    out_file.write('\n')
            except Exception as e:
                print(e)
                pass
        except:
            pass



# # test that file is normal csv and can be handled without transformation
# import sys
# import csv
# import urllib

# firstRow = True
# cp_index = None

# with open(sys.argv[2], 'wb') as out_file:
#     for row in csv.reader(open(sys.argv[1],'rb')):
#         try:
#             if firstRow:
#                 firstRow = False
#                 out_file.write(','.join(row))
#                 out_file.write('\n')
#                 cp_index = row.index('cp_cd')
#             else:
#                 try:
#                     row[cp_index] = urllib.unquote(row[cp_index])
#                     out_file.write(','.join(row))
#                     out_file.write('\n')
#                 except:
#                     print('errored')
#                     out_file.write(','.join(row))
#                     out_file.write('\n')
#         except:
#             pass

# import sys
# import csv

# csv.field_size_limit(sys.maxsize)

# reader = csv.reader(open(sys.argv[1],'rb'))
# first_row = True
# # row_objects = dict()

# with open(sys.argv[2], 'w') as out_file:
#     for row in reader:
#         if first_row:
#             out_file.write(','.join(['order_id', 'email', 'total', 'created', 'product_ids']))
#             out_file.write('\n')
#             first_row = False
#         else:
#             product_ids = []
#             for pid in row[5].split('|'):
#                 product_ids.append(pid.split('-')[0] + '-' + row[1])
#             out_file.write(','.join([row[0], row[2], row[3], row[4], '|'.join(product_ids)]))
#             out_file.write('\n')
#             key = str(row[1])
#             if key not in row_objects.keys():
#                 row_objects[key] = row
#                 row_objects[key][3] = float(row[3])
#             else:
#                 current_ids = row_objects.get(key)[2]
#                 row_objects[key][2] = current_ids + '|' + row[2] if not row[2] == 'GIFTCARD' else current_ids
#                 row_objects[key][3] += float(row[3])
#     for key, value in row_objects.items():
#         row_objects[key][3] = str(row_objects[key][3])
#         split_ids = row_objects[key][2].split('GIFTCARD|')
#         row_objects[key][2] = split_ids[1] if len(split_ids) == 2 else row_objects[key][2]
#         out_file.write(','.join(row_objects[key]))
#         out_file.write('\n')


# import sys
# import csv

# reader = csv.reader(open(sys.argv[1], 'rU'))
# first_row = True

# with open(sys.argv[2], 'w') as out_file:
#     for row in reader:
#         if first_row:
#             out_file.write('product_id')
#             out_file.write('\n')
#             first_row = False
#         else:
#             try:
#                 prod_id = row[5].split('-')[0]
#                 if prod_id:
#                     country = row[8]
#                     if country:
#                         prod_id = prod_id + '-' + country
#                     out_file.write(prod_id)
#                     out_file.write('\n')
#             except:
#                 pass
# # import csv
# # # import hashlib
# # # # import datetime

# # reader = csv.reader(open(sys.argv[1], 'rU'))
# # first_row = True
# # second_row = True

# # with open(sys.argv[2], 'w') as out_file:
# #     row_objects = {}
# #     for row in reader:
# #         if first_row:
# #             out_file.write(','.join(["id", "out_of_stock"]))
# #             out_file.write('\n')
# #             first_row = False
# #         else:
# #             product_id = row[0]
# #             if not row_objects.get(product_id, None):
# #                 row_objects[product_id] = [product_id, row[1]]
# #             else:
# #                 if row[1] != "out of stock":
# #                     row_objects[product_id][1] = row[1]
# #     for key, value in row_objects.items():
# #         out_file.write(','.join(row_objects[key]))
# #         out_file.write('\n')







#     # for row in reader:
#     #     if first_row:
#     #         out_file.write(','.join(row))
#     #         out_file.write('\n')
#     #         first_row = False
#     #     else:
#     #         # OSIS,last_name,first_name,grade_level,home_room,full_name,group,advisory,locker
#     #         if not row_objects.get(row[0], None):
#     #             row_objects[row[0]] = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
#     #         else:
#     #             student = row_objects.get(row[0], None)
#     #             for i in range(len(student)):
#     #                 if (not student[i] or student[i] == '') and not row[i] == '':
#     #                     student[i] = row[i]
#     #             row_objects[row[0]] = student
#     # for key, value in row_objects.items():
#     #     out_file.write(','.join(row_objects[key]))
#     #     out_file.write('\n')

#     # row_objects = {}
#     # out_file.write(','.join(['name', 'category', 'id', 'url', 'image', 'price', 'oos', 'artist_country', 'artist_id', 'artist_name', 'sa_cs', 'date_uploaded']))
#     # out_file.write('\n')
#     # first_row = False
#     # for row in reader:
#     #     prod_id = row[2].strip()
#     #     if not row_objects.get(prod_id, None):
#     #         try:
#     #             row[5] = (float(row[5]) / 100)
#     #         except:
#     #             row[5] = -1
#     #         row[0] = '"' + row[0] + '"' if ',' in row[0] else row[0]
#     #         row[9] = '"' + row[9] + '"' if ',' in row[9] else row[9]
#     #         prod = [row[0].strip(), row[1].strip(), prod_id, row[3].strip(), row[4], str(row[5]), str((False if row[6] == 'avail' else True)), row[7], row[8], row[9], row[10], datetime.datetime.fromtimestamp(int(row[11])).strftime('%Y-%m-%d %H:%M:%S')]
#     #         row_objects[prod_id] = prod
#     # for key, value in row_objects.items():
#     #     out_file.write(','.join(row_objects[key]))
#     #     out_file.write('\n')

#     # for row in reader:
#     #     if first_row:
#     #         out_file.write(','.join(['order_id', 'email', 'product_ids', 'total', 'created']))
#     #         out_file.write('\n')
#     #         first_row = False
#     #     else:
#     #         order = row[0]
#     #         if not row_objects.get(order, None):
#     #             row_objects[order] = [order, row[2], row[6], float(row[4]), row[3]]
#     #         else:
#     #             current_ids = row_objects[order][2]
#     #             row_objects[order][2] = current_ids + '|' + row[6]
#     #             row_objects[order][3] += float(row[4])
#     # for key, value in row_objects.items():
#     #     row_objects[key][3] = str(row_objects[key][3])
#     #     out_file.write(','.join(row_objects[key]))
#     #     out_file.write('\n')

# # add \r\n for {CR}{LF} row delimiter for windows
# import sys
# import csv

# firstLine = True

# with open(sys.argv[2], 'wb') as out_file:
#     for row in csv.reader(open(sys.argv[1], 'rU')):
#         if firstLine:
#             firstLine = False
#             continue
#         else:
#             try:
#                 out_file.write(row[0] + '\r\n')
#             except:
#                 pass


# # to eliminate carriage returns
# import sys
# import csv
# import codecs

# with open(sys.argv[2], 'wb') as out_file:
#     for row in csv.reader(codecs.open(sys.argv[1], 'rU', 'utf-16')):
#         try:
#             out_file.write(row[0] + '\n')
#         except:
#             pass

# import sys
# import csv
# # import os

# # csv.field_size_limit(sys.maxsize)
# kwargs = dict(delimiter=",")
# kwargs.update(quoting=csv.QUOTE_NONE)

# reader = csv.reader(open(sys.argv[1]), **kwargs)
# outfile = sys.argv[2]

# with open(outfile, "w") as out:
#     for idx, line in enumerate(reader):
#         # previous = None
#         if "adelaida" in line:
#             print(line)
#         # for value in line:
#         #     if len(value) > 131072:
#         #         out.write(value)
#         #         out.write('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
#         #         print('found')
#             #     print('previous --> {}'.format(previous))
#             # previous = value
