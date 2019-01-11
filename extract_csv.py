import csv
from connection import ElementsConnection
from datetime import datetime
import os

import argparse

def main(user, password, filename):
    my_con = ElementsConnection(user, password)
    file_exists = os.path.isfile(filename)
    myfile = open(filename, mode='a')
    my_csv = csv.DictWriter(myfile, ['date', 'name', 'type', 'etat', 'temperature', 'pressure', 'relay', 'humidity', 'smokeDetected'], delimiter=';', lineterminator='\n')    
    if not file_exists:
        my_csv.writeheader()
    my_date = datetime.now()
    for asensor in my_con._get_sensors_states():
        asensor['date'] = my_date.strftime('%Y-%m-%d %H:%M:%S')
        my_csv.writerow(asensor)
    myfile.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get GigasetElements Sensor values')
    parser.add_argument('-u', '--username', metavar='username', type=str, nargs=1, required=True,
                    help='Gigaset Elements Username')
    parser.add_argument('-p', '--password', metavar='password', type=str, nargs=1, required=True,
                    help='Gigaset Elements password')                    
    parser.add_argument('-f', '--filename', metavar='filename', type=str, nargs=1, default='output.csv',
                    help='File to store values')
    args = parser.parse_args()
    main(args.username, args.password, args.filename)    