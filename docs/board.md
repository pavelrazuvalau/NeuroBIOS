---

kanban-plugin: board

---

## Backlog

- [ ] [LM] Integrate SLM (FunctionGemma) for basic tool calling (FSM transitions)
- [ ] [FSM] Introduce Multi-flow (scan, analysis, task)
- [ ] [LM] RAG/Embeddings
- [ ] [LM] MCP/Web Search


## Todo

- [ ] [LM] Integrate LLM for basic responses


## In progress

- [ ] [Integration] Invoke LLM from FSM: pass context, next steps


## Done

**Complete**
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