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
roomfinder_cmd_list = ['find', 'find room', 'where is room']

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
elif args.verb in roomfinder_cmd_list:
    # Tell the user which building and floor a room is in
    finder_message = ''
    if args.verb_object:
        if len(args.verb_object) >= 2:
            room_letter = args.verb_object.upper()[0]
            room_floor = args.verb_object.upper()[1]
            building_dict = {'A': 'Architecture Building',
                             'B': 'Business Services Building',
                             'C': 'A. Alfred Taubman Student Services Center',
                             'D': 'Art and Design Center',
                             'F': 'CIMR Building',
                             'E': 'Engineering Building',
                             'R': 'Ridler Field House and Applied Research Center',
                             'M': 'Wayne H. Buell Management Building',
                             'S': 'Arts and Sciences Building',
                             'T': 'University Technology and Learning Center'
                            }
            if room_letter in building_dict.keys():
                building = building_dict[room_letter]
            else:
                building = ''

            if building != '':
                finder_message = 'Your room is in the ' + building + ' on floor ' + room_floor + '.'
            else:
                finder_message = 'Sorry, I don\'t know which building that is.'
        else:
            finder_message = 'Sorry, but I don\'t think that\'s a valid room number.'
    else:
        finder_message = 'Sorry, but I don\'t think you told me which room you want.'
    speak(finder_message, args.verbose)
else:
    speak('Sorry, I don\'t understand what you want.', args.verbose)
exit()
