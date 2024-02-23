# Network Basics Concept Page

In the realm of computer networking, understanding network basics is fundamental. Networks facilitate communication and data transfer between devices such as computers, servers, routers, and switches. Key concepts include:

- **IP Addressing**: An IP address uniquely identifies a device on a network. IPv4 and IPv6 are the two main types of IP addresses.
- **Subnetting and CIDR**: Subnetting involves dividing a network into smaller, more manageable sub-networks. CIDR (Classless Inter-Domain Routing) notation is used to represent subnet masks.
- **Routing**: Routing involves directing data packets between networks using routers. Routing protocols such as OSPF and BGP determine the best paths for data to travel.
- **TCP/IP Stack**: The TCP/IP protocol suite governs how data is transmitted and received across networks. It consists of layers like the application layer, transport layer, internet layer, and link layer.

# Server Concept Page

Servers are powerful computers or software systems that provide services or resources to other devices on a network. Key points about servers include:

- **Types of Servers**: Examples include web servers, application servers, file servers, database servers, and mail servers.
- **Server Hardware**: Servers are often equipped with robust hardware configurations to handle high workloads and ensure reliability.
- **Server Operating Systems**: Operating systems like Linux, Windows Server, and Unix are commonly used on servers.
- **Server Management**: Server administration involves tasks such as configuration, maintenance, monitoring, and security.

# Web Server Concept Page

A web server is a specialized server that delivers web content over the internet. Key aspects of web servers include:

- **HTTP Protocol**: Web servers use the HTTP (Hypertext Transfer Protocol) to transmit web pages and files to clients.
- **Common Web Servers**: Examples include Apache HTTP Server, Nginx, Microsoft Internet Information Services (IIS), and LiteSpeed.
- **Virtual Hosting**: Web servers can host multiple websites on a single physical server using virtual hosting techniques.
- **Security Considerations**: Web servers must be configured securely to prevent unauthorized access and mitigate common web-based attacks.

# DNS Concept Page

The Domain Name System (DNS) is a hierarchical decentralized naming system for computers, services, or other resources connected to the internet or a private network. Key aspects of DNS include:

- **Domain Names**: Domain names provide human-readable addresses for websites and other resources.
- **DNS Resolution**: DNS servers translate domain names into IP addresses, allowing clients to locate resources on the internet.
- **DNS Records**: DNS records store various types of information associated with domain names, such as IP addresses, mail server addresses, and aliases.
- **DNS Hierarchy**: DNS operates in a hierarchical structure, with different levels of DNS servers responsible for different parts of the DNS namespace.

# Load Balancer Concept Page

A load balancer is a device or software application that distributes network or application traffic across multiple servers. Key points about load balancers include:

- **Traffic Distribution**: Load balancers evenly distribute incoming traffic among a group of servers to optimize performance and reliability.
- **Types of Load Balancers**: Load balancers can be hardware-based or software-based and operate at different layers of the network stack.
- **Health Checking**: Load balancers monitor the health and availability of backend servers and route traffic only to healthy servers.
- **Session Persistence**: Load balancers can maintain session persistence by ensuring that subsequent requests from the same client are sent to the same backend server.

# Monitoring Concept Page

Monitoring involves observing and analyzing the performance and health of systems, networks, applications, and services. Key aspects of monitoring include:

- **Metrics Collection**: Monitoring systems collect data on various performance metrics such as CPU utilization, memory usage, disk I/O, and network traffic.
- **Alerting**: Monitoring systems can be configured to generate alerts or notifications when predefined thresholds or conditions are met.
- **Logging and Log Analysis**: Logging involves recording events, errors, and activities within a system for analysis and troubleshooting.
- **Dashboarding and Visualization**: Monitoring tools often provide dashboards and visualization features to help users understand and interpret monitoring data.

# What is a Database

A database is a structured collection of data organized for efficient storage, retrieval, and manipulation. Key aspects of databases include:

- **Data Models**: Databases can be relational, NoSQL, or other specialized types, depending on the data model and requirements.
- **Querying and Indexing**: Databases support querying operations to retrieve specific data based on defined criteria. Indexes improve query performance by facilitating faster data retrieval.
- **ACID Properties**: Transactional databases adhere to the ACID (Atomicity, Consistency, Isolation, Durability) properties to ensure data integrity and reliability.
- **Database Management Systems (DBMS)**: Examples include MySQL, PostgreSQL, MongoDB, Oracle, and Microsoft SQL Server.

# Difference Between Web Server and App Server

While web servers and application servers are both types of servers, they serve different roles in the web application architecture:

- **Web Server**: A web server primarily handles HTTP requests, serves static content like HTML, CSS, and images, and may also handle some basic server-side scripting.
- **Application Server**: An application server hosts the business logic and application code of a web application. It executes dynamic code, interacts with databases, and generates dynamic content for client requests.

# DNS Record Types

DNS supports various record types, each serving a specific purpose:

- **A (Address) Record**: Maps a domain name to an IPv4 address.
- **AAAA (IPv6 Address) Record**: Maps a domain name to an IPv6 address.
- **CNAME (Canonical Name) Record**: Alias of one domain name to another.
- **MX (Mail Exchange) Record**: Specifies the mail server responsible for receiving email messages for a domain.
- **TXT (Text) Record**: Stores text-based information associated with a domain, often used for DNS-based verification and authentication.

# Single Point of Failure (SPOF)

A Single Point of Failure (SPOF) is a component within a system whose failure would cause the entire system to fail. SPOFs pose a risk to system reliability and uptime and should be identified and mitigated through redundancy and fault-tolerant design.

# Avoiding Downtime When Deploying New Code

To avoid downtime when deploying new code, consider implementing strategies such as:

- **Blue-Green Deployment**: Deploy new code to a parallel environment (green) while keeping the existing environment (blue) operational. Traffic is switched to the green environment once deployment is complete.
- **Canary Deployment**: Gradually roll out new code to a subset of users or servers to monitor its performance and stability before deploying it to the entire system.
- **Rolling Deployment**: Deploy new code in small increments across multiple servers or instances, allowing the system to remain operational throughout the deployment process.

# High Availability Cluster (Active-Active/Active-Passive)

A High Availability (HA) cluster is a group of interconnected servers or systems designed to ensure continuous operation and minimize downtime. Two common configurations are:

- **Active-Active Cluster**: All nodes in the cluster actively handle client requests and share the workload. If one node fails, the remaining nodes continue to serve traffic.
- **Active-Passive Cluster**: One node (active) handles client requests while the other node (passive) remains on standby. If the active node fails, the passive node takes over to maintain service availability.

# HTTPS

HTTPS (Hypertext Transfer Protocol

 Secure) is an extension of HTTP that encrypts data transmitted between a client (such as a web browser) and a server. HTTPS uses SSL/TLS encryption to secure sensitive information, such as login credentials, financial transactions, and personal data, against eavesdropping and tampering.

# System Redundancy

System redundancy involves duplicating critical components or functions of a system to increase reliability and availability. Redundancy can be implemented at various levels, including hardware redundancy (e.g., redundant power supplies, hard drives), software redundancy (e.g., load balancers, clustering), and data redundancy (e.g., backups, replication).

# Acronyms

- **LAMP**: Stands for Linux, Apache, MySQL, and PHP/Python/Perl, a common open-source web development stack.
- **SPOF**: Stands for Single Point of Failure, a component whose failure would cause the entire system to fail.
- **QPS**: Stands for Queries Per Second, a metric used to measure the rate of queries or requests processed by a system.
