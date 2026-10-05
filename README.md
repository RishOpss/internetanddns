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

# 🔎 4. How Does the Browser Find `euron.one`?

Suppose we type:

```text
https://euron.one
```

into the browser.

The browser ultimately needs an IP address before it can contact the web server. DNS provides that mapping.

## The four important DNS components

### 1. Recursive DNS Resolver — "Let me find the answer for you"

The **recursive resolver** is the DNS service that the client normally asks first.

For example:

```text
Browser
   ↓
Recursive DNS Resolver
```

The resolver may already have the answer in its **cache**. If it does not, it performs the DNS lookup on the client's behalf.

Think of it as a librarian:

> "You give me the website name. I will find the answer for you."

---

### 2. Root DNS Server — "Ask the `.one` TLD"

The **Root DNS** layer sits at the top of the DNS hierarchy.

For `euron.one`, the root does **not** normally return the final IP address.

Instead, it points the recursive resolver toward the DNS servers responsible for the `.one` TLD.

```text
Recursive Resolver
        ↓
      Root
        ↓
      .one
```

Think:

> "I don't know the final address, but I know who handles `.one`."

---

### 3. TLD DNS Server — "Ask the authoritative servers"

TLD means **Top-Level Domain**.

For:

```text
euron.one
```

the TLD is:

```text
.one
```

The `.one` TLD DNS servers know which **authoritative DNS servers** are responsible for `euron.one`.

```text
Root
  ↓
.one TLD
  ↓
Authoritative DNS for euron.one
```

Think:

> "I don't have the final IP, but I know which DNS servers are responsible for `euron.one`."

---

### 4. Authoritative DNS Server — "Here is the DNS record"

The **authoritative DNS server** is the source of DNS records for the domain.

For example, it can return an `A` record containing an IPv4 address or an `AAAA` record containing an IPv6 address.

For `euron.one`, public DNS data currently shows the authoritative nameservers:

```text
nia.ns.cloudflare.com
sevki.ns.cloudflare.com
```

and observed IPv4 A records include:

```text
13.226.209.13
13.226.209.28
13.226.209.53
13.226.209.76
```

These observed records indicate that `euron.one` is currently resolving to addresses in an AWS/CloudFront range. DNS answers can change over time, so the output from your own lookup is the authoritative practical evidence for the moment you run it. citeturn2search0

Think:

> "I am responsible for this domain. Here is the DNS record."

---

# 🧭 DNS Resolution Diagram

The complete hierarchy can be visualized as:

```text
                    Browser
                       │
                       │ "Where is euron.one?"
                       ↓
             ┌────────────────────┐
             │ Recursive Resolver │
             └─────────┬──────────┘
                       │
                       │ If not cached
                       ↓
             ┌────────────────────┐
             │    Root DNS        │
             │       "."          │
             └─────────┬──────────┘
                       │
                       │ "Who handles .one?"
                       ↓
             ┌────────────────────┐
             │    .one TLD DNS    │
             └─────────┬──────────┘
                       │
                       │ "Who handles euron.one?"
                       ↓
             ┌────────────────────┐
             │ Authoritative DNS  │
             │ for euron.one      │
             └─────────┬──────────┘
                       │
                       │ A / AAAA record
                       ↓
                 IP Address
                       │
                       ↓
             Recursive Resolver
                       │
                       ↓
                    Browser
                       │
                       │ HTTPS request
                       ↓
                Web Server
                euron.one
```

### Important clarification

The browser normally does **not** independently walk through Root → TLD → Authoritative DNS.

The normal conceptual flow is:

```text
Browser
   ↓
OS / Stub Resolver
   ↓
Recursive DNS Resolver
   ↓
Root → TLD → Authoritative DNS
   ↓
IP Address
   ↓
Recursive Resolver
   ↓
Browser
```

The recursive resolver performs the hierarchy lookup and can cache the result for the DNS record's TTL.

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

# 🧪 11. Practical DNS Demonstration — `euron.one`

We can use two standard command-line tools to inspect DNS:

