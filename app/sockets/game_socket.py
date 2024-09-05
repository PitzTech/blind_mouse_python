import socketio
from ..controllers.game_controller import GameController

sio = socketio.AsyncServer(async_mode='asgi')

class GameSocket:
    def __init__(self, game_controller: GameController):
        self.game_controller = game_controller
        self.sio = sio

    def initialize_game(self, size: int):
        self.game_controller.initialize_game(size)

        @self.sio.event
        async def connect(sid, environ):
            current_position = self.game_controller.get_start_node()
            await self.sio.emit('game-start', {
                'startNode': self.game_controller.get_start_node(),
                'endNode': self.game_controller.get_end_node()
            }, to=sid)

            @self.sio.on('move')
            async def move(sid, data):
                direction = data.get('direction')
                available_moves = self.game_controller.get_available_moves(current_position)
                if direction in available_moves:
                    current_position = direction
                    await self.sio.emit('position-update', {
                        'currentPosition': current_position,
                        'availableMoves': available_moves
                    }, to=sid)

                    if self.game_controller.is_game_end(current_position):
                        await self.sio.emit('game-end', {'message': 'You reached the end!'}, to=sid)
                else:
                    await self.sio.emit('invalid-move', {'message': 'Move not allowed!'}, to=sid)
