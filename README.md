<div align="center">

# Terminal Souls

### A Turn-Based RPG Combat Engine Built in Python

Battle powerful enemies across multiple environments while managing health, abilities, healing resources, and strategic combat decisions.

<br>

<a href="https://melissagarridos.github.io/">Portfolio</a> •
<a href="https://www.linkedin.com/in/melissavgs/">LinkedIn</a> •
<a href="https://github.com/melissagarridos">GitHub</a>

<br><br>

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-Terminal-green?style=for-the-badge)
![Game Development](https://img.shields.io/badge/Game-RPG-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</div>

---

## Overview

Terminal Souls is a turn-based RPG combat game developed in Python that challenges players to battle different enemies across unique environments.

Players must manage health, healing resources, and special abilities while facing increasingly dangerous opponents controlled by AI-driven combat behaviors.

The project demonstrates software engineering principles through modular architecture, game state management, and combat system implementation.

---

## Gameplay

Players begin by selecting a battle path:

- Shadow Dungeon
- Eternal Forest
- Old Graveyard
- Vampire Castle

Each location contains a unique enemy:

| Scenario | Enemy |
|-----------|--------|
| Shadow Dungeon | Dragon |
| Eternal Forest | Werewolf |
| Old Graveyard | Zombie |
| Vampire Castle | Vampire |

Victory is achieved by reducing the enemy's health to zero before the hero falls.

---

## Core Features

### Combat System

- Turn-based gameplay
- Standard attacks
- Special abilities
- Critical hit mechanics

### Health Management

- Dynamic health bars
- Health recovery system
- Potion inventory

### Enemy AI

- Conditional healing behavior
- Critical hit chance
- Dynamic combat responses

### User Experience

- Colored terminal interface
- ASCII game logo
- Interactive menus
- Real-time battle feedback

---

## Architecture

```text
Player Input
      │
      ▼
Combat Engine
      │
      ├── Hero Actions
      │
      ├── Enemy AI
      │
      ├── Damage System
      │
      └── Health Management
      │
      ▼
Battle Resolution
```

---

## Technical Highlights

### Enemy AI

Enemies automatically evaluate their health and may choose to heal when entering critical health ranges.

### Critical Hit System

Both the player and enemies can trigger critical hits that deal double damage.

### State Management

The game maintains and updates:

- Player Health
- Enemy Health
- Potion Count
- Turn Number
- Scenario State

### Modular Design

Game logic is separated into multiple modules, improving maintainability and readability.

---

## Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Terminal UI | Colorama |
| Architecture | Modular Programming |
| Logic | Turn-Based Combat System |

---

## Skills Demonstrated

- Python Development
- Software Architecture
- State Management
- Game Logic Design
- AI Behavior Systems
- User Interaction Design
- Modular Programming
- Error Handling

---

## Future Improvements

- Character Classes
- Inventory System
- Equipment Management
- Experience and Leveling
- Save / Load Functionality
- Multiple Enemy Types
- Boss Battles
- Story Progression
- Object-Oriented Refactor

---

## Learning Outcomes

This project strengthened practical experience in:

- Python Programming
- Software Design
- Game Mechanics
- State Management
- Interactive Applications
- Modular Code Organization

---

## Project Status

Completed and available for portfolio review.
