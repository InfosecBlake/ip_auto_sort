import sys
import argparse
import datetime

now = datetime.datetime.now()
current_date = str(now.month) + "_" + str(now.day) + "_" + str(now.year)

def main():
    parser = argparse.ArgumentParser(description='Sort IP address in a file.')
    parser.add_argument('file', metavar='<filepath>', type=str, nargs='+',
                        help='file containing IP addresses to be sorted')
    parser.add_argument('-o', '--output', action='store_true',
                        help='output results to a file')
    args = parser.parse_args()
    if args.file:
        with open(sys.argv[1],"r") as f:
            ip_list = [ip.strip() for ip in f]
        for ip in sorted(ip_list, key = lambda ip: [int(ip) for ip in ip.split(".")] ):
            print(ip)
    if args.output:
        with open(sys.argv[1],"r") as f:
            ip_list = [ip.strip() for ip in f]
        test = sorted(ip_list, key = lambda ip: [int(ip) for ip in ip.split(".")])
        with open('output' + current_date + '.txt', 'w') as i:
            for ip in test:
                i.writelines('%s\n' % ip)
    if len(sys.argv) > 3:
        print('Invalid input use -h for help')
        sys.exit()

if __name__=='__main__':
    main()