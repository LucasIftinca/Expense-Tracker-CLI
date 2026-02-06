import json
from datetime import date
from google import genai
from .models import Transaction

class AIAgent:
    def __init__(self, api_key: str):
        """
        Initializes the GenAI client using the stable v1 API version.
        """
        self.client = genai.Client(
            api_key=api_key,
            http_options={'api_version': 'v1'}
        )
        self.model_name = "gemini-2.0-flash"

    def parse_expense(self, user_input: str) -> Transaction:
        """
        Processes natural language to extract structured financial data.
        """
        today = date.today().isoformat()
        
        # Instruction prompt for precise JSON extraction
        prompt = f"""
        Extract expense data from the following text: "{user_input}"
        Today's date is {today}.
        
        Return ONLY a JSON object with this structure:
        {{
          "date": "YYYY-MM-DD",
          "category": "Food/Transport/Utilities/Entertainment/Shopping/Other",
          "amount": number,
          "description": "short summary"
        }}
        """
        
        try:
            # Calling the model via the stable API route
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            
            raw_text = response.text.strip()
            
            # Cleaning markdown delimiters if present
            if "```" in raw_text:
                raw_text = raw_text.split("```")[1]
                if raw_text.startswith("json"):
                    raw_text = raw_text[4:]
            
            data = json.loads(raw_text.strip())
            
            return Transaction(
                date=data.get("date", today),
                category=data.get("category", "Other"),
                amount=float(data.get("amount", 0.0)),
                description=data.get("description", "AI Entry")
            )
        except Exception as e:
            # English comment: Log parsing errors for debugging
            print(f"\n❌ AI parsing failed: {e}")
            return None