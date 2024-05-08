import wmi

# Obtain network adaptors configurations
nic_config = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

# First network adaptor
nic = nic_config[0]

# IP address, subnetmask and gateway values should be unicode objects
ip = u'10.0.0.100'
subnetmask = u'255.255.255.0'
gateway = u'10.0.0.1'
dns1_server = '10.0.0.254'
dns2_server = '10.0.0.1'

# Set IP address, subnetmask and default gateway
# Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
nic.SetGateways(DefaultIPGateway=[gateway])
nic.SetDNSServerSearchOrder([dns1_server, dns2_server])
