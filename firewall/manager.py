from firewall.powershell import PowerShellExecutor


class FirewallManager:

    def __init__(self):

        self.prefix = "IOC_"

    def create_many(self, ips):

        result = PowerShellExecutor.create_rules(ips)

        print("RETURN CODE:", result.returncode)

        print("STDOUT:")
        print(result.stdout)

        print("STDERR:")
        print(result.stderr)

        return result.returncode == 0

    def delete_many(self, ips):

        result = PowerShellExecutor.delete_rules(ips)

        return result.returncode == 0

    def list(self):

        result = PowerShellExecutor.list_rules()

        if result.returncode != 0:

            return set()

        rules = set()

        for line in result.stdout.splitlines():

            line = line.strip()

            if not line:

                continue

            if line.startswith("DisplayName"):

                continue

            if line.startswith("-----------"):

                continue

            rules.add(

                line.replace(self.prefix, "")

            )

        return rules
