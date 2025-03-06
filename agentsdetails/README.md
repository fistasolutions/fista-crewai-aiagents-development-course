# CrewAI Agent Attributes Guide

This guide explains all the attributes of a CrewAI agent with step-by-step examples.

## **1. Basic Agent Structure**
Defines the agent’s **role, goal, backstory, and LLM**.

```yaml
blog_writer:
  role: "Blog Writer"
  goal: "Write a blog post about the {topic}"
  backstory: "You're a talented writer with a passion for technology and a knack for explaining complex concepts in a clear and engaging way."
  llm: "gpt-4"
```

---

## **2. Adding Tools**
Defines external tools the agent can use.

```yaml
  tools:
    - ScrapeTool()
```

---

## **3. Adding Function Calling LLM**
Specifies an **LLM that supports function calling**.

```yaml
  function_calling_llm: "gpt-4-1106-preview"
```

---

## **4. Adding Max Iterations**
Limits how many times an agent **retries**.

```yaml
  max_iter: 5  # Limits to 5 retries
```

---

## **5. Adding Max Requests Per Minute (max_rpm)**
Prevents exceeding API limits.

```yaml
  max_rpm: 60  # Limits to 60 requests per minute
```

---

## **6. Adding Max Execution Time**
Stops the agent if it **takes too long**.

```yaml
  max_execution_time: 30  # Stops after 30 seconds
```

---

## **7. Adding Memory**
Allows the agent to **remember past interactions**.

```yaml
  memory: True
```

---

## **8. Adding Verbose Mode**
Enables **detailed logs**.

```yaml
  verbose: True
```

---

## **9. Allowing Delegation**
Allows the agent to **assign tasks** to other agents.

```yaml
  allow_delegation: True
```

---

## **10. Adding Step Callback**
Runs a function **after each step**.

```python
def log_step(agent, step):
    print(f"Agent {agent} completed step: {step}")
```

```yaml
  step_callback: log_step
```

---

## **11. Enabling Caching**
Caches responses **to speed up processing**.

```yaml
  cache: True
```

---

## **12. Customizing System Prompt Template**
Defines a **custom system message**.

```yaml
  system_template: "You are an expert blog writer. Be detailed and engaging."
```

---

## **13. Enabling Code Execution**
Allows the agent to **run Python code**.

```yaml
  allow_code_execution: True
  code_execution_mode: "safe"
```

---

## **Conclusion**
This guide covers all **CrewAI agent attributes** with examples.  
Try each feature step by step to understand its impact.

🚀 Happy coding with CrewAI! 🎉
