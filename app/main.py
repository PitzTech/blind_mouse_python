import uvicorn
from fastapi import FastAPI
from .services.graph_service import GraphService
from .services.maze_service import MazeService
from .controllers.game_controller import GameController
from .sockets.game_socket import GameSocket, sio

app = FastAPI()

# Inicializar serviços
graph_service = GraphService()
maze_service = MazeService(graph_service)
game_controller = GameController(maze_service)
game_socket = GameSocket(game_controller)
game_socket.initialize_game(10)  # Tamanho do labirinto

# Montar o Socket.IO no FastAPI
app.mount('/', sio.asgi_app)

# Rota de teste
@app.get('/')
async def read_root():
    return {"message": "Blind Mouse Maze Game is running"}

if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
