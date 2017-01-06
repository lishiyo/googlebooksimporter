# util functions
import json

def print_everything(*args):
    for count, thing in enumerate(args):
        print '{0}. {1}'.format(count, thing)

def table_things(**kwargs):
    for name, value in kwargs.items():
        print '{0} = {1}'.format(name, value)

# write to data.txt to see the response from the api
def writefile(data, filepath):
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4)
