from tools.llm_tool import run_llm


def reflection_agent(code):

    prompt = f"""
    Review this code critically.

    Find:
    - bugs
    - edge cases
    - architecture issues
    - scalability problems

    CODE:
    {code}
    """

    return run_llm(prompt)