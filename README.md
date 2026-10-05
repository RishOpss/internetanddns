# DNS Practical — `euron.one`

This repository contains a **runnable DNS demonstration**, not just documentation.

## Run

From the repository root:

```bash
python3 src/dns_demo.py
```

On Windows, if `python3` is unavailable:

```powershell
python src\dns_demo.py
```

The script:

1. Runs `nslookup euron.one`
2. Runs `dig euron.one`
3. Performs an OS-level DNS lookup using Python
4. Prints the IP addresses returned to the client
5. Explains the browser-style flow from `euron.one` to the resolved address
6. Generates `artifacts/dns-resolution-flow.svg`

No third-party Python packages are required.

---

# 1. Why DNS Exists

Humans use domain names:

```text
euron.one
```

Networks need IP addresses to reach a destination.

DNS provides the mapping:

```text
euron.one
     ↓
DNS
     ↓
IP address
```

The browser can then use the returned address to continue the web connection.

---

# 2. DNS Hierarchy

A DNS lookup can involve these roles:

```text
Browser
   ↓
Recursive DNS Resolver
   ↓
Root DNS (.)
   ↓
.one TLD DNS
   ↓
Authoritative DNS for euron.one
   ↓
A / AAAA record
   ↓
IP Address
   ↓
Browser
```

### Recursive Resolver

The client normally asks a **recursive DNS resolver** first.

The resolver checks its cache. If the answer is not cached, it performs the required DNS lookups on behalf of the client.

### Root DNS

The Root DNS layer is at the top of the hierarchy. It directs the resolver toward the DNS servers responsible for the requested TLD.

For `euron.one`:

```text
Root → .one
```

### TLD DNS

`.one` is the top-level domain.

The `.one` TLD DNS layer directs the resolver toward the authoritative DNS servers for `euron.one`.

### Authoritative DNS

The authoritative DNS servers are responsible for the domain's DNS records and can return the relevant `A` or `AAAA` record.

---

# 3. Resolution Flow Artifact

The executable source generates the actual SVG artifact:

```text
src/dns_demo.py
        ↓
artifacts/dns-resolution-flow.svg
```

The submitted diagram represents:

```text
Browser
   ↓
Recursive Resolver
   ↓
Root
   ↓
.one TLD
   ↓
Authoritative DNS
   ↓
IP Address
   ↓
Browser
   ↓
HTTPS Request
   ↓
Web Server
```

**Generated artifact:** [`artifacts/dns-resolution-flow.svg`](artifacts/dns-resolution-flow.svg)

---

# 4. Practical Command Demonstration

The source executes the exact requested commands:

```bash
nslookup euron.one
dig euron.one
```

It also performs a portable DNS lookup through Python's operating-system resolver.

Run:

```bash
python3 src/dns_demo.py
```

The script prints the actual command output from the machine on which it is executed.

### Example structure

```text
--- nslookup ---

$ nslookup euron.one
...

--- dig ---

$ dig euron.one
...

--- Browser-style OS DNS resolution ---

A records: ...
AAAA records: ...

Browser flow:
  https://euron.one
       ↓ DNS lookup
  <resolved IP>
       ↓ HTTPS request
  Web server
```

The actual addresses are intentionally **not hard-coded**, because DNS responses can change by resolver, location, caching, CDN routing, and time.

---

# 5. How the Browser Uses the Result

The important distinction is:

```text
DNS
 ↓
"Where should I connect?"
```

Then:

```text
Resolved IP
 ↓
Network connection
 ↓
HTTPS request
 ↓
Web server
 ↓
HTTPS response
 ↓
Browser
```

DNS does not return the webpage itself. It helps the client discover the network destination.

---

# 6. Source Code

The complete runnable implementation is:

```text
src/dns_demo.py
```

The generated resolution-flow artifact is:

```text
artifacts/dns-resolution-flow.svg
```

The implementation uses only Python's standard library plus the locally installed `nslookup` and `dig` command-line tools when available.

---

# 7. YouTube

### Internet / Client-Server Video

https://youtu.be/pbxancP8Ogs

### DNS Video

https://youtu.be/UXGip5xoATU

---

# 8. Assignment Mapping

| Requirement | Implementation |
|---|---|
| DNS purpose and domain names | `README.md` + `src/dns_demo.py` |
| DNS hierarchy | `src/dns_demo.py` + generated SVG |
| Root / TLD / Authoritative roles | `README.md` + resolution-flow artifact |
| `nslookup` practical | Executed by `src/dns_demo.py` |
| `dig` practical | Executed by `src/dns_demo.py` |
| `euron.one` browser resolution | Python OS resolver + browser-style output |
| DNS resolution flow diagram | `artifacts/dns-resolution-flow.svg` |

---

## Project Structure

```text
dns-practical/
│
├── README.md
│
├── src/
│   └── dns_demo.py
│
└── artifacts/
    └── dns-resolution-flow.svg
```
