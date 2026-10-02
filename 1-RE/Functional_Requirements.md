# Functional Requirements (FR)
## Project: Automated Rubric Assignment Evaluator
**Student:** Sharat Doddihal | **SRN:** PES1UG24CS430

---

## 1. Introduction

This document outlines the **Functional Requirements** for the Automated Rubric Assignment Evaluator system. The system automates student project submission evaluation using predefined rubrics and supports peer reviewer assignment.

---

## 2. Actors

| Actor | Description |
|---|---|
| **Student** | Submits project files for evaluation |
| **Faculty Evaluator** | Reviews and adjusts AI-generated scores |
| **System (Automated)** | Runs test cases, scores submissions, assigns peers |

---

## 3. Functional Requirements

| FR ID | Requirement Name | Description | Priority |
|---|---|---|---|
| FR-01 | User Registration & Login | Students and faculty must be able to register and log in securely | High |
| FR-02 | Project Submission | Student must be able to upload project files (zip, pdf, etc.) to the system | High |
| FR-03 | File Validation | System must validate uploaded files for format, size, and completeness | High |
| FR-04 | Automated Test Case Execution | System must automatically run predefined test cases against submitted code | High |
| FR-05 | Rubric-Based Scoring | System must evaluate submissions against defined rubrics and generate scores | High |
| FR-06 | Peer Reviewer Assignment | System must automatically assign peer reviewers to submissions | Medium |
| FR-07 | Flagged Submission Review | Faculty must be able to view and manually review flagged submissions | High |
| FR-08 | Score Adjustment by Faculty | Faculty Evaluator must be able to modify scores before finalization | High |
| FR-09 | Score Finalization | System must finalize and lock scores after faculty approval | Medium |
| FR-10 | Result Notification | System must notify students about their final evaluation results | Medium |
| FR-11 | Submission History | Students must be able to view past submissions and their scores | Low |
| FR-12 | Rubric Management | Faculty must be able to create, update, and delete rubrics | Medium |
| FR-13 | Report Generation | System must generate evaluation reports for faculty | Low |
| FR-14 | Dashboard | Both students and faculty must have a personalized dashboard | Medium |

---

## 4. Use Case Summary

### UC-01: Submit Project
- **Actor:** Student
- **Main Flow:** Student logs in → uploads project files → system validates → confirms submission

### UC-02: Assign Peer Reviewer
- **Actor:** System
- **Main Flow:** Submission received → system selects eligible peer reviewer → notifies reviewer

### UC-03: Evaluate Submission
- **Actor:** System, Faculty Evaluator
- **Main Flow:** System runs test cases → generates rubric scores → Faculty reviews → adjusts if needed → finalizes

### UC-04: View Results
- **Actor:** Student
- **Main Flow:** Student logs in → navigates to results → views score and feedback

---

## 5. Activity Flow Reference

See `fr_functional_activity_flow.png` (in root) for the complete functional activity flow diagram.
