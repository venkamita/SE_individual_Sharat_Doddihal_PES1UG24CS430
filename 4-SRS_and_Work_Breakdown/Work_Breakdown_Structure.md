# Work Breakdown Structure (WBS)
## Project: Automated Rubric Assignment Evaluator
**Student:** Sharat Doddihal | **SRN:** PES1UG24CS430

---

## 1. Introduction

The Work Breakdown Structure (WBS) decomposes the project into hierarchical work packages, making it easier to plan, assign, and track progress.

---

## 2. WBS Diagram (Text Format)

```
Automated Rubric Assignment Evaluator
│
├── 1. Project Management
│   ├── 1.1 Project Planning
│   ├── 1.2 Stakeholder Communication
│   └── 1.3 Progress Tracking & Reporting
│
├── 2. Requirements Engineering
│   ├── 2.1 Requirement Elicitation
│   ├── 2.2 Functional Requirements (FR) Documentation
│   ├── 2.3 Non-Functional Requirements (NFR) Documentation
│   └── 2.4 Requirements Traceability Matrix (RTM)
│
├── 3. System Design
│   ├── 3.1 Use Case Modeling
│   │   ├── 3.1.1 Use Case Diagram
│   │   └── 3.1.2 Use Case Specifications (UC-01 to UC-04)
│   ├── 3.2 Architectural Design
│   │   ├── 3.2.1 3-Tier Architecture Design
│   │   └── 3.2.2 Component Diagram
│   └── 3.3 Database Design
│       ├── 3.3.1 ER Diagram
│       └── 3.3.2 Schema Definition
│
├── 4. Implementation
│   ├── 4.1 Backend Development
│   │   ├── 4.1.1 Authentication Module
│   │   ├── 4.1.2 Submission Module
│   │   ├── 4.1.3 Evaluation Engine
│   │   ├── 4.1.4 Scoring Module
│   │   └── 4.1.5 Notification Service
│   ├── 4.2 Frontend Development
│   │   ├── 4.2.1 Student Portal UI
│   │   └── 4.2.2 Faculty Portal UI
│   └── 4.3 Integration
│       ├── 4.3.1 API Integration
│       └── 4.3.2 File Storage Integration
│
├── 5. Testing
│   ├── 5.1 Unit Testing
│   ├── 5.2 Integration Testing
│   ├── 5.3 System Testing
│   ├── 5.4 Performance Testing
│   └── 5.5 User Acceptance Testing (UAT)
│
└── 6. Deployment
    ├── 6.1 Environment Setup (Docker / Cloud)
    ├── 6.2 Deployment to Production
    └── 6.3 Post-Deployment Monitoring
```

---

## 3. Detailed Work Packages

### Phase 1: Requirements Engineering
| WBS ID | Task | Deliverable | Duration |
|---|---|---|---|
| 2.1 | Requirement Elicitation | Meeting notes, user stories | 1 week |
| 2.2 | FR Documentation | Functional_Requirements.md | 3 days |
| 2.3 | NFR Documentation | Non_Functional_Requirements.md | 2 days |
| 2.4 | RTM | RTM_Requirements_Traceability_Matrix.md | 2 days |

### Phase 2: System Design
| WBS ID | Task | Deliverable | Duration |
|---|---|---|---|
| 3.1 | Use Case Modeling | UC Diagram + Spec | 1 week |
| 3.2 | Architectural Design | Architecture Document | 1 week |
| 3.3 | Database Design | ER Diagram + Schema | 3 days |

### Phase 3: Implementation
| WBS ID | Task | Deliverable | Duration |
|---|---|---|---|
| 4.1 | Backend Development | REST API (all modules) | 4 weeks |
| 4.2 | Frontend Development | Student + Faculty UI | 3 weeks |
| 4.3 | Integration | End-to-end working system | 1 week |

### Phase 4: Testing
| WBS ID | Task | Deliverable | Duration |
|---|---|---|---|
| 5.1–5.5 | All Testing Phases | Test Reports | 2 weeks |

### Phase 5: Deployment
| WBS ID | Task | Deliverable | Duration |
|---|---|---|---|
| 6.1–6.3 | Deployment | Live System | 1 week |

---

## 4. Project Timeline Summary

| Phase | Duration | Milestone |
|---|---|---|
| Requirements Engineering | Week 1–2 | FR, NFR, RTM docs complete |
| System Design | Week 3–4 | Architecture, UC diagrams done |
| Implementation | Week 5–11 | All modules coded and integrated |
| Testing | Week 12–13 | All test reports complete |
| Deployment | Week 14 | System live and monitored |
