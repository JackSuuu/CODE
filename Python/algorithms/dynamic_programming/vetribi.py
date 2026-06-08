

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # Initialise base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]

    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            # * This step is hidden markov chain process
            # key step for this dynamic programming algorithm, choose one with highest probability
            (prob, state) = max([(V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states])
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        path = newpath

    (prob, state) = max([(V[-1][y], y) for y in states])
    return (prob, path[state])

observations = ('the', 'old', 'man', 'the', 'lifeboats')
states = ('DT', 'N', 'Adj', 'V')

start_probability = {'DT': 0.4, 'N': 0.3, 'Adj': 0.2, 'V': 0.1}

transition_probability = {
    'DT': {'DT': 0, 'N': 0.6, 'V': 0, 'Adj': 0.4},
    'N': {'DT': 0.05, 'N': 0.3, 'V': 0.4, 'Adj': 0.25},
    'V': {'DT': 0.4, 'N': 0.3, 'V': 0.1, 'Adj': 0.2},
    'Adj': {'DT': 0.1, 'N': 0.5, 'V': 0.2, 'Adj': 0.2}
}

emission_probability = {
    'DT': {'lifeboats': 0, 'man': 0, 'old': 0, 'the': 0.5, 'other': 0.5},
    'N': {'lifeboats': 0.2, 'man': 0.3, 'old': 0.2, 'the': 0, 'other': 0.3},
    'V': {'lifeboats': 0, 'man': 0.1, 'old': 0, 'the': 0, 'other': 0.9},
    'Adj': {'lifeboats': 0, 'man': 0, 'old': 0.4, 'the': 0, 'other': 0.6}
}

print(viterbi(observations, states, start_probability, transition_probability, emission_probability))