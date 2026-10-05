# 🌐 How the Internet Works in 10 Minutes

## Client–Server Architecture Explained

This project explains how the Internet works by following a real browser request and showing how **DNS, IP addresses, routers, and servers** work together.

The main real-world example used in this assignment is:

> **What happens when a browser tries to open `euron.one`?**

---

# 🎯 Learning Objectives

By the end of this session, you will understand:

- What the Internet is
- Client vs Server architecture
- How a browser starts a request
- What a domain name is
- What an IP address is
- How DNS resolution works
- DNS hierarchy: Root → TLD → Authoritative DNS
- Recursive DNS resolvers
- How a browser ultimately finds the server for `euron.one`
- Public vs Private networks
- Request → Response cycle
- Basic network troubleshooting commands

---

# 🌐 1. What Is the Internet?

The Internet is a **network of networks**.

A simplified view:

```text
Laptop
   ↓
Wi-Fi Router
   ↓
ISP
   ↓
Other Networks
   ↓
Web Server
```

Routers and network infrastructure allow different networks to communicate with destinations around the world.

### Simple analogy

Think of the Internet like a huge road network.

- Your laptop = starting location
- Server = destination
- Routers = intersections
- Internet = complete road network

---

# 👨‍💻 2. Client vs Server

The **client** is the system making a request.

The **server** receives the request, processes it, and provides the requested resource or service.

```text
CLIENT                         SERVER

Browser  ───── Request ─────→ Web Server

Browser  ←──── Response ───── Web Server
```

### Restaurant analogy

| Real World | Internet |
|---|---|
| Customer | Client |
| Order | Request |
| Kitchen | Server |
| Food | Response |

When we open `euron.one`, our browser acts as the client and the web server hosting the website acts as the server.

---

# 🌍 3. Domain Name and IP Address

Humans prefer names:

```text
euron.one
```

Networks need an IP address to reach a destination.

Conceptually:

```text
euron.one
     ↓
    DNS
     ↓
IP Address
```

A domain name is therefore a human-friendly way to identify a service or destination.

---

# 🔎 4. How Does the Browser Find euron.one?

This is the most important part of the assignment.

Suppose we type:

```text
https://euron.one
```

into the browser.

The browser needs to discover the IP address associated with `euron.one`.

A simplified DNS resolution flow is:

```text
┌──────────────────────┐
│      Browser         │
│   euron.one          │
└──────────┬───────────┘
           │
           │ DNS query
           ↓
┌──────────────────────┐
│ Recursive DNS        │
│ Resolver              │
└──────────┬───────────┘
           │
           │ Ask Root
           ↓
┌──────────────────────┐
│ Root DNS Servers     │
│ "."                  │
└──────────┬───────────┘
           │
           │ Where is .one?
           ↓
┌──────────────────────┐
│ .one TLD DNS Servers │
└──────────┬───────────┘
           │
           │ Where is euron.one?
           ↓
┌──────────────────────────┐
│ Authoritative DNS Server │
│ for euron.one            │
└──────────┬───────────────┘
           │
           │ A / AAAA record
           ↓
      IP Address
           │
           ↓
┌──────────────────────┐
│    Web Server        │
│    euron.one         │
└──────────────────────┘
```

## Important clarification

The browser normally does **not** independently query the Root, TLD, and Authoritative servers.

The typical flow is:

```text
Browser
   ↓
OS / Stub Resolver
   ↓
Recursive DNS Resolver
   ↓
Root DNS
   ↓
.one TLD DNS
   ↓
Authoritative DNS
   ↓
IP Address
   ↓
Recursive Resolver
   ↓
Browser
```

The recursive resolver performs the DNS hierarchy lookup on behalf of the client and can cache the result.

---

# 🏛️ 5. DNS Hierarchy

DNS is hierarchical.

```text
                         Root
                          "."
                           │
                           ↓
                         .one
                       TLD Server
                           │
                           ↓
                       euron.one
                  Authoritative DNS
                           │
                           ↓
                       IP Address
```

## Level 1 — Root DNS

The Root DNS layer is at the top of the DNS hierarchy.

Its job is not to provide the IP address of `euron.one`.

