# Non-Functional Requirements (NFR)
## Project: Automated Rubric Assignment Evaluator
**Student:** Sharat Doddihal | **SRN:** PES1UG24CS430

---

## 1. Introduction

This document describes the **Non-Functional Requirements** that define the quality attributes, constraints, and operational standards of the Automated Rubric Assignment Evaluator system.

---

## 2. Non-Functional Requirements

### 2.1 Performance

| NFR ID | Requirement | Metric/Criteria |
|---|---|---|
| NFR-01 | Response Time | System must respond to user requests within **2 seconds** under normal load |
| NFR-02 | Evaluation Speed | Automated evaluation of a submission must complete within **5 minutes** |
| NFR-03 | Throughput | System must support at least **100 concurrent submissions** without degradation |

---

### 2.2 Reliability & Availability

| NFR ID | Requirement | Metric/Criteria |
|---|---|---|
| NFR-04 | System Uptime | System must achieve at least **99.5% uptime** during academic sessions |
| NFR-05 | Fault Tolerance | System must recover from single-point failures within **30 seconds** |
| NFR-06 | Data Persistence | Submission data must not be lost in the event of system crash (auto-save) |

---

### 2.3 Security

| NFR ID | Requirement | Metric/Criteria |
|---|---|---|
| NFR-07 | Authentication | All users must authenticate using secure login (JWT / OAuth 2.0) |
| NFR-08 | Authorization | Role-based access control (RBAC) must be enforced at all endpoints |
| NFR-09 | Data Encryption | All data in transit must be encrypted using **TLS 1.2+** |
| NFR-10 | Audit Logging | All score modifications by faculty must be logged with timestamp and user ID |

---

### 2.4 Usability

| NFR ID | Requirement | Metric/Criteria |
|---|---|---|
| NFR-11 | Learnability | A new user should be able to submit a project within **5 minutes** of first use |
| NFR-12 | Accessibility | UI must comply with **WCAG 2.1 AA** standards |
| NFR-13 | Mobile Support | System must be usable on mobile devices (responsive design) |

---

### 2.5 Maintainability & Scalability

| NFR ID | Requirement | Metric/Criteria |
|---|---|---|
| NFR-14 | Modularity | System must follow a modular architecture for easy feature addition |
| NFR-15 | Scalability | System must scale horizontally to support up to **10,000 registered users** |
| NFR-16 | Documentation | All APIs must have up-to-date documentation (Swagger / OpenAPI) |

---

### 2.6 Portability

| NFR ID | Requirement | Metric/Criteria |
|---|---|---|
| NFR-17 | Browser Compatibility | System must work on Chrome, Firefox, Edge (latest 2 major versions) |
| NFR-18 | Deployment | System must be deployable on cloud platforms (AWS, GCP, or Azure) |

---

## 3. Summary Table

| Category | # Requirements |
|---|---|
| Performance | 3 |
| Reliability & Availability | 3 |
| Security | 4 |
| Usability | 3 |
| Maintainability & Scalability | 3 |
| Portability | 2 |
| **Total** | **18** |
