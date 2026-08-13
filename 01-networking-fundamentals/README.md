# 01 Networking Fundamentals

A portfolio-ready study module based on the networking fundamentals section of *The Complete Hands-On Cybersecurity Analyst Course*. It connects foundational networking theory to the evidence, controls, and questions a security analyst works with every day.

## Learning objectives

By the end of this module, I can:

- Explain how LAN devices communicate using MAC addresses, ARP, switching, and routing.
- Interpret DHCP activity to associate an IP address with an endpoint and time window.
- Map common protocols, telemetry, and security controls to the OSI and TCP/IP models.
- Read the basic structure of packets and frames in a network capture.
- Describe how firewall policy and network segmentation constrain attack paths.
- Use DNS activity as evidence in phishing, malware, and outbound-traffic investigations.

## Concept map

| Topic | What it does | Analyst relevance |
|---|---|---|
| LAN, MAC, ARP | Delivers traffic locally and resolves IP-to-MAC mappings | Attribute local devices; investigate unexpected ARP behavior or rogue systems |
| DHCP | Assigns IP configuration automatically | Link an address, hostname, MAC, and lease time during triage |
| OSI / TCP-IP | Models how communication responsibilities are layered | Identify where a failure, control, or alert belongs |
| Packets and frames | Carry encapsulated data across networks and LANs | Read PCAPs, ports, flags, addresses, and protocol metadata |
| Firewalls | Enforce allow/deny rules across traffic paths | Validate egress, segmentation, and least-privilege policy |
| DNS | Resolves names to IP addresses | Detect malicious domains, suspicious query volume, and resolver anomalies |

## Key notes

### LANs, MAC addresses, and ARP

- A local area network (LAN) connects systems within a local broadcast domain.
- MAC addresses are Layer 2 identifiers used for local delivery.
- ARP maps an IPv4 address to a MAC address so a host can construct a local frame.
- A switch forwards frames within a LAN; a router forwards IP packets between networks.

**Security lens:** ARP anomalies, unknown MAC addresses, and unusual east-west communication can indicate rogue devices, spoofing, or lateral movement.

### DHCP

DHCP typically follows the DORA sequence:

1. **Discover** — a client searches for a DHCP service.
2. **Offer** — the server offers configuration.
3. **Request** — the client requests the offered lease.
4. **Acknowledge** — the server confirms the assignment.

**Security lens:** DHCP leases provide attribution evidence. Combine IP, MAC, hostname, lease timestamps, and authentication logs to build a reliable timeline.

### OSI and TCP/IP mapping

| OSI layer | Examples | Typical evidence |
|---|---|---|
| 7 Application | HTTP, DNS, SMTP, SSH | Proxy logs, DNS logs, email headers, application alerts |
| 6 Presentation | TLS, encoding, compression | Certificates, cipher suites, encoded payloads |
| 5 Session | Session setup and continuity | Authentication state, session activity |
| 4 Transport | TCP, UDP, ports | TCP flags, connections, resets, flow records |
| 3 Network | IP, ICMP, routing | Source/destination IP, TTL, ICMP, routes |
| 2 Data Link | Ethernet, ARP, VLAN | MAC addresses, ARP, VLAN observations |
| 1 Physical | Cables, radio, interfaces | Link state, wireless signal, interface errors |

TCP/IP groups these operationally into Application, Transport, Internet, and Link layers.

### Packets, frames, and encapsulation

As data moves down the stack, each layer adds its own information:

- Application data becomes a **segment** or **datagram** at transport.
- It becomes an IP **packet** at network.
- It becomes an Ethernet **frame** at data link.

**Security lens:** In Wireshark or tcpdump, start with the five essentials: timestamp, source, destination, protocol, and port. Then pivot into flags, payload metadata, DNS names, or session behavior.

### Firewalls and segmentation

- A firewall applies policy to traffic based on attributes such as source, destination, protocol, port, connection state, and zone.
- Least privilege means allowing only the flows a service genuinely requires.
- Segmentation divides networks into controlled zones to contain compromise and limit lateral movement.

**Security lens:** Treat firewall allow and deny logs as telemetry. Investigate unexpected outbound connections, newly opened ports, policy changes, and denied traffic that could indicate discovery or misconfiguration.

### DNS

DNS translates a hostname into an IP address. A client generally asks a recursive resolver, which may consult root, top-level-domain, and authoritative name servers before returning an answer.

**Security lens:** Look for newly registered or low-reputation domains, beacon-like periodic queries, unusually long subdomains, high NXDOMAIN rates, and DNS requests inconsistent with the host role.

## Analyst workflow example

> Alert: A workstation is contacting an unfamiliar external IP over TCP/443.

1. Check DHCP records to attribute the internal IP to the endpoint and lease window.
2. Review DNS telemetry to determine the requested domain and resolver response.
3. Inspect proxy, firewall, or flow logs for destination, port, volume, and timing.
4. Use a PCAP if available to assess TLS metadata, connection behavior, and related hosts.
5. Decide whether the connection violates normal egress policy or matches an approved application.

## Practical tools

- **Wireshark / tcpdump:** packet and protocol inspection
- **nslookup / dig:** DNS query and response validation
- **ipconfig /all:** endpoint addressing and DNS/DHCP details on Windows
- **arp -a:** local ARP cache inspection
- **Splunk / Wazuh / EDR:** correlate endpoint, authentication, network, and DNS evidence

## Portfolio evidence to add

- Annotated screenshot of a DHCP DORA exchange.
- Wireshark capture with Ethernet, IP, TCP, and DNS fields highlighted.
- A short firewall-rule review demonstrating least privilege.
- A DNS investigation write-up showing a domain-to-IP pivot and conclusion.
