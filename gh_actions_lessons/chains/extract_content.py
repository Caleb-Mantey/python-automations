from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate



openai_api_key = "dsdsdsds"
class ExtractContentChain():
    def __init__(self, prompt_template: str, openai_api_key: str):
        self.prompt_template = ChatPromptTemplate.from_messages(['system', prompt_template])
        self.llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4o-mini", temperature=0,request_timeout=60)
        self.chain =( self.prompt_template | self.llm)

    def run(self, inputs: dict) -> dict:
        # prompt = self.prompt_template.format(**inputs)
        # response = self.llm(prompt)
        # result = {"result": response}
        result = self.chain.invoke(inputs)
        return result

# Example usage
if __name__ == "__main__":
    prompt_template = """
**Prompt:**  
You are provided with a list of cities, each containing information about the country, zip code, population, wealth level, and safety index. Your task is to filter this list based on the criteria provided below. Return the results formatted as a JSON array, where each object contains the city's name, country, zip code, population, wealth, and safety.  

### Filtering Rules:  
1. Only include cities that match all specified criteria.  
2. Criteria can include conditions such as:
   - Minimum or maximum population.  
   - Wealth level (e.g., "High", "Medium", "Low").  
   - Minimum or maximum safety index.  
   - Specific countries or continents.  
3. If no cities meet the criteria, return an empty JSON array `[]`.  

### Example Input Criteria:  
```json
{{
  "min_population": 1000000,
  "max_population": 10000000,
  "wealth": "High",
  "min_safety": 70,
  "countries": ["USA", "Canada", "Australia"]
}}
```

### Example Output Format:  
```json
[
  {{
    "city": "Toronto",
    "country": "Canada",
    "zip_code": "M5A 1A1",
    "population": 3000000,
    "wealth": "High",
    "safety": 70
  }},
  {{
    "city": "Sydney",
    "country": "Australia",
    "zip_code": "2000",
    "population": 5300000,
    "wealth": "High",
    "safety": 85
  }}
]
```

### Additional Notes:  
- Always validate that the input criteria are complete and handle cases where certain filters (e.g., "wealth") are omitted.  
- If a criterion like "countries" is absent, include cities from all countries.  
- Ensure the JSON is valid and correctly formatted.

**Input:**
Cities: {data}

Filtering Criteria: {criteria}
---
"""


    data = """
1. **USA** - **New York, NY**  
   - Zip Code: 10001  
   - Population: ~8.5 million  
   - Wealth: High (GDP per capita: ~$85,000)  
   - Safety: 52/100  

2. **Canada** - **Toronto, ON**  
   - Zip Code: M5A 1A1  
   - Population: ~3 million  
   - Wealth: High (GDP per capita: ~$60,000)  
   - Safety: 70/100  

3. **UK** - **London**  
   - Zip Code: SW1A 1AA  
   - Population: ~9 million  
   - Wealth: High (GDP per capita: ~$65,000)  
   - Safety: 66/100  

4. **Australia** - **Sydney, NSW**  
   - Zip Code: 2000  
   - Population: ~5.3 million  
   - Wealth: High (GDP per capita: ~$70,000)  
   - Safety: 85/100  

5. **Germany** - **Berlin**  
   - Zip Code: 10115  
   - Population: ~3.7 million  
   - Wealth: High (GDP per capita: ~$60,000)  
   - Safety: 72/100  

6. **France** - **Paris**  
   - Zip Code: 75001  
   - Population: ~2.2 million  
   - Wealth: High (GDP per capita: ~$55,000)  
   - Safety: 60/100  

7. **Italy** - **Rome**  
   - Zip Code: 00184  
   - Population: ~2.8 million  
   - Wealth: High (GDP per capita: ~$45,000)  
   - Safety: 55/100  

8. **Japan** - **Tokyo**  
   - Zip Code: 100-0001  
   - Population: ~14 million  
   - Wealth: High (GDP per capita: ~$45,000)  
   - Safety: 88/100  

9. **India** - **Mumbai, Maharashtra**  
   - Zip Code: 400001  
   - Population: ~20 million  
   - Wealth: Medium (GDP per capita: ~$8,000)  
   - Safety: 50/100  

10. **Brazil** - **São Paulo**  
    - Zip Code: 01000-000  
    - Population: ~12.3 million  
    - Wealth: Medium (GDP per capita: ~$12,000)  
    - Safety: 35/100  

11. **South Africa** - **Cape Town**  
    - Zip Code: 8001  
    - Population: ~4.8 million  
    - Wealth: Medium (GDP per capita: ~$15,000)  
    - Safety: 42/100  

12. **China** - **Beijing**  
    - Zip Code: 100000  
    - Population: ~22 million  
    - Wealth: Medium-High (GDP per capita: ~$18,000)  
    - Safety: 65/100  

13. **Russia** - **Moscow**  
    - Zip Code: 101000  
    - Population: ~12.4 million  
    - Wealth: Medium (GDP per capita: ~$12,000)  
    - Safety: 50/100  

14. **Mexico** - **Mexico City**  
    - Zip Code: 01000  
    - Population: ~9.2 million  
    - Wealth: Medium (GDP per capita: ~$9,000)  
    - Safety: 40/100  

15. **Netherlands** - **Amsterdam**  
    - Zip Code: 1012 WX  
    - Population: ~900,000  
    - Wealth: High (GDP per capita: ~$65,000)  
    - Safety: 78/100  

16. **Spain** - **Madrid**  
    - Zip Code: 28001  
    - Population: ~6.7 million  
    - Wealth: High (GDP per capita: ~$45,000)  
    - Safety: 70/100  

17. **Switzerland** - **Zurich**  
    - Zip Code: 8001  
    - Population: ~430,000  
    - Wealth: Very High (GDP per capita: ~$95,000)  
    - Safety: 90/100  

18. **Sweden** - **Stockholm**  
    - Zip Code: 111 22  
    - Population: ~975,000  
    - Wealth: High (GDP per capita: ~$60,000)  
    - Safety: 85/100  

19. **Argentina** - **Buenos Aires**  
    - Zip Code: C1001AAA  
    - Population: ~15 million  
    - Wealth: Medium (GDP per capita: ~$10,000)  
    - Safety: 48/100  

20. **New Zealand** - **Auckland**  
    - Zip Code: 1010  
    - Population: ~1.7 million  
    - Wealth: High (GDP per capita: ~$55,000)  
    - Safety: 88/100 
"""

    chain = ExtractContentChain(prompt_template, openai_api_key)
        
    inputs = {"data": data, "criteria": "This is the criteria to filter the data"}
    result = chain.run(inputs)
        
    print(result)