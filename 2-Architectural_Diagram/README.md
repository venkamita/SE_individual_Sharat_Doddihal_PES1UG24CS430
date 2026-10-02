# Architectural Diagram Folder

This folder contains the system architecture documentation and diagrams for the **Automated Rubric Assignment Evaluator**.

## Contents

| File | Description |
|---|---|
| [`Architecture_Document.md`](./Architecture_Document.md) | Complete architectural description including 3-tier layered architecture, component descriptions, data flow, and deployment architecture |
| *(Add visual diagrams here)* | Export draw.io / Lucidchart diagrams as PNG and place here |

## Architecture Summary

- **Pattern:** 3-Tier Layered Architecture
- **Frontend:** React.js / HTML5 (Student + Faculty portals)
- **Backend:** Node.js REST API + Python Evaluation Engine
- **Database:** PostgreSQL + File Storage (S3)
- **Auth:** JWT + OAuth 2.0
- **Deployment:** Docker + Kubernetes (Cloud)