Instead, it can direct the resolver toward the appropriate **TLD DNS servers** for `.one`.

```text
Root
  ↓
.one TLD
```

---

## Level 2 — TLD DNS

TLD means **Top-Level Domain**.

For:

```text
euron.one
```

the TLD is:

```text
.one
```

The `.one` TLD DNS servers can direct the resolver toward the authoritative DNS servers responsible for `euron.one`.

```text
Root
  ↓
.one TLD
  ↓
Authoritative DNS for euron.one
```

---

## Level 3 — Authoritative DNS

The authoritative DNS server is the source of DNS records for the domain.

For example, it may provide:

```text
euron.one
   ↓
A record
   ↓
IPv4 address
```

or:

```text
euron.one
   ↓
AAAA record
   ↓
IPv6 address
```

The exact IP returned can change, so use the output of `nslookup` or `dig` during the practical demonstration rather than hard-coding an IP address in the documentation.

---

# 🔄 6. Complete DNS Resolution Flow for euron.one

The complete conceptual journey:

```text
User types:

https://euron.one
        │
        ↓
     Browser
        │
        ↓
Recursive DNS Resolver
        │
        ↓
   Root DNS Server
        │
        │ "Who handles .one?"
        ↓
   .one TLD Server
        │
        │ "Who handles euron.one?"
        ↓
Authoritative DNS Server
        │
        │ "Here is the DNS record."
        ↓
    IP Address
        │
        ↓
Recursive Resolver
        │
        ↓
     Browser
        │
        ↓
HTTP/HTTPS Request
        │
        ↓
Web Server for euron.one
        │
        ↓
     Response
        │
        ↓
     Browser
```

### The key distinction

DNS resolution answers:

> **"Where is euron.one?"**

The web request then asks:

> **"Give me the resource from that server."**

---

# 🖥️ 7. From IP Address to Web Server

Once DNS resolution returns an IP address:

```text
euron.one
     ↓
DNS
     ↓
IP Address
     ↓
Internet
     ↓
Web Server
```

The browser can now establish the appropriate network connection and send its web request.

The server processes the request and returns a response.

```text
Browser ───── Request ─────→ Web Server

Browser ←──── Response ───── Web Server
```

---

# 🔐 8. HTTPS in the Flow

When the browser opens:

```text
https://euron.one
```

the communication uses **HTTPS**.

At a high level:

```text
DNS
 ↓
Find IP
 ↓
Connect to destination
 ↓
HTTPS communication
 ↓
Web server
 ↓
Response
```

The detailed HTTP/HTTPS protocol mechanics can be covered separately.

---

# 🏠 9. Private vs Public Network

Your computer may be inside a private local network.

Example:

```text
              PRIVATE NETWORK

Laptop
192.168.1.10
      │
      ↓
Wi-Fi Router
192.168.1.1
      │
      ↓
=============================
       PUBLIC INTERNET
=============================
      │
      ↓
  Web Server
 euron.one
```

### Private Network

Used inside local networks such as:

- Home networks
- Office networks
- Internal enterprise networks

Common private IPv4 ranges:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

### Public Internet

The public Internet connects different networks and destinations globally.

---

# 🔁 10. Request → Response Cycle

After DNS resolution:

```text
Client                         Server

Browser ───── Request ───────→ Web Server

Browser ←──── Response ─────── Web Server
```

For a website:

```text
Browser
   ↓
Request
   ↓
Web Server
   ↓
Process Request
   ↓
Response
   ↓
Browser
   ↓
Webpage
```

---

# 🧪 11. Practical DNS Demonstration

## Windows

Run:

```cmd
nslookup euron.one
```

This demonstrates:

```text
euron.one
    ↓
DNS Resolver
    ↓
DNS Records
    ↓
IP Address
```

Look for the returned:

- DNS server
- Domain name
- IP address / addresses

---

## Linux / macOS

Run:

```bash
dig euron.one
```

For a more focused lookup:

```bash
dig euron.one A
```

And for IPv6:

```bash
dig euron.one AAAA
```

---

# 🧪 12. Practical Connectivity Test

Run:

```cmd
ping euron.one
```

