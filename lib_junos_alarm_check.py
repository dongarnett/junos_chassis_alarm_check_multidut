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

    # log_errors = []
    # log_failures = []
    # log_fail_no_route = []
    # log_down = []
    # log_ddos = []
    # log_traceback = []
    # log_core = []
    # log_wedge = []
    # log_exception = []
    # log_restart = []
    # log_fpc = []
    # log_chassisd = []
    # log_heap = []
    # log_alarm = []
    # log_toggletrace = []
    # log_badpdu = []
    # log_tracesevice = []
    # log_jtask_rpdtogtrace = []
    # fail_no_route = ['fail', 'route']
    # jtask_tracethread = ['jtask_jthr', 'rpd', 'TraceThread']
    # bad_pdu = ['bad', 'pdu']

'''
don@milnet-r4> show chassis alarms
5 alarms currently active
Alarm time                Class   Description
2023-04-14 18:02:12 UTC   Minor   Host 1 ECC single bit parity error
2023-04-14 17:55:52 UTC   Major   PEM 3 Input Failure
2023-04-14 17:55:52 UTC   Major   PEM 3 Not OK
2023-04-14 17:55:42 UTC   Minor   Mixed Master and Backup RE types
2023-04-14 17:55:31 UTC   Minor   CPU DRAM size mismatch for Master and Backup RE
(master}
'''

    #         #print(k)
    #         proc_res_mem_use.append(k)
    # log_file = inputs.split('\r\n')
    # #print(log_file)
    # for line in log_file:
    #     if "error" in line:
    #         log_errors.append(line)
    #     if "fail" in line:
    #         log_failures.append(line)
    #     if all([x in line for x in fail_no_route]):
    #         log_fail_no_route.append(line)
    #     if "down" in line:
    #         log_down.append(line)
    #     if "ddos" in line:
    #         log_ddos.append(line)
    #     if "traceback" in line:
    #         log_traceback.append(line)
    #     if "core" in line:
    #         log_core.append(line)
    #     if "wedge" in line:
    #         log_wedge.append(line)
    #     if "log_exception" in line:
    #         log_exception.append(line)
    #     if "restart" in line:
    #         log_restart.append(line)
    #     if "fpc" in line:
    #         log_fpc.append(line)
    #     if "chassisd" in line:
    #         log_chassisd.append(line)
    #     if "heap" in line:
    #         log_heap.append(line)
    #     if "alarm" in line:
    #         log_alarm.append(line)
    #     if "toggletrace" in line:
    #         log_toggletrace.append(line)
    #     if all([x in line for x in bad_pdu]):
    #         log_badpdu.append(line)
    #     if "tracesevice" in line:
    #         log_tracesevice.append(line)
    #     if all([x in line for x in jtask_tracethread]):
    #         log_jtask_rpdtogtrace.append(line)
    #
    # error_count = len(log_errors)
    # fail_count = len(log_failures)
    # down_count = len(log_down)
    # ddos_count = len(log_ddos)
    # traceback_count = len(log_traceback)
    # core_count = len(log_core)
    # wedge_count = len(log_wedge)
    # exception_count = len(log_exception)
    # restart_count = len(log_restart)
    # fpc_count = len(log_fpc)
    # chassisd_count = len(log_chassisd)
    # heap_count = len(log_heap)
    # fail_no_route_count = len(log_fail_no_route)
    # alarm_count = len(log_alarm)
    # toggletrace_count = len(log_toggletrace)
    # badpdu_count = len(log_badpdu)
    # traceservice_count = len(log_tracesevice)
    # jtask_count = len(log_jtask_rpdtogtrace)
    # print('################################################')
    # print('########### Log Message Type Counts ############')
    # print('################################################')
    # print(f'There are {error_count} error messages present')
    # print(f'There are {fail_count} failure messages present - check BGP peerings if no route msg counts are high')
    # #print(f'There are {fail_no_route_count} failure no route messages present')
    # print(f'There are {down_count} down messages present')
    # print(f'There are {ddos_count} ddos messages present')
    # print(f'There are {traceback_count} traceback messages present')
    # print(f'There are {core_count} core messages present')
    # print(f'There are {wedge_count} wedge messages present')
    # print(f'There are {exception_count} exception messages present')
    # print(f'There are {restart_count} restart messages present')
    # print(f'There are {fpc_count} fpc messages present')
    # print(f'There are {chassisd_count} chassisd messages present')
    # print(f'There are {heap_count} heap messages present')
    # print(f'There are {alarm_count} alarm messages present')
    # print(f'There are {toggletrace_count} toggletrace messages present')
    # print(f'There are {badpdu_count} bad pdu messages present')
    # print(f'There are {traceservice_count} traceservice messages present')
    # print(f'There are {jtask_count} jtask rpd messages present')
    # print('################################################')
    # print('############# System Log Analysis ##############')
    # print('################################################')
    # log_threshold_count = 1
    # log_display_count = 10
    # if error_count > log_threshold_count:
    #     print(f'The first {log_display_count} error log messages are displayed below.')
    #     for l in log_errors[:10]:
    #         print(l)
    # if fail_count > log_threshold_count:
    #     print(f'The first {log_display_count} failure log messages are displayed below.')
    #     for l in log_failures[:10]:
    #         print(l)
    # # if fail_no_route_count > log_threshold_count:
    # #     print(f'The first {log_display_count} failure no route log messages are displayed below.')
    # #     for l in log_fail_no_route[:10]:
    # #         print(l)
    # if down_count > log_threshold_count:
    #     print(f'The first {log_display_count} log_down log messages are displayed below.')
    #     for l in log_down[:10]:
    #         print(l)
    # if ddos_count > log_threshold_count:
    #     print(f'The first {log_display_count} ddos log messages are displayed below.')
    #     for l in log_ddos[:10]:
    #         print(l)
    # if traceback_count > log_threshold_count:
    #     print(f'The first {log_display_count} traceback log messages are displayed below.')
    #     for l in log_traceback[:10]:
    #         print(l)
    # if core_count > log_threshold_count:
    #     print(f'The first {log_display_count} core log messages are displayed below.')
    #     for l in log_core[:10]:
    #         print(l)
    # if wedge_count > log_threshold_count:
    #     print(f'The first {log_display_count} wedge log messages are displayed below.')
    #     for l in log_wedge[:10]:
    #         print(l)
    # if exception_count > log_threshold_count:
    #     print(f'The first {log_display_count} exception log messages are displayed below.')
    #     for l in log_exception[:10]:
    #         print(l)
    # if restart_count > log_threshold_count:
    #     print(f'The first {log_display_count} restart log messages are displayed below.')
    #     for l in log_restart[:10]:
    #         print(l)
    # if fpc_count > log_threshold_count:
    #     print(f'The first {log_display_count} fpc log messages are displayed below.')
    #     for l in log_fpc[:10]:
    #         print(l)
    # if chassisd_count > log_threshold_count:
    #     print(f'The first {log_display_count} chassisd log messages are displayed below.')
    #     for l in log_chassisd[:10]:
    #         print(l)
    # if heap_count > log_threshold_count:
    #     print(f'The first {log_display_count} heap log messages are displayed below.')
    #     for l in log_heap[:10]:
    #         print(l)
    # if alarm_count > log_threshold_count:
    #     print(f'The first {log_display_count} alarm log messages are displayed below.')
    #     for l in log_alarm[:10]:
    #         print(l)
    # if toggletrace_count > log_threshold_count:
    #     print(f'The first {log_display_count} toggletrace log messages are displayed below.')
    #     for l in log_toggletrace[:10]:
    #         print(l)
    # if badpdu_count > log_threshold_count:
    #     print(f'The first {log_display_count} bad lacp pdu log messages are displayed below.')
    #     for l in log_badpdu[:10]:
    #         print(l)
    # if traceservice_count > log_threshold_count:
    #     print(f'The first {log_display_count} traceservice log messages are displayed below.')
    #     for l in log_tracesevice[:10]:
    #         print(l)
    # if jtask_count > log_threshold_count:
    #     print(f'The first {log_display_count} jtask rpd toggletrace log messages are displayed below.')
    #     for l in log_jtask_rpdtogtrace[:10]:
    #         print(l)
    # #return []
