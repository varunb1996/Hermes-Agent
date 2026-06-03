from agents.planner_agent import planner_agent
from agents.executor_agent import executor_agent
from agents.reflection_agent import reflection_agent
from agents.repair_agent import repair_agent

from tools.file_tool import write_file
from tools.code_executor import execute_python
from tools.logger_tool import log_event


def supervisor_agent(task):

    log_event("Starting task")

    # PLAN
    plan = planner_agent(task)

    log_event("Planning complete")

    # GENERATE CODE
    code = executor_agent(plan)

    log_event("Code generation complete")

    # SAVE FILE
    write_file(
        "generated_code.py",
        code
    )

    # EXECUTE
    execution = execute_python(
        "generated_code.py"
    )

    # REFLECT
    reflection = reflection_agent(code)

    repaired_code = None

    # REPAIR LOOP
    if execution["stderr"]:

        repaired_code = repair_agent(
            code,
            execution["stderr"]
        )

        write_file(
            "repaired_code.py",
            repaired_code
        )

    log_event("Task complete")

    return {
        "plan": plan,
        "code": code,
        "execution": execution,
        "reflection": reflection,
        "repaired_code": repaired_code
    }