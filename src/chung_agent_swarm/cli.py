import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="chung-swarm")
    subparsers = parser.add_subparsers(dest="command", required=True)

    demo_parser = subparsers.add_parser("demo", help="Run an offline demo without API calls.")
    demo_parser.add_argument(
        "--goal",
        default="From an empty folder, scaffold a FastAPI project skeleton with unit tests.",
    )

    run_parser = subparsers.add_parser("run", help="Run against the real Claude Agent SDK (requires API key).")
    run_parser.add_argument("prompt", nargs="?", default="Analyze this repository and propose improvements.")
    run_parser.add_argument("--max-turns", type=int, default=10)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "demo":
        from .orchestrator import run_demo

        return run_demo(goal=args.goal)

    if args.command == "run":
        from .orchestrator import run_real

        return run_real(prompt=args.prompt, max_turns=args.max_turns)

    parser.error(f"Unknown command: {args.command}")
    return 2
