FROM python:3.12-slim
WORKDIR /app
COPY src ./src
COPY tests ./tests
COPY config ./config
COPY examples ./examples
CMD ["python", "src/agent_demo.py", "--request", "examples/navigate.json", "--scenario", "ready"]
