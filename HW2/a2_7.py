import numpy as np

def steady_state_power(transition_matrix):
    prev_state = np.linalg.matrix_power(transition_matrix, 2)
    curr_state = np.linalg.matrix_power(transition_matrix, 3)
    i = 4
    while((curr_state != prev_state).any()):
        prev_state = curr_state
        curr_state = np.linalg.matrix_power(transition_matrix, i)
        i += 1
    print("%d >> %s" % (i, curr_state[0, :]))
    return curr_state[0,:]

transition_matrix = np.array([[0.9, 0.0, 0.1, 0.0],
							  [0.8, 0.0, 0.2, 0.0],
              				  [0.0, 0.5, 0.0, 0.5],
              				  [0.0, 0.1, 0.0, 0.9]])

steady_state = steady_state_power(transition_matrix)
prob_snowy = steady_state[2] + steady_state[3]

print('Probability of snowy 3 days from today: %.2f' % (prob_snowy))
