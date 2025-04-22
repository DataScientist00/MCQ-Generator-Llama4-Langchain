import streamlit as st
import json
import os
import re
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@st.cache_data     # "Only run this function again if the inputs change."
def fetch_questions_raw(text_content, quiz_level):
    sample_format = {
        "mcqs": [
            {
                "mcq": "Sample question?",
                "options": {
                    "a": "Option A",
                    "b": "Option B",
                    "c": "Option C",
                    "d": "Option D"
                },
                "correct": "a"
            }
        ]
    }

    prompt = f"""
        Text: {text_content}

        You are an expert quiz generator. Based on the above text_content, create 5 multiple choice questions with difficulty level '{quiz_level}'.

        ⚠️ Respond with ONLY valid JSON matching the format below. Do not include any explanation or extra text.

        {json.dumps(sample_format, indent=2)}
        """

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    content = response.choices[0].message.content.strip()
    # Remove triple backticks if present
    content = re.sub(r"^```json|```$", "", content, flags=re.MULTILINE).strip()
    return content


def main():
    st.title("🧠 Quiz Generator with GROQ")
    text_content = st.text_area("📄 Paste content for quiz:", height=200)
    quiz_level = st.selectbox("🎯 Choose difficulty:", ["Easy", "Medium", "Hard"]).lower()

    session_state = st.session_state
    if 'quiz_generated' not in session_state:
        session_state.quiz_generated = False

    if not session_state.quiz_generated:
        session_state.quiz_generated = st.button("🚀 Generate Quiz")

    if session_state.quiz_generated and text_content:
        raw_output = fetch_questions_raw(text_content, quiz_level)

        try:
            questions = json.loads(raw_output).get("mcqs", [])
        except json.JSONDecodeError:
            st.error("❌ Model did not return valid JSON.")
            return

        st.divider()
        st.subheader("📝 Your Quiz:")
        selected_options = []
        correct_answers = []

        for q in questions:
            opts = list(q["options"].values())
            selected = st.radio(q["mcq"], opts, index=None)
            selected_options.append(selected)
            correct_answers.append(q["options"][q["correct"]])

        if st.button("✅ Submit Answers"):
            st.balloons()
            score = 0
            st.subheader("📊 Results:")
            for i, q in enumerate(questions):
                st.markdown(f"**Q{i+1}. {q['mcq']}**")
                st.write(f"Your answer: {selected_options[i]}")
                st.write(f"Correct answer: {correct_answers[i]}")
                if selected_options[i] == correct_answers[i]:
                    score += 1
                st.markdown("---")
            st.success(f"🎉 You scored **{score} / {len(questions)}**")

if __name__ == "__main__":
    main()
        
    
    



  
     
      
    
        
    
    
    
