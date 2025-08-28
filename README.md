**1)Install the required Libraries**
# pip install langchain==0.1.17
# pip install langchain-Community
# pip install gpt4all
# pip install langchain-google-community
# pip install google-api-python-client
# pip install python-dotenv
# pip install pydantic==2.11.1
# pip install sentencepiece
# pip install -q langchain==0.0.152
# pip install pyllamacpp==1.0.7


**2 )Make .env file and Add required API's**
# for example:
# GOOGLE_CSE_ID = "Add you CSE_Id her"
# GOOGLE_API_KEY ="Add your google api here"


**3)Download Meta-Llama-3-8B-Instruct.Q4_0.gguf and Place in model folder**

**Meta-Llama-3**
Meta → developed by Meta (formerly Facebook).
LLaMA-3 → third version of the Large Language Model Meta AI.
These are open-weight LLMs used for research or integration in applications.

**8B**
Refers to the number of parameters in the model.
8B = 8 billion parameters.
Bigger number → usually more capable but also requires more memory / GPU RAM.
Instruct
This variant is instruction-tuned, meaning it is fine-tuned to follow human instructions.
Better for chatbots, question-answering, or summarization tasks.

**Q4_0**
Refers to quantization of the model
Q4_0 = 4-bit quantization (a way to reduce memory usage and disk size) while still keeping decent performance.
Smaller file → easier to run on consumer GPUs or less powerful machines

**.gguf**
GGUF = GGML Unified Format.
It’s a file format used for efficient LLM inference in local libraries like llama.cpp or ggml.
Allows running large models on CPU or GPU efficiently without the full framework of PyTorch/TensorFlow.


