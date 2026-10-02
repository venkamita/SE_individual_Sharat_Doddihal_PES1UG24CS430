import urllib.request

puml = """@startuml
!theme plain
skinparam componentStyle uml2

interface "Authentication API" as IAuth
interface "Submission API" as ISub
interface "Evaluation API" as IEval
interface "Database API" as IDB

component "Student Portal UI" as SP <<component>>
component "Auth Service" as Auth <<component>>
component "Submission Manager" as SM <<component>>
component "Evaluation Engine" as EE <<component>>
component "Database Component" as DB <<component>>

Auth -up- IAuth
SM -up- ISub
EE -up- IEval
DB -up- IDB

SP ..> IAuth : use
SP ..> ISub : use
SM ..> IEval : use
SM ..> IDB : use
EE ..> IDB : use

note right of SP : Frontend Application
note right of EE : Executes Sandboxed Code
@enduml"""

req = urllib.request.Request('https://kroki.io/plantuml/png', data=puml.encode('utf-8'), headers={'Content-Type': 'text/plain', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req) as response:
    with open('2-Architectural_Diagram/Lab3_Component_Diagram.png', 'wb') as f:
        f.write(response.read())
print('Diagram successfully generated and saved!')
