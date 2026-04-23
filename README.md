# NeuroBIOS

This is the **NeuroBIOS** project - the orchestrator for an LLM model designed as a finite state machine.

The tasks of the orchestrator:
- Finite state machine control flow
- State management
- Context management
- Executing current state of the flow

## High-level structure

### Flow

Flow define the sequence of states that the agent will execute. The sequence of execution of states can be changed dynamically by the **Controller** which can decide to continue the flow with the next state, or switch to a different state making the flow linear or circular.

### Controllers

**Controller** is an entity that is responsible for the execution of the agent's current state, processing the LLM model responses, and dynamically changing the flow.

The controller-based architecture is chosen to provide easier development and control of the agent's behavior on each state.

### System Prompt

Each controller can build its own system prompt or supplement the globally defined one before sending the context to the model.

### Context Management

Context is stored in the **Context Manager** that manages messages history and [WIP] context compression mechanism.

## Future evolution plans

- A context compression mechanism will be implemented upon reaching the context window limit.
- It was planned that this repository would serve as a foundational layer, while the remaining actions for storing the entire message history, transitioning between context checkpoints, and managing the core would be handled separately.
- Further improvements and features for the core orchestrator are expected while developing new agents.
