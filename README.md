# Easy Janus


# Running Code Instructions

## Setup and Execution

### 1. Start Containers
```bash
# For attached logs (view in terminal)
docker compose -f 'docker-compose-cql-es.yml' up --build

# For detached mode (run in background)
docker compose -f 'docker-compose-cql-es.yml' up -d --build
```

### 2. Verify Container Status
Wait for all containers to fully initialize before proceeding.

**Option A**: Check from terminal (if running with attached logs)
- Wait until all startup messages complete and the system is ready

**Option B**: Check from Portainer (if available)
- Open Portainer interface
- Verify all containers are in "running" state

### 3. Connect to Gremlin (Optional)
Opens a connection at terminal.
```bash
# Make the connection script executable
chmod +x path/to/connect-gremlin.sh

# Execute the script
./connect-gremlin.sh
```

### 4. Verify Gremlin Connection (Optional)
Test the connection by running a simple Gremlin query:
```
g.V()
```

### 5. Using the Utilities

Make sure to activate .venv by source .venv/bin/activate
Check `main.py` for example utility functions and their usage.

## Additional Resources
- [Gremlin Documentation](https://tinkerpop.apache.org/docs/current/reference/)
- [ElasticSearch Documentation](https://www.elastic.co/guide/index.html)
