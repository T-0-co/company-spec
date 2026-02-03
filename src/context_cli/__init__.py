#!/usr/bin/env python3
"""
Company Spec CLI - Structured organizational knowledge capture for AI deployment

Built on GitHub's Spec Kit methodology, adapted for company knowledge capture
instead of software development.

Usage:
    companyspec init <engagement-name>
    companyspec init . --org "Company Name"
    companyspec init --here --org "Acme Corp" --scope "Marketing Team"

Or install globally:
    uv tool install company-spec --from git+https://github.com/T-0-co/company-spec.git
    companyspec init <engagement-name>
"""

import os
import subprocess
import sys
import shutil
import json
from pathlib import Path
from typing import Optional
from datetime import datetime

import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.table import Table
from rich.tree import Tree
from rich.live import Live
from typer.core import TyperGroup

import readchar

# Banner art
BANNER = """
 ██████╗ ██████╗ ███╗   ███╗██████╗  █████╗ ███╗   ██╗██╗   ██╗
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔══██╗████╗  ██║╚██╗ ██╔╝
██║     ██║   ██║██╔████╔██║██████╔╝███████║██╔██╗ ██║ ╚████╔╝
██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██╔══██║██║╚██╗██║  ╚██╔╝
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║  ██║██║ ╚████║   ██║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝
███████╗██████╗ ███████╗ ██████╗
██╔════╝██╔══██╗██╔════╝██╔════╝
███████╗██████╔╝█████╗  ██║
╚════██║██╔═══╝ ██╔══╝  ██║
███████║██║     ███████╗╚██████╗
╚══════╝╚═╝     ╚══════╝ ╚═════╝
"""

TAGLINE = "Company Spec - Knowledge Capture for AI Deployment (Built on Spec Kit)"

console = Console()


class StepTracker:
    """Track and render hierarchical steps with live updates."""

    def __init__(self, title: str):
        self.title = title
        self.steps = []
        self._refresh_cb = None

    def attach_refresh(self, cb):
        self._refresh_cb = cb

    def add(self, key: str, label: str):
        if key not in [s["key"] for s in self.steps]:
            self.steps.append({"key": key, "label": label, "status": "pending", "detail": ""})
            self._maybe_refresh()

    def start(self, key: str, detail: str = ""):
        self._update(key, status="running", detail=detail)

    def complete(self, key: str, detail: str = ""):
        self._update(key, status="done", detail=detail)

    def error(self, key: str, detail: str = ""):
        self._update(key, status="error", detail=detail)

    def skip(self, key: str, detail: str = ""):
        self._update(key, status="skipped", detail=detail)

    def _update(self, key: str, status: str, detail: str):
        for s in self.steps:
            if s["key"] == key:
                s["status"] = status
                if detail:
                    s["detail"] = detail
                self._maybe_refresh()
                return
        self.steps.append({"key": key, "label": key, "status": status, "detail": detail})
        self._maybe_refresh()

    def _maybe_refresh(self):
        if self._refresh_cb:
            try:
                self._refresh_cb()
            except Exception:
                pass

    def render(self):
        tree = Tree(f"[cyan]{self.title}[/cyan]", guide_style="grey50")
        for step in self.steps:
            label = step["label"]
            detail_text = step["detail"].strip() if step["detail"] else ""
            status = step["status"]

            if status == "done":
                symbol = "[green]●[/green]"
            elif status == "pending":
                symbol = "[green dim]○[/green dim]"
            elif status == "running":
                symbol = "[cyan]○[/cyan]"
            elif status == "error":
                symbol = "[red]●[/red]"
            elif status == "skipped":
                symbol = "[yellow]○[/yellow]"
            else:
                symbol = " "

            if status == "pending":
                if detail_text:
                    line = f"{symbol} [bright_black]{label} ({detail_text})[/bright_black]"
                else:
                    line = f"{symbol} [bright_black]{label}[/bright_black]"
            else:
                if detail_text:
                    line = f"{symbol} [white]{label}[/white] [bright_black]({detail_text})[/bright_black]"
                else:
                    line = f"{symbol} [white]{label}[/white]"

            tree.add(line)
        return tree


