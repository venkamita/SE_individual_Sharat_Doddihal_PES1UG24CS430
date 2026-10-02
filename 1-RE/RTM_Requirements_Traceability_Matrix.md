# Requirements Traceability Matrix (RTM)
## Project: Automated Rubric Assignment Evaluator
**Student:** Sharat Doddihal | **SRN:** PES1UG24CS430

---

## 1. Introduction

The **Requirements Traceability Matrix (RTM)** maps each requirement to its corresponding design element, implementation module, and test case. This ensures full coverage and helps track implementation progress.

---

## 2. RTM Table — Functional Requirements

| Req ID | Requirement Description | Use Case | Module / Component | Test Case ID | Status |
|---|---|---|---|---|---|
| FR-01 | User Registration & Login | UC-00 | Auth Service | TC-01 | ✅ Defined |
| FR-02 | Project Submission | UC-01 | Submission Module | TC-02 | ✅ Defined |
| FR-03 | File Validation | UC-01 | File Validator | TC-03 | ✅ Defined |
| FR-04 | Automated Test Case Execution | UC-03 | Test Runner Engine | TC-04 | ✅ Defined |
| FR-05 | Rubric-Based Scoring | UC-03 | Scoring Engine | TC-05 | ✅ Defined |
| FR-06 | Peer Reviewer Assignment | UC-02 | Reviewer Assigner | TC-06 | ✅ Defined |
| FR-07 | Flagged Submission Review | UC-03 | Faculty Dashboard | TC-07 | ✅ Defined |
| FR-08 | Score Adjustment by Faculty | UC-03 | Score Manager | TC-08 | ✅ Defined |
| FR-09 | Score Finalization | UC-03 | Score Manager | TC-09 | ✅ Defined |
| FR-10 | Result Notification | UC-04 | Notification Service | TC-10 | ✅ Defined |
| FR-11 | Submission History | UC-04 | Student Dashboard | TC-11 | ✅ Defined |
| FR-12 | Rubric Management | — | Rubric Manager | TC-12 | ✅ Defined |
| FR-13 | Report Generation | — | Report Service | TC-13 | ✅ Defined |
| FR-14 | Dashboard | — | UI Layer | TC-14 | ✅ Defined |

---

## 3. RTM Table — Non-Functional Requirements

| Req ID | Requirement Description | Design Element | Verification Method | Status |
|---|---|---|---|---|
| NFR-01 | Response Time ≤ 2 sec | Load Balancer + Caching | Performance Testing (JMeter) | ✅ Defined |
| NFR-02 | Evaluation ≤ 5 min | Async Job Queue | Integration Testing | ✅ Defined |
| NFR-03 | 100 Concurrent Submissions | Horizontal Scaling | Stress Testing | ✅ Defined |
| NFR-04 | 99.5% Uptime | HA Deployment (Cloud) | Monitoring (Uptime Robot) | ✅ Defined |
| NFR-05 | Fault Recovery ≤ 30 sec | Auto-restart Service | Chaos Testing | ✅ Defined |
| NFR-06 | Data Persistence | DB Transactions + Backup | Recovery Testing | ✅ Defined |
| NFR-07 | Secure Authentication | JWT / OAuth 2.0 | Security Audit | ✅ Defined |
| NFR-08 | RBAC Authorization | Middleware Auth Guard | Unit Testing | ✅ Defined |
| NFR-09 | TLS 1.2+ Encryption | HTTPS Enforcement | SSL Scan | ✅ Defined |
| NFR-10 | Audit Logging | Log Service | Manual Review | ✅ Defined |
| NFR-11 | Learnability ≤ 5 min | UX Design | Usability Testing | ✅ Defined |
| NFR-12 | WCAG 2.1 AA | Accessible UI Components | Accessibility Audit | ✅ Defined |
| NFR-13 | Mobile Responsive | Responsive CSS | Cross-device Testing | ✅ Defined |
| NFR-14 | Modular Architecture | Microservices / Layered | Code Review | ✅ Defined |
| NFR-15 | Scale to 10,000 Users | Cloud Auto-scaling | Load Testing | ✅ Defined |
| NFR-16 | API Documentation | Swagger / OpenAPI | Doc Review | ✅ Defined |
| NFR-17 | Browser Compatibility | Cross-browser CSS | Manual Testing | ✅ Defined |
| NFR-18 | Cloud Deployment | Docker + K8s | Deployment Testing | ✅ Defined |

---

## 4. Use Case to Requirement Mapping

| Use Case | Functional Requirements Covered |
|---|---|
| UC-01: Submit Project | FR-02, FR-03 |
| UC-02: Assign Peer Reviewer | FR-06 |
| UC-03: Evaluate Submission | FR-04, FR-05, FR-07, FR-08, FR-09 |
| UC-04: View Results | FR-10, FR-11 |

---

## 5. Coverage Summary

| Type | Total Requirements | Traced | Coverage |
|---|---|---|---|
| Functional | 14 | 14 | **100%** |
| Non-Functional | 18 | 18 | **100%** |
| **Total** | **32** | **32** | **100%** |
