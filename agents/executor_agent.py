from tools.llm_tool import run_llm


def executor_agent(plan):

    prompt = f"""
    Generate production-grade Python code.

    PLAN:
    {plan}

    Requirements:
    - scalable
    - modular
    - robust
    - documented
    """

    return run_llm(prompt)