def get_key():
    """Get a single keypress in a cross-platform way."""
    key = readchar.readkey()

    if key == readchar.key.UP or key == readchar.key.CTRL_P:
        return 'up'
    if key == readchar.key.DOWN or key == readchar.key.CTRL_N:
        return 'down'
    if key == readchar.key.ENTER:
        return 'enter'
    if key == readchar.key.ESC:
        return 'escape'
    if key == readchar.key.CTRL_C:
        raise KeyboardInterrupt

    return key


def select_with_arrows(options: dict, prompt_text: str = "Select an option", default_key: str = None) -> str:
    """Interactive selection using arrow keys."""
    option_keys = list(options.keys())
    if default_key and default_key in option_keys:
        selected_index = option_keys.index(default_key)
    else:
        selected_index = 0

    selected_key = None

    def create_selection_panel():
        table = Table.grid(padding=(0, 2))
        table.add_column(style="cyan", justify="left", width=3)
        table.add_column(style="white", justify="left")

        for i, key in enumerate(option_keys):
            if i == selected_index:
                table.add_row("▶", f"[cyan]{key}[/cyan] [dim]({options[key]})[/dim]")
            else:
                table.add_row(" ", f"[cyan]{key}[/cyan] [dim]({options[key]})[/dim]")

        table.add_row("", "")
        table.add_row("", "[dim]Use ↑/↓ to navigate, Enter to select, Esc to cancel[/dim]")

        return Panel(
            table,
            title=f"[bold]{prompt_text}[/bold]",
            border_style="cyan",
            padding=(1, 2)
        )

    console.print()

    def run_selection_loop():
        nonlocal selected_key, selected_index
        with Live(create_selection_panel(), console=console, transient=True, auto_refresh=False) as live:
            while True:
                try:
                    key = get_key()
                    if key == 'up':
                        selected_index = (selected_index - 1) % len(option_keys)
                    elif key == 'down':
                        selected_index = (selected_index + 1) % len(option_keys)
                    elif key == 'enter':
                        selected_key = option_keys[selected_index]
                        break
                    elif key == 'escape':
                        console.print("\n[yellow]Selection cancelled[/yellow]")
                        raise typer.Exit(1)

                    live.update(create_selection_panel(), refresh=True)

                except KeyboardInterrupt:
                    console.print("\n[yellow]Selection cancelled[/yellow]")
                    raise typer.Exit(1)

    run_selection_loop()

    if selected_key is None:
        console.print("\n[red]Selection failed.[/red]")
        raise typer.Exit(1)

    return selected_key


def show_banner():
    """Display the ASCII art banner."""
    banner_lines = BANNER.strip().split('\n')
    colors = ["bright_blue", "blue", "cyan", "bright_cyan", "white", "bright_white"]

    styled_banner = Text()
    for i, line in enumerate(banner_lines):
        color = colors[i % len(colors)]
        styled_banner.append(line + "\n", style=color)

    console.print(Align.center(styled_banner))
    console.print(Align.center(Text(TAGLINE, style="italic bright_yellow")))
    console.print()


class BannerGroup(TyperGroup):
    """Custom group that shows banner before help."""
    def format_help(self, ctx, formatter):
        show_banner()
        super().format_help(ctx, formatter)


app = typer.Typer(
    name="companyspec",
    help="Company Spec - Structured organizational knowledge capture for AI deployment. Built on GitHub's Spec Kit.",
    add_completion=False,
    invoke_without_command=True,
    cls=BannerGroup,
)


@app.callback()
def callback(ctx: typer.Context):
    """Show banner when no subcommand is provided."""
    if ctx.invoked_subcommand is None and "--help" not in sys.argv and "-h" not in sys.argv:
        show_banner()
        console.print(Align.center("[dim]Run 'companyspec --help' for usage information[/dim]"))
        console.print()


