import subprocess


class PowerShellExecutor:

    @staticmethod
    def execute(command: str):

        return subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-NonInteractive",
                "-ExecutionPolicy",
                "Bypass",
                "-Command",
                command
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

    @staticmethod
    def create_rules(ips):

        if not ips:

            return subprocess.CompletedProcess([], 0, "", "")

        script = []

        for ip in ips:

            script.append(
                f'New-NetFirewallRule -DisplayName "IOC_{ip}" '
                f'-Direction Outbound '
                f'-Action Block '
                f'-RemoteAddress "{ip}"'
            )

        return PowerShellExecutor.execute(";".join(script))

    @staticmethod
    def delete_rules(ips):

        if not ips:

            return subprocess.CompletedProcess([], 0, "", "")

        names = ",".join([f'"IOC_{ip}"' for ip in ips])

        script = f"""
$names=@({names})
Get-NetFirewallRule |
Where-Object {{$names -contains $_.DisplayName}} |
Remove-NetFirewallRule
"""

        return PowerShellExecutor.execute(script)

    @staticmethod
    def list_rules():

        command = '''
Get-NetFirewallRule -DisplayName "IOC_*" |
Select-Object -ExpandProperty DisplayName
'''

        return PowerShellExecutor.execute(command)
