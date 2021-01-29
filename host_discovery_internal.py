import subprocess;
import sys;
import shlex;
import os.path

file_name = None;
resume_file_name = None;
output_file = None;

nmap_command = '/usr/bin/nmap -PE -PA80 -PP -p- '


def init():
    self.file_name = sys.argv[1];
    self.resume_file_name = file_name+'_resume.bee';
    self.output_file = file_name+'_output.bee';

def main():
    print('----- Host Discovery -----')
    self.file_name = sys.argv[1];
    host_list = get_hosts(file_name);
    for host in host_list:
        discover_host(host);


def discover_host(host):
    print('----- Scanning ' + host.rstrip() + '-----')
    command = nmap_command + host.rstrip();
    args = shlex.split(command)
    output = subprocess.run(args , universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
    write_output_to_file(output.stdout, host);


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
    #save_scan(host);


def save_scan(host):
    if not os.path.isfile(resume_file_name):
        print("toodo")


def get_hosts(file_name):
    try:
        f = open(resume_file_name, 'r');
        arr = f.readlines(); 
        print('Resuming process from file: ' + file_name)
        return arr;
    except:
        try:
            f = open(file_name, 'r');
            arr = f.readlines();
            return arr;
        except:
            example_usage();
            sys.exit(0);


def example_usage():
    print('Exmaple usage:')
    print('     python3 host_discovery_internal.py <host list file>')


if __name__ == '__main__':
    try:
        init()
        main()
    except:
        example_usage();
        sys.exit(0);
    