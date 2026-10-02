# Architectural Diagram Folder

This folder contains the system architecture documentation and diagrams for the **Automated Rubric Assignment Evaluator**.

## Contents

| File | Description |
|---|---|
| [`Architecture_Document.md`](./Architecture_Document.md) | Complete architectural description including 3-tier layered architecture, component descriptions, data flow, and deployment architecture |
| [`Lab3_Component_Diagram.png`](./Lab3_Component_Diagram.png) | Generated UML Component Diagram (5 components, 4 interfaces, ball/socket notation) |
| [`Lab3_Architecture_Justification.md`](./Lab3_Architecture_Justification.md) | Lab 3 required architecture justification (Microservices: 2 reasons, security, performance) |
| [`Lab3_Component_Diagram_Instructions.md`](./Lab3_Component_Diagram_Instructions.md) | PlantUML source code used to generate the component diagram |

## Component Diagram Preview

![Lab 3 UML Component Diagram](./Lab3_Component_Diagram.png)

## Architecture Summary

- **Pattern:** 3-Tier Layered Architecture
- **Frontend:** React.js / HTML5 (Student + Faculty portals)
- **Backend:** Node.js REST API + Python Evaluation Engine
- **Database:** PostgreSQL + File Storage (S3)
- **Auth:** JWT + OAuth 2.0
- **Deployment:** Docker + Kubernetes (Cloud)
