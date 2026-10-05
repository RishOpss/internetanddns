# 🌐 How the Internet Works in 10 Minutes

## Client–Server Architecture Explained

This project explains how the Internet works by following the complete journey of a browser request from a user's device to a remote server and back.

### 🎯 Learning Objectives

- Understand the Internet and network of networks
- Understand client vs server architecture
- Understand browser request flow
- Understand DNS and IP addresses
- Understand public vs private networks
- Understand the request → response cycle
- Use basic network troubleshooting commands

---

## 🔄 Complete Internet Request Flow

```text
Browser
   ↓
DNS
   ↓
IP Address
   ↓
Home Router
   ↓
ISP / Internet Routers
   ↓
Web Server
   ↓
Response
   ↓
Browser
```

### In one line

```text
Domain Name → DNS → IP Address → Router/ISP → Internet → Server → Response → Browser
```

---

## 📚 Topics Covered

### 1. What Is the Internet?

The Internet is a **network of networks**.

```text
Laptop
   ↓
Wi-Fi Router
   ↓
ISP
   ↓
Other Networks
   ↓
Server
```

Routers and network infrastructure allow different networks to communicate.

### 2. Client vs Server

The **client** makes a request and the **server** receives the request and provides the requested resource or service.

```text
Client                         Server

Browser  ───── Request ─────→ Google
Browser  ←──── Response ───── Google
```

**Restaurant analogy:**

| Real World | Internet |
|---|---|
| Customer | Client |
| Order | Request |
| Kitchen | Server |
| Food | Response |

### 3. Domain Name and IP Address

Humans prefer names such as:

```text
google.com
```

Networks use IP addresses to reach destinations.

```text
google.com
     ↓
DNS
     ↓
IP Address
```

### 4. DNS Resolution

DNS stands for **Domain Name System**.

```text
Browser
   │
   │ google.com
   ↓
 DNS
   │
   │ IP Address
   ↓
142.x.x.x
```

The detailed Root → TLD → Authoritative DNS hierarchy is covered in the separate DNS Deep Dive session.

### 5. How the Request Travels

A simplified path is:

```text
Laptop
   ↓
Home Router
   ↓
ISP
   ↓
Network Router
   ↓
Network Router
   ↓
Destination Network
   ↓
Server
```

### 6. Private vs Public Network

A device inside a home or office network may have a private IP:

```text
Laptop
192.168.1.10
     │
     ↓
Wi-Fi Router
     │
     ↓
Public Internet
     │
     ↓
Web Server
```

Common private IPv4 ranges:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

---

# 🔁 Request → Response Cycle

```text
Client                         Server

Browser ───── Request ───────→ Server

Browser ←──── Response ─────── Server
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

# 🧪 Practical Demonstrations

## 1. DNS Lookup

### Windows

```cmd
nslookup google.com
```

### Linux / macOS

```bash
dig google.com
```

This shows DNS information associated with the domain.

## 2. Test Connectivity

```cmd
ping google.com
```

`ping` sends network probes and reports whether replies are received along with round-trip timing.

> A successful ping does not necessarily mean that the website's HTTP/HTTPS service is working.

## 3. View Network Hops

### Windows

```cmd
tracert google.com
```

### Linux / macOS

```bash
traceroute google.com
```

This gives an approximate view of the network hops observed between your machine and the destination.

---

# 🧠 The Complete Story

When you type:

```text
google.com
```

the simplified journey is:

```text
1. Browser receives google.com
             ↓
2. DNS resolves the domain
             ↓
3. Browser obtains an IP address
             ↓
4. Request leaves the local network
             ↓
5. Routers forward the traffic
             ↓
6. Request reaches the server
             ↓
7. Server processes the request
             ↓
8. Server sends a response
             ↓
9. Response travels back
             ↓
10. Browser displays the webpage
```

---

# 🏁 Key Takeaway

> **Domain Name → DNS → IP Address → Router → Internet → Server → Response → Browser**

| Component | Main Role |
|---|---|
| Browser | Client that makes the request |
| DNS | Helps resolve domain names |
| IP Address | Identifies the network destination |
| Router | Forwards traffic between networks |
| ISP | Provides Internet connectivity |
| Server | Processes requests and provides resources |
| Response | Data returned to the client |

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
    └── network-architecture-diagram.png
```

---

# 🎥 Assignment Deliverables

- [x] Internet fundamentals
- [x] Client–Server architecture
- [x] Browser request flow
- [x] DNS resolution
- [x] IP addresses
- [x] Public vs Private networks
- [x] `nslookup` demonstration
- [x] `ping` demonstration
- [x] `tracert` demonstration
- [x] Network architecture diagram
- [ ] YouTube video

---

## 👨‍💻 Author

**Rishabh**
