#!/usr/bin/env python3

import sys

'''
This Program will encode a message into a provide HTML text file

This will encode the message as spaces at the end of each line where a single
space is a space character, 2 spaces is a, 3 is b ...

As a result the longest message codable is equal to the number of lines in a
given HTML file.
'''

def whitespace(source, usrin):
    # define writable alphabet
    alph = 'abcdefghijklmnopqrstuvwxyz'
    mesg = ''

    # Sanitize User input to ensure only permitted characters are present
    usrin = filter(lambda x: True if x in alph else False, usrin)

    # Convert filter object to a string
    for x in usrin:
        mesg += x

    # Open source and destination files
    with open(source, 'r') as f_in, \
         open('encoded.html', 'w') as f_out:
        
        # Create Encoded Message Whitespace
        # If message is longer than HTML will only encode message until HTML
        # is depleted!
        i = 0

        for l in f_in:
            # Strip newline off end of each line in source HTML
            l = l.replace('\n', '')

            # replace line with line + whitespace
            try:
                # Encode the line with spaces
                f_out.write(f'{l}{" " * alph.index(mesg[i])}\n')
            except IndexError:
                # If HTML is longer than message simply return HTML after
                # message runs out
                f_out.write(f'{l}\n')
            i += 1
    
    return 0

if __name__ == '__main__':
    '''
    To use the program call it on the command line and provide 2 arguments.
    Argument 1 should be the path to the HTML file we will encode the message
    into. The second argument should be the message we will be encoding.

    Valid codable characters are lowercase letters a-z
    '''
    # TODO: Make the script match the file type of provided in file.
    #       This would allow for a user to provide any text file for encoding
    #       such as HTML, TXT, PY or C
    #
    #       This might be done by reverse seeking through the provided in file's
    #       name to search for a file extension and match that to the output
    #       file name
    #       
    #       NOTE: Update above comments to indicate generic files instead of
    #       HTML if this is done.
    whitespace(sys.argv[1], sys.argv[2].lower())