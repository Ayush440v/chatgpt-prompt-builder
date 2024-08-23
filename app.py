import streamlit as st
from components.domain_options import get_domain_options
from components.expertise_options import get_expertise_options
from components.task_options import get_task_options
from models.prompt_builder import PromptBuilder

# Load domain options from the components module
domains = get_domain_options()

# Set the title of the Streamlit application
st.title("ChatGPT Prompt Builder")

# Step 1: Select Domain
# Create a dropdown (selectbox) for selecting a domain from the loaded domain options
selected_domain = st.selectbox("Select a Domain", options=domains)

# Step 2: Select Expertise based on selected domain
# If a domain is selected, load and display expertise options related to the selected domain
if selected_domain:
    expertise_options = get_expertise_options(selected_domain)
    selected_expertise = st.selectbox("Select Expertise", options=expertise_options)

# Step 3: Select Task based on selected expertise
# If an expertise is selected, load and display task options related to the selected expertise
if selected_expertise:
    task_options = get_task_options(selected_expertise)
    selected_task = st.selectbox("Select Task", options=task_options)

# Step 4: User input for specific requirements
# If a task is selected, provide a text area for the user to specify their requirements
if selected_task:
    user_input = st.text_area("Specify your requirements")

# Step 5: Generate Prompt
# When the "Generate Prompt" button is clicked, create a PromptBuilder instance and generate a prompt
if st.button("Generate Prompt"):
    prompt_builder = PromptBuilder(selected_domain, selected_expertise, selected_task, user_input)
    generated_prompt = prompt_builder.generate_prompt()
    # Display the generated prompt in a text area
    st.text_area("Generated Prompt", value=generated_prompt, height=200)

# Add custom styles if necessary
st.markdown(
    '<link rel="stylesheet" href="assets/styles.css">',
    unsafe_allow_html=True
)