# 🌍 AI Trip Planner

An intelligent travel planning application powered by CrewAI that creates personalized 5-day itineraries using multiple AI agents working together.

## ✨ Features

- **Multi-Agent System**: Three specialized AI agents collaborate to create comprehensive trip plans
- **Interactive Web Interface**: Clean, user-friendly Streamlit frontend
- **Detailed Itineraries**: Complete 5-day travel plans with activities, meals, and costs
- **Budget Breakdown**: Automatic cost calculations and budget summaries
- **Downloadable Plans**: Export your trip plan as a text file
- **Real-time Processing**: Live progress updates during trip planning

## 🤖 AI Agents

### 1. Expert Travel Agent
- Creates detailed 5-day itineraries
- Includes budget estimates and packing suggestions
- Provides flight and hotel recommendations
- Integrates practical travel logistics

### 2. City Selection Expert
- Analyzes weather patterns and seasonal events
- Compares multiple destinations
- Considers travel costs and current conditions
- Provides detailed reports on chosen cities

### 3. Local Tour Guide
- Offers insider knowledge and hidden gems
- Suggests local spots and cultural insights
- Provides practical tips and recommendations
- Shares authentic local experiences

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd Trip\ Planner/starter_template
   ```

2. **Install dependencies**
    Poetry:
   ```bash
   poetry install
   ```

3. **Set up environment variables**
   
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run front_end.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 📝 How to Use

1. **Enter Trip Details**:
   - Origin city (where you're traveling from)
   - Destination cities or countries
   - Travel date range
   - Your interests and hobbies

2. **Click "Plan My Trip"** and wait for the AI agents to work their magic

3. **Review Your Plan**:
   - Detailed day-by-day itinerary
   - Activity recommendations
   - Restaurant suggestions
   - Cost breakdowns
   - Budget summary

4. **Download** your trip plan for offline reference

## 🏗️ Project Structure
