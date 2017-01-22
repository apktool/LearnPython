# 参数解析|argparse|group

import argparse

parser=argparse.ArgumentParser(prog='myProgram',description='It will show something') # --help 会输出description部分；prog选项则决定help中输出的不是文件名，而是定义的名称

group1=parser.add_argument_group('MyFistGroup')
group1.add_argument('--run', action='store',
                    dest='value', # 将输入的参数绑定到value上，比如输入下述指令，则有value=rerun
                    help='just test rerun')
group1.add_argument('--walk', action='store',
                    dest='rewalk',
                    help='just test walk')

group2=parser.add_argument_group('MyScondGroup')
group2.add_argument('--dog', action='store_true',
                    dest='dog',
                    help='just test dog')
group2.add_argument('--cat', action='store_false',
                    dest='cat',
                    help='just test cat')

args=parser.parse_args()
print(args)
# print(args.value)

def fun_dest(value):
    print('->'+value)

if args.value=='rerun':
    fun_dest(args.value)

# python3 1.22.02.py --help
# python3 1.22.02.py --run rerun

'''
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
    name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
    action - The basic type of action to be taken when this argument is encountered at the command line.
    nargs - The number of command-line arguments that should be consumed.
    const - A constant value required by some action and nargs selections.
    default - The value produced if the argument is absent from the command line.
    type - The type to which the command-line argument should be converted.
    choices - A container of the allowable values for the argument.
    required - Whether or not the command-line option may be omitted (optionals only).
    help - A brief description of what the argument does.
    metavar - A name for the argument in usage messages.
    dest - The name of the attribute to be added to the object returned by parse_args().
'''
