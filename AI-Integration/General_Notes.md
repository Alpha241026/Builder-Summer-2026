# These are some notes refined from my Oracle GenAI certificate prep back in 1st sem...just enough to understand AI basics. Can be used to build a foundation for integrating AI in backend applications and choose appropriate prompting techniques for practical software engineering tasks. Also added some more topics to it that werent covered in the original notes and are worth keeping a few lines.

---

# Fundamentals of LLMs

## What is an LLM?

A **Large Language Model (LLM)** is a neural network trained on massive amounts of text that predicts the **next most likely token (word/subword)** in a sequence.

Example:

> *I wrote to the zoo to send me a pet. They sent me a ______.*

| Word      | Probability |
| --------- | ----------: |
| Dog       |        0.30 |
| Cat       |        0.20 |
| Lion      |        0.10 |
| Elephant  |        0.10 |
| Panther   |        0.05 |
| Alligator |        0.02 |

The model assigns a probability to every token in its vocabulary and selects one according to the decoding strategy.

> **Takeaway:** An LLM doesn't "know" facts like a database—it predicts statistically likely text.

---

## LLM Architectures

### Encoder Models

Convert input text into vector representations (**embeddings**).

Main use cases:

* Semantic Search
* Text Classification
* Similarity Search
* Embedding Generation

Examples:

* BERT
* RoBERTa
* MiniLM
* SBERT
* DistilBERT

---

### Decoder Models

Generate text **one token at a time**.

Used for:

* Chatbots
* Code Generation
* Content Writing
* Summarization

Examples:

* GPT family
* Llama
* Falcon
* BLOOM

---

### Encoder-Decoder Models

First understand the input, then generate output.

Commonly used for:

* Translation
* Summarization
* Question Answering

Examples:

* T5
* BART
* UL2

---

# Prompt Engineering

Prompt Engineering is the process of designing prompts to obtain better responses.

Common techniques:

### Zero-shot

Only instructions.

### One-shot / Few-shot (k-shot)

Provide one or more examples before asking the actual task.

### In-context Learning

The model learns from examples inside the prompt without changing its parameters.

### Chain of Thought (CoT)

Encourage the model to reason step-by-step.

### Least-to-Most

Break a difficult task into smaller easier subtasks.

### Step-back Prompting

Ask for higher-level concepts before solving the actual problem.

---

# Prompt Injection (Jailbreaking)

A prompt intentionally crafted to make an LLM ignore its instructions, reveal restricted information, or behave unexpectedly.

---

# Training (High-Level)

Prompting is not always enough.

Sometimes the model itself must be adapted.

Common approaches:

| Method                                 | Purpose                                             |
| -------------------------------------- | --------------------------------------------------- |
| Fine Tuning                            | Retrain the model on task-specific labeled data     |
| PEFT (Parameter Efficient Fine Tuning) | Modify only a small number of parameters            |
| Soft Prompting                         | Learn prompts instead of retraining the whole model |

> **Builder Note:** Good to know these exist, but API users rarely perform them directly.

---

# Decoding

LLMs generate output one token at a time.

Different decoding strategies produce different outputs.

### Greedy Decoding

Always choose the highest-probability token.

Predictable but less creative.

---

### Sampling

Randomly choose among likely tokens.

Produces more diverse outputs.

---

### Temperature 

Controls randomness during sampling.

Lower temperature (≈0–0.3)

* More deterministic
* Better for:

  * SQL generation
  * Code generation
  * Summaries

Higher temperature (≈0.8–1.2)

* More creative
* Better for:

  * Brainstorming
  * Story writing
  * Idea generation

Temperature changes the probability distribution but **not** the ranking of tokens.

---

# Hallucination

An LLM sometimes generates information that sounds correct but is unsupported or false.

Ways to reduce hallucinations:

* Better prompting
* Retrieval-Augmented Generation (RAG)
* Providing citations
* Grounding the model with external knowledge

No method completely eliminates hallucinations.

---

# Retrieval-Augmented Generation (RAG)

Instead of relying only on the model's training data:

```
User Question

↓

Retrieve relevant documents

↓

Provide documents to LLM

↓

Generate grounded answer
```

Benefits:

* More up-to-date information
* Reduced hallucinations
* Domain-specific knowledge

---

# Code Models

Models trained heavily on source code.

Examples:

* GitHub Copilot
* Code Llama
* Codex

Tasks:

* Code completion
* Debugging
* Code explanation
* Documentation generation

---

# Multimodal Models

Models capable of understanding multiple input/output modalities.

Examples:

* Text ↔ Image
* Image → Text
* Audio → Text
* Video → Text

Examples:

* Gemini
* GPT-4o
* Claude (selected capabilities)

---

# AI Agents (Overview)

LLM-powered systems capable of:

* Planning
* Reasoning
* Tool usage
* Multi-step execution

Examples of research ideas:

* ReAct
* Toolformer

(the topics below this werent in the original notes)

---

# 1. Tokens

## Tokens

A **token** is the basic unit an LLM processes. It may represent a whole word, part of a word, punctuation, or even whitespace.

Examples:

```text
"Hello world!"

↓

["Hello", " world", "!"]
```

AI providers price their APIs based on **tokens processed**, since computation depends on the number of tokens rather than the number of words.

There are usually three metrics:

* **Input Tokens** → tokens in your prompt
* **Output Tokens** → tokens generated by the model
* **Total Tokens** → Input + Output

> **Builder Note:** Shorter prompts reduce cost and latency.

---

# 2. Embeddings

## Embeddings

Embeddings are **vector (numerical) representations** of data that capture its semantic meaning.

Similar pieces of information produce similar vectors.

Generated mainly by **encoder models**.

Common applications:

* Semantic Search
* Recommendation Systems
* Clustering
* Retrieval-Augmented Generation (RAG)

> **Builder Note:** Unlike chat models, embeddings are used for *finding* relevant information rather than generating text.

---

# 3. Context Window

## Context Window

The **context window** is the maximum number of tokens an LLM can process in a single request.

It includes:

* Input prompt
* Conversation history
* Generated output

If the limit is exceeded, older context may be discarded or the request may fail.

A larger context window allows the model to remember longer conversations and process larger documents.

> **Builder Note:** Context window is the model's temporary working memory—not permanent memory.

---

# 4. System Prompt vs User Prompt

## System Prompt vs User Prompt

### System Prompt

Defines the model's role, behavior and constraints.

Example:

> You are a backend software engineer who always returns JSON.

---

### User Prompt

Contains the actual request from the user.

Example:

> Explain Binary Search.

The system prompt stays consistent while user prompts change.

> **Builder Note:** In production applications, developers control the **system prompt**, while users only provide **user prompts**.

---

# 5. Temperature vs Top-p

## Temperature vs Top-p

Both control randomness, but in different ways.

### Temperature

Changes how adventurous the model is.

* Low → predictable
* High → creative

---

### Top-p (Nucleus Sampling)

Limits the pool of candidate tokens.

Only tokens whose cumulative probability reaches **p** are considered.

Example:

```
top-p = 0.9

↓

Only the most likely 90% probability mass is considered.
```

### Simple Difference

**Temperature**

> *How creative should the model be?*

**Top-p**

> *Which words are allowed to be chosen?*

> **Builder Note:** Most applications adjust only Temperature. Top-p is usually left at its default value.

---

# 6. Anatomy of an AI API Request

## AI API Request Flow

```text
Application

↓

Endpoint

↓

Headers
(API Key)

↓

JSON Request

↓

AI Model

↓

JSON Response

↓

Application
```

### Endpoint

The URL where the request is sent.

Example:

```
https://generativelanguage.googleapis.com/...
```

---

### Headers

Metadata about the request.

Common headers:

* Content-Type
* Authorization / API Key

---

### API Key

A secret credential used to authenticate your application.

Never expose it publicly.

---

### JSON Request

Contains:

* model
* prompt/messages
* generation parameters
* safety settings (if any)

---

### JSON Response

Contains:

* generated content
* metadata
* token usage
* finish reason

> **Builder Note:** Most backend applications simply extract the generated text from the response and ignore the rest unless needed.

---

# 7. JSON Response Structure

## JSON Response Structure

AI APIs usually return structured JSON rather than plain text.

Typical response contains:

```text
Response

├── Generated Content
├── Metadata
├── Token Usage
└── Finish Reason
```

Structured JSON makes responses easy to parse inside applications.

Instead of asking for plain text, you can request specific JSON formats like:

```json
{
  "summary": "",
  "keywords": [],
  "category": ""
}
```

This is especially useful for:

* Data Extraction
* Classification
* Backend APIs
* Agent Workflows

> **Builder Note:** Returning JSON instead of free-form text makes AI much easier to integrate into software.

---

# LLM API Workflow

```text
User

↓

Application (Python / Go)

↓

HTTP Request

↓

LLM API

↓

JSON Response

↓

Application processes response

↓

User
```

### Important

The LLM is **not running inside your application**.

Your application is simply acting as a client that communicates with a remote AI service over HTTP.

---
