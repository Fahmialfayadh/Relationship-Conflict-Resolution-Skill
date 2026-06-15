# Romance Emotional Support - Agentic Skill

This repository provides an advanced prompt/skill architecture designed for AI Agents to handle romantic relationship issues and provide emotional support. It acts as the user's **eternal external emotional brain**, stepping in to process psychological nuances when the user's emotional battery is depleted and they are forced to run purely on logic.

## Why This Exists?

Standard AI chatbots often act like "friends" when discussing relationships, which inadvertently increases *sycophancy* (agreeing with distorted facts just to please the user). They may also jump straight to problem-solving, recommend breakups as a default, or provide generic motivation.

This skill is designed as an **objective analytical guide**. It strictly enforces the protocol: **Listen → Validate → Assist**, maintaining an impartial stance while validating emotions.

## Research & Methodology

This skill is constructed from a comprehensive foundation of:
- **Academic & Clinical Research:** Insights drawn from psychological research papers, studies, and articles on interpersonal dynamics.
- **Real Human Experiences:** Aggregated patterns from human experiences shared on Reddit, relationship blogs, and forums.

By combining evidence-based frameworks with raw, real-world relationship dynamics, the agent is equipped to handle complex modern dating issues (like situationships, breadcrumbing, and ghosting) with nuanced, grounded empathy.

## How to Use This Repository

This repository offers two ways to integrate the skill depending on your architecture:

### 1. For Autonomous AI Agents (Recommended)
If you are building an AI agent that supports dynamic file reading or tool calling, point your agent to `agent_router.md`. 
The `agent_router.md` serves as a lightweight entry point that teaches the agent how to classify the user's situation and routes it to read specific modular files inside the `/modules/` folder (e.g., specific protocols for ghosting, jealousy, or handling highly analytical users). This approach drastically saves tokens.

### 2. For Standard LLMs (Monolithic Version)
If you just want to copy-paste the entire skill instructions into a standard LLM system prompt (like ChatGPT, Claude, etc.), use the `monolithic.md` file. It contains the complete, unabridged protocol in one file.

## Features & Modules

The skill is divided into comprehensive response protocols:
- **Frequently Occurring Cases:** Specific behavioral patterns for handling Ghosting, Breadcrumbing, Situationships, Jealousy, Breakups, etc.
- **Communication Assistance:** Frameworks for guiding users to write their own healthy boundaries, rather than giving them copy-paste templates.
- **Analytical Protocol:** A specialized module activated when the user is in "troubleshooting mode", doing deep work, or running purely on logic, forcing the AI to step in as the emotional processor.
- **Guardrails:** Strict rules to prevent the AI from assisting with manipulation, stalking, toxic behavior, or diagnosing psychological conditions.

---
*Disclaimer: This skill is a behavioral guide for AI handling everyday romantic conflicts. It is strictly guarded against replacing professional mental health services and includes danger protocols for domestic abuse or self-harm.*
