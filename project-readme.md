# FastAPI Chat Application with LangChain

A robust FastAPI backend application that handles chat interactions using LangChain and OpenAI's GPT models. This application follows MVC architecture and provides a clean API for chat interactions.

## 🚀 Features

- FastAPI backend with MVC architecture
- LangChain integration for chat completions
- OpenAI GPT model support
- Swagger/OpenAPI documentation
- Pydantic models for request/response validation
- Environment-based configuration
- CORS middleware support

## 📋 Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Git (for version control)

## 🛠️ Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Create and activate virtual environment
```bash
# For Windows
python -m venv project_common_environment
project_common_environment\Scripts\activate

# For Linux/Mac
python3.11 -m venv project_common_environment
source project_common_environment/bin/activate
```

3. Upgrade pip and install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Create `.env` file in the root directory
```env
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-3.5-turbo  # optional, this is the default
```

## 🚀 Running the Application

1. Start the server
```bash
python server.py
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📁 Project Structure

```
├── api/
│   └── chat_router.py
├── config/
│   └── settings.py
├── models/
│   └── chat.py
├── services/
│   └── chat_service.py
├── .env
├── main.py
├── server.py
├── requirements.txt
└── README.md
```

## 🔄 API Endpoints

### POST /api/v1/chat
Generate an AI chat response based on user prompt.

Example request:
```json
{
    "prompt": "What is the capital of France?",
    "context": "Discussing geography and European capitals"
}
```

Example response:
```json
{
    "response": "The capital of France is Paris.",
    "prompt": "What is the capital of France?"
}
```

## 💻 Development

To contribute to this project:

1. Create a new branch
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit
```bash
git add .
git commit -m "Add your message here"
```

3. Push to your branch
```bash
git push origin feature/your-feature-name
```

4. Create a Pull Request

## 🔧 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| OPENAI_API_KEY | Your OpenAI API key | Required |
| MODEL_NAME | GPT model to use | gpt-3.5-turbo |

## 📚 Dependencies

- fastapi==0.109.0
- uvicorn==0.27.0
- pydantic==2.5.3
- pydantic-settings==2.1.0
- python-dotenv==1.0.0
- langchain==0.1.0
- openai==1.3.0
- langchain-community==0.0.10
- langchain-core==0.1.8
- typing-extensions>=4.5.0

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI framework
- LangChain
- OpenAI

## 📧 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/your-repo-name](https://github.com/yourusername/your-repo-name)

---
⚡ Remember to replace placeholder values (your.email@example.com, yourusername, your-repo-name) with your actual information before committing.
