from firewall.powershell import PowerShellExecutor


result = PowerShellExecutor.list_rules()

print(result.stdout)
