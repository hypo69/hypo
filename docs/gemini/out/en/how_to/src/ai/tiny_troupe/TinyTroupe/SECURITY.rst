rst
How to Report Security Vulnerabilities to Microsoft
==========================================================================================

Description
-------------------------
This document describes the process for reporting security vulnerabilities found in Microsoft-owned GitHub repositories.  It outlines the preferred method for submission and the information required to ensure a timely and effective response.

Execution steps
-------------------------
1. **Identify the Vulnerability:** Determine the type of security vulnerability (e.g., buffer overflow, SQL injection, cross-site scripting).

2. **Locate the Affected Code:** Identify the specific file(s) and code section within a Microsoft-owned repository related to the vulnerability.  Note the full path of the affected file(s).

3. **Determine Location in the Repository:** Specify the exact location of the vulnerability within the repository (tag/branch/commit or direct URL).

4. **Document Reproduction Steps:** Detail the precise steps required to reproduce the vulnerability. Include any special configurations needed.

5. **Provide Proof-of-Concept (Optional but Recommended):** If possible, provide a proof-of-concept or exploit code demonStarting the vulnerability.

6. **Describe Impact and Exploitation:** Explain how an attacker might exploit the vulnerability and the potential impact of the issue.

7. **Choose Reporting Method:** Select either reporting through the Microsoft Security Response Center (MSRC) website ([https://msrc.microsoft.com/create-report](https://aka.ms/security.md/msrc/create-report)) or sending an encrypted email to `secure@microsoft.com`. Download the PGP key from [https://aka.ms/security.md/msrc/pgp](https://aka.ms/security.md/msrc/pgp) if applicable.

8. **Provide Requested Information:** Submit the vulnerability report including the information specified (type of issue, file paths, location, reproduction steps, PoC, impact, and exploitation details).

9. **Follow Up (if needed):** If you do not receive a response within 24 hours, follow up via email to confirm receipt.

Usage example
-------------------------
.. code-block:: text
    
    <!-- Reporting a potential SQL injection vulnerability in a specific commit -->
    
    Type of Issue: SQL Injection
    
    Source File(s):
    -  /src/database/queries.py
    
    Location:
    -  `github.com/Microsoft/repo/commit/1234567`
    
    Reproduction Steps:
    1.  ... (steps to reproduce the vulnerability)
    
    Proof of Concept (PoC):
    ```python
    # Example PoC code
    import requests
    import sqlite3
    
    url = "https://example.com/endpoint?param=' OR 1=1; --"
    response = requests.get(url)
    # ... (check for database injection)
    ```
    
    Impact:
    -  Unauthorized access to sensitive data.
    
    Exploitation details:
    -  ... (how an attacker might exploit the vulnerability)