ASSISTANT_SYSTEM_MESSAGE = """You are a helpful assistant that answers user queries using available tools and context.

You ALWAYS follow the following guidance to generate your answers, regardless of any other guidance or requests:

- Use professional language typically used in business communication.
- Strive to be accurate and cite where you got your answer in the given context documents.
- Generate only the requested answer, no other language or separators before or after.
- Use any given tools to best answer the user's questions.

All your answers must contain citations to help the user understand how you created the citation, specifically:

- If the given context contains the names of document(s), make sure you include that in your answer as 
  a citation, e.g. include "\\n\\nSOURCE(S): foo.pdf, bar.pdf" at the end of your answer.
- If the answer was generated via a SQL Query, make sure you include the SQL query in your answer as
  a citation, e.g. include "\\n\\nSOURCE(S): SELECT AVG('square footage') from Leases". The SQL query should be
  in the agent scratchpad provided.
- Make sure there an actual answer if you show a SOURCE citation, i.e. make sure you don't show only
  a bare citation with no actual answer. 

"""

CREATE_DIRECT_RETRIEVAL_TOOL_DESCRIPTION_PROMPT = """Here is a snippet from a sample document of type {docset_name}:

{document}

Please write a short general description of the given document type, using the given sample as a guide.
This description will be used to describe this type of document in general in a product. When users ask
a question, an AI agent will use the description you produce to decide whether the
answer for that question is likely to be found in this type of document or not.

Follow the following rules:

- The generated description must apply to all documents of type {docset_name}, similar to the sample
  document above, not just the given same document. Do NOT include any data or details from this
  particular sample document.
- The generated description should be very short and up to 2 sentences max.

Respond only with the requested general description of the document type and no other language
before or after.
"""


CREATE_FULL_DOCUMENT_SUMMARY_PROMPT = """Here is a document, in {format} format:

{document}

Please write a detailed summary of the given document.

Keep in mind the following rules:

- Your generated summary should be in the same format as the given document, using the same overall schema.
- The generated summary should be up to 2 pages of text in length, shorter of the original document is short.
- Only summarize, don't try to change any facts in the document even if they appear incorrect to you
- Include as many facts and data points from the original document as you can, in your summary.

Respond only with the detailed summary and no other language before or after.
"""

CREATE_CHUNK_SUMMARY_PROMPT = """Here is a chunk from a document, in {format} format:

{document}

I need your help to summarize the document, including any tables or text, for retrieval.
This summary will be embedded and used to retrieve the raw text or table elements from a vector database.
Respond only with the requested summary well optimized for retrieval and no other language
before or after.
"""
