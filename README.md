# EC2 Instance Management Package

### This package provides functions to manage Amazon Elastic Compute Cloud (EC2) instances using the Boto3 Python library.

### Installation

### This package can be installed using pip:
#### `pip install ec2-instance-management`

### Importing the package
#### ` import ec2_instance_management`

### Starting an EC2 instance
#### ` ec2_instance_management.start_instance(instance_id)`

### Stopping an EC2 instance
#### ` ec2_instance_management.stop_instance(instance_id)`

### Getting the state of an EC2 instance
#### ` state = ec2_instance_management.get_instance_state(instance_id)`

### Getting information about an EC2 instance
#### ` instance_info = ec2_instance_management.get_instance_info(instance_id)`

### SSHing into an EC2 instance
#### ` ec2_instance_management.ssh_to_instance(instance_id, username, private_key_file)`