def is_git_repo(path: Path = None) -> bool:
    """Check if the specified path is inside a git repository."""
    if path is None:
        path = Path.cwd()

    if not path.is_dir():
        return False

    try:
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            capture_output=True,
            cwd=path,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def init_git_repo(project_path: Path, quiet: bool = False):
    """Initialize a git repository in the specified path."""
    try:
        original_cwd = Path.cwd()
        os.chdir(project_path)
        if not quiet:
            console.print("[cyan]Initializing git repository...[/cyan]")
        subprocess.run(["git", "init"], check=True, capture_output=True, text=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True, text=True)
        subprocess.run(["git", "commit", "-m", "Initial commit from Context Framework"], check=True, capture_output=True, text=True)
        if not quiet:
            console.print("[green]✓[/green] Git repository initialized")
        return True, None

    except subprocess.CalledProcessError as e:
        error_msg = f"Command: {' '.join(e.cmd)}\nExit code: {e.returncode}"
        if e.stderr:
            error_msg += f"\nError: {e.stderr.strip()}"
        if not quiet:
            console.print(f"[red]Error initializing git repository:[/red] {e}")
        return False, error_msg
    finally:
        os.chdir(original_cwd)


def get_templates_dir() -> Path:
    """Get the path to the templates directory."""
    # First check if running from source (development)
    source_templates = Path(__file__).parent.parent.parent / ".context" / "templates"
    if source_templates.exists():
        return source_templates

    # Check shared-data location (wheel install via uv tool or pip)
    # pyproject.toml installs templates to share/company-spec/templates
    import sysconfig
    shared_data = Path(sysconfig.get_path('data')) / 'share' / 'company-spec' / 'templates'
    if shared_data.exists():
        return shared_data

    # Check installed package location
    import importlib.resources
    try:
        with importlib.resources.files("context_cli").joinpath("templates") as p:
            if p.exists():
                return Path(p)
    except Exception:
        pass

    # Fallback to current directory's .context/templates
    local_templates = Path.cwd() / ".context" / "templates"
    if local_templates.exists():
        return local_templates

    return None


def copy_templates(dest_path: Path, tracker: StepTracker = None):
    """Copy template files to the destination directory."""
    templates_dir = get_templates_dir()

    if templates_dir is None or not templates_dir.exists():
        if tracker:
            tracker.error("templates", "templates directory not found")
        return False

    context_dir = dest_path / ".context"

    # Create directory structure
    dirs_to_create = [
        context_dir / "memory",
        context_dir / "outcomes",
        context_dir / "templates" / "commands",
        context_dir / "scripts" / "bash",
    ]

    for d in dirs_to_create:
        d.mkdir(parents=True, exist_ok=True)

    # Copy templates
    if (templates_dir / "constitution-template.md").exists():
        shutil.copy(templates_dir / "constitution-template.md", context_dir / "templates")
    if (templates_dir / "outcome-template.md").exists():
        shutil.copy(templates_dir / "outcome-template.md", context_dir / "templates")
    if (templates_dir / "strategy-template.md").exists():
        shutil.copy(templates_dir / "strategy-template.md", context_dir / "templates")
    if (templates_dir / "tasks-template.md").exists():
        shutil.copy(templates_dir / "tasks-template.md", context_dir / "templates")

    # Copy commands
    commands_dir = templates_dir / "commands"
    if commands_dir.exists():
        for cmd_file in commands_dir.glob("*.md"):
            shutil.copy(cmd_file, context_dir / "templates" / "commands")

    # Copy scripts
    scripts_src = templates_dir.parent / "scripts" / "bash"
    if scripts_src.exists():
        for script in scripts_src.glob("*.sh"):
            dest_script = context_dir / "scripts" / "bash" / script.name
            shutil.copy(script, dest_script)
            # Make executable on Unix
            if os.name != "nt":
                os.chmod(dest_script, 0o755)

    # Create context-artifacts directory
    artifacts_dir = dest_path / "context-artifacts"
    for subdir in ["glossaries", "processes", "decisions", "authorities", "systems"]:
        (artifacts_dir / subdir).mkdir(parents=True, exist_ok=True)

    if tracker:
        tracker.complete("templates", "copied")

    return True


