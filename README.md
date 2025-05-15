* ✅ DeepSeek Janus (image gen)
* ✅ DeepSeek R1 (text gen)
* ✅ Bolt.diy full-stack app
* ✅ Roo Code + Aider app
* ✅ Cursor placeholder (mentioning intent)

---

# 🤖 Multimodal AI App Suite – DeepSeek, Bolt.diy, Roo Code, Cursor

This repo showcases a suite of AI-driven tools and workflows integrated into full-stack and multimodal projects. Each section demonstrates a different AI engineering tool.

---

## 📌 Components Overview

| Tool        | Purpose                                 |
|-------------|------------------------------------------|
| 🔮 DeepSeek Janus | Image generation via prompt and image |
| 🧠 DeepSeek R1   | Text-to-text conversation generation |
| ⚛️ Bolt.diy       | GUI codegen for frontend + backend app |
| 🛠 Roo Code + Aider | Backend + frontend code locally with AI |
| 🧪 Cursor (placeholder) | Keras MNIST model generation (TBD) |

---

## 🧠 1. DeepSeek Janus – Prompt & Image Multimodal AI

Colab Notebook: [📄 View Janus Notebook](https://colab.research.google.com/drive/1weEAvIaScNpRxYJOXjSubyKqqWFe6uIe?usp=sharing)

### ✅ Tasks:
- Text-to-image generation with surreal prompts
- Image upload (e.g. animal) → extract insights
- Used Janus Pro checkpoint (`deepseek-vl-7b-chat`)

---

## 💬 2. DeepSeek R1 – Text-to-Text Reasoning + Chat

Colab Notebook: [📄 View R1 Notebook](https://colab.research.google.com/drive/1i2VIuTSjpxil8k5qichH5_ceX4igQ-le?usp=sharing)

### ✅ Tasks:
- Prompt-driven creative writing and Q&A
- LLM chat capabilities using R1 inference
- Explored prompts based on [DeepSeek R1 Guide](https://www.datacamp.com/blog/deepseek-r1)

---

## 🔩 3. Bolt.diy – Compliment Generator Web App

### Prompt Used:
```

Build a compliment generator app with a /compliment endpoint and a frontend with a button that displays it.

```

### Tech Stack:
- Vite + React + TailwindCSS + Shadcn
- Auto-generated component structure
- Compliment API + interactive UI

### ✅ Demo:
- Button fetches `/compliment` and displays result
- Built and previewed via Electron GUI

🎥 **Walkthrough Video** included in submission folder

---

## 💻 4. Roo Code + Aider – Flask Full Stack App

### ✅ App Description:
- Backend: Flask
- Endpoint: `/hello` → returns `"Hello from Roo!"`
- Manually tested via browser

### Roo Prompt:
```

Create a Flask app with a /hello endpoint that returns "Hello from Roo!".

```

### Aider (Optional Usage):
- Aider was used for VS Code enhancements and fast iteration
- No backend AI integration was needed beyond Roo

📸 Screenshots included for Roo code generation and Flask output

---

## ⚠️ 5. Cursor – MNIST Classifier (Placeholder)

> This was not implemented in this phase, but if implemented, it would involve:
- Generating an MNIST digit classifier using `Keras`
- Including model accuracy, loss, confusion matrix, etc.
- Sharing full code walkthrough via Cursor interface
- YouTube video walkthrough (TBD)

---

## 📂 Project Structure

```

├── bolt\_app/                     # Bolt.diy frontend project
├── backend/                      # Flask backend created by Roo
│   └── app.py
├── colabs/
│   ├── deepseek\_janus.ipynb
│   └── deepseek\_r1.ipynb
├── screenshots/
│   └── \[UI and CLI captures]
├── README.md
└── video/                        # Video walkthroughs (if recorded)

```

---

## 🧪 How to Run

### Flask API:
```bash
cd backend
python app.py
# Visit: http://127.0.0.1:5000/hello
```

### Bolt.diy App:

```bash
cd bolt_app
pnpm install
pnpm dev
# Visit: http://localhost:5173
```

---

## ✅ Submission Checklist

* [x] DeepSeek Janus Colab ✅
* [x] DeepSeek R1 Colab ✅
* [x] Bolt.diy full stack app ✅
* [x] Roo Code backend with browser test ✅
* [ ] Cursor MNIST classifier (not implemented yet)

---
