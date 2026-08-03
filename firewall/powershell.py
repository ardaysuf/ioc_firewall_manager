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

        BATCH_SIZE = 100

        last = subprocess.CompletedProcess([], 0, "", "")

        for i in range(0, len(ips), BATCH_SIZE):

            batch = ips[i:i + BATCH_SIZE]

            script = []

            for ip in batch:

                script.append(
                    f'New-NetFirewallRule '
                    f'-DisplayName "IOC_OUT_{ip}" '
                    f'-Direction Outbound '
                    f'-Action Block '
                    f'-RemoteAddress "{ip}"'
                )

                script.append(
                    f'New-NetFirewallRule '
                    f'-DisplayName "IOC_IN_{ip}" '
                    f'-Direction Inbound '
                    f'-Action Block '
                    f'-RemoteAddress "{ip}"'
                )

            last = PowerShellExecutor.execute(";".join(script))

            if last.returncode != 0:

                return last

        return last

    @staticmethod
    def delete_rules(ips):

        if not ips:

            return subprocess.CompletedProcess([], 0, "", "")

        BATCH_SIZE = 100

        last = subprocess.CompletedProcess([], 0, "", "")

        for i in range(0, len(ips), BATCH_SIZE):

            batch = ips[i:i + BATCH_SIZE]

            names = []

            for ip in batch:

                names.append(f'"IOC_OUT_{ip}"')
                names.append(f'"IOC_IN_{ip}"')

            script = f"""
$names=@({",".join(names)})
Get-NetFirewallRule |
Where-Object {{$names -contains $_.DisplayName}} |
Remove-NetFirewallRule
"""

            last = PowerShellExecutor.execute(script)

            if last.returncode != 0:

                return last

        return last

    @staticmethod
    def list_rules():

        command = r'''
Get-NetFirewallRule -DisplayName "IOC_*" |
Select-Object -ExpandProperty DisplayName |
ForEach-Object {
    $_ -replace '^IOC_(OUT|IN)_',''
} |
Sort-Object -Unique
'''

        return PowerShellExecutor.execute(command)