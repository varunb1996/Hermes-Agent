from tools.llm_tool import run_llm


def repair_agent(code, errors):

    prompt = f"""
    Fix the following Python code.

    CODE:
    {code}

    ERRORS:
    {errors}

    Return corrected code only.
    """

    return run_llm(prompt)