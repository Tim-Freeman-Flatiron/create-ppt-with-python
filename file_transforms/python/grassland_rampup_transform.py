import sys
import csv
import datetime

import glob

# with open("combined_grassland_ramp_up.csv", "wb") as outfile:
#     for f in read_files:
#         with open(f, "rb") as infile:
#             outfile.write(infile.read())


read_files = glob.glob("grassland_beef_ramp_up_data_files/*.csv")

with open('GB_transformed.csv', 'w') as out_file:
    # headers
    out_file.write(','.join(['email', 'opener_7_day', 'opener_30_day', 'opener_60_day', 'opener_90_day', 'opener_120_day', 'opener_180_day', 'opener_365_day']))
    out_file.write('\n')

    # engagement segments
    _7_day = ['True', 'True', 'True', 'True', 'True', 'True', 'True']
    _30_day = ['False', 'True', 'True', 'True', 'True', 'True', 'True']
    _60_day = ['False', 'False', 'True', 'True', 'True', 'True', 'True']
    _90_day = ['False', 'False', 'False', 'True', 'True', 'True', 'True']
    _120_day = ['False', 'False', 'False', 'False', 'True', 'True', 'True']
    _180_day = ['False', 'False', 'False', 'False', 'False', 'True', 'True']
    _365_day = ['False', 'False', 'False', 'False', 'False', 'False', 'True']
    non_engager = ['False', 'False', 'False', 'False', 'False', 'False', 'False']

    out_map = {}

    for file in read_files:
        reader = csv.reader(open(file, 'rU'))
        first_row = True
        for row in reader:
            if not first_row:
                email = row[email_index]
                if not email in out_map:
                    out_map[email] = {'email': email, 'engaged_date': ''}

                    # make engagement datetime
                    engagement_yyyy_mm_dd = row[-1].split(' ')[0]
                    split_engaged = engagement_yyyy_mm_dd.split('/')
                    engaged = datetime.date(int(split_engaged[2]), int(split_engaged[0]), int(split_engaged[1]))

                    out_map[email]['engaged_date'] = engaged
                else:
                    engagement_yyyy_mm_dd = row[-1].split(' ')[0]
                    split_engaged = engagement_yyyy_mm_dd.split('/')
                    engaged = datetime.date(int(split_engaged[2]), int(split_engaged[0]), int(split_engaged[1]))

                    if engaged > out_map[email]['engaged_date']:
                        print(engaged, out_map[email]['engaged_date'])
                        out_map[email]['engaged_date'] = engaged
            else:
                email_index = row.index('Email address - other')
                first_row = False

    # make today's datetime
    strf_today = datetime.datetime.today().strftime('%Y-%m-%d').split('-')
    today = datetime.date(int(strf_today[0]), int(strf_today[1]), int(strf_today[2]))

    for key in out_map:
        # determine difference in days
        diff = (today - out_map[key]['engaged_date']).days
        segment = _7_day if diff <= 7 else _30_day if diff <= 30 else _60_day if diff <= 60 else _90_day if diff <= 90 else _120_day if diff <= 120 else _180_day if diff <= 180 else _365_day if diff <= 365 else non_engager
        output = [key] + segment
        out_file.write(','.join(output))
        out_file.write('\n')
