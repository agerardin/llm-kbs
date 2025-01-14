def generate_prompt_examples(exs: list[str,str]):
    ex_prompt = ""
    prompt = """
    example reaction description: {}, 
    example reaction output: {}"""
    for ex in exs:
        ex_prompt += prompt.format(ex[0], ex[1])
    return ex_prompt