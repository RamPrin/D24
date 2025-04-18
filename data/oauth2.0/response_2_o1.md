### STRIDE Threats

#### Spoofing
- **Threat Title: Spoofed Authorization Request**
  - Unauthorized actor may spoof the authorization request intended for the authorization server.-

- **Threat Title: Impersonation of Resource Owner**
  - Attacker could impersonate the resource owner in interactions with the client application. +

#### Tampering
- **Threat Title: Tampered Authorization Code**
  - An attacker could intercept and modify the authorization code in transit between the authorization server and client app. +

- **Threat Title: Tampered Access Token Request**
  - The access token request could be tampered with during transmission. +

#### Repudiation
- **Threat Title: Unauthorized Actions without Traceability**
  - The client app may not log actions properly, allowing users to deny performing actions. -

#### Information Disclosure
- **Threat Title: Intercepted Tokens**
  - Access tokens could be intercepted during transmission, exposing sensitive credentials. +

- **Threat Title: Sensitive Data Exposure in Resource Requests**
  - Sensitive data involved in protected resource requests could be exposed in transit. +

#### Denial of Service
- **Threat Title: DoS on Authorization Server**
  - An attacker may flood the authorization server with requests, leading to service unavailability. +

- **Threat Title: Resource Exhaustion on Resource Server**
  - Overloading the resource server with requests can exhaust resources, leading to denial of service. +

#### Elevation of Privilege
- **Threat Title: Unauthorized Token Generation**
  - Unauthorized actors could generate valid access tokens if vulnerabilities exist in the authorization server. -

- **Threat Title: Privilege Escalation through Access Tokens**
  - An attacker could exploit a flaw to escalate privileges using a compromised token. -

### DREAD Evaluation

#### Spoofing
- **Spoofed Authorization Request**: Moderate
- **Impersonation of Resource Owner**: High

#### Tampering
- **Tampered Authorization Code**: High
- **Tampered Access Token Request**: Moderate

#### Repudiation
- **Unauthorized Actions without Traceability**: Low

#### Information Disclosure
- **Intercepted Tokens**: High
- **Sensitive Data Exposure in Resource Requests**: Moderate

#### Denial of Service
- **DoS on Authorization Server**: High
- **Resource Exhaustion on Resource Server**: High

#### Elevation of Privilege
- **Unauthorized Token Generation**: High
- **Privilege Escalation through Access Tokens**: High

The DREAD scores are subjective and can vary based on specific implementation details and existing mitigations.