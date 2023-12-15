server_name = "my_server"
port = 80
is_https_enable = True
max_connections = 1000

print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enable}")
print(f"Max Connections: {max_connections}")

# Update the configurations values
port = 443
is_https_enable = False

# Print the updated configuration
print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enable}")