from tools.llm_tool import run_llm


def planner_agent(task):

    prompt = f"""
    You are a senior software architect.

    Create a step-by-step implementation plan.

    TASK:
    {task}

    Include:
    - architecture
    - files needed
    - dependencies
    - execution flow
    """

    return run_llm(prompt)