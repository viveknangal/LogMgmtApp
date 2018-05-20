#!/usr/local/bin/python
from prettytable import PrettyTable
import requests
import csv
import json
import logging
import sys

# Global Variables
github_api='https://api.github.com/repos/'
output_file="repo_details.csv"
all_repo_entries=[]

# Function to validate the command line arguments
def env_variables():
	if len(sys.argv) >2:
		input_file_name=sys.argv[1]
		output_file_name=sys.argv[2]
		# Invoke the function to read the input file contents having GitHub details
		read_file(input_file_name,output_file_name)
	else:
		logging.error('......Please provide file as an Input......')
		sys.exit(1)
	
# Function to read the Input file having the Repo details for which information need to be fetched
def read_file(input_file_name,output_file_name):
	# Initialize TABLE object for displaying output on STDOUT in tabular format
	table = PrettyTable(['Repo_Name', 'Clone URL','Date of Latest Commit','Author'])
	# Access File object which has Repository Details
	repo_list = open("/app/"+input_file_name) 
	# Iterating over the File Object
	for repo_name in repo_list:
		fetch_repo_details(repo_name.strip(),table)
	# Printing Data in tabular format for STDOUT
	print table
	# Writing Data to CSV file
	write_file(all_repo_entries,output_file_name)

# Function for writing data to CSV format file
def write_file(all_repo_entries,output_file_name):
	f = open("/app/"+output_file_name, 'w')
	with f:
		writer = csv.writer(f)
		for row in all_repo_entries:
			writer.writerow(row)
        print "CSV format output file=",output_file_name

# Function for fetching GITHUB Repo metadata using REST API
def fetch_repo_details(repo_name,table):
	# Dynamically creating a GITHUB URL
	repo_link=github_api+repo_name
	# Access the GITHUB REST API for accessing REPOSITORY information
	repos = requests.get(repo_link)
	repo_json = json.loads(repos.text)
	# Condition to check if there are any errors returned in JSON
	if 'message' in repo_json:
		logging.error(repo_json['message']+">>"+repo_link)
	else:
	# Fetches the REPO NAME and CLONE URL attributes
		repo_name=repo_json['name']
		clone_url=repo_json['clone_url']

	# Access the GITHUB REST API for accessing COMMITS information
		commits = requests.get(repo_link+'/commits')
		commit_json = json.loads(commits.text)
	# Fetches the AUTHOR & COMMIT DATE attribute
		author_name=commit_json[0]['commit']['author']['name']
		commit_date=commit_json[0]['commit']['author']['date']
	# This adds a  row to a Table object
		table.add_row([repo_name,clone_url,commit_date,author_name])
		repo_data=[]
		repo_data.append(repo_name)
		repo_data.append(clone_url)
		repo_data.append(commit_date)
		repo_data.append(author_name)
		all_repo_entries.append(repo_data)
		
if __name__ == '__main__':
	try:
		# Initializing the Logger Object
		logging.basicConfig(level=logging.INFO)
		logging.info('......Program Started......')
		# Invoking read_file function
		env_variables()
	except Exception as e:
		logging.error('......Exception Occured......')
		print e
