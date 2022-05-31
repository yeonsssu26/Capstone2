import gym


class MultiAgentActionSpace(list):
    def __init__(self, agents_action_space):
        for x in agents_action_space:
            assert isinstance(x, gym.spaces.space.Space)

        super(MultiAgentActionSpace, self).__init__(agents_action_space)
        self._agents_action_space = agents_action_space

    '''
    >> OpenAI/gym/discrete.py
    https://github.com/openai/gym/blob/master/gym/spaces/discrete.py

    def sample(self) -> int:

        # Generates a single random sample from this space.
        # A sample will be chosen uniformly at random.
        # Returns:
        #    A sampled integer from the space
        
        return int(self.start + self.np_random.integers(self.n))
    '''

    # NEED TO FIX
    # 1. SAMPLE RANDOM ACTION >> 성능 낮은 원인으로 추정됨
    # 2. 경쟁상황 발생하면 >> auction theory 적용하기 >> 둘다 observation space 안에 있으면 beeding
    def sample(self):
        """ samples action for each agent from uniform distribution"""
        return [agent_action_space.sample() for agent_action_space in self._agents_action_space]
