"""OmniResearch AI - Unified Application Launcher."""
import argparse
import asyncio
import os
import sys
import uvicorn
from dotenv import load_dotenv

# Load local .env if present
load_dotenv()


def main():
    parser = argparse.ArgumentParser(
        description="OmniResearch AI — Autonomous Multi-Agent Deep Research & Intelligence Engine"
    )
    parser.add_argument(
        "--web",
        action="store_true",
        default=True,
        help="Launch the interactive Web Dashboard (default mode)",
    )
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Run via terminal CLI interface",
    )
    parser.add_argument(
        "--topic",
        type=str,
        default="Autonomous Multi-Agent AI Frameworks and Benchmark Results",
        help="Research topic when running in CLI mode",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for Web Dashboard (default: 8000)",
    )
    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host for Web Dashboard (default: 127.0.0.1)",
    )

    args = parser.parse_args()

    # If --cli explicitly passed, execute terminal mode
    if args.cli:
        from src.cli import run_cli
        asyncio.run(run_cli(args.topic))
    else:
        print("\n" + "=" * 65)
        print("  ⚡ OmniResearch AI - Web Dashboard Initializing")
        print(f"  🌐 Open your browser at: http://{args.host}:{args.port}")
        print("  💡 Tip: You can test directly without an API key using Mock mode!")
        print("=" * 65 + "\n")
        uvicorn.run("src.api.server:app", host=args.host, port=args.port, reload=False)


if __name__ == "__main__":
    main()
