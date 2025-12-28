import argparse
from synthetix.core.engine import SynthetixEngine

def main():
    parser = argparse.ArgumentParser(description="Synthetix: Self-Evolving Algorithm Engine")
    parser.add_argument('--cycles', type=int, default=3, help='Number of evolution cycles to run')
    args = parser.parse_args()

    engine = SynthetixEngine()
    engine.initialize()
    engine.run_evolution_cycle(cycles=args.cycles)

if __name__ == "__main__":
    main()