`ping` sends network probes and reports whether replies are received and the approximate round-trip time.

Example:

```text
Reply from ...
bytes=32
time=...
TTL=...
```

> A successful ping does not necessarily mean that the website's HTTP/HTTPS service is working. A server or network can block ICMP while the website remains accessible.

---

# 🧪 13. View Network Hops

### Windows

```cmd
tracert euron.one
```

### Linux / macOS

```bash
traceroute euron.one
```

This gives an approximate view of intermediate network hops observed between your machine and the destination.

Example:

```text
1    192.168.1.1
2    ...
3    ...
4    ...
5    ...
...
```

This helps demonstrate that network traffic may cross multiple routers and networks before reaching the destination.

---

# 🧠 14. Complete Story: Opening euron.one

When the user enters:

```text
https://euron.one
```

the simplified journey is:

```text
1. User enters euron.one
              ↓
2. Browser needs an IP address
              ↓
3. DNS query goes to a recursive resolver
              ↓
4. Resolver queries Root DNS if required
              ↓
5. Root directs resolver to .one TLD
              ↓
6. .one TLD directs resolver to authoritative DNS
              ↓
7. Authoritative DNS returns DNS record
              ↓
8. Resolver returns IP address to the client
              ↓
9. Browser connects toward that IP
              ↓
10. Browser sends web request
              ↓
11. Web server processes the request
              ↓
12. Server sends response
              ↓
13. Browser displays the website
```

---

# 🏁 Final Architecture Diagram

```text
                         USER
                          │
                          ↓
                  ┌───────────────┐
                  │    Browser    │
                  │  euron.one    │
                  └───────┬───────┘
                          │
                          ↓
                  ┌───────────────┐
                  │   Recursive   │
                  │ DNS Resolver  │
                  └───────┬───────┘
                          │
                          ↓
                    ┌───────────┐
                    │   Root    │
                    │    DNS    │
                    └─────┬─────┘
                          │
                          ↓
                    ┌───────────┐
                    │ .one TLD  │
                    │    DNS    │
                    └─────┬─────┘
                          │
                          ↓
                ┌──────────────────┐
                │  Authoritative   │
                │  DNS for         │
                │  euron.one       │
                └────────┬─────────┘
                         │
                         ↓
                    IP Address
                         │
                         ↓
                 ┌───────────────┐
                 │    Internet   │
                 │ Routers / ISP │
                 └───────┬───────┘
                         │
                         ↓
                 ┌───────────────┐
                 │ Web Server    │
                 │  euron.one    │
                 └───────┬───────┘
                         │
                         │ Response
                         ↓
                     Browser
```

---

# 🎯 Key Takeaways

Remember these four concepts:

### 1. DNS

> **DNS helps find where a domain is.**

### 2. IP Address

> **The IP address identifies the network destination.**

### 3. Routers

> **Routers forward traffic between networks.**

### 4. Client–Server

> **The client sends a request and the server sends a response.**

### Complete flow

```text
euron.one
    ↓
Recursive DNS Resolver
    ↓
Root
    ↓
.one TLD
    ↓
Authoritative DNS
    ↓
IP Address
    ↓
Internet / Routers
    ↓
Web Server
    ↓
Response
    ↓
Browser
```

---

# 📂 Project Structure

```text
how-the-internet-works/
│
├── README.md
├── presentation/
│   └── how_the_internet_works_presentation.html
│
└── diagrams/
    └── dns-and-network-architecture.png
```

---

# 🎥 Assignment Deliverables

- [x] What is the Internet
- [x] Client vs Server
- [x] Browser request flow
- [x] Domain names
- [x] IP addresses
- [x] DNS resolution
- [x] Recursive DNS Resolver
- [x] Root DNS
- [x] TLD DNS
- [x] Authoritative DNS
- [x] Complete `euron.one` resolution flow
- [x] Public vs Private networks
- [x] Request → Response cycle
- [x] `nslookup euron.one`
- [x] `dig euron.one`
- [x] `ping euron.one`
- [x] `tracert euron.one`
- [x] Network architecture diagram
- [ ] YouTube video

---

## 👨‍💻 Author

**Rishabh**