def create_initial_constitution(dest_path: Path, org: str, scope: str, goal: str, tracker: StepTracker = None):
    """Create an initial constitution file with provided values."""
    templates_dir = get_templates_dir()
    if templates_dir is None:
        if tracker:
            tracker.error("constitution", "templates not found")
        return False

    template_path = templates_dir / "constitution-template.md"
    if not template_path.exists():
        if tracker:
            tracker.error("constitution", "template not found")
        return False

    constitution_path = dest_path / ".context" / "memory" / "constitution.md"

    # Read template
    content = template_path.read_text()

    # Replace placeholders
    today = datetime.now().strftime("%Y-%m-%d")
    engagement_name = f"{org} - {scope}" if scope else org

    replacements = {
        "[ENGAGEMENT_NAME]": engagement_name,
        "[DATE]": today,
        "[ORGANIZATION_NAME]": org,
        "[INDUSTRY]": "[To be filled]",
        "[EMPLOYEE_COUNT / TEAM_SIZE]": "[To be filled]",
        "[Whole Company | Division | Department | Team | Project]": scope or "Team",
        "[SPECIFIC_SCOPE_NAME]": scope or "[To be filled]",
        "[BRIEF_DESCRIPTION_OF_SCOPE]": "[To be filled]",
    }

    # Handle AI deployment goal
    if goal:
        content = content.replace(
            "[What AI capability are we enabling? What will the AI do with this context?]",
            goal
        )

    for old, new in replacements.items():
        content = content.replace(old, new)

    # Write constitution
    constitution_path.parent.mkdir(parents=True, exist_ok=True)
    constitution_path.write_text(content)

    if tracker:
        tracker.complete("constitution", "created")

    return True


def discover_existing_context(project_path: Path) -> dict:
    """
    Scan the project directory for existing documentation and context.

    Returns a dict with:
    - docs_found: list of documentation files found
    - frameworks_found: list of existing frameworks detected
    - extracted_context: dict with any extracted project info (scope, goals, etc.)
    - warnings: list of potential conflicts or considerations
    """
    result = {
        "docs_found": [],
        "frameworks_found": [],
        "extracted_context": {},
        "warnings": [],
    }

    # Patterns to look for
    doc_patterns = [
        "README.md", "README.txt", "README",
        "CLAUDE.md", ".claude/CLAUDE.md",
        "docs/project_mission.md", "docs/PROJECT_MISSION.md",
        "docs/project_structure.md",
        "PROJECT.md", "ABOUT.md",
    ]

    # Framework indicators
    framework_patterns = {
        ".context": "Company Spec (already initialized)",
        ".specify": "Spec Kit",
        "docs/_legacy": "Legacy framework",
        ".claude": "Claude Code configuration",
        "specs/": "Specs directory",
    }

    # Scan for documentation files
    for pattern in doc_patterns:
        path = project_path / pattern
        if path.exists():
            result["docs_found"].append(str(pattern))

    # Also find all markdown files in docs/
    docs_dir = project_path / "docs"
    if docs_dir.exists():
        for md_file in docs_dir.rglob("*.md"):
            rel_path = md_file.relative_to(project_path)
            if str(rel_path) not in result["docs_found"]:
                result["docs_found"].append(str(rel_path))

    # Check for existing frameworks
    for pattern, name in framework_patterns.items():
        path = project_path / pattern
        if path.exists():
            result["frameworks_found"].append((pattern, name))

    # Try to extract context from key files
    mission_file = project_path / "docs" / "project_mission.md"
    if mission_file.exists():
        try:
            content = mission_file.read_text()
            result["extracted_context"]["has_mission"] = True

            # Try to extract intent/scope
            if "## Intent" in content or "## intent" in content:
                lines = content.split("\n")
                for i, line in enumerate(lines):
                    if line.strip().lower() == "## intent":
                        # Get the next non-empty line
                        for j in range(i + 1, min(i + 5, len(lines))):
                            if lines[j].strip() and not lines[j].startswith("#"):
                                result["extracted_context"]["intent"] = lines[j].strip()
                                break
                        break

            # Check for scope constraints
            if "Must Not" in content or "Non-Goals" in content:
                result["extracted_context"]["has_constraints"] = True

        except Exception:
            pass

    # Check CLAUDE.md for project context
    claude_paths = [project_path / "CLAUDE.md", project_path / ".claude" / "CLAUDE.md"]
    for claude_path in claude_paths:
        if claude_path.exists():
            result["extracted_context"]["has_claude_md"] = True
            break

    # Generate warnings
    if ".context" in [f[0] for f in result["frameworks_found"]]:
        result["warnings"].append("Company Spec already initialized - will overwrite existing .context/")

    if result["extracted_context"].get("has_constraints"):
        result["warnings"].append("Project has defined constraints/non-goals - review before defining outcomes")

    if len(result["docs_found"]) > 5:
        result["warnings"].append(f"Found {len(result['docs_found'])} existing docs - consider reviewing before capture")

    return result


