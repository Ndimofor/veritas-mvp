import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up Streamlit UI
st.set_page_config(page_title="Veritas: AI-Powered Truth Checker", layout="centered")
st.title("🔍 Veritas: AI-Powered Truth Checker")
st.markdown("Quickly analyze and verify the credibility of claims using AI.\n")

st.markdown("**Enter a claim you'd like to verify:**")
claim = st.text_area(" ", height=100)

# Response display
if st.button("Verify Claim") and claim.strip():
    with st.spinner("Analyzing..."):
        try:
            # Use OpenAI Chat API (v1.0+ syntax)
            response = openai.chat.completions.create(
                model="gpt-4",  # You can also use "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": "You are a truth-checking assistant. Analyze the user's claim and evaluate its accuracy."},
                    {"role": "user", "content": claim}
                ],
                temperature=0.3
            )
            result = response.choices[0].message.content.strip()
            st.success("✅ AI Analysis Complete:")
            st.markdown(result)

        except Exception as e:
            st.error("⚠️ An error occurred while verifying the claim.")
            st.code(str(e))
else:
    st.caption("Powered by Veritas • Built By Louis & ❤️ Streamlit")
