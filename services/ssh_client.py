import paramiko

__author__ = "nmoreno"
__copyright__ = "Copyright (c) 2018 Monica Natalia Moreno"


class SSHClient:

    bytes = 4096

    def __init__(self, hostname, port=None, user=None, passoword=None):
        '''
        Constructor
        :param hostname:
        :param port:
        :param user:
        :param passoword:
        :return:
        '''
        self.ssh_client = paramiko.Transport(hostname, port)
        self.ssh_client.connect(username=user, password=passoword)

    def run_cmd(self, command):
        '''
        Run ssh command
        :param command:
        :return:
        '''
        session = self.ssh_client.open_channel(kind='session')
        session.exec_command(command)
        stout = session.recv(self.bytes)
        error = session.recv_stderr(self.bytes)
        session.close()
        return stout, error
