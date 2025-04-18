Spoofing  
S1. Phishing Login Page  
An attacker impersonates the Authorization Server’s login/consent UI to harvest user credentials.  
DREAD: D=8, R=9, E=7, A=9, D=9 → Total=42  

S2. Malicious Client Registration  
An attacker registers a rogue client with attacker‑controlled redirect URIs to capture authorization codes.  
DREAD: D=7, R=8, E=7, A=8, D=6 → Total=36  

S3. Man‑in‑the‑Middle Auth‑Code Intercept  
An attacker positions between client and auth server to intercept or replay the authorization code flow.  
DREAD: D=6, R=8, E=8, A=8, D=6 → Total=36  

S4. Impersonate Resource Server  
An attacker spins up a fake API endpoint to trick the client into sending stolen access tokens.  
DREAD: D=7, R=7, E=7, A=8, D=7 → Total=36  


Tampering  
T1. Redirect‑URI Parameter Modification  
An attacker alters the redirect_uri parameter in the auth request to divert the code to themselves.  
DREAD: D=6, R=8, E=7, A=7, D=6 → Total=34  

T2. Authorization Code Tampering  
An attacker intercepts and modifies the auth code in transit to invalidate or redirect it.  
DREAD: D=6, R=7, E=7, A=7, D=5 → Total=32  

T3. Token‑Request Payload Tampering  
An attacker alters client_id, client_secret or requested scopes in the /token POST to escalate privileges.  
DREAD: D=7, R=8, E=8, A=8, D=6 → Total=37  

T4. Token Store Manipulation  
An attacker with datastore access tampers with stored tokens to extend or revoke user sessions.  
DREAD: D=8, R=6, E=6, A=9, D=5 → Total=34  


Repudiation  
R1. Missing Auth‑Server Audit Logs  
No tamper‑evident logs of token issuance means neither user nor admin can prove issuance occurred.  
DREAD: D=5, R=5, E=4, A=10, D=3 → Total=27  

R2. Client Consent Repudiation  
Client denies having obtained valid user consent; lack of consent records prevents dispute resolution.  
DREAD: D=5, R=6, E=5, A=9, D=4 → Total=29  

R3. Resource‑Server Validation Repudiation  
Resource Server cannot prove it validated the token (no logs), so access decisions can’t be audited.  
DREAD: D=5, R=5, E=4, A=8, D=3 → Total=25  


Information Disclosure  
I1. Auth Code in Referer Header  
Authorization code leaks via HTTP Referer to third‑party domains when redirecting back to client.  
DREAD: D=6, R=9, E=7, A=8, D=7 → Total=37  

I2. Access Token in Browser History/Logs  
Client stores tokens insecurely (e.g. localStorage or logs), exposing them to local compromise.  
DREAD: D=7, R=8, E=8, A=9, D=6 → Total=38  

I3. Eavesdropping on Token Exchange  
Weak or mis‑configured TLS allows MITM attackers to read auth code or tokens in flight.  
DREAD: D=8, R=7, E=8, A=9, D=7 → Total=39  

I4. Client‑Secret Exposure  
Client_secret sent in POST body can be exposed if logs capture request payload or TLS is broken.  
DREAD: D=8, R=8, E=6, A=8, D=7 → Total=37  

I5. Refresh‑Token Leakage  
Long‑lived refresh tokens stolen from local storage or over‑the‑wire give persistent access.  
DREAD: D=8, R=7, E=8, A=9, D=8 → Total=40  


Denial of Service  
D1. Auth Server Flooding  
Attackers send massive auth‐code requests to exhaust CPU/memory on the Authorization Server.  
DREAD: D=7, R=9, E=9, A=8, D=6 → Total=39  

D2. Token Endpoint Flood  
A high rate of POST /token requests overwhelms the token‐issuing endpoint.  
DREAD: D=7, R=9, E=9, A=8, D=6 → Total=39  

D3. Resource‑Server Validation Flood  
Flooding the Resource Server with invalid tokens forces repeated validation calls to the Auth Server.  
DREAD: D=6, R=8, E=9, A=8, D=6 → Total=37  

D4. Token‑Store Capacity Exhaustion  
Continuous token creations fill the Token Store, causing new requests to fail.  
DREAD: D=6, R=8, E=7, A=8, D=5 → Total=34  


Elevation of Privilege  
E1. Scope Manipulation  
An attacker tampers with the scope parameter to obtain broader permissions than intended.  
DREAD: D=7, R=8, E=8, A=8, D=6 → Total=37  

E2. Access‑Token Replay  
A stolen access token is replayed to access protected resources as the victim.  
DREAD: D=7, R=7, E=8, A=9, D=5 → Total=36  

E3. Refresh‑Token Abuse  
An attacker repeatedly uses a stolen refresh token to mint new access tokens.  
DREAD: D=8, R=7, E=8, A=9, D=6 → Total=38  

E4. Grant‑Type Parameter Tampering  
An attacker changes grant_type (e.g. to client_credentials) to escalate privileges.  
DREAD: D=6, R=7, E=7, A=8, D=5 → Total=33