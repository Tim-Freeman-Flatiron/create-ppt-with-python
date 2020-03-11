import sys
import csv

print(sys.argv[1])
reader = csv.reader(open(sys.argv[1], 'rU'))

first_row = True
mapper = {}

for row in reader:
    if first_row:
        first_row = False
        pass
    else:
        namespace, old_segment_id, new_segment_id, old_cp_code, new_cp_code, old_tsd, new_tsd, comm_id = row
        print(namespace)

        if not mapper.get(namespace):
            mapper[namespace] = {}

        this_campaign = {}
        this_campaign['new_cp_code'] = new_cp_code
        this_campaign['old_tsd'] = old_tsd
        this_campaign['new_tsd'] = new_tsd
        this_campaign['old_segment_id'] = old_segment_id
        this_campaign['new_segment_id'] = new_segment_id
        this_campaign['comm_id'] = comm_id
        mapper[namespace][old_cp_code] = this_campaign
