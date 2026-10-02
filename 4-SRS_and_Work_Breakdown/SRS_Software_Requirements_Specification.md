# Software Requirements Specification (SRS)
## Project: Automated Rubric Assignment Evaluator
**Student:** Sharat Doddihal | **SRN:** PES1UG24CS430  
**Date:** October 2026 | **Version:** 1.1

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) defines the complete requirements for the **Automated Rubric Assignment Evaluator** — a web-based system that automates evaluation of student project submissions using predefined rubrics, test case execution, and peer review assignment.

### 1.2 Scope
The system will:
- Accept project submissions from students
- Validate uploaded files
- Automatically run test cases and assign rubric-based scores
- Allow faculty to review and adjust scores
- Notify students of final results

---

## 2. Overall Description

### 2.1 Product Functions
The functions are grouped into **four main Epics**:
1. **Submission Management:** Uploading and validating project files.
2. **Automated Evaluation:** Queuing submissions, running test cases, generating rubric scores.
3. **Peer Review Assignment:** Assigning peers and flagging failed evaluations.
4. **Faculty Review & Results:** Faculty auditing, adjusting scores, and presenting final results.

### 2.2 User Classes
| User Class | Description |
|---|---|
| Student | Submits projects, views scores and feedback |
| Faculty Evaluator | Reviews AI-generated scores, manages rubrics |

---

## 3. Specific Requirements

### 3.1 Agile User Stories (Functional Requirements)
The functional requirements are structured as 10 User Stories tracked across 2 Sprints.

**Sprint 1: Core Workflow**
- **US-01 (Submit Project):** Student uploads project files.
- **US-02 (Validate Submission):** System validates file format and size.
- **US-03 (Add to Evaluation Queue):** System adds submission to asynchronous queue.
- **US-04 (Run Test Cases):** Evaluation Engine executes sandboxed test cases.
- **US-05 (Generate Rubric Score):** System calculates automated score based on rubric.

**Sprint 2: Review and Finalization**
- **US-06 (Assign Peer Reviewer):** System automatically assigns a peer to a successful submission.
- **US-07 (Flag Failed Evaluation):** System flags failing submissions for manual audit.
- **US-08 (Review Automated Score):** Faculty Evaluator reviews the system-generated score.
- **US-09 (Adjust Final Score):** Faculty Evaluator finalizes and modifies the score if needed.
- **US-10 (View Final Result):** Student views finalized result and feedback on the dashboard.

### 3.2 Non-Functional Requirements
- **Performance:** ≤ 2s response time, ≤ 5 min evaluation.
- **Security:** JWT/OAuth, RBAC, TLS 1.2+.
- **Availability:** 99.5% uptime.
- **Architecture:** Microservices (isolated Evaluation Engine).

---

## 4. Use Case Specifications

### Main Flow: Automated Evaluation (US-04, US-05)
1. System receives valid submission from the queue.
2. Evaluation engine executes predefined test cases.
3. System generates rubric-based score.
4. If score fails threshold, system flags it (US-07).
5. If passed, system triggers peer assignment (US-06).

**Exception Flow (E1) – Submission file corrupted (US-02):**
- File validation fails → submission rejected → student notified to resubmit.

*(See [`uc03_exception_flow.png`](../uc03_exception_flow.png) in root for visual exception flow diagram)*

---

## 5. Constraints
- System must be deployed on HTTPS only.
- Code execution must happen in an isolated sandbox environment (Microservice).

---

## 6. Appendices
- **Appendix A:** Activity Flow Diagram → [`fr_functional_activity_flow.png`](../fr_functional_activity_flow.png)
- **Appendix B:** Exception Flow Diagram → [`uc03_exception_flow.png`](../uc03_exception_flow.png)
- **Appendix C:** RTM → [`RTM_Requirements_Traceability_Matrix.md`](../1-RE/RTM_Requirements_Traceability_Matrix.md)
- **Appendix D:** UML Component Diagram → [`Lab3_Component_Diagram.png`](../2-Architectural_Diagram/Lab3_Component_Diagram.png)
