import streamlit as st
from langchain.llms import OpenAI
import re

# Initialize OpenAI LLM with your API key
llm = OpenAI(model="text-davinci-003", openai_api_key="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")

def generate_content(topic, max_length=1000):
    # Prepare the prompt for content generation
    prompt = f"Generate the best solutions and advice to the problem in the topic: {topic}\n\n"
    
    # Generate the content using the LLM
    generated_content = llm(prompt)
    
    # Optionally split the generated content into smaller sections or pages
    pages = re.split(r"\n{2,}", generated_content)  # Split by two newlines for better structure
    
    return pages

def download_text(text):
    # Save the generated solutions into a text file
    with open("generated_solutions.txt", "w", encoding="utf-8") as file:
        file.write(text)
    
    # Provide a download button to download the file
    with open("generated_solutions.txt", "rb") as file:
        st.download_button(
            label="Download Generated Solutions",
            data=file,
            file_name="generated_solutions.txt",
            mime="text/plain"
        )

def main():
    st.title("AI Solutions for Mental Well-being")
    st.write("Enter a problem you're facing and let the AI generate solutions.")
    
    # Get user input for the topic
    topic = st.text_input("Enter a problem:")
    
    if st.button("Generate Solutions"):
        if topic:
            # Generate the content
            pages = generate_content(topic)
            
            # Display the generated content
            st.subheader("Generated Solutions")
            for i, page_content in enumerate(pages, start=1):
                st.write(f"### Page {i}")
                st.write(page_content)
                st.write("---")
            
            # Download the generated content as a text file
            download_text("\n".join(pages))
        else:
            st.warning("Please enter a topic to generate solutions.")

if __name__ == "__main__":
    main()
