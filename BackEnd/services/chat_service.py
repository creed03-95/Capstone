from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from config.settings import settings
from models.chat import ChatPrompt, ChatResponse

class ChatService:
    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=0.7
        )
        
        self.prompt_template = PromptTemplate(
            input_variables=["context", "prompt"],
            template="""
            Context: {context}
            User: {prompt}
            Assistant: Let me help you with that.
            """
        )
        
        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt_template
        )
    
    async def generate_response(self, chat_prompt: ChatPrompt) -> ChatResponse:
        context = chat_prompt.context if chat_prompt.context else "No additional context provided."
        
        response = await self.chain.ainvoke({
            "context": context,
            "prompt": chat_prompt.prompt
        })
        
        return ChatResponse(
            response=response["text"],
            prompt=chat_prompt.prompt
        )
