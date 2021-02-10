#!/usr/bin/python3

#Module required to use command line arguments
import argparse

#Create argument parser with description
parser = argparse.ArgumentParser(description='Log file parser for specific IP Address')
#Add --ip and -h/--help areguments to parser
parser.add_argument("--ip", required=True, type=str, help="Run script, with the following required argument, --ip <IP ADDRESS>")
#parse_args method. This will inspect the command line, convert each argument to the appropriate type and then invoke the appropriate action
args = parser.parse_args()
#Set ip to user input argument
ip = args.ip

#Create empty results list
search_results = []

#Open FULL LOGFILE PATH in 'read mode'. Absolute path given so the script can be run anywhere on the filesystem
with open(r'FULL LOGFILE PATH', 'r') as log:
    #Read each line in the file
    for line in log:
        #If ip in line, add ip and subsequent line to search_results list
        if ip in line:
            search_results.append((line))
            #Print search_results list
            print (search_results)