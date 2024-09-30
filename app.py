import streamlit as st
import requests
import re

# Replace with your actual Groq API key
GROQ_API_KEY = "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"

def generate_content(topic, max_length=1000):
    # Prepare the prompt for content generation
    prompt = f"Generate the best solutions and advice to the problem in the topic: {topic}\n\n"

    # Make an API call to Groq
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    
    # Assuming the Groq API has an endpoint like this (adjust according to their docs)
    api_url = "https://api.groq.com/v1/completions"  # Update based on Groq's actual API URL
    
    data = {
        "prompt": prompt,
        "max_tokens": max_length,
    }
    
    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        generated_content = response.json().get("choices", [])[0].get("text", "")
        # Optionally split the generated content into pages
        pages = re.split(r"\n{2,}", generated_content)  # Split by two newlines for better structure
        return pages
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return []

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
