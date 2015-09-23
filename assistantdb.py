#!/usr/bin/python3

import argparse, sys, webbrowser

parser = argparse.ArgumentParser()
parser.add_argument('verb', type=str, help='Assistant database command.')
parser.add_argument('verb_object', type=str, help='Object passed to command.')
parser.add_argument('-v', '--verbose',
                    help='Explain what action is being taken.',
                    action='store_true')
args = parser.parse_args()

browse_cmd_list = ['open', 'go to', 'browse to', 'launch', 'take me to']

if args.verbose:
    print(sys.version)
if args.verb in browse_cmd_list:
    # Open an indicated web page in the default browser
    site_name = args.verb_object.lower()
    if site_name in ['bannerweb', 'banner', 'registration', 'financial aid']:
        print('Opening BannerWeb...')
        webbrowser.open('https://www.ltu.edu/bannerweb')
    elif site_name in ['blackboard', 'bb']:
        print('Opening BlackBoard...')
        webbrowser.open('https://my.ltu.edu')
    elif site_name in ['ltu.edu', 'ltu website', 'ltu homepage']:
        print('Opening the main LTU website...')
        webbrowser.open('http://www.ltu.edu')
    elif site_name in ['email', 'webmail', 'mail', 'gmail']:
        print('Opening Gmail...')
        webbrowser.open('https://gmail.com')
    elif site_name in ['calendar', 'schedule', 'events']:
        print('Opening Google Calendar...')
        webbrowser.open('https://calendar.google.com')
    else:
        print('Opening website: ' + args.verb_object)
        webbrowser.open(args.verb_object)
else:
    print('Unrecognized verb; no action taken.')
exit()
