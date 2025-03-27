from fastapi import FastAPI
from api.routes import agents, simulation, voting, dao

app = FastAPI(title="Lumina Backend")

# Register API routers
app.include_router(agents.router, prefix="/agents")
app.include_router(simulation.router, prefix="/simulation")
app.include_router(voting.router, prefix="/voting")
app.include_router(dao.router, prefix="/dao")