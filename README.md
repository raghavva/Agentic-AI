# 🌍 AI Trip Planner

An intelligent, multi-agent travel planning system powered by CrewAI that creates personalized 5-day trip itineraries using AI agents working collaboratively.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [System Components](#system-components)
- [Execution Flow](#execution-flow)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Frontend Interface](#frontend-interface)
- [Project Structure](#project-structure)
- [File Descriptions](#file-descriptions)
- [Future Enhancements](#future-enhancements)

## 🎯 Overview

The AI Trip Planner is a CrewAI-based application that leverages multiple specialized AI agents to create comprehensive travel plans. The system uses a collaborative approach where different agents handle specific aspects of trip planning, resulting in detailed itineraries that include:

- **5-day detailed itineraries** with day-by-day plans
- **City selection** based on weather, season, and prices
- **Local insights** from a virtual tour guide
- **Budget estimates** and cost breakdowns
- **Packing suggestions** tailored to destination and season
- **Flight and hotel recommendations**

## 🏗️ Architecture

The system follows a **multi-agent architecture** using CrewAI framework, where specialized agents collaborate to complete complex travel planning tasks.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                      │
│  ┌──────────────────────┐  ┌─────────────────────────────┐ │
│  │  Streamlit Frontend  │  │   Command Line Interface    │ │
│  │    (front_end.py)    │  │       (main.py)             │ │
│  └──────────┬───────────┘  └──────────────┬──────────────┘ │
└─────────────┼──────────────────────────────┼────────────────┘
              │                              │
              └──────────────┬───────────────┘
                             │
              ┌──────────────▼───────────────┐
              │      TripCrew (main.py)      │
              │   - Orchestrates the crew    │
              │   - Manages agent workflow   │
              └──────────────┬───────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼────────┐  ┌────────▼────────┐  ┌──────▼──────────┐
│  TravelAgents  │  │   TravelTasks   │  │     Tools        │
│   (agents.py)  │  │   (tasks.py)    │  │  (tools/*.py)    │
└───────┬────────┘  └────────┬────────┘  └──────┬───────────┘
        │                    │                    │
        │                    │                    │
┌───────▼────────────────────▼────────────────────▼───────────┐
│                    CrewAI Framework                          │
│  - Agent Management                                           │
│  - Task Orchestration                                         │
│  - LLM Integration (OpenAI GPT-4o-mini)                      │
└───────────────────────────────────────────────────────────────┘
```

### Key Architectural Principles

1. **Agent Specialization**: Each agent has a specific role and expertise
2. **Task Decomposition**: Complex trip planning is broken into manageable tasks
3. **Tool Integration**: Agents use external tools for web search and calculations
4. **Collaborative Workflow**: Agents share information and build upon each other's work

## 🧩 System Components

### 1. Agents (`agents.py`)

The system uses three specialized AI agents:

#### 🧑‍💼 Expert Travel Agent
- **Role**: Primary trip planner and coordinator
- **Responsibilities**:
  - Creates comprehensive 5-day itineraries
  - Integrates information from other agents
  - Provides budget estimates and packing suggestions
  - Recommends flights and hotels
- **Tools**: Internet search, calculator
- **LLM**: GPT-4o-mini (temperature: 0.7)

#### 🏙️ City Selection Expert
- **Role**: Destination analyst and selector
- **Responsibilities**:
  - Analyzes multiple city options
  - Compares weather patterns and seasonal factors
  - Evaluates travel costs and prices
  - Selects the best destination based on criteria
- **Tools**: Internet search
- **LLM**: GPT-4o-mini (temperature: 0.7)

#### 🗺️ Local Tour Guide
- **Role**: Destination insider and cultural expert
- **Responsibilities**:
  - Provides local insights and hidden gems
  - Shares cultural information and customs
  - Recommends authentic restaurants and activities
  - Offers practical travel tips
- **Tools**: Internet search
- **LLM**: GPT-4o-mini (temperature: 0.7)

### 2. Tasks (`tasks.py`)

Tasks define the specific work each agent performs:

#### 📅 Plan Itinerary Task
- **Agent**: Expert Travel Agent
- **Purpose**: Create a detailed 5-day travel itinerary
- **Inputs**: City, travel dates, interests
- **Output**: Complete itinerary with:
  - Day-by-day plans
  - Weather forecasts
  - Restaurant recommendations
  - Packing suggestions
  - Budget breakdown

#### 🎯 Identify City Task
- **Agent**: City Selection Expert
- **Purpose**: Select the best city from options
- **Inputs**: Origin, city options, interests, travel dates
- **Output**: Detailed report on chosen city including:
  - Flight costs
  - Weather forecast
  - Attractions
  - Justification for selection

#### 📚 Gather City Info Task
- **Agent**: Local Tour Guide
- **Purpose**: Compile comprehensive city guide
- **Inputs**: City, travel dates, interests
- **Output**: In-depth city guide with:
  - Key attractions
  - Local customs
  - Special events
  - Hidden gems
  - Cultural insights

### 3. Tools (`tools/`)

Agents use specialized tools to perform their tasks:

#### 🔍 Search Tools (`search_tools.py`)
- **Function**: `search_internet(query)`
- **Purpose**: Search the web for real-time information
- **API**: Serper API (Google Search)
- **Returns**: Top 4 relevant search results with titles, links, and snippets
- **Usage**: Used by all agents to gather current information

#### 🧮 Calculator Tools (`calculator_tools.py`)
- **Function**: `calculate(operation)`
- **Purpose**: Perform mathematical calculations
- **Usage**: Budget calculations, cost estimates
- **Example**: `200*7`, `5000/2*10`

#### ✈️ Flight Tools (`flight_tools.py`) - *Currently Disabled*
- **Status**: Commented out, available for future use
- **Purpose**: Web scraping for flight prices
- **Technology**: Crawl4AI for web scraping
- **Note**: Requires additional setup and API keys

## 🔄 Execution Flow

### Step-by-Step Process

```
1. USER INPUT
   ├─ Origin location
   ├─ City options
   ├─ Date range
   └─ Interests/hobbies

2. TRIPCREW INITIALIZATION
   ├─ Create TripCrew instance
   ├─ Initialize TravelAgents
   └─ Initialize TravelTasks

3. AGENT CREATION
   ├─ Expert Travel Agent (with search + calculator tools)
   ├─ City Selection Expert (with search tool)
   └─ Local Tour Guide (with search tool)

4. TASK CREATION
   ├─ Identify City Task → City Selection Expert
   ├─ Gather City Info Task → Local Tour Guide
   └─ Plan Itinerary Task → Expert Travel Agent

5. CREW EXECUTION
   ├─ CrewAI orchestrates agent workflow
   ├─ Agents execute tasks in sequence
   ├─ Information flows between agents
   └─ Each agent uses tools as needed

6. RESULT AGGREGATION
   └─ Final trip plan with all details

7. OUTPUT
   └─ Display to user (CLI or Streamlit)
```

### Detailed Execution Sequence

1. **User provides input** via CLI or Streamlit interface
2. **TripCrew initializes** with user parameters
3. **Agents are instantiated** with their roles, backstories, goals, and tools
4. **Tasks are created** and assigned to specific agents
5. **Crew is assembled** with agents and tasks
6. **Crew.kickoff()** starts the execution:
   - City Selection Expert identifies the best city
   - Local Tour Guide gathers detailed city information
   - Expert Travel Agent creates the final itinerary
7. **Results are returned** and displayed to the user

### Agent Collaboration

- **Sequential Task Execution**: Tasks are executed in order, with later tasks using outputs from earlier ones
- **Shared Context**: CrewAI manages context sharing between agents
- **Tool Usage**: Agents autonomously decide when to use tools (search, calculator)
- **Information Integration**: Expert Travel Agent integrates all information into final plan

## 🚀 Installation

### Prerequisites

- Python 3.10 or 3.11
- Poetry (package manager)
- OpenAI API key
- Serper API key (for web search)

### Setup Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd "Trip Planner/starter_template"
   ```

2. **Install dependencies using Poetry**
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**
   ```bash
   poetry shell
   OR
   eval $(poetry env activate)
   ```

4. **Create a `.env` file** in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

5. **Verify installation**
   ```bash
   python main.py
   ```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Required
OPENAI_API_KEY=sk-...          # OpenAI API key for LLM
SERPER_API_KEY=...             # Serper API key for web search

# Optional (for future flight tools)
# Additional API keys may be needed for flight scraping features
```

### Model Configuration

The system uses **GPT-4o-mini** by default. To change the model, edit `agents.py`:

```python
self.OpenAIGPT41Mini = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
```

- **Model**: `gpt-4o-mini` (cost-effective, fast)
- **Temperature**: `0.7` (balanced creativity and consistency)

## 📖 Usage

### Command Line Interface

Run the application from the command line:

```bash
python main.py
```

The CLI will prompt you for:
1. **Origin**: Where you're traveling from
2. **Cities**: City options you're interested in (comma-separated)
3. **Date Range**: Your travel dates
4. **Interests**: Your hobbies and interests

Example:
```
From where will you be traveling from? New York
What are the cities options you are interested in visiting? Paris, Rome, Barcelona
What is the date range you are interested in traveling? March 15-20, 2024
What are some of your high level interests and hobbies? Art museums, local cuisine, historical sites
```

### Streamlit Web Interface

Launch the web interface:

```bash
streamlit run front_end.py
```

The interface will open in your browser at `http://localhost:8501`

**Features:**
- Interactive form for trip details
- Real-time trip planning
- Download trip plans as text files
- User-friendly interface with tabs

## 🖥️ Frontend Interface

The Streamlit frontend (`front_end.py`) provides:

### Trip Planning Tab
- **Input Form**:
  - Origin location
  - City options
  - Date range
  - Interests
- **Output Display**:
  - Complete trip plan in text area
  - Download button for trip plan
- **Information Panel**:
  - Explanation of how each agent works
  - System capabilities overview

### Flight Search Tab (Currently Disabled)
- Reserved for future flight scraping functionality
- Will include flight search and comparison features

## 📁 Project Structure

```
starter_template/
├── __pycache__/              # Python cache files
├── agents.py                  # Agent definitions
├── tasks.py                   # Task definitions
├── main.py                    # CLI entry point and TripCrew class
├── front_end.py               # Streamlit web interface
├── README.md                   # This file
├── .env                        # Environment variables (create this)
├── .gitignore                  # Git ignore rules
└── tools/
    ├── __pycache__/
    ├── search_tools.py         # Web search tool
    ├── calculator_tools.py     # Calculator tool
    └── flight_tools.py         # Flight scraping (disabled)
```

## 📄 File Descriptions

### agents.py
This file contains the definition of custom agents.
To create an Agent, you need to define the following:
1. **Role**: The role of the agent.
2. **Backstory**: The backstory of the agent.
3. **Goal**: The goal of the agent.
4. **Tools**: The tools that the agent has access to (optional).
5. **Allow Delegation**: Whether the agent can delegate tasks to other agents (optional).

[More Details about Agent](https://docs.crewai.com/concepts/agents).

### tasks.py
This file contains the definition of custom tasks.
To create a task, you need to define the following:
1. **description**: A string that describes the task.
2. **agent**: An agent object that will be assigned to the task.
3. **expected_output**: The expected output of the task.

[More Details about Task](https://docs.crewai.com/concepts/tasks).

### main.py (Crew)
This is the main file that you will use to run your custom crew.
To create a Crew, you need to define Agent, Task and following Parameters:
1. **Agent**: List of agents that you want to include in the crew.
2. **Task**: List of tasks that you want to include in the crew.
3. **verbose**: If True, print the output of each task (default is False).
4. **debug**: If True, print the debug logs (default is False).

[More Details about Crew](https://docs.crewai.com/concepts/crew).

### front_end.py
Streamlit-based web interface for the Trip Planner. Provides a user-friendly GUI for:
- Inputting trip details
- Viewing generated trip plans
- Downloading trip plans as text files

## 🔮 Future Enhancements

### Planned Features

1. **Flight Price Scraping** (Currently commented out)
   - Real-time flight price scraping from multiple sources
   - Flight comparison and analysis
   - Integration with flight booking APIs

2. **Hotel Recommendations**
   - Hotel search and price comparison
   - Booking integration
   - Reviews and ratings

3. **Weather Integration**
   - Real-time weather forecasts
   - Weather-based activity recommendations
   - Packing suggestions based on weather

4. **Budget Tracking**
   - Detailed cost breakdowns
   - Budget alerts
   - Expense tracking

5. **Multi-language Support**
   - Support for multiple languages
   - Localized recommendations

6. **User Preferences**
   - Save user preferences
   - Personalized recommendations
   - Trip history

## 🛠️ Development

### Adding New Agents

1. Define agent in `agents.py`:
   ```python
   def new_agent(self):
       return Agent(
           role="Role description",
           backstory="Agent backstory",
           goal="Agent goal",
           tools=[tool1, tool2],
           verbose=True,
           llm=self.OpenAIGPT41Mini,
       )
   ```

2. Create corresponding task in `tasks.py`
3. Add agent and task to crew in `main.py`

### Adding New Tools

1. Create tool file in `tools/` directory
2. Use `@tool` decorator from LangChain
3. Add tool to agent's tools list in `agents.py`

### Testing

Run the application and test with various inputs:
- Different cities and countries
- Various date ranges
- Different interest combinations

## 📝 Notes

- The system uses CrewAI framework for multi-agent orchestration
- All agents use GPT-4o-mini for cost-effectiveness
- Web search is powered by Serper API
- Flight tools are available but currently disabled (requires additional setup)

## 🤝 Contributing

When contributing:
1. Follow the existing code structure
2. Add appropriate docstrings
3. Test with various inputs
4. Update this README if adding new features

## 📄 License

[Add your license information here]

## 👤 Author

Raghav

---

**Built with ❤️ using CrewAI, OpenAI, and Streamlit**
