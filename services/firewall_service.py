from firewall.synchronizer import FirewallSynchronizer


class FirewallService:

    def __init__(self):

        self.synchronizer = FirewallSynchronizer()

    def sync(self):

        return self.synchronizer.sync()
