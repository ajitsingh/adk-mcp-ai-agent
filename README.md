# ADK MCP AI Agent

MCP-enabled AI agent built with Google ADK that connects to real-world data sources and generates grounded responses.

## Project Summary
This project implements an AI agent using Google ADK and Model Context Protocol (MCP). The agent connects to BigQuery through MCP Toolbox for Databases, retrieves structured data, and generates grounded responses. It is deployed on Google Cloud Run as a scalable service.

## Problem Statement
Build an AI agent that uses MCP to connect to one external tool or data source, retrieve information, and use that information in its response.

## Architecture
User → Cloud Run ADK Agent → Cloud Run MCP Toolbox → BigQuery → Structured Data → Grounded Response

## Tech Stack
- Google ADK
- MCP Toolbox for Databases
- BigQuery
- FastAPI
- Cloud Run
- Python

## Local Setup
1. Create virtual environment
2. Install requirements
3. Authenticate gcloud
4. Run MCP Toolbox
5. Run FastAPI agent
6. Test `/ask`

## Deployment
1. Deploy MCP Toolbox to Cloud Run
2. Deploy Agent to Cloud Run
3. Test live `/ask` endpoint

## Sample Request
```bash
curl -X POST https://YOUR-AGENT-URL/ask \
  -H "Content-Type: application/json" \
  -d '{"query":"bigquery"}'