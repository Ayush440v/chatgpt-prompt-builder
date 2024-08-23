class PromptBuilder:
    
    # A class to generate prompts based on domain, expertise, task, and user input.
    

    def __init__(self, domain, expertise, task, user_input):
        # Initialize the PromptBuilder with domain, expertise, task, and user input
        self.domain = domain
        self.expertise = expertise
        self.task = task
        self.user_input = user_input

    def generate_prompt(self):
        
        # Generates a prompt based on the provided domain, expertise, task, and user input.
        
        # Create the base prompt using the domain, expertise, and task
        prompt = f"For the domain of {self.domain}, I need help with {self.expertise} specifically for {self.task}."
        
        # If there is additional user input, append it to the prompt
        if self.user_input:
            prompt += f" Additionally, consider this requirement: {self.user_input}"
        
        # Return the generated prompt
        return prompt