def display_discovery_results(discovery: dict, console: Console) -> bool:
    """
    Display discovery results and ask user how to proceed.
    Returns True if user wants to continue, False to abort.
    """
    if not discovery["docs_found"] and not discovery["frameworks_found"]:
        return True  # Nothing found, proceed normally

    console.print()
    console.print("[cyan]━━━ Project Discovery ━━━[/cyan]")
    console.print()

    # Show existing documentation
    if discovery["docs_found"]:
        console.print(f"[yellow]Found {len(discovery['docs_found'])} existing documentation files:[/yellow]")
        # Show first 10, summarize rest
        for doc in discovery["docs_found"][:10]:
            console.print(f"  • {doc}")
        if len(discovery["docs_found"]) > 10:
            console.print(f"  [dim]... and {len(discovery['docs_found']) - 10} more[/dim]")
        console.print()

    # Show existing frameworks
    if discovery["frameworks_found"]:
        console.print("[yellow]Existing frameworks detected:[/yellow]")
        for pattern, name in discovery["frameworks_found"]:
            console.print(f"  • {pattern} → {name}")
        console.print()

    # Show extracted context
    if discovery["extracted_context"]:
        console.print("[yellow]Extracted project context:[/yellow]")
        if discovery["extracted_context"].get("intent"):
            intent = discovery["extracted_context"]["intent"]
            if len(intent) > 100:
                intent = intent[:100] + "..."
            console.print(f"  Intent: [green]{intent}[/green]")
        if discovery["extracted_context"].get("has_constraints"):
            console.print("  [dim]Project has defined constraints/non-goals[/dim]")
        if discovery["extracted_context"].get("has_claude_md"):
            console.print("  [dim]CLAUDE.md configuration present[/dim]")
        console.print()

    # Show warnings
    if discovery["warnings"]:
        console.print("[yellow]⚠ Considerations:[/yellow]")
        for warning in discovery["warnings"]:
            console.print(f"  • {warning}")
        console.print()

    # Ask user how to proceed
    if sys.stdin.isatty():
        console.print("[cyan]How would you like to proceed?[/cyan]")
        options = {
            "continue": "Continue with init (I'll review existing docs manually)",
            "abort": "Abort (I want to review existing documentation first)",
        }
        choice = select_with_arrows(options, "Select action", "continue")
        if choice == "abort":
            console.print("\n[yellow]Aborted.[/yellow] Review existing documentation, then run init again.")
            return False

    return True


SCOPE_OPTIONS = {
    "company": "Whole organization",
    "division": "Business division or unit",
    "department": "Single department",
    "team": "Specific team",
    "project": "Project-specific context",
}


