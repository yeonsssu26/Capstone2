import argparse
import os
import gym
import imageio
import multi_agent_charging_station


def parse_arguments():
    parser = argparse.ArgumentParser(description='Record the environment.')
    parser.add_argument('--output_dir', type=str, default='output',
                        help='Output directory with GIF record.')
    parser.add_argument('--frames', type=int, default=10000,
                        help='Number of frames in GIF record.')
    parser.add_argument('--fps', type=int, default=4,
                        help='Frame per second.')
    return parser.parse_args()


def main(args):
    env = gym.make('ChargingStation-v0')
    images = []
    done_n = [False] * env.n_agents

    env.reset()
    while not all(done_n):
        images.append(env.render(mode='rgb_array'))
        _, _, done_n, _ = env.step(env.action_space.sample())

    print("Environment finished.")
    imageio.mimwrite(os.path.join(os.getcwd(), "ouput", "ChargingStation-v0" + '.mp4'), images[:args.frames], fps=args.fps)


if __name__ == "__main__":
    args = parse_arguments()
    main(args)