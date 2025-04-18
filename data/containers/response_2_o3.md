Spoofing  
1. Registry Impersonation  
  Description: Attacker spoofs the container registry endpoint to serve malicious or tampered images.  +
  DREAD – Damage:8, Reproducibility:6, Exploitability:5, Affected Users:10, Discoverability:8 → Score 37 

2. Orchestrator API Spoofing  
  Description: Attacker forges requests to the Orchestrator API, causing unauthorized container deployments or modifications.  +
  DREAD – Damage:7, Reproducibility:5, Exploitability:6, Affected Users:8, Discoverability:7 → Score 33  

Tampering  
3. Image Tampering in Transit -
  Description: An attacker intercepts and modifies container images during HTTPS pull/push operations (e.g. via compromised certificates).  
  DREAD – Damage:9, Reproducibility:7, Exploitability:6, Affected Users:10, Discoverability:8 → Score 40  

4. Container Filesystem Tampering -  
  Description: A malicious or compromised container alters its writable layer or underlying FS store to inject malware or backdoors.  
  DREAD – Damage:8, Reproducibility:6, Exploitability:6, Affected Users:9, Discoverability:7 → Score 36  

5. Orchestrator Configuration Tampering + 
  Description: Unauthorized changes to orchestrator resource definitions (e.g. privilege escalation flags, mounts) weaken isolation.  
  DREAD – Damage:8, Reproducibility:5, Exploitability:5, Affected Users:8, Discoverability:6 → Score 32  

Repudiation  
6. Insufficient Audit Logging  +
  Description: Lack of non‑repudiable logs for image pulls/pushes and container lifecycle events inhibits traceability.  
  DREAD – Damage:7, Reproducibility:8, Exploitability:9, Affected Users:10, Discoverability:8 → Score 42  

7. Unlogged Privileged Operations - 
  Description: Host OS fails to record insider’s local privilege uses and container runtime controls, enabling undetected misuse.  
  DREAD – Damage:6, Reproducibility:7, Exploitability:8, Affected Users:8, Discoverability:7 → Score 36  

Information Disclosure  
8. Secrets Leakage via Image Metadata -
  Description: Sensitive information (tokens, credentials) embedded in image labels or environment variables is exposed from the registry.  
  DREAD – Damage:9, Reproducibility:6, Exploitability:6, Affected Users:9, Discoverability:7 → Score 37  

9. Host Kernel Info Disclosure -
  Description: Container uses crafted syscalls or /proc access to infer or leak host kernel memory/layout details.  
  DREAD – Damage:8, Reproducibility:5, Exploitability:7, Affected Users:10, Discoverability:6 → Score 36  

10. Application Traffic Eavesdropping +
  Description: Interception of container‑generated network traffic (if TLS is not enforced) exposes sensitive data in transit.  
  DREAD – Damage:7, Reproducibility:8, Exploitability:5, Affected Users:8, Discoverability:8 → Score 36  

Denial of Service  
11. Registry Storage Exhaustion -
  Description: Attacker pushes large or numerous images to exhaust the registry’s disk quota, preventing legitimate pulls.  
  DREAD – Damage:8, Reproducibility:7, Exploitability:6, Affected Users:10, Discoverability:5 → Score 36  

12. Orchestrator API Flood  -
  Description: High‑volume or malformed API requests overwhelm the orchestrator, blocking container management actions.  
  DREAD – Damage:8, Reproducibility:9, Exploitability:8, Affected Users:10, Discoverability:8 → Score 43  

13. Container Runtime Crash via Malformed Syscalls +
  Description: Malformed or excessive syscalls from a container crash or hang the container runtime, affecting all hosted containers.  
  DREAD – Damage:7, Reproducibility:6, Exploitability:7, Affected Users:9, Discoverability:6 → Score 35  

Elevation of Privilege  
14. Container Breakout via Kernel Exploit  +
  Description: A malicious container leverages a kernel vulnerability to escape isolation and gain host privileges.  
  DREAD – Damage:10, Reproducibility:5, Exploitability:4, Affected Users:10, Discoverability:4 → Score 33  

15. Insider Host Privilege Escalation  -
  Description: An insider on the Host OS abuses local privileges to control the container runtime and all running containers.  
  DREAD – Damage:9, Reproducibility:6, Exploitability:7, Affected Users:8, Discoverability:5 → Score 35  

16. Malicious Image with Root Capabilities +  
  Description: A crafted image grants root inside the container and requests elevated Linux capabilities to break out.  
  DREAD – Damage:9, Reproducibility:7, Exploitability:6, Affected Users:9, Discoverability:6 → Score 37