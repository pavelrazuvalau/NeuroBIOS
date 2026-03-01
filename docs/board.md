---

kanban-plugin: board

---

## Backlog

- [ ] [FSM] Introduce Multi-flow (scan, analysis, task)
- [ ] [FSM] Introduce quality metrics of risks/probability
- [ ] [LM] Integrate SLM (FunctionGemma) for basic tool calling (FSM transitions)
- [ ] [LM] Create a mock quality metrics predictor (random HIGH/LOW generator)
- [ ] [FSM] Implement quality metrics prediction parser from plain text for further deterministic transitions
- [ ] [FSM] Use quality metrics for state/flow transition (risks, success/failure rate)
- [ ] [FSM] Extract configuration to a separate file
- [ ] [LM] RAG/Embeddings
- [ ] [LM] MCP/Web Search


## Todo

- [ ] [FSM] Extend set_state with event handling
- [ ] [FSM] Add dummy action callbacks (prints)
- [ ] [LM] Integrate LLM for basic responses


## In progress

- [ ] [FSM] Implement state transition validation


## Done

**Complete**
- [x] Init project
- [x] [FSM] Implement base class
- [x] [FSM] Validate setting state string based on allowed list




%% kanban:settings
```
{"kanban-plugin":"board","list-collapse":[false,false,false,false]}
```
%%