@app.command()
def init(
    engagement_name: str = typer.Argument(None, help="Name for your engagement (or '.' for current directory)"),
    org: str = typer.Option(None, "--org", "-o", help="Organization name"),
    scope: str = typer.Option(None, "--scope", "-s", help="Scope level: company, division, department, team, project"),
    goal: str = typer.Option(None, "--goal", "-g", help="AI deployment goal (what capability needs this context)"),
    here: bool = typer.Option(False, "--here", help="Initialize in the current directory"),
    force: bool = typer.Option(False, "--force", help="Force initialization even if directory not empty"),
    no_git: bool = typer.Option(False, "--no-git", help="Skip git repository initialization"),
):
    """
    Initialize a new Company Context Framework engagement.

    This command will:
    1. Discover existing documentation and frameworks in the directory
    2. Present findings and ask how to proceed
    3. Create the .context/ directory structure
    4. Copy all templates and scripts
    5. Create an initial constitution
    6. Initialize a git repository (unless --no-git)

    The discovery phase scans for existing docs/, README.md, CLAUDE.md,
    and other documentation to help you understand what context already
    exists before setting up the framework.

    Examples:
        companyspec init acme-marketing --org "Acme Corp" --scope team
        companyspec init . --org "Startup Inc"
        companyspec init --here --org "BigCo" --scope department --goal "AI customer support"
    """
    show_banner()

    # Handle "." as current directory
    if engagement_name == ".":
        here = True
        engagement_name = None

    if here and engagement_name:
        console.print("[red]Error:[/red] Cannot specify both engagement name and --here flag")
        raise typer.Exit(1)

    if not here and not engagement_name:
        console.print("[red]Error:[/red] Must specify engagement name, use '.' for current directory, or use --here")
        raise typer.Exit(1)

    if here:
        project_path = Path.cwd()
        engagement_name = project_path.name
    else:
        project_path = Path(engagement_name).resolve()
        if project_path.exists() and not force:
            if any(project_path.iterdir()):
                console.print(f"[red]Error:[/red] Directory '{engagement_name}' already exists and is not empty")
                console.print("[dim]Use --force to initialize anyway[/dim]")
                raise typer.Exit(1)

    # Discovery phase: scan for existing documentation and context
    if project_path.exists():
        discovery = discover_existing_context(project_path)
        if not display_discovery_results(discovery, console):
            raise typer.Exit(0)  # User chose to abort

        # Use extracted context to inform defaults
        if discovery["extracted_context"].get("intent") and not goal:
            # Suggest the extracted intent as a starting point
            extracted_intent = discovery["extracted_context"]["intent"]
            if sys.stdin.isatty():
                console.print(f"\n[dim]Extracted project intent: {extracted_intent[:80]}...[/dim]" if len(extracted_intent) > 80 else f"\n[dim]Extracted project intent: {extracted_intent}[/dim]")

    # Interactive prompts for missing required info
    if not org:
        org = typer.prompt("Organization name")

    if not scope:
        if sys.stdin.isatty():
            scope = select_with_arrows(SCOPE_OPTIONS, "Select scope level:", "team")
        else:
            scope = "team"
    elif scope not in SCOPE_OPTIONS:
        console.print(f"[red]Error:[/red] Invalid scope '{scope}'. Choose from: {', '.join(SCOPE_OPTIONS.keys())}")
        raise typer.Exit(1)

    if not goal and sys.stdin.isatty():
        goal = typer.prompt("AI deployment goal (what capability needs this context)", default="")

    # Display setup info
    setup_lines = [
        "[cyan]Context Framework Setup[/cyan]",
        "",
        f"{'Engagement':<15} [green]{engagement_name}[/green]",
        f"{'Organization':<15} [green]{org}[/green]",
        f"{'Scope':<15} [green]{scope}[/green] [dim]({SCOPE_OPTIONS.get(scope, '')})[/dim]",
    ]
    if goal:
        setup_lines.append(f"{'AI Goal':<15} [green]{goal}[/green]")
    setup_lines.append(f"{'Path':<15} [dim]{project_path}[/dim]")

    console.print(Panel("\n".join(setup_lines), border_style="cyan", padding=(1, 2)))

    # Check for git
    should_init_git = False
    if not no_git:
        should_init_git = shutil.which("git") is not None
        if not should_init_git:
            console.print("[yellow]Git not found - will skip repository initialization[/yellow]")

    # Set up tracker
    tracker = StepTracker("Initialize Context Framework")

    tracker.add("directory", "Create directory structure")
    tracker.add("templates", "Copy templates and scripts")
    tracker.add("constitution", "Create initial constitution")
    tracker.add("artifacts", "Create artifacts directory")
    tracker.add("git", "Initialize git repository")
    tracker.add("final", "Finalize")

    git_error_message = None

    with Live(tracker.render(), console=console, refresh_per_second=8, transient=True) as live:
        tracker.attach_refresh(lambda: live.update(tracker.render()))

        try:
            # Create directory
            tracker.start("directory")
            if not here:
                project_path.mkdir(parents=True, exist_ok=True)
            tracker.complete("directory", str(project_path))

            # Copy templates
            tracker.start("templates")
            if not copy_templates(project_path, tracker):
                raise Exception("Failed to copy templates")

            # Create constitution
            tracker.start("constitution")
            create_initial_constitution(project_path, org, scope, goal, tracker)

            # Artifacts directory already created by copy_templates
            tracker.complete("artifacts", "created")

            # Git initialization
            if not no_git:
                tracker.start("git")
                if is_git_repo(project_path):
                    tracker.complete("git", "existing repo detected")
                elif should_init_git:
                    success, error_msg = init_git_repo(project_path, quiet=True)
                    if success:
                        tracker.complete("git", "initialized")
                    else:
                        tracker.error("git", "init failed")
                        git_error_message = error_msg
                else:
                    tracker.skip("git", "git not available")
            else:
                tracker.skip("git", "--no-git flag")

            tracker.complete("final", "engagement ready")

        except Exception as e:
            tracker.error("final", str(e))
            console.print(Panel(f"Initialization failed: {e}", title="Failure", border_style="red"))
            raise typer.Exit(1)

    # Print final tree
    console.print(tracker.render())
    console.print("\n[bold green]Engagement ready.[/bold green]")

    if git_error_message:
        console.print()
        console.print(Panel(
            f"[yellow]Warning:[/yellow] Git initialization failed\n\n{git_error_message}",
            title="[red]Git Error[/red]",
            border_style="red",
            padding=(1, 2)
        ))

    # Next steps
    steps_lines = []
    if not here:
        steps_lines.append(f"1. Go to the engagement folder: [cyan]cd {engagement_name}[/cyan]")
        step_num = 2
    else:
        steps_lines.append("1. You're already in the engagement directory!")
        step_num = 2

    steps_lines.append(f"{step_num}. Review and complete the constitution: [cyan].context/memory/constitution.md[/cyan]")
    steps_lines.append(f"{step_num + 1}. Start using slash commands with your AI agent:")
    steps_lines.append("   • [cyan]/context.constitution[/] - Review and finalize engagement setup")
    steps_lines.append("   • [cyan]/context.outcome[/] - Define knowledge artifacts needed")
    steps_lines.append("   • [cyan]/context.strategy[/] - Plan capture approach")
    steps_lines.append("   • [cyan]/context.tasks[/] - Generate extraction tasks")
    steps_lines.append("   • [cyan]/context.capture[/] - Execute and validate")

    console.print()
    console.print(Panel("\n".join(steps_lines), title="Next Steps", border_style="cyan", padding=(1, 2)))


