---

kanban-plugin: board

---

## Backlog

- [ ] [FSM] Introduce Multi-flow (scan, analysis, task)
- [ ] [LM] Integrate SLM (FunctionGemma) for basic tool calling (FSM transitions)
- [ ] [LM] RAG/Embeddings
- [ ] [LM] MCP/Web Search


## Todo

- [ ] [FSM] Create TOOL_EXECUTOR dynamic routing


## In progress

- [ ] [Integration] Create PLANNER and TOOL_EXECUTOR states


## Done

**Complete**
- [x] [Integration] Implement Agentic Memory (Message History)
- [x] [LM] Replace raw requests with OpenAI SDK
- [x] [LM] Define Tool Schemas
- [x] [LM] Integrate LLM for basic responses
- [x] [Integration] Invoke LLM from FSM: pass context, next steps
- [x] [FSM] Implement quality metrics prediction parser from plain text for further deterministic transitions
- [x] [FSM] Extract configuration to a separate file
- [x] [FSM] Support branch/loop
- [x] [LM] Create a mock quality metrics predictor (random HIGH/LOW generator)
- [x] [FSM] Interrupt flow for escalation
- [x] [FSM] Implement basic shared context among states
- [x] [FSM] Add dummy action callbacks (prints)
- [x] [FSM] Implement state transition validation
- [x] [FSM] Validate setting state string based on allowed list
- [x] [FSM] Implement base class
- [x] Init project




%% kanban:settings
```
{"kanban-plugin":"board","list-collapse":[false,false,false,false]}
```
%%