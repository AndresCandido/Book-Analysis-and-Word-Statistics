#!/usr/bin/env python
#
import sys
import string
def readbook(filename, clean=True):
    ###
    """
    Reads a textfile into a single string, ignoring line breaks.
    The function has a single argument: the infile name
    and it returns a single string containing the whole file,
    removing end-of-line characters.
    
    if the variable clean is True then replace all upper case letters
    with lowercase and also remove ",;:-’
    """
    ###
    with open(filename, 'r') as myfile:
        data=myfile.read().replace('\n', ' ').replace('\r',' ').replace('\t',' ')
    #print(data)
    # remove the Gutenberg material as good as we can
    prolog = data.find("*** START")
    if prolog > -1:
        data = data[prolog:]
    epilog = data.find('End of the Project Gutenberg EBook')
    if epilog > -1:
        data = data[:epilog]
    epilog2 = data.find('*** END')
    if epilog2 > -1:
        data = data[:epilog2]
    #print(prolog,epilog,epilog2)
    if clean:
        printable = set(string.printable)
        data = ''.join(filter(lambda x: x in printable, data))
        data = data.replace(';',' ').replace(',',' ').replace(':',' ')
        data = data.replace('?','.').replace('!','.').replace(':','.')
        data = data.replace('-',' ').replace('"',' ').replace("'"," ").lower()        
    return data
#


if __name__ == '__main__':
    data = readbook(sys.argv[1],True)
    print(data)
