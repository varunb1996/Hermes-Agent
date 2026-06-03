from agents.supervisor_agent import supervisor_agent


task = input(
    "Enter engineering task: "
)

result = supervisor_agent(task)

print("\nIMPLEMENTATION PLAN:\n")
print(result["plan"])

print("\nGENERATED CODE:\n")
print(result["code"])

print("\nEXECUTION RESULT:\n")
print(result["execution"])

print("\nREFLECTION:\n")
print(result["reflection"])

if result["repaired_code"]:

    print("\nREPAIRED CODE:\n")

    print(result["repaired_code"])