import numpy as np

class QLearningAgent:
    def __init__(self, state_space_size, action_space_size, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.state_space_size = state_space_size
        self.action_space_size = action_space_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

        # Initialize Q-values to zeros
        self.q_values = np.zeros((state_space_size, action_space_size))

    def choose_action(self, state):
        # Epsilon-greedy strategy for action selection
        if np.random.rand() < self.exploration_rate:
            # Explore: choose a random action
            return np.random.choice(self.action_space_size)
        else:
            # Exploit: choose the action with the highest Q-value
            return np.argmax(self.q_values[state, :])

    def update_q_values(self, state, action, reward, next_state):
        # Q-value update using the Q-learning formula
        current_q_value = self.q_values[state, action]
        best_next_q_value = np.max(self.q_values[next_state, :])
        new_q_value = current_q_value + self.learning_rate * (reward + self.discount_factor * best_next_q_value - current_q_value)
        self.q_values[state, action] = new_q_value

# Simple environment with three states and two actions
class SimpleEnvironment:
    def __init__(self):
        self.num_states = 3
        self.num_actions = 2

    def step(self, state, action):
        # Define a simple transition and reward function
        transitions = {0: {0: (1, 0), 1: (0, 1)},
                       1: {0: (0, 1), 1: (2, 0)},
                       2: {0: (1, 0), 1: (2, 0)}}

        next_state, reward = transitions[state][action]
        return next_state, reward

# Training the Q-learning agent in the simple environment
def train_q_learning_agent(agent, environment, num_episodes=1000):
    for episode in range(num_episodes):
        state = np.random.choice(environment.num_states)  # Start in a random state

        while True:
            action = agent.choose_action(state)  # Choose an action
            next_state, reward = environment.step(state, action)  # Take a step in the environment
            agent.update_q_values(state, action, reward, next_state)  # Update Q-values

            state = next_state

            if state == 2:
                # Reached the goal state, break the episode
                break

# Create Q-learning agent and environment
agent = QLearningAgent(state_space_size=3, action_space_size=2)
env = SimpleEnvironment()

# Train the agent
train_q_learning_agent(agent, env)

# Print the learned Q-values
print("Learned Q-values:")
print(agent.q_values)
