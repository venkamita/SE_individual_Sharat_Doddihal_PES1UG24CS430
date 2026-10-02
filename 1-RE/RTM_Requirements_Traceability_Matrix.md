# Requirements Traceability Matrix (RTM)
## Project: Automated Rubric Assignment Evaluator
**Student:** Sharat Doddihal | **SRN:** PES1UG24CS430

---

## 1. Introduction
The **Requirements Traceability Matrix (RTM)** maps each User Story (FR) to its corresponding Epic, module, and test case to ensure full coverage.

---

## 2. RTM Table — Functional Requirements (User Stories)

| Epic | User Story ID | User Story Description | Module / Component | Test Case ID | Status |
|---|---|---|---|---|---|
| **Submission Management** | US-01 | Submit Project | Student Portal UI | TC-01 | ✅ Defined |
| **Submission Management** | US-02 | Validate Submission | Submission Manager | TC-02 | ✅ Defined |
| **Automated Evaluation** | US-03 | Add Submission to Evaluation Queue | Job Queue (Redis) | TC-03 | ✅ Defined |
| **Automated Evaluation** | US-04 | Run Test Cases | Evaluation Engine | TC-04 | ✅ Defined |
| **Automated Evaluation** | US-05 | Generate Rubric Score | Evaluation Engine | TC-05 | ✅ Defined |
| **Peer Review Assignment**| US-06 | Assign Peer Reviewer | Reviewer Assigner | TC-06 | ✅ Defined |
| **Peer Review Assignment**| US-07 | Flag Failed Evaluation | Evaluation Engine | TC-07 | ✅ Defined |
| **Faculty Review & Results**| US-08 | Review Automated Score | Faculty Dashboard | TC-08 | ✅ Defined |
| **Faculty Review & Results**| US-09 | Adjust Final Score | Faculty Dashboard | TC-09 | ✅ Defined |
| **Faculty Review & Results**| US-10 | View Final Result | Student Portal UI | TC-10 | ✅ Defined |

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

## 4. Coverage Summary

| Type | Total Requirements | Traced | Coverage |
|---|---|---|---|
| User Stories (Functional) | 10 | 10 | **100%** |
| Non-Functional | 18 | 18 | **100%** |
| **Total** | **28** | **28** | **100%** |
