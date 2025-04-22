
# 🧠 Quiz Generator with GROQ

Learning just got smarter. Instantly turn any block of text into a custom multiple-choice quiz using the power of LLMs.

Whether you're a student, teacher, or just a knowledge junkie, this app helps reinforce understanding by auto-generating quizzes based on pasted content. Powered by **Groq** and **Meta’s LLaMA**, it makes learning interactive, personalized, and fun.

![Image](https://github.com/user-attachments/assets/077cddde-b0da-4e02-b5a3-27ec31a9826d)

## 🎥 Watch the Demo
[![YouTube Video](https://img.shields.io/badge/YouTube-Watch%20Demo-red?logo=youtube&logoColor=white&style=for-the-badge)](https://youtu.be/Zenvo0z6p4w)

---

## 📚 What is Quiz Generator?

This is a lightweight Streamlit-based web app that uses a **Groq-hosted LLaMA model** to generate 5 MCQs from any given text. Just paste the content, select difficulty, and click "Generate." Great for revising concepts, creating practice sets, or even gamifying reading sessions.

---

## ⚙️ Tech Stack

| Component           | Description                                                   |
|--------------------|---------------------------------------------------------------|
| 🧠 LLM             | LLaMA 4 via Groq API                                           |
| 🌐 API Provider    | [Groq Cloud](https://console.groq.com)                         |
| 🎨 UI Framework    | [Streamlit](https://streamlit.io) – For fast and sleek UIs     |
| 🔐 Env Management  | python-dotenv – Securely manage API keys and configs           |

---

## 🚀 Features

✅ Paste any text (articles, textbook excerpts, etc.)  
✅ Choose quiz difficulty (Easy / Medium / Hard)  
✅ Auto-generates 5 MCQs using LLMs  
✅ Clean, interactive UI  
✅ Instant feedback and scoring system  
✅ Runs locally with just two files  

---

## 🧪 How It Works

1. User pastes any text and selects quiz difficulty.
2. App sends a prompt to the **Groq-hosted LLaMA model**, instructing it to return 5 MCQs in JSON format.
3. JSON is parsed and rendered as a quiz in the UI.
4. After answering, the app displays correct/incorrect responses and a total score.

---

## 📂 File Structure

```
├── app.py               # Main Streamlit app – frontend + backend logic
├── requirements.txt     # All necessary Python packages
```

---

## 🧑‍💻 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/DataScientist00/MCQ-Generator-Llama4-Langchain.git
cd MCQ-Generator-Llama4-Langchain
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Setup your environment:
- Create a `.env` file and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key
```

4. Run the app:
```bash
streamlit run app.py
```

---

## 💡 Example Usage

📄 Input:
> "The water cycle consists of various stages like evaporation, condensation, precipitation, and collection..."

🎯 Difficulty: *Medium*

✅ Output (Sample):
- What is the stage where water vapor cools and becomes liquid?  
  A. Precipitation  
  B. Evaporation  
  C. Condensation *(Correct)*  
  D. Collection

---

## 🌍 Why Use This?

This quiz generator is perfect for:
- Teachers creating rapid quizzes for classroom material  
- Students testing their knowledge on readings  
- EdTech demos and interactive workshops  
- Anyone who loves smart learning tools 🎓

---

## 🧠 Future Enhancements

- Export quizzes as PDF or CSV  
- Add support for true/false and fill-in-the-blank questions  
- User login and progress tracking  
- Save and share quizzes  
- Drag-and-drop text file upload  

---

## 🙌 Acknowledgements

- [Groq Cloud](https://groq.com)
- [Meta LLaMA](https://ai.meta.com/llama/)
- [Streamlit](https://streamlit.io)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 📞 Contact

For feedback or collab ideas:

- **Email**: nikzmishra@gmail.com  
- **YouTube**: [Data Science Alchemist](https://www.youtube.com/@DataScience00/videos)

---

⭐ Star the repo if this helped you!  
Made with ❤️ to make learning more engaging and AI-powered.
