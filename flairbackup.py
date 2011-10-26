#!/usr/bin/python

"""Tool for backing up user flair on reddit with a local CSV file

This script outputs a simple CSV file containing a subreddits flair

Example:
$ ./flairbackup.py FFFFFFFUUUUUUUUUUUU f7u12backup.csv
reddit username: Paradox
reddit password: 
Writing flair to CSV file f7u12backup.csv at 7:53:27 PM
Done! Took 0:02:34

"""

import argparse
import csv
import redditclient
import time
import datetime

def parse_args():
    parser = argparse.ArgumentParser(description='backup subreddit flair to CSV')

    parser.add_argument('subreddit', metavar='SUBREDDIT')
    parser.add_argument('csvfile', metavar='CSVFILE')
    
    parser.add_argument('-b', '--batch_size', type=int, default=100,
                        help='number of users to read at a time from the site')
    return parser.parse_args()


def user_flair_to_csv(path, client, config):
    starttime = time.time()
    print 'Writing flair to CSV file "{}" at {start}'.format(config.csvfile, start = time.strftime('%I:%M:%S %p') )    
    c = csv.writer(open(path, 'wb'))
    # write a header
    c.writerow(['user', 'text', 'css'])
    for r in client.flair_list(config.subreddit, config.batch_size):
        c.writerow()
    elapsed = time.time() - starttime
    print 'Done! Took {}'.format(datetime.timedelta(seconds=elapsed))

def main():
    config = parse_args()

    client = redditclient.RedditClient()
    # Prompts user for login
    client.log_in()

    return user_flair_to_csv(config.csvfile, client, config)

if __name__ == '__main__':
    main()
