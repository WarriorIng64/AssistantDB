#!/usr/bin/python3

import argparse
import subprocess
import sys
import webbrowser

def speak(message, also_cmd=False):
    '''Speak the given message using the text-to-speech backend.'''
    if also_cmd:
        print(message)
    subprocess.call('espeak "' + message + '"', shell=True)

parser = argparse.ArgumentParser()
parser.add_argument('verb', type=str, help='Assistant database command.')
parser.add_argument('verb_object', type=str, help='Object passed to command.')
parser.add_argument('-v', '--verbose',
                    help='Explain what action is being taken.',
                    action='store_true')
args = parser.parse_args()

browse_cmd_list = ['open', 'go to', 'browse to', 'launch', 'take me to']
email_cmd_list = ['email', 'compose', 'send']

if args.verbose:
    print(sys.version)
if args.verb in browse_cmd_list:
    # Open an indicated web page in the default browser
    site_name = args.verb_object.lower()
    if site_name in ['bannerweb', 'banner', 'registration', 'financial aid']:
        speak('Opening BannerWeb...', args.verbose)
        webbrowser.open('https://www.ltu.edu/bannerweb')
    elif site_name in ['blackboard', 'bb']:
        speak('Opening BlackBoard...', args.verbose)
        webbrowser.open('https://my.ltu.edu')
    elif site_name in ['ltu.edu', 'ltu website', 'ltu homepage']:
        speak('Opening the main LTU website...', args.verbose)
        webbrowser.open('http://www.ltu.edu')
    elif site_name in ['email', 'webmail', 'mail', 'gmail']:
        speak('Opening Gmail...', args.verbose)
        webbrowser.open('https://gmail.com')
    elif site_name in ['calendar', 'schedule', 'events']:
        speak('Opening Google Calendar...', args.verbose)
        webbrowser.open('https://calendar.google.com')
    else:
        speak('Opening website: ' + args.verb_object, args.verbose)
        webbrowser.open(args.verb_object)
elif args.verb in email_cmd_list:
    # Open a window to compose an email
    if args.verb_object:
        recipient = 'mailto:' + args.verb_object  # Open default email client
    else:
        recipient = 'https://mail.google.com/mail/u/0/#compose' # Gmail
    speak('Composing an email...', args.verbose)
    webbrowser.open(recipient)
else:
    speak('Sorry, I don\'t understand what you want.', args.verbose)
exit()
