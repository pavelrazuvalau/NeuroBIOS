---

kanban-plugin: board

---

## Backlog

- [ ] [FSM] Error handling
- [ ] [FSM] Interrupt flow for escalation
- [ ] [LM] Integrate LLM for basic responses
- [ ] [FSM] Introduce Multi-flow (scan, analysis, task)
- [ ] [FSM] Introduce quality metrics of risks/probability
- [ ] [FSM] Extend set_state with event handling
- [ ] [FSM] Allow backward transition to support rollback (e.g. LLM hallucinated bad response)
- [ ] [LM] Integrate SLM (FunctionGemma) for basic tool calling (FSM transitions)
- [ ] [LM] Create a mock quality metrics predictor (random HIGH/LOW generator)
- [ ] [FSM] Implement quality metrics prediction parser from plain text for further deterministic transitions
- [ ] [FSM] Use quality metrics for state/flow transition (risks, success/failure rate)
- [ ] [FSM] Extract configuration to a separate file
- [ ] [LM] RAG/Embeddings
- [ ] [LM] MCP/Web Search


## Todo

- [ ] [Integration] Invoke LLM from FSM: pass context, next steps


## In progress

- [ ] [LM] Implement mock LLM class for static/random text


## Done

**Complete**
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