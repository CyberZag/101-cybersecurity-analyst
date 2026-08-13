# Networking Fundamentals Lab Checklist

Use this checklist to create reproducible evidence for the portfolio module. Run all exercises only in environments you own or are authorized to use.

## Lab 1 — Local network identity

- [ ] Record the workstation IP, gateway, DNS servers, and DHCP server using `ipconfig /all`.
- [ ] Inspect the ARP cache with `arp -a`.
- [ ] Identify the difference between an IP address and a MAC address.
- [ ] Capture a small amount of local traffic and identify an Ethernet frame.

**Evidence to save:** a redacted command output and an annotated explanation of source/destination MAC versus source/destination IP.

## Lab 2 — DHCP DORA

- [ ] Use a controlled virtual lab or packet capture containing DHCP traffic.
- [ ] Identify Discover, Offer, Request, and Acknowledge messages.
- [ ] Record client MAC, offered IP, DHCP server, lease time, gateway, and DNS settings.
- [ ] Explain how you would use this data to attribute a security event.

**Evidence to save:** one annotated screenshot or a concise four-step DORA walkthrough.

## Lab 3 — DNS resolution

- [ ] Query a known benign domain with `nslookup` or `Resolve-DnsName`.
- [ ] Capture the query and response in Wireshark if feasible.
- [ ] Identify query name, record type, resolver, response address, and TTL.
- [ ] Compare a successful lookup with an NXDOMAIN response.

**Evidence to save:** a short diagram of the client → resolver → authoritative-resolution path and a note on what you would hunt for in DNS logs.

## Lab 4 — TCP, UDP, ports, and packets

- [ ] Capture a TCP connection and locate SYN, SYN-ACK, and ACK packets.
- [ ] Identify source port, destination port, source IP, and destination IP.
- [ ] Compare the TCP exchange with a UDP DNS query.
- [ ] Describe the difference between a packet and a frame in the capture.

**Evidence to save:** an annotated capture with a five-field analyst summary: time, source, destination, protocol, port.

## Lab 5 — Firewall policy

- [ ] Document three required flows in a small lab, such as workstation → DNS resolver, workstation → web service, and administrator → management interface.
- [ ] Create or review allow rules that only permit these flows.
- [ ] Add a default-deny or equivalent restrictive policy for unneeded flows.
- [ ] Verify permitted and denied traffic with logs or tests.

**Evidence to save:** a sanitized rule table with business purpose, source, destination, protocol/port, and expected logging behavior.

## Lab 6 — Segmentation scenario

- [ ] Create at least two zones in a home lab: user network and server network.
- [ ] Allow only required user-to-server services.
- [ ] Test blocked lateral movement between systems.
- [ ] Explain how segmentation reduces the impact of a compromised endpoint.

**Evidence to save:** a simple network diagram, test results, and a one-paragraph risk statement.

## Completion criteria

This module is portfolio-ready when you can explain each capture or log artifact in plain language, identify its corresponding OSI/TCP-IP layer, and state the security decision it supports.
