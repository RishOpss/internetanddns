#!/usr/bin/env python3
"""
Runnable DNS practical for euron.one.

Runs:
  - nslookup euron.one
  - dig euron.one
  - Python socket resolution (portable fallback / browser-style resolution demo)
  - Generates artifacts/dns-resolution-flow.svg

Run:
  python3 src/dns_demo.py
"""

from __future__ import annotations

import shutil
import socket
import subprocess
from pathlib import Path

DOMAIN = "euron.one"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)


def run_command(command: list[str]) -> str:
    """Run a command and return stdout/stderr without failing the whole demo."""
    executable = shutil.which(command[0])
    if executable is None:
        return f"$ {' '.join(command)}\n[not installed: {command[0]}]\n"

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
        output = result.stdout.strip()
        if result.stderr.strip():
            output += ("\n" if output else "") + result.stderr.strip()
        return f"$ {' '.join(command)}\n{output}\n"
    except (subprocess.TimeoutExpired, OSError) as exc:
        return f"$ {' '.join(command)}\n[command failed: {exc}]\n"


def resolve_domain(domain: str) -> tuple[list[str], list[str]]:
    """Resolve A and AAAA records using the OS resolver."""
    ipv4 = sorted(
        {
            item[4][0]
            for item in socket.getaddrinfo(domain, 443, socket.AF_INET, socket.SOCK_STREAM)
        }
    )
    ipv6 = sorted(
        {
            item[4][0]
            for item in socket.getaddrinfo(domain, 443, socket.AF_INET6, socket.SOCK_STREAM)
        }
    )
    return ipv4, ipv6


def make_svg() -> Path:
    """Generate a self-contained DNS resolution-flow SVG."""
    svg = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1050" viewBox="0 0 1200 1050">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L10,3 L0,6 Z" fill="#2563eb"/>
    </marker>
    <style>
      .box { fill:#eff6ff; stroke:#2563eb; stroke-width:3; rx:16; }
      .title { font:700 30px Arial; fill:#0f172a; }
      .label { font:700 22px Arial; fill:#0f172a; }
      .small { font:18px Arial; fill:#334155; }
      .arrow { stroke:#2563eb; stroke-width:4; marker-end:url(#arrow); }
    </style>
  </defs>
  <rect width="1200" height="1050" fill="#f8fafc"/>
  <text x="600" y="55" text-anchor="middle" class="title">DNS Resolution Flow — euron.one</text>

  <rect x="400" y="85" width="400" height="95" class="box"/>
  <text x="600" y="125" text-anchor="middle" class="label">Browser / Client</text>
  <text x="600" y="155" text-anchor="middle" class="small">https://euron.one</text>

  <line x1="600" y1="180" x2="600" y2="235" class="arrow"/>

  <rect x="400" y="235" width="400" height="105" class="box"/>
  <text x="600" y="275" text-anchor="middle" class="label">Recursive DNS Resolver</text>
  <text x="600" y="307" text-anchor="middle" class="small">Checks cache; queries DNS hierarchy if needed</text>

  <line x1="600" y1="340" x2="600" y2="395" class="arrow"/>

  <rect x="400" y="395" width="400" height="90" class="box"/>
  <text x="600" y="435" text-anchor="middle" class="label">Root DNS (.)</text>
  <text x="600" y="463" text-anchor="middle" class="small">Points to .one TLD DNS</text>

  <line x1="600" y1="485" x2="600" y2="540" class="arrow"/>

  <rect x="400" y="540" width="400" height="90" class="box"/>
  <text x="600" y="580" text-anchor="middle" class="label">.one TLD DNS</text>
  <text x="600" y="608" text-anchor="middle" class="small">Points to authoritative DNS</text>

  <line x1="600" y1="630" x2="600" y2="685" class="arrow"/>

  <rect x="400" y="685" width="400" height="105" class="box"/>
  <text x="600" y="725" text-anchor="middle" class="label">Authoritative DNS</text>
  <text x="600" y="757" text-anchor="middle" class="small">Returns A / AAAA record for euron.one</text>

  <line x1="600" y1="790" x2="600" y2="845" class="arrow"/>

  <rect x="400" y="845" width="400" height="90" class="box"/>
  <text x="600" y="885" text-anchor="middle" class="label">IP Address</text>
  <text x="600" y="913" text-anchor="middle" class="small">Browser can connect to the destination</text>

  <line x1="400" y1="890" x2="210" y2="890" class="arrow"/>
  <line x1="210" y1="890" x2="210" y2="130" class="arrow"/>
  <text x="160" y="520" text-anchor="middle" transform="rotate(-90 160 520)" class="small">Result returned to browser</text>

  <rect x="45" y="70" width="330" height="125" fill="#ecfdf5" stroke="#059669" stroke-width="3" rx="16"/>
  <text x="210" y="108" text-anchor="middle" class="label">Next: HTTPS Request</text>
  <text x="210" y="140" text-anchor="middle" class="small">Browser uses the resolved IP</text>
  <text x="210" y="168" text-anchor="middle" class="small">to reach the web server.</text>
</svg>
"""
    path = ARTIFACTS / "dns-resolution-flow.svg"
    path.write_text(svg, encoding="utf-8")
    return path


def main() -> None:
    print("=" * 72)
    print(f"DNS PRACTICAL: {DOMAIN}")
    print("=" * 72)

    nslookup = run_command(["nslookup", DOMAIN])
    dig = run_command(["dig", DOMAIN])
    print("\n--- nslookup ---")
    print(nslookup)
    print("--- dig ---")
    print(dig)

    print("--- Browser-style OS DNS resolution ---")
    try:
        ipv4, ipv6 = resolve_domain(DOMAIN)
        print(f"A    records: {', '.join(ipv4) if ipv4 else 'none returned'}")
        print(f"AAAA records: {', '.join(ipv6) if ipv6 else 'none returned'}")
        print("\nBrowser flow:")
        print(f"  https://{DOMAIN}")
        print("       ↓ DNS lookup")
        print(f"  {ipv4[0] if ipv4 else (ipv6[0] if ipv6 else 'no address returned')}")
        print("       ↓ HTTPS request")
        print("  Web server")
    except socket.gaierror as exc:
        print(f"DNS resolution failed: {exc}")
        print("The nslookup/dig output above can still be inspected if those tools are available.")

    svg = make_svg()
    print(f"\nGenerated flow artifact: {svg}")
    print("\nHierarchy demonstrated:")
    print("Browser → Recursive Resolver → Root → .one TLD → Authoritative DNS → IP → Browser")


if __name__ == "__main__":
    main()