- `nslookup` — commonly available on Windows
- `dig` — commonly available on Linux/macOS and in many WSL environments

> **Note:** DNS responses can vary by resolver, cache, and time. The IPv4 values below are a captured public DNS result for `euron.one`; your local command may return the same set in a different order or may show different resolver metadata. Public DNS data currently lists four IPv4 A records for `euron.one`: `13.226.209.13`, `13.226.209.28`, `13.226.209.53`, and `13.226.209.76`. citeturn2search0

## A. `nslookup euron.one`

Run on Windows:

```cmd
nslookup euron.one
```

A typical result will look like:

```text
> nslookup euron.one
Server:  <your-configured-DNS-resolver>
Address: <resolver-IP>

Non-authoritative answer:
Name:    euron.one
Addresses: 13.226.209.13
           13.226.209.28
           13.226.209.53
           13.226.209.76
```

### What does this mean?

The important part is:

```text
Name: euron.one
Addresses:
13.226.209.13
13.226.209.28
13.226.209.53
13.226.209.76
```

This tells us that DNS has returned IPv4 addresses for the domain.

The exact `Server:` line depends on which DNS resolver your machine is configured to use.

---

## B. `dig euron.one`

Run on Linux/macOS/WSL:

```bash
dig euron.one
```

The relevant part of a typical response is:

```text
; <<>> DiG <<>> euron.one
;; QUESTION SECTION:
;euron.one.              IN      A

;; ANSWER SECTION:
euron.one.       <TTL>   IN      A       13.226.209.13
euron.one.       <TTL>   IN      A       13.226.209.28
euron.one.       <TTL>   IN      A       13.226.209.53
euron.one.       <TTL>   IN      A       13.226.209.76
```

The exact TTL, query time, resolver address, and record order can change between lookups.

For a cleaner result, run:

```bash
dig euron.one A +short
```

Expected address values from the current public DNS observation:

```text
13.226.209.13
13.226.209.28
13.226.209.53
13.226.209.76
```

Public DNS data also reports the authoritative nameservers as:

```text
nia.ns.cloudflare.com
sevki.ns.cloudflare.com
```

citeturn2search0

---

# 🌐 How Does the Browser Use This Result?

The DNS lookup is **not the webpage itself**.

It gives the browser a destination.

The simplified flow is:

```text
User
  │
  │ Types https://euron.one
  ↓
Browser
  │
  │ DNS lookup
  ↓
Recursive DNS Resolver
  │
  │ Returns A/AAAA record
  ↓
IP Address
  │
  │ Connect to destination
  ↓
Web Server
  │
  │ HTTPS response
  ↓
Browser
  │
  ↓
Web Page
```

For an IPv4 connection, the browser can use one of the returned `A` record addresses to reach the destination. A DNS `A` record maps a hostname to an IPv4 address, while an `AAAA` record provides an IPv6 address. citeturn0search0turn2search3

So:

```text
euron.one
     ↓
DNS
     ↓
13.226.209.x
     ↓
Network connection
     ↓
HTTPS request
     ↓
Web server
     ↓
HTTPS response
     ↓
Browser renders the website
```

### The key distinction

**DNS answers:**

> "Where should I connect?"

**HTTP/HTTPS then handles:**

> "What resource do I want from that destination?"

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
4. Resolver checks its cache
              ↓
5. If needed, resolver asks Root DNS
              ↓
6. Root points to the .one TLD DNS
              ↓
7. .one TLD points to authoritative DNS
              ↓
8. Authoritative DNS returns the A/AAAA record
              ↓
9. Resolver returns the IP address to the browser
              ↓
10. Browser connects toward that IP
              ↓
11. Browser sends the HTTPS request
              ↓
12. Web server processes the request
              ↓
13. Server sends the response
              ↓
14. Browser displays the website
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
- [x] `nslookup euron.one` output
- [x] `dig euron.one` output
- [x] `ping euron.one`
- [x] `tracert euron.one`
- [x] Network architecture diagram
- [ ] YouTube video

---

## 👨‍💻 Author

**Rishabh**
