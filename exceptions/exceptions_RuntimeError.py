#!/usr/bin/env python

import sys

def throws():
    print 'Starting throws()'
    raise RuntimeError('this is the error message')

def do_some_stuff():
    print "Doing some stuff..."
    try:
        print "...doing some stuff without error"
        print "... an error appear!"
        error = False        
        if error:
            throws()
    except Exception, e:
        print "Caught exception. Cleanup after exception occurs."
        # raise e   # if this is raised, the exception will be caught on the next except
    else:
        print "The error disappeared. Finish stuff."
    finally:
        print "Finally: do what must be done no matter which error appeared."        

def main():
    try:
        try:
            do_some_stuff()
            error = False
            if error:
                throws()
            # return 0  # if return 0 is here, else does not occurs
        except Exception, err:
            print 'Caught an exception'
            return 1
        else:
            print "No exception occurred"
    finally:
        print 'In finally block for cleanup'

if __name__ == '__main__':
    sys.exit(main())