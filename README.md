# SE Individual Assignment — Automated Rubric Assignment Evaluator

**Name:** Sharat Doddihal  
**SRN:** PES1UG24CS430  
**Course:** Software Engineering Lab  

---

## Project Overview

This project focuses on designing and documenting an **Automated Rubric Assignment Evaluator** — a web-based system that automates the evaluation of student project submissions. The system accepts project files, runs predefined test cases, generates rubric-based scores, and assigns peer reviewers automatically. The Faculty Evaluator can review and modify generated scores before they are finalized and shown to the student.

### Main Actors
- 🎓 **Student** — Submits project, views results
- 👩‍🏫 **Faculty Evaluator** — Reviews, adjusts, and finalizes scores

### Core Features
- Project file submission & validation
- Automated test case execution
- Rubric-based scoring engine
- Automatic peer reviewer assignment
- Faculty score review & adjustment
- Final result notification to student

---

## 📁 Repository Structure

```
SE_individual_Sharat_Doddihal_PES1UG24CS430/
│
├── 📁 1-RE/                          ← Requirements Engineering
│   ├── Functional_Requirements.md
│   ├── Non_Functional_Requirements.md
│   ├── RTM_Requirements_Traceability_Matrix.md
│   └── README.md
│
├── 📁 2-Architectural_Diagram/        ← System Architecture
│   ├── Architecture_Document.md
│   └── README.md
│
├── 📁 3-Project_Creation_Screenshots/ ← GitHub & Jira Screenshots (to be added)
│   └── README.md
│
├── 📁 4-SRS_and_Work_Breakdown/       ← SRS & WBS
│   ├── SRS_Software_Requirements_Specification.md
│   ├── Work_Breakdown_Structure.md
│   └── README.md
│
├── 📁 5-GitHub_Copilot_Code/          ← AI-Generated Code & Screenshots
│   └── README.md
│
├── _Automated Rubric Assignment Evaluator.pdf   ← Original submission PDF
├── fr_functional_activity_flow.png              ← Activity flow diagram
├── uc03_exception_flow.png                      ← UC-03 exception flow diagram
└── README.md                                    ← This file
```

---

## 📋 Deliverables Index

### 1️⃣ Requirements Engineering (RE) → [`1-RE/`](./1-RE/)

| Document | Description |
|---|---|
| [Functional_Requirements.md](./1-RE/Functional_Requirements.md) | 14 Functional Requirements (FR-01 to FR-14) |
| [Non_Functional_Requirements.md](./1-RE/Non_Functional_Requirements.md) | 18 Non-Functional Requirements across 6 quality categories |
| [RTM_Requirements_Traceability_Matrix.md](./1-RE/RTM_Requirements_Traceability_Matrix.md) | Full RTM linking every requirement to design, module, and test case |

---

### 2️⃣ Architectural Diagram → [`2-Architectural_Diagram/`](./2-Architectural_Diagram/)

| Document | Description |
|---|---|
| [Architecture_Document.md](./2-Architectural_Diagram/Architecture_Document.md) | 3-Tier architecture overview, component descriptions, data flow, deployment diagram |

**Architecture Summary:**
- Pattern: 3-Tier Layered Architecture
- Frontend: React.js / HTML5
- Backend: Node.js + Python Evaluation Engine
- Database: PostgreSQL + File Storage (S3)

---

### 3️⃣ Project Creation Screenshots → [`3-Project_Creation_Screenshots/`](./3-Project_Creation_Screenshots/)

> 📸 **To be added by student** — Screenshots of project setup in GitHub and Jira tool.

---

### 4️⃣ SRS & Work Breakdown → [`4-SRS_and_Work_Breakdown/`](./4-SRS_and_Work_Breakdown/)

| Document | Description |
|---|---|
| [SRS_Software_Requirements_Specification.md](./4-SRS_and_Work_Breakdown/SRS_Software_Requirements_Specification.md) | Complete SRS v1.0 with all requirements, use case specs, constraints |
| [Work_Breakdown_Structure.md](./4-SRS_and_Work_Breakdown/Work_Breakdown_Structure.md) | Hierarchical WBS with 6 phases, work packages, and 14-week timeline |

---

### 5️⃣ GitHub Copilot Generated Code → [`5-GitHub_Copilot_Code/`](./5-GitHub_Copilot_Code/)

| Document | Description |
|---|---|
| [README.md](./5-GitHub_Copilot_Code/README.md) | Copilot usage summary, sample generated code (file upload, JWT auth, rubric scorer), and instructions for adding screenshots |

**Repository Link:** [venkamita/SE_individual_Sharat_Doddihal_PES1UG24CS430](https://github.com/venkamita/SE_individual_Sharat_Doddihal_PES1UG24CS430)

---

## 📊 Requirements Summary

| Type | Count | Status |
|---|---|---|
| Functional Requirements | 14 | ✅ Documented |
| Non-Functional Requirements | 18 | ✅ Documented |
| Use Cases | 4 | ✅ Specified |
| RTM Coverage | 32/32 | ✅ 100% |

---

## 🔗 Key Diagrams

| Diagram | File |
|---|---|
| Functional Activity Flow | [fr_functional_activity_flow.png](./fr_functional_activity_flow.png) |
| UC-03 Exception Flow | [uc03_exception_flow.png](./uc03_exception_flow.png) |

---

## 📄 Original Submission

The original PDF submission (Lab 1) is available at: [_Automated Rubric Assignment Evaluator.pdf](./_Automated%20Rubric%20Assignment%20Evaluator.pdf)

---

*Last Updated: October 2026*
