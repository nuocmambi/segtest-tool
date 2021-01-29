import subprocess;
import sys;
import shlex;
import os.path


output_file = 'final_result.bee'
nmap = 'nmap -sT -p'

def main():
    file_name = sys.argv[1]
    input = read_from_file(file_name)
    
    for host in input:
        find_open_ports(host.rstrip());


def find_open_ports(line):
    arr = line.split(';');
    command = nmap+arr[1]+' '+arr[0];
    args = shlex.split(command)
    output = subprocess.run(args , universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
    write_output_to_file(output.stdout, arr[0]);
    

def write_output_to_file(output, host):
    print('----- Writing to file -----')
    f = open(output_file, 'a+')
    string = host.rstrip('\n')+';';
    for line in output.split('\n'):
        if 'open' in line:
            info = line.split("/")
            string+=info[0]+','
    
    string = string[:-1]
    string+='\n'
    print(string)
    f.write(string)

def read_from_file(file_name):
    f = open(file_name, 'r');
    arr = f.readlines(); 
    print('Reading from: ' + file_name)
    return arr;
    

def example_usage():
    print('Exmaple usage:')
    print('     python3 port_scan_from_outside.py <output file>')
    print('\n     Use output file from the host_discovery_internal.py script as input')

if __name__ == '__main__':
    try:
        main();
    except:
        example_usage();
        sys.exit(0);