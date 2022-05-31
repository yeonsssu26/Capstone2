from gym.envs.registration import register

register(
    id='ChargingStation-v0',
    entry_point='multi_agent_charging_station.envs:ChargingStation',
    # max_episode_steps=1000,
)