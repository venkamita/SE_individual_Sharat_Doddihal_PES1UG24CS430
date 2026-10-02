# Architecture Selection: We chose Microservices Architecture for the Automated Rubric Assignment Evaluator System.

## Architectural Choice
We selected **Microservices Architecture** because it allows us to decouple the resource-intensive code evaluation process from the core web portal functionalities, ensuring the system remains scalable, isolated, and highly available.

## Two Reasons
1. **Independent Scalability:** The Evaluation Engine requires heavy computational resources to compile and run student test cases in sandboxed environments. With microservices, we can independently scale the Evaluation Engine horizontally during peak submission times (e.g., hours before an assignment deadline) without needing to duplicate the entire web server or database infrastructure.
2. **Fault Isolation:** If a student submits a malicious or infinite-looping script that causes the evaluation sandbox to crash, the failure is isolated to that specific microservice instance. The rest of the system (Authentication, Student Portal, and Submissions) remains fully operational and unaffected.

## Security Advantage
By using Microservices, the **Evaluation Engine** (which executes untrusted, third-party student code) can be hosted in a strictly isolated, secure network segment (a VPC or isolated Kubernetes namespace) with no direct access to the internet or the main database. It communicates only via tightly controlled APIs, preventing any malicious code from compromising the main system or accessing sensitive user data.

## Performance Benefit
This architecture provides superior performance through **asynchronous processing**. When a student uploads a large project, the Submission Manager simply accepts the file and queues a message to the Evaluation Engine. This immediate offloading frees up the Submission Manager to instantly respond to the user, ensuring the UI remains highly responsive rather than forcing the user to wait for the evaluation to finish synchronously.
