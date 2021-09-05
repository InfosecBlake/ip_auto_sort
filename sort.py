import argparse

def main():
    parser = argparse.ArgumentParser(description='Sort IP address in a file.')
    parser.add_argument('file', metavar='<filepath>', type=str,
                        help='file containing IP addresses to be sorted')
    parser.add_argument('-o', '--output', help='output results to a file of your choice')
    args = parser.parse_args()

    if args.file:
        with open(args.file,"r") as i:
            ip_list = [ip.strip() for ip in i]
        sort_ip = sorted(ip_list, key = lambda ip: [int(ip) for ip in ip.split(".")])
        for ip in sort_ip:
            print(ip)
        if args.output:
            with open(args.output, 'w') as o:
                for ip in sort_ip:
                    o.writelines('%s\n' % ip)

if __name__=='__main__':
    main()
