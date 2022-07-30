import requests
import colorama
from colorama import Fore

target=[]
cnt = 0

payload_save_verify = input("[-] Do you want to save your payload as a textfile? (Y/N) -> ")

if payload_save_verify == "y" or payload_save_verify ==  "Y":
	file_name = input("[-] Create your textfile -> ")
	f = open(file_name,"w+")
	file_path = input("[-] List of Targets ->")
	fileOB = open(file_path,"r")
	lines = fileOB.read().splitlines()
	for line in lines:
		target.extend(line.split())
	total_len = len(target)
	print("Total of List -> " + str(total_len))

	try:
		while cnt != total_len:
			cnt = cnt + 1
			webTarget = target[cnt]
			request = requests.get(webTarget)
			if request.status_code == 200:
				print(Fore.GREEN +'Web site exists -> '+ str(webTarget))
				f.write(str(webTarget) + '\n')
			
			else:print(Fore.RED + 'Not Existing -> '+str(webTarget))
	except Exception as e:
		pass
	else:
		print("cant proceed :(")
	finally:
		pass

elif payload_save_verify == "n" or payload_save_verify ==  "N":
	file_path = input("[-] List of Targets ->")
	fileOB = open(file_path,"r")
	lines = fileOB.read().splitlines()
	for line in lines:
		target.extend(line.split())
	total_len = len(target)
	print("Total of List -> " + str(total_len))

	try:
		while cnt != total_len:
			cnt = cnt + 1
			webTarget = target[cnt]
			request = requests.get(webTarget)
			if request.status_code == 200:
				print(Fore.GREEN +'Web site exists -> '+ str(webTarget))
			else:print(Fore.RED + 'Not Existing -> '+str(webTarget))
	except Exception as e:
		pass
	else:
		print("cant proceed :(")
	finally:
		pass





