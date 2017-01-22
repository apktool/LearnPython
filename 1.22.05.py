# 解析命令行的简单实现

import getopt,sys

def usage():
    print('Usage about this file')
    print(' \n option:  -h help \
            \n          -o output \
        ')

def main():
    try:
        opts,args=getopt.getopt(sys.argv[1:],'ho:v',["help","output="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    output=None
    verbose=False
    for o,a in opts:
        if o=='-v':
            verbose=True
        elif o in ('-h','--help'):
            usage()
            sys.exit()
        elif o in ('-o','--output'):
            output=a
            print(output)
        else:
            assert False,'unhandled option'

if __name__=='__main__':
    main()

'''
python3 1.22.05.py -h
python3 1.22.05.py --help
python3 1.22.05.py -o 'hello world'
python3 1.22.05.py --output 'hello world'
'''
