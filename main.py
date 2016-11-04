#!/usr/bin/python3

from ann import ANN, Neuron
from game2048 import GAME2048

BRAIN = [16,8,8,4]
GENERATION_SIZE = 20
FREEPASS_SIZE = 2
SELECTION_SIZE = 5
MUTATION_RATE = 0.1

ILLEGAL_MOVE_CUTOFF = 20


generation_no = 0

current_gen = []
holding_tank = []
next_generation = []

current_games = []

# seed initial network
for i in range(GENERATION_SIZE):
    current_gen.append(ANN(BRAIN, Neuron.Perceptron))
    current_gen[i].seed_network()
    current_games.append(GAME2048())


# runs 1 generation
def run_generation():
    while len(holding_tank) < GENERATION_SIZE:
        for i, network in enumerate(current_gen):
            chosen_move = network.run(current_games[i].board[k] for k in range(4))
            current_games[i].play_move

            if current_games[i].illegal_moves == ILLEGAL_MOVE_CUTOFF:
                holding_tank.append([current_games[i].get_highest, network])


# top "FREEPASS SIZE" go to next round for free, top "SELECTION SIZE" are bred from
def breed_and_mutate():


while True:
    run_generation()
    breed_and_mutate()
    print("GENERATION {} HIGHEST TILE IS {}".format(generation_no,0))
    generation_no += 1