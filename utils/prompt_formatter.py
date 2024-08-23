def format_prompt(domain, expertise, task, user_input):
    
    # Formats the prompt based on the domain, expertise, task, and user input.
    
    prompt = f"Act as an expert in {domain}, I need help with {expertise} specifically for {task}."
    if user_input:
        prompt += f" Additionally, consider this requirement: {user_input}"
    return prompt
