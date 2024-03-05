import requests
import os

with open('list.txt', 'r') as handle:
        list = handle.readlines()
        for x in list:
            vanities = x.rstrip()
            checker = requests.get(f"https://discord.com/api/v9/invites/{vanities}")
            if checker.status_code == 404:
                print(f"{vanities} is available.")
                with open("output/available.txt","a+") as file:
                    file.write(vanities)
                    file.write("\n")
                valid =+ 1
            else:
                print(f"{vanities} is unavailable.")
                with open("output/unavailable.txt","a+") as file:
                    file.write(vanities)
                    file.write("\n")
                invalid =+ 1