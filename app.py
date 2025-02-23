import streamlit as st
import openai
import os

def get_openai_response(prompt, api_key):
    """Function to generate AI responses using OpenAI's latest API."""
    openai_client = openai.OpenAI(api_key=api_key)
    
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an interview preparation assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
def main():
    st.title("AI-Powered Interview Prep Tool")
    
    st.sidebar.header("Settings")
    api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
    
    st.write("This tool helps you generate and refine interview responses using AI.")
    
    job_description = st.text_area("Paste the job description here:")
    question = st.text_input("Enter an interview question:")
    
    if st.button("Generate Answer"):
        if api_key and job_description and question:
            prompt = f"Job Description: {job_description}\n\nInterview Question: {question}\n\nProvide a STAR-format response."
            answer = get_openai_response(prompt, api_key)
            st.subheader("AI-Generated Answer:")
            st.write(answer)
        else:
            st.warning("Please enter your API key, job description, and question.")
    
    st.subheader("Refine Your Answer:")
    refinement_options = [
        "Make it more concise",
        "Add more technical details",
        "Improve storytelling",
        "Emphasize leadership aspects"
    ]
    selected_refinement = st.radio("Select a refinement option:", refinement_options)
    
    if st.button("Refine Answer"):
        if api_key and selected_refinement:
            refinement_prompt = f"Refine the following response by applying: {selected_refinement}.\n\n{answer}"
            refined_answer = get_openai_response(refinement_prompt, api_key)
            st.subheader("Refined Answer:")
            st.write(refined_answer)
        else:
            st.warning("Please generate an answer first and select a refinement option.")

if __name__ == "__main__":
    main()
