# Security Policy

## Supported Versions

Only the latest release on `master` receives fixes.

| Version | Supported |
| --- | --- |
| `0.1.x` / `master` | Yes |

## Verifying Release Binaries

Windows executables published on [GitHub Releases](https://github.com/fuckula/rebank/releases) include a `rebank.exe.sha256` checksum file. Verify the download before running:

```powershell
Get-FileHash .\rebank.exe -Algorithm SHA256
Get-Content .\rebank.exe.sha256
```

## Reporting a Vulnerability

If you find a security issue (for example, path traversal in `.fspro` / asset extraction, unsafe XML/file handling on malformed `.bank` inputs, or an issue in bundled DLLs):

1. **Do not** open a public issue with exploit payloads or proprietary `.bank` files.
2. Use GitHub's **Private vulnerability reporting** (*Security → Advisories → Report a vulnerability*) if enabled, or open a minimal issue asking for a private contact channel without disclosing exploit details.
3. Include the `rebank --version` output, OS, and minimal synthetic/hex reproduction steps.

We aim to acknowledge reports within 7 days.
