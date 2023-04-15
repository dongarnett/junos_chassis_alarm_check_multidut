import paramiko
from lib_ssh_connectivity import Device
from lib_ssh_connectivity import create_handle_quiet
import os
import re
import sys
import time
import datetime
from pprint import pprint
import argparse
from collections import defaultdict




'''Get chassis alarm values from device'''
def get_alarm_messages(dut_host):
    date_time = datetime.datetime.now()
    current_time = date_time.timestamp()
    '''Command sets for device configuration'''
    command_set_1 = [f'show chassis alarms | no-more']
    '''Create handle'''
    dut_host_session = create_handle_quiet(dut_host)
    dut_host_terminal = dut_host_session.invoke_shell()
    '''Start execution'''
    for command in command_set_1:
        print(f'Sending command: {command}\n')
        try:
            dut_host_terminal.send(f'{command}\n')
            time.sleep(5)
        except:
            print(f"An error occurred.")
            time.sleep(1)
        output = dut_host_terminal.recv(1000000).decode('utf-8')
    output_recv = output.split('\r\n')
    dut_host_terminal.send('exit\n')
    return output


'''Parse output from logging data retrieved'''
def parse_alarm_count(inputs):
    init_alarm_data = re.findall(r'^(\d+|No)\s+alarms', inputs, re.MULTILINE)
    #init_alarm_count =
    for init_line in init_alarm_data:
        line_list = re.findall(r'^(\d+|No)', init_line)
        for line in line_list:
            #print(line)
            if line == "No":
                alarm_count = 0
            else:
                alarm_count = int(line)
    return alarm_count