@app.command()
def check():
    """Check the current engagement status and prerequisites."""
    show_banner()

    cwd = Path.cwd()
    context_dir = cwd / ".context"

    if not context_dir.exists():
        console.print("[red]Not in a Context Framework engagement[/red]")
        console.print("[dim]Run 'companyspec init' to create one[/dim]")
        raise typer.Exit(1)

    tracker = StepTracker("Engagement Status")

    # Check constitution
    constitution = context_dir / "memory" / "constitution.md"
    tracker.add("constitution", "Constitution")
    if constitution.exists():
        tracker.complete("constitution", "found")
    else:
        tracker.error("constitution", "missing")

    # Check templates
    templates = context_dir / "templates"
    tracker.add("templates", "Templates")
    if templates.exists() and any(templates.glob("*.md")):
        count = len(list(templates.glob("*.md")))
        tracker.complete("templates", f"{count} templates")
    else:
        tracker.error("templates", "missing")

    # Check scripts
    scripts = context_dir / "scripts" / "bash"
    tracker.add("scripts", "Scripts")
    if scripts.exists() and any(scripts.glob("*.sh")):
        count = len(list(scripts.glob("*.sh")))
        tracker.complete("scripts", f"{count} scripts")
    else:
        tracker.skip("scripts", "none found")

    # Check outcomes
    outcomes = context_dir / "outcomes"
    tracker.add("outcomes", "Knowledge Outcomes")
    if outcomes.exists():
        outcome_dirs = [d for d in outcomes.iterdir() if d.is_dir()]
        if outcome_dirs:
            tracker.complete("outcomes", f"{len(outcome_dirs)} outcomes")
        else:
            tracker.skip("outcomes", "none defined yet")
    else:
        tracker.skip("outcomes", "directory missing")

    # Check artifacts
    artifacts = cwd / "context-artifacts"
    tracker.add("artifacts", "Context Artifacts")
    if artifacts.exists():
        artifact_files = list(artifacts.rglob("*.md"))
        if artifact_files:
            tracker.complete("artifacts", f"{len(artifact_files)} artifacts")
        else:
            tracker.skip("artifacts", "none created yet")
    else:
        tracker.skip("artifacts", "directory missing")

    console.print(tracker.render())
    console.print()
    console.print("[bold green]Context Framework check complete.[/bold green]")


