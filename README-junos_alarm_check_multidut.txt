# junos_alarm_check_multidut


Purpose:
This tool checks for active chassis alarms across multiple devices by reading a list of device IP addresses from an external file.

It perform the following workflow on each device:
1. Obtain currently active alarm counts.
2. Displays alarms if there are any currently active.

This tool can be run at the end of a larger script after device triggers have been exercised.
This tool can also be run without triggers to determine any existing alarms present.




Requirements:
The Paramiko SSH library is required for connectivity to the target device.


Usage:
junos_alarm_check_multidut.py -t <device_list_file> -u <username> -p <password>

Options:
-t     <device_list_file>      List of device IPs to analyze logs
-u     <username>              Device username
-p     <password>              Device passwword
--targets     <device_list_file>      List of device IPs to analyze logs
-username     <username>              Device username
-password     <password>              Device passwword



Example Run:
me@my_computer# python3 junos_alarm_check_multidut.py -t dut_list.txt -u user123 -p pass123


Analyzing target host 10.0.0.11:
Sending command: show chassis alarms | no-more

No alarms currently active




Analyzing target host 10.0.0.21:
Sending command: show chassis alarms | no-more

##################################################
############# Active Chassis Alarms ##############
##################################################
Last login: Sat Apr 15 02:02:49 2023 from 10.0.0.49
--- JUNOS 22.3R1.11 Kernel 64-bit  JNPR-12.1-20220816.a81ed05_buil
show chassis alarms | no-more
don@milnet-r4> show chassis alarms | no-more
1 alarms currently active
Alarm time               Class  Description
2023-04-03 06:24:53 UTC  Minor  Loss of communication with Backup RE

don@milnet-r4>




Analyzing target host 10.0.0.31:
Sending command: show chassis alarms | no-more

No alarms currently active
