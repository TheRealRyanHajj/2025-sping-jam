import pygame
pygame.init()
import sys
from util.grefs import grefs

class EventMachine:
    def __init__(self, state_machine):
        self.state_machine = state_machine
        grefs["EventMachine"] = self
        # Dictionary to track key states
        self.key_states = {
            "isMovingUp": False,
            "isMovingRight": False,
            "isMovingDown": False,
            "isMovingLeft": False,
            "keyEDown": False,
            "keyTabDown": False,
            "keyShiftDown": False,
            "keySPACEDown": False
        }

    def check_events(self):
        """Processes events and updates key states, then returns the current state dictionary."""
        for event in pygame.event.get():
            # Handle exiting the game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.state_machine.exit_state()

            # Handle key presses
            if event.type == pygame.KEYDOWN:
                self._update_key_state(event.key, True)

            # Handle key releases
            elif event.type == pygame.KEYUP:
                self._update_key_state(event.key, False)

    def _update_key_state(self, key, is_pressed):
        """Updates the key state dictionary based on key input."""
        key_map = {
            pygame.K_w: "keyWDown",
            pygame.K_d: "keyDDown",
            pygame.K_s: "keySDown",
            pygame.K_a: "keyADown",
            pygame.K_e: "keyEDown",
            pygame.K_q: "keyQDown",
            pygame.K_SPACE: "keySPACEDown",
            pygame.K_TAB: "keyTabDown",
            pygame.K_LSHIFT: "keyShiftDown",
            pygame.K_F1: "keyF1Down"
        }

        if key in key_map:
            self.key_states[key_map[key]] = is_pressed

