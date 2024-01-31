1. **localhost/127.0.0.1**:
   - `localhost` is a hostname that typically resolves to the loopback IP address `127.0.0.1`.
   - The loopback address (`127.0.0.1`) is a special IP address that allows a device to communicate with itself.
   - When you access `localhost` or `127.0.0.1` in a web browser or any other application on your computer, you are connecting to services running on your own machine.

2. **0.0.0.0**:
   - `0.0.0.0` is a special IP address used to represent an invalid or unknown target.
   - In networking, `0.0.0.0` is often used in routing tables or configuration settings to indicate that a particular network interface should listen for connections from any available IP address.
   - For example, if a service is configured to listen on `0.0.0.0`, it will accept connections from any network interface on the machine.

3. **/etc/hosts**:
   - `/etc/hosts` is a system file used by operating systems like Linux and Unix-based systems (e.g., macOS) to map hostnames to IP addresses.
   - It is a simple text file that allows users to manually specify the IP address for a given hostname, bypassing DNS (Domain Name System) resolution.
   - Entries in `/etc/hosts` can be used to override DNS entries or define local hostnames for development and testing purposes.

4. **How to display your machine’s active network interfaces**:
   - On Windows:
     - Open Command Prompt (`cmd`) and run the command `ipconfig`. This will display information about all active network interfaces, including their IP addresses, subnet masks, and default gateways.
   - On Linux/Unix-based systems:
     - Open Terminal and run the command `ifconfig` or `ip addr`. This will display information about all active network interfaces, including their IP addresses, subnet masks, and other relevant details.
     - Alternatively, you can use the `ip link show` command to display a list of network interfaces along with their state and assigned MAC addresses.
