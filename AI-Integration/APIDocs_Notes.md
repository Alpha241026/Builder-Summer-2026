
---

# Gemini API Crash Notes

## What is the Gemini API?

The Gemini API allows an application to communicate with Google's Gemini models over HTTP.

Instead of running an AI model locally, your application sends a request to Google's servers and receives the generated response.

```text
My Application

↓

Gemini API

↓

Gemini Model

↓

JSON Response

↓

My Application
```

---

# SDK vs REST

There are two common ways to call the API.

### SDK

Google provides libraries for languages like Python and JavaScript.

Example:

```python
client.interactions.create(...)
```

The SDK hides the HTTP request details.

---

### REST

Uses raw HTTP requests.

```text
POST

↓

Headers

↓

JSON Body

↓

JSON Response
```

REST is language-independent and is what every SDK uses internally.

> **Builder Note:** Learn REST first. SDKs become much easier afterward.

---

# API Key

Every request must include an API key.

Purpose:

* Authenticates your application
* Tracks usage
* Prevents unauthorized access

Never:

* Commit API keys to GitHub
* Hardcode them into projects

Instead:

Store them as environment variables.

```text
GEMINI_API_KEY
```

Think of an API key as:

> The password for your application.

---

# Anatomy of a Gemini Request

Every request has four important parts.

## 1. Endpoint

The URL where the request is sent.

Example:

```text
https://generativelanguage.googleapis.com/v1beta/interactions
```

Think of it as:

> The destination address.

---

## 2. Headers

Metadata sent with every request.

Usually includes:

```text
Content-Type

API Key
```

---

## 3. JSON Body

Contains everything the model needs.

Typically includes:

```json
{
  "model": "...",
  "input": "...",
  ...
}
```

Important fields:

### model

Which Gemini model should answer?

Example:

```text
gemini-3.6-flash
```

---

### input

The prompt.

Example:

```text
Explain Binary Search.
```

---

## 4. Response

The server returns JSON.

Example:

```text
Status

↓

Usage

↓

Generated Text

↓

Metadata
```

---

# Response Structure

Unlike ChatGPT's website,

APIs return **structured JSON**.

Example:

```json
{
  "status": "...",
  "usage": {},
  "steps": [],
  "model": "..."
}
```

The generated answer lives inside the response—not as plain text.

SDKs expose convenient properties like:

```text
interaction.output_text
```

so you don't have to manually parse the JSON.

> **Builder Note:** In REST, you'll often extract the text yourself. In SDKs, helper methods do it for you.

---

# Streaming

Normal request:

```text
Send Prompt

↓

Wait

↓

Entire Response
```

Streaming:

```text
Send Prompt

↓

AI starts generating

↓

Receive chunks continuously
```

Useful for:

* Chat applications
* AI assistants
* Live typing effect

Not necessary for your first project.

---

# Structured Outputs

Normally the model returns free-form text.

Example:

```text
Here's a summary...
```

Instead, you can request structured JSON.

Example:

```json
{
  "summary": "",
  "keywords": [],
  "difficulty": ""
}
```

Benefits:

* Easy to parse
* Predictable
* Better for backend applications

Common use cases:

* Data extraction
* Classification
* APIs
* Automation

---

# Safety Settings

Gemini includes configurable safety filters.

Developers can control how the model handles categories such as:

* Harassment
* Hate Speech
* Sexually Explicit Content
* Dangerous Content

Purpose:

Prevent harmful or inappropriate outputs.

Most applications can simply use the default settings.

---

# Why JSON?

Applications don't understand paragraphs very well.

Applications understand structured data.

Instead of

```text
The weather tomorrow will probably be sunny.
```

Return

```json
{
  "weather": "Sunny",
  "temperature": 32
}
```

JSON is much easier for programs to process.

---