@app.command(name="list")
def list_outcomes():
    """List all knowledge outcomes in the current engagement."""
    show_banner()

    cwd = Path.cwd()
    outcomes_dir = cwd / ".context" / "outcomes"

    if not outcomes_dir.exists():
        console.print("[yellow]No outcomes directory found[/yellow]")
        console.print("[dim]Run 'companyspec init' first, then define outcomes with /context.outcome[/dim]")
        raise typer.Exit(1)

    outcome_dirs = sorted([d for d in outcomes_dir.iterdir() if d.is_dir()])

    if not outcome_dirs:
        console.print("[yellow]No outcomes defined yet[/yellow]")
        console.print("[dim]Use /context.outcome to define your first knowledge outcome[/dim]")
        return

    table = Table(title="Knowledge Outcomes", border_style="cyan")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="white")
    table.add_column("Status", style="green")
    table.add_column("Tasks", style="dim")

    for outcome_dir in outcome_dirs:
        name = outcome_dir.name
        outcome_id = name.split("-")[0] if "-" in name else name
        outcome_name = "-".join(name.split("-")[1:]) if "-" in name else name

        # Determine status
        has_outcome = (outcome_dir / "outcome.md").exists()
        has_strategy = (outcome_dir / "strategy.md").exists()
        has_tasks = (outcome_dir / "tasks.md").exists()

        if not has_outcome:
            status = "[red]missing outcome.md[/red]"
        elif not has_strategy:
            status = "[yellow]needs strategy[/yellow]"
        elif not has_tasks:
            status = "[yellow]needs tasks[/yellow]"
        else:
            # Count tasks
            tasks_content = (outcome_dir / "tasks.md").read_text()
            total = tasks_content.count("- [ ]") + tasks_content.count("- [x]") + tasks_content.count("- [X]")
            done = tasks_content.count("- [x]") + tasks_content.count("- [X]")
            if done == total and total > 0:
                status = "[green]complete[/green]"
            else:
                status = f"[blue]in progress[/blue]"

        # Task count
        if has_tasks:
            tasks_content = (outcome_dir / "tasks.md").read_text()
            total = tasks_content.count("- [ ]") + tasks_content.count("- [x]") + tasks_content.count("- [X]")
            done = tasks_content.count("- [x]") + tasks_content.count("- [X]")
            task_info = f"{done}/{total}"
        else:
            task_info = "-"

        table.add_row(f"KO-{outcome_id}", outcome_name, status, task_info)

    console.print(table)


@app.command()
def version():
    """Display version and system information."""
    import platform

    show_banner()

    # Get CLI version
    cli_version = "0.1.0"
    try:
        import importlib.metadata
        cli_version = importlib.metadata.version("company-spec")
    except Exception:
        pass

    info_table = Table(show_header=False, box=None, padding=(0, 2))
    info_table.add_column("Key", style="cyan", justify="right")
    info_table.add_column("Value", style="white")

    info_table.add_row("CLI Version", cli_version)
    info_table.add_row("", "")
    info_table.add_row("Python", platform.python_version())
    info_table.add_row("Platform", platform.system())
    info_table.add_row("Architecture", platform.machine())

    panel = Panel(
        info_table,
        title="[bold cyan]Context CLI Information[/bold cyan]",
        border_style="cyan",
        padding=(1, 2)
    )

    console.print(panel)


def main():
    app()


if __name__ == "__main__":
    main()
