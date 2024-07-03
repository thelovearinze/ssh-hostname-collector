import paramiko
import getpass

def get_ssh_client(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    return client

def collect_hostname(client):
    stdin, stdout, stderr = client.exec_command('hostname')
    return stdout.read().decode().strip()

def main():
    hostname = input("Enter the SSH server hostname: ")
    username = input("Enter your SSH username: ")
    password = getpass.getpass("Enter your SSH password: ")

    client = get_ssh_client(hostname, username, password)
    remote_hostname = collect_hostname(client)
    print(f"Remote hostname: {remote_hostname}")

    client.close()

if __name__ == "__main__":
    main()
