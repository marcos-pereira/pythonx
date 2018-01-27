import sys
import getopt

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg
        print "help usage"   

def do_stuff():
    status = False
    print "my_function status = "
    print status    

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            # The ":" after the each letter enable arguments
            # For example "s:" will enable the use of arguments for the option "s"
            # The typed arguments will be stored in the arg variable
            # To use the opt as "--opt" plus args, add "opt=" with the equal sign
            opts, args = getopt.getopt(argv[1:], "hs:o:vi:", ["help", "output=", "verbose", "version","superuser=", "input="])   
            do_stuff()

            print 'OPTIONS   :', opts

            for opt, arg in opts:
                if opt in ('-o', '--output'):   # if the opt "-o" is used
                    print "opt ="
                    print opt
                    print "arg ="
                    print arg
                elif opt in ('-v', '--verbose'): # if the opt "-v" is used
                    verbose = True
                    print "verbose = " + str(verbose);
                elif opt == '--version':        # if the opt "--version" is used
                    version = arg
                elif opt in ('-h','--help'):
                    print "opt ="
                    print opt
                    print "arg ="
                    print arg
                elif opt in ('-s','--superuser'):
                    print "opt ="
                    print opt
                    print "arg ="
                    print arg
                elif opt in ('-i','--input'):
                    print "opt ="
                    print opt
                    print "arg ="
                    print arg

        except getopt.error, msg:
             raise Usage(msg)
        # more code, unchanged
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())