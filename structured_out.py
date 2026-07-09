# from pydantic import BaseModel
# from google import genai
# from google.genai import types
# import json

# client = genai.Client(api_key="AQ.Ab8RN6LZYQuaECx70GsGmoPsRidFysrPgdBevv-MhjMR-lIjFw")

# class recipe(BaseModel):
#     title: str
#     ingradients: list[str]
#     calories : int
#     prepration_time_minutes : float 

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents='''Give me a simple Indian dal recipe.
#     return only JSON with these keys: title,calories,prepration_time_minutes.''',
#     config = types.GenerateContentConfig(
#         response_mime_type= "application/json",
#         response_schema=recipe
#     )
# )
# reply = response.parsed
# print(reply)


## Exercise: Customer review analyzer
# Companies drown in free-text reviews. Let's turn one into structured data your code can sort and chart.
# Given this review:
# "I ordered the wireless earbuds last week. Sound quality is amazing and battery lasts all day, but the case feels cheap and it arrived two days late. Probably won't buy from this brand again."
# 1. Create a Pydantic model ReviewAnalysis with these fields:
# sentiment: str (should come back as "positive", "negative", or "neutral")
# rating: int (the model's guess, 1 to 5)
# pros: list[str]
# cons: list[str]
# 2. Send the review with response_schema=.
# 3. Print the sentiment and rating, then loop over pros and cons and print each one.

import os
from pydantic import BaseModel , Field
from google import genai
from google.genai import types
client = genai.Client(api_key="")

class ReviewAnalysis(BaseModel):
    sentiment: str = Field(description ="positive negative neutral")
    rating: int = Field(description="The model's guess, 1 to 5")
    pros: list[str]
    cons: list[str]
    recommended_action: str

review_text = "I ordered the wireless earbuds last week. Sound quality is amazing and battery lasts all day, but the case feels cheap and it arrived two days late. Probably won't buy from this brand again."


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Analyze the review {review_text}",
    config={
    "response_mime_type": "application/json",
    "response_schema": ReviewAnalysis,
}
) 
analysis: ReviewAnalysis = response.parsed
print(f"Sentiment: {analysis.sentiment.capitalize()}")
print(f"Rating: {analysis.rating}/5")
print("Pros:", ", ".join(analysis.pros))
print("Cons:", ", ".join(analysis.cons))
print(f"Recommended Action: {analysis.recommended_